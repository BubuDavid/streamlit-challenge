import streamlit as st #jerjerjer
from PIL import Image
import PIL
from bounding import bounding_boxes
import urllib

img = st.markdown('''
# YoLov8n Demo - HackCIMaT
------

¡Hola! En esta página web puedes probar el modelo YoLov8n entrenado para detectar objetos en imágenes.
Toda esta aplicación tiene menos de 100 líneas de código, y está hecha con [Streamlit](https://streamlit.io/).
Puedes revisar el código en [GitHub](https://github.com/GabrielMissael/CV_YoLo_workshop)

Puedes probarlo con imágenes de internet, subir una imagen desde tu computadora, o tomar una foto con tu cámara web.
''')

# Sidebar
st.sidebar. markdown ('''
## opciones
''')
#SI SE PUEDE, SI SE PUEDE 🥳
# Select image source
source = st.sidebar.selectbox ("Saca la imágen", ("Internet", "Subir imagen", "Cámara web"))

# Load image
if source == "Internet":
    url = st.sidebar.text_input("URL de la imagen", "")
    if url != "": #ENSEEEEERIOOOO?????
        try:
            img = Image.open(urllib.request.urlopen(url))
        except:
            st.sidebar.error("No se pudo cargar la imagen")
            img = None
    else:
        img = None


elif source == "Subir imagen":
    img = st.sidebar.file_uploader("Sube una imagen", type=['png', 'jpg', 'jpeg'])

    if img is not None:
        img = Image.open(img)

elif source == "Cámara web":
    img_photo = st.camera_input(label="Toma una foto 📷", key="camera")

    if img_photo is not None:
        img = Image.open(img_photo)
    else:
        img = None

# Show image (POFAVO)
if img is not None:
    if source == "Cámara web":
        st.image(img, caption='Imagen original', use_column_width=True)
    # Show bounding boxes
    st.pyplot(bounding_boxes(img))
# EXITO :)