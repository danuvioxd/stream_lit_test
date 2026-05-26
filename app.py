import pandas as pd
import streamlit as st
import  plotly.express as px

st.header('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

car_data = pd.read_csv(r'C:\Users\Denisse\Desktop\Damian\practicas\app_lanzar_moneda\stream_lit_test\vehicles_us.csv') # leer los datos
#creacion de botones para mostrar los graficos
hist_button = st.button('Construir histograma')
hist_button2 = st.button('Construir gráfico de dispersión')
     
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
         fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)
if hist_button2:
    st.write('Creacion de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico
    
    st.plotly_chart(fig, use_container_width=True)
#Actividad adicional: crear una casillas de verificación
build_histogram = st.checkbox('Construir un histograma')
build_histogram2 = st.checkbox('Construir un gráfico de dispersión')
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    fig = px.histogram(car_data, x="odometer") # crear un histograma
    
    st.plotly_chart(fig, use_container_width=True)
if build_histogram2:
    st.write('Creacion de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico
    
    st.plotly_chart(fig, use_container_width=True)