import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
import mysql.connector


# Titre et image
st.title("Down Jones")
image = Image.open('./michael.jfif')
st.image(image)

# Data
# data1 = pd.read_csv("trade5.csv")
config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'port': '3300',
    'database': 'downjones',
    'raise_on_warnings': True,
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()
cursor.execute("""select * from trade5 """)
#fetchall prend toutes les données sous forme de tableau.
dataun = cursor.fetchall()
data1 = pd.DataFrame(dataun)
#Renommer les colonnes.
data1.columns = ["Index", "Annee", "Closing value", "Change in points", "Change in percent"]


# Selection
#symbols = data1.columns.sort_values().tolist()
#on prends les table pour les mettres dans une liste pour pouvoir les inserer dans le selecteur.
sy = ["Closing value", "Change in points", "Change in percent"]
ticker = st.sidebar.selectbox(
    'Choisir une valeur',
    sy)

# Affichage de la data
st.dataframe(data1.loc[:, ['Annee', ticker]])


# Affichage des graphiques
fig = go.Figure(data=go.Scatter(x=data1['Annee'], y=data1['Closing value']))

fig.update_layout(
    title={
        'text': "Valeur du Down Jones à la fermeture selon l'année",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
st.plotly_chart(fig, use_container_width=True)

fig = go.Figure(data=go.Scatter(x=data1['Annee'], y=data1['Change in points']))

fig.update_layout(
    title={
        'text': "Nombre de points du Down Jones à l'année",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
st.plotly_chart(fig, use_container_width=True)

fig = go.Figure(data=go.Scatter(x=data1['Annee'], y=data1['Change in percent']))

fig.update_layout(
    title={
        'text': "Change en pourcentage du Down Jones à l'année",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
st.plotly_chart(fig, use_container_width=True)
