import streamlit as st
from PIL import Image
import io

def hacer_cuadrada(imagen):
    ancho, alto = imagen.size
    tamaño = min(ancho, alto)
    left = (ancho - tamaño) // 2
    top = (alto - tamaño) // 2
    right = left + tamaño
    bottom = top + tamaño
    return imagen.crop((left, top, right, bottom))

def escalar_imagen(imagen, tamaño_destino):
    return imagen.resize((tamaño_destino, tamaño_destino), Image.LANCZOS)

st.title("Procesador de Imágenes")
st.write("Sube una imagen para recortarla al centro y escalarla a 3000x3000 píxeles.")

uploaded_file = st.file_uploader("Elige una imagen", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    imagen = Image.open(uploaded_file)
    
    st.write("Imagen original:")
    st.image(imagen, use_column_width=True)
    
    if imagen.width != imagen.height:
        st.write("La imagen no es cuadrada. Se recortará al centro.")
        imagen = hacer_cuadrada(imagen)
    
    imagen_escalada = escalar_imagen(imagen, 3000)
    
    st.write("Imagen procesada:")
    st.image(imagen_escalada, use_column_width=True)
    
    # Convertir la imagen procesada a bytes para permitir la descarga
    buf = io.BytesIO()
    imagen_escalada.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    st.download_button(
        label="Descargar imagen procesada",
        data=byte_im,
        file_name="imagen_procesada.png",
        mime="image/png"
    )
