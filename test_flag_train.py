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

#model = YOLO('model/yolov8x.pt')
model = YOLO('model/yolov8n.pt')

height = 640

# Training the model
#model.train(data = '/kaggle/input/ships-in-aerial-images/ships-aerial-images/data.yaml',
model.train(data = './datasets/Flags/data.yaml',
            epochs = 20,
            imgsz = height,
            seed = 42,
            batch = 8,
            workers = 4)

print("finished")
