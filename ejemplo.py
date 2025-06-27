# Importo librerias necesarias
import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer

import pandas as pd 
import streamlit as st
from io import StringIO

# defino laa columnas
col1,col2=st.columns([0.7,0.3])

with col1:
    col1.write("Esto ")
    # Subir archivo selecccionando de carpetas en formato csv
    uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    #st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file,sep=";")
    datospyg = StreamlitRenderer(dataframe,appearance="dark")
    pyg.walk(dataframe,appearance="dark")

    #mdf=pd.DataFrame(dataframe)
    #nom_colum=mdf.columns
    #numero_col=mdf.shape[1]
    #print(list(nom_colum))
    #print(numero_col)
    
    #mi_eleccionX=st.pills("Elija las variables :", nom_colum, selection_mode="multi")
    #st.markdown(f"Sus variables seleccionadas: {mi_eleccionX}.")
