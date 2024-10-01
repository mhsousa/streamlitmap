import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

df=pd.DataFrame({
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador'],
    'lat': [-23.5505, -22.9083, -19.9208, -12.9704],
    'lon': [-46.6333, -43.1728, -43.9389, -38.5019],
    'populacao': [12912.3, 226444.7, 533112.5, 147722.9],
    'cor':np.random.rand(4, 4).tolist()
})

st.title("Teste mapa scatter")
st.map(df, size="populacao", color="cor", zoom=3)
