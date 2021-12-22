import streamlit as st
import functions as ft

csv_name = 'red_recarga_acceso_publico _2021.csv'

ft.configuracion()
st.balloons()

datos_propios = st.sidebar.file_uploader("Tienes otros datos?", type=['csv'])

df = ft.cargar_datos(csv_name, datos_propios)

menu = st.sidebar.selectbox("Selecciona el menu:", ['home', 'datos', 'filtros'])

if menu == 'home':
    ft.home(df)

elif menu == 'datos':
    ft.datos(df)

elif menu == 'filtros':
    ft.datos_filtrados(df)
