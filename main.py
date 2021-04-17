import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import tensorflow as tf 
from PIL import Image
import os
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Dense , Flatten, Dropout
import time
data = []
labels = []
classes = 43
cur_path = os.getcwd() # gets the current working directory

for i in range(1): # 0 to 42
    path = os.path.join(cur_path,'Data/Train',str(i))
    images = os.listdir(path)
    # print(images[0:11])
    # time.sleep(5)
    for a in images:
        try:
            imagePath=path+'/'+a
            image =Image.open(imagePath)
            image = image.resize((30,30))
            image = np.array(image)
            data.append(image)
            labels.append(i)
            print("loaded:"+imagePath)
        except:
            print("Error loading image")
        # time.sleep(5)
data = np.array(data)
labels=np.array(labels)

