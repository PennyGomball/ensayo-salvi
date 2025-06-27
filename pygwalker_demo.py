from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
# Import your data
dataf=pd.read_csv('/workspace/Miensayo/ventasejemplo.csv',sep=";")


 
pyg_app = StreamlitRenderer(dataf)
 
pyg_app.explorer()
