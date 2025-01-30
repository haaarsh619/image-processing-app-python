import streamlit as st
from PIL import Image, ImageFilter
import cv2
import numpy as np

# Start the camera
with st.expander("Start Camera"):
    camera_image = st.camera_input("Capture an Image")

# Process the captured image
if camera_image:
    img = Image.open(camera_image)
    
    # Convert to grayscale
    gray_img = img.convert("L")

    # Apply blur
    blurred_img = img.filter(ImageFilter.GaussianBlur(5))

    # Convert to OpenCV format for edge detection
    img_cv = np.array(img)
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(img_cv, 100, 200)  # Edge detection
    edges_img = Image.fromarray(edges)

    # Display images side by side
    st.subheader("Original Image")
    st.image(img, caption="Original", use_container_width=True)

    st.subheader("Grayscale Image")
    st.image(gray_img, caption="Grayscale", use_container_width=True)

    st.subheader("Blurred Image")
    st.image(blurred_img, caption="Blurred", use_container_width=True)

    st.subheader("Edge Detection")
    st.image(edges_img, caption="Edges", use_container_width=True)