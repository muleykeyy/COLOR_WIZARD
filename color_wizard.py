import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import streamlit as st
import numpy as np

title = '<h1 style="font-family:Arial Bold; color:Purple; font-size: 72px;">🎨 COLOR WIZARD</h1>'
st.markdown(title,unsafe_allow_html=True)
st.subheader("😎 Check out the examples before you start.")
exm=Image.open("allex.jpeg")
st.image(exm,"EXAMPLES")
st.subheader("🎥 Upload the photo you want to play with the colors.")
img_file_buffer = st.file_uploader("Upload an image",type=["jpg","jpeg"])

if img_file_buffer is not None:
    image = Image.open(img_file_buffer,mode="r") 
    st.image(image, caption="Original Image")
    img_array = np.array(image)
    st.subheader("✅ Now you can play with the colors of the photo with the slider")
    st.warning("This process may take some time 😕")
    img_flat=img_array.reshape(img_array.shape[0]*img_array.shape[1],3)
    clusters=st.slider(max_value=30,min_value=2,value=8,step=2,label="Level")
    kmeans=KMeans(n_clusters=clusters,random_state=0).fit(img_flat)
    for i in np.unique(kmeans.labels_):
        img_flat[kmeans.labels_==i,:]=kmeans.cluster_centers_[i]
    img2=img_flat.reshape(img_array.shape)
    st.image(img2)
