import streamlit as st
from PIL import Image, ImageFilter
import cv2
import numpy as np


def imageConvert(captured_img):
    # Open the image
    img = Image.open(captured_img)
    
    # Convert to grayscale
    gray_img = img.convert("L")

    # Apply blur effect
    blurred_img = img.filter(ImageFilter.GaussianBlur(5))

    # Convert to OpenCV format for edge detection
    img_cv = np.array(img)
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(img_cv, 100, 200)  # Edge detection
    edges_img = Image.fromarray(edges)
    
    return img, gray_img, blurred_img, edges_img

# Initialize session state for camera
if "open_camera" not in st.session_state:
    st.session_state.open_camera = False

st.title("Image Processing")
st.text("Upload or Capture From Camera")
# Button to open the camera
if st.button("Open Camera", use_container_width=True):
    st.session_state.open_camera = True  # Set flag to show camera
st.text("Or")

# Button to upload images
uploaded_image = st.file_uploader("Upload Image")

# Process the image after capturing
if st.session_state.open_camera:
    camera_image = st.camera_input("Capture an Image")    
    filteredImages= imageConvert(camera_image)
if uploaded_image :
    filteredImages = imageConvert(uploaded_image)
    # Display images in a 2x2 grid
    col1, col2 = st.columns(2)

    with col1:
        st.image(filteredImages[0], caption="Original", use_container_width=True)
        st.image(filteredImages[1], caption="Grayscale", use_container_width=True)

    with col2:
        st.image(filteredImages[2], caption="Blurred", use_container_width=True)
        st.image(filteredImages[3], caption="Edges", use_container_width=True)
