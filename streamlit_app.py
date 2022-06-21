import streamlit as st
import pandas as pd
import numpy as np

st.title('Count the number of cows on the farm')

DATA_URL = ('https://drive.google.com/file/d/14nQpk8gInuhtlLiWr6-WedQjmDmdRF1_/view?usp=sharing')

#Nhan file upload len
file = st.file_uploader("Choose a file")
name_file =st.text_input('Name of file: ')

#if file is not None:
#            file = str(file)
#            img = load_img(


