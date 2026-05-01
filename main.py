import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "simple_rnn.keras")

@st.cache_resource
def load_my_model():
    return load_model(model_path, compile=False)

model = load_my_model()

st.title("IMDB Sentiment Analysis")

text = st.text_area("Enter review")

if st.button("Predict"):
    st.write("Result here")