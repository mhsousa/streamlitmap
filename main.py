import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
st.set_page_config(
        
	layout = 'wide',
        
	initial_sidebar_state = 'collapsed' 
)

df=pd.DataFrame({
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador'],
    'lat': [-23.5505, -22.9083, -19.9208, -12.9704],
    'lon': [-46.6333, -43.1728, -43.9389, -38.5019],
    'populacao': [12912.3, 226444.7, 533112.5, 147722.9],
    'cor':np.random.rand(4, 4).tolist()
})

df2=pd.DataFrame({
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador'],
    'lat': [-23.5505, -22.9083, -19.9208, -12.9704],
    'lon': [-46.6333, -43.1728, -43.9389, -38.5019],
    'populacao': [412912.3, 26444.7, 33112.5, 547722.9],
    'cor':np.random.rand(4, 4).tolist()
})

df3=pd.DataFrame({
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador'],
    'lat': [-23.5505, -22.9083, -19.9208, -12.9704],
    'lon': [-46.6333, -43.1728, -43.9389, -38.5019],
    'populacao': [1912.3, 3226444.7, 33112.5, 37722.9],
    'cor':np.random.rand(4, 4).tolist()
})

st.title("Teste mapa scatter")
st.map(df, size="populacao", color="cor", zoom=2)

c1, c2=st.columns(2)
with c1:
	st.map(df2, size="populacao", color="cor", zoom=3)
with c2:
	st.map(df3, size="populacao", color="cor", zoom=4)
