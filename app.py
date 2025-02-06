from tensorflow.keras.models import load_model
import numpy as np
import streamlit as st
from PIL import Image

# Cargar el modelo
model= load_model('fashion_mnist.keras')

# Crear la interface de usuario
st.title("Clasificador de Fashion MNIST")
st.write("Subir una imagen en escala de grises de 28x28 píxeles")

uploaded_file = st.file_uploader("Sube una imagen en escala de grises de 28x28 píxeles.", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Leer la imagen y mostrarla
    image = Image.open(uploaded_file).convert('L') # Convertir RGB a ByN
    image = image.resize((28, 28))
    image_array = np.array(imge) / 255.0 # Normalizar
    # El primer 1 indica que sólo hay una imagen, luego las dimensiones
    # y el último 1 indica que sólo hay una canal de color
    img_array=img_array.reshape(1,28,28,1)

    # Mostrar la imagen subida
    st.image(image, caption="Imagen subida", use_column_width=True)

    # Predicción
    prediction = model.predict(img_array)
    classes = ["Camiseta/Top", "Pantalón", "Jersey", "Vestido", "Abrigo", "Sandalia", "Camisa", "Zapatilla", "Bolso", "Bota"]
    st.write("Predicción:", classes[np.argmax(prediction)])
