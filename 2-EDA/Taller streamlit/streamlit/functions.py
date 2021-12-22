import streamlit as st
import pandas as pd

def configuracion():
    st.set_page_config(page_title='Cargatron',
                       page_icon=':electric_plug:',
                       layout='wide')

@st.cache(suppress_st_warning=True)
def cargar_datos(csv_path, datos_propios):

    st.write(datos_propios)

    if datos_propios is None:

        df = pd.read_csv(csv_path, sep=';')
        df = df.rename(columns={"latidtud": "lat",
                                "longitud": "lon"})

    else:

        df = pd.read_csv(datos_propios, sep=';')

    return df


def home(df):

    st.title("Cargatron")
    st.subheader("Puntos de carga para coches electricos en Madrid.")

    st.image("cargador-de-cable-gordo.jpg")

    with st.expander("De que me hablas?"):

        st.write("Ante el problema climatico al que nos enfrentamos el coche electrico se plantea como una solución posible. Aquí queremos facilitarte que encuentres tu puesto de carga más cercano.")

    with st.echo():
        #Esta linea de codigo es equivalente a st.dataframe()
        st.write(df)


def datos(df):

    st.header('Mapa')
    mostrar_mapa(df)

    st.header("Cargadores por distrito:")
    bar_chart_variable(df, 'DISTRITO')

    st.header("Cargadores por operador:")
    bar_chart_variable(df, 'OPERADOR')


def bar_chart_variable(df, column):
    if column != 'Nº CARGADORES':
        cargadores_por_ope = df.groupby(column)['Nº CARGADORES'].sum()
    else:
        cargadores_por_ope = df.groupby(column)['DISTRITO'].count()

    st.bar_chart(cargadores_por_ope)


def datos_filtrados(df):
    distrito, check_dis = crear_filtro(df, 'DISTRITO')
    operador, check_op = crear_filtro(df, 'OPERADOR')
    cargadores = filtro_cargadores(df)

    if check_dis:
        df = aplicar_filtro(df, 'DISTRITO', distrito)

    if check_op:
        df = aplicar_filtro(df, 'OPERADOR', operador)

    df = aplicar_filtro_cargadores(df, cargadores)

    if df.shape[0] == 0:
        st.warning("Tu filtrado me ha dejado sin estaciones")
        st.stop()
    col1, col2 = st.columns([3, 2])
    with col1:
        if check_dis:
            mostrar_mapa(df, 13)

        else:
            mostrar_mapa(df)
    with col2:
        if not check_dis:
            bar_chart_variable(df, 'DISTRITO')

        if not check_op:
            bar_chart_variable(df, 'OPERADOR')

        bar_chart_variable(df, 'Nº CARGADORES')

def crear_filtro(df, tipo):

    opciones = df[tipo].unique()
    filtro = st.sidebar.selectbox("Selecciona tu " + tipo,
                        opciones)

    check = st.sidebar.checkbox("Quiero utilizar el filtro de " + tipo)

    return filtro, check


def filtro_cargadores(df):
    max_carg = df['Nº CARGADORES'].max()
    min_carg = df['Nº CARGADORES'].min()

    filtro = st.sidebar.select_slider("Selecciona el numero de cargadores",
                    range(min_carg, max_carg+1),
                     value=(min_carg, max_carg))

    return filtro


def aplicar_filtro(df, tipo, distrito):

    df = df[df[tipo] == distrito]

    return df

def aplicar_filtro_cargadores(df, cargadores):

    filtro = (df['Nº CARGADORES'] >= cargadores[0]) & (df['Nº CARGADORES'] <= cargadores[1])
    return df[filtro]
def mostrar_mapa(df, zoom=11):
    st.map(df, zoom=zoom)
