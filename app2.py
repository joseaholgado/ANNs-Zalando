import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Cargar el modelo
model = load_model("fashion_mnist.keras")

# Crear la interfaz de usuario
st.title("Clasificador Fashion MNIST")
st.write("Sube una imagen para clasificarla como una categoría de ropa.")

uploaded_file = st.file_uploader("Sube una imagen en escala de grises (28x28)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Procesar la imagen
    image = Image.open(uploaded_file).convert('L')
    image = image.resize((28, 28))
    img_array = np.array(image) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    # Mostrar la imagen subida
    st.image(image, caption="Imagen cargada", use_column_width=True)

    # Predicción
    prediction = model.predict(img_array)
    classes = ["Camiseta/Top", "Pantalón", "Suéter", "Vestido", "Abrigo",
               "Sandalia", "Camisa", "Zapatilla", "Bolso", "Botas"]
    st.write("Predicción:", classes[np.argmax(prediction)])

    # Mostrar probabilidades
    for i, prob in enumerate(prediction[0]):
        st.write(f"{classes[i]}: {prob:.2%}")

    # Clase con mayor probabilidad
    st.write("Predicción:", classes[np.argmax(prediction)])