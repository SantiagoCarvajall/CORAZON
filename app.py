import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Cargar el modelo y el escalador
svc_model = joblib.load('svc_model.jb')
scaler = joblib.load('scaler.jb')

# Título de la aplicación
st.title("Predictor de Problemas Cardiacos")
st.subheader("Elaborado por ® UNAB 2025")

# Sliders para la edad y colesterol
edad = st.slider("Edad", 25, 80, 55, 1)
colesterol = st.slider("Colesterol", 120, 600, 242, 2)

# Normalización de las variables
data = np.array([[edad, colesterol]])
data_normalizada = scaler.transform(data)

# Predicción usando el modelo SVC
prediccion = svc_model.predict(data_normalizada)

# Resultados
if prediccion == 1:
    st.image("https://www.clikisalud.net/wp-content/uploads/2018/09/problemas-cardiacos-jovenes.jpg")
    st.write("La predicción indica que **sufrirá problemas cardiacos**.")
else:
    st.image("https://img.freepik.com/foto-gratis/feliz-mujer-atractiva-bailando-divirtiendose-levantando-manos-preocupaciones-disfrutando-musica-pie-contra-pared-blanca_176420-38816.jpg?semt=ais_hybrid&w=740&q=80")
    st.write("La predicción indica que **no sufrirá problemas cardiacos**.")
