import streamlit as st
import pandas as pd
st.balloons()
st.write('Todo va bien')
"hola que tal va todo?"

mi_df = pd.DataFrame({'A':[1, 2], 'B':[2,3]})

selected = st.checkbox("A tope")


if selected:
    st.write("Alguien ha hecho click")
    contento = st.button("Haz click si estas contento")

    if contento:
        st.write("Estoy tela contento")
else:
    st.write("Estoy triste")

option = st.sidebar.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

col1, col2 = st.columns(2)

col1.write("Estamos en la primera columna")
col2.write("estamos en la segunda columnas")

c1, c2 = st.columns(2)

with c2:

    st.write("Estamos en la segunda col")

st.write("estamos fuera")

with c1:
    st.write(mi_df)
    st.write("todo bien")
