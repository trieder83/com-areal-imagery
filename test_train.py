from ultralytics import YOLO


import squarify
import matplotlib.pyplot as plt
import cv2
import os
import random
import pandas as pd
import matplotlib.image as mpimg
import seaborn as sns

sns.set_style('darkgrid')

model = YOLO('model/yolov8n.pt')


# Load an image using OpenCV
image = cv2.imread("data/ship/train/images/06573fb73_jpg.rf.1cac92cdc84d92789ac1304b719bbcbf.jpg")
print("image read")

# Get the size of the image
height, width, channels = image.shape
print(f"The image has dimensions {width}x{height} and {channels} channels.")


model = YOLO('model/yolov8x.pt')

# Training the model
#model.train(data = '/kaggle/input/ships-in-aerial-images/ships-aerial-images/data.yaml',
model.train(data = './datasets/data.yaml',
            epochs = 20,
            imgsz = height,
            seed = 42,
            batch = 8,
            workers = 4)

print("finished")
