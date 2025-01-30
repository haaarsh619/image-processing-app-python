import streamlit as st
from  PIL import Image

# Start the camera
with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

# Create a Image instance
if camera_image:
    img = Image.open(camera_image)

    # Converting the image to grayscale
    gray_img = img.convert("L")

    # rendering the new grayscaled image
    st.image(gray_img)