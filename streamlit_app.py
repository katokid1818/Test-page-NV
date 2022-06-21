import streamlit as st
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import os
import keras
import tensorflow as tf

from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint
from keras import datasets,Sequential,callbacks
from keras.layers import Conv2D, Dense, MaxPooling2D, Flatten
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from keras.layers import Dense,Activation,BatchNormalization,Dropout
from keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from keras import callbacks
from sklearn.metrics import precision_score, recall_score,confusion_matrix,classification_report,accuracy_score,f1_score
from keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import RMSprop
from matplotlib import scale
from sklearn.metrics import confusion_matrix
from keras.utils import np_utils
from keras.preprocessing.image import load_img, img_to_array,array_to_img,ImageDataGenerator, image
from tensorflow.keras.optimizers import RMSprop, SGD
import os

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


