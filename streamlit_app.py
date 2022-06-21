import streamlit as st
import pandas as pd
import numpy as np

import os
import keras
import tensorflow as tf

from keras.preprocessing.image import load_img, img_to_array,array_to_img,ImageDataGenerator, image

from keras.models import load_model

st.title('Count the number of cows on the farm')

DATA_URL = ('https://drive.google.com/file/d/14nQpk8gInuhtlLiWr6-WedQjmDmdRF1_/view?usp=sharing')

model = load_model('checkpoint_cow.h5')

#Nhan file upload len
file = st.file_uploader("Choose a file")
name_file =st.text_input('Name of file: ')

#if file is not None:
#            file = str(file)
#            img = load_img(


