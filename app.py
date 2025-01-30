import streamlit as st
from PIL import Image, ImageFilter
import cv2
import numpy as np

# Initialize session state for camera
if "open_camera" not in st.session_state:
    st.session_state.open_camera = False

# Button to open the camera
if st.button("Open Camera", use_container_width=True):
    st.session_state.open_camera = True  # Set flag to show camera

# Show camera only when button is clicked
if st.session_state.open_camera:
    camera_image = st.camera_input("Capture an Image")
    
    # Process the image after capturing
    if camera_image:
        
        # Open the image
        img = Image.open(camera_image)
        
        # Convert to grayscale
        gray_img = img.convert("L")

        # Apply blur effect
        blurred_img = img.filter(ImageFilter.GaussianBlur(5))

        # Convert to OpenCV format for edge detection
        img_cv = np.array(img)
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(img_cv, 100, 200)  # Edge detection
        edges_img = Image.fromarray(edges)

        # Display images in a 2x2 grid
        col1, col2 = st.columns(2)

        with col1:
            st.image(img, caption="Original", use_container_width=True)
            st.image(gray_img, caption="Grayscale", use_container_width=True)

        with col2:
            st.image(blurred_img, caption="Blurred", use_container_width=True)
            st.image(edges_img, caption="Edges", use_container_width=True)
