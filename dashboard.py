import streamlit as st 
import pandas as pd 
import plotly.express as px

def main():
    data = pd.read_excel('Base.xlsx',sheet_name='Base')
    titulo = 'Dashboard - Projeto Vendas'
    st.set_page_config(page_title=titulo, layout='wide')
    st.title(titulo)

    ano = data ['Ano'].unique()
    paises = data ['País'].unique()

    filtro_ano=st.sidebar.selectbox('selecione o ano:', options=['todos'] + sorted (ano), index=0)
    filtro_pais = st.sidebar.selectbox('selecione o pais:', options=['todos'] + sorted(paises), index=0)

    data_filtrada = data.copy()
    if filtro_ano != "todos":
        data_filtrada = data_filtrada[data_filtrada['Ano']== filtro_ano]
    if filtro_pais != "todos":
        data_filtrada = data_filtrada[data_filtrada['País']== filtro_pais]

main()
     
