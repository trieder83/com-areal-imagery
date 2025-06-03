from ultralytics import YOLO


import squarify
import matplotlib.pyplot as plt
import cv2
import os
import random
import pandas as pd
import matplotlib.image as mpimg
import seaborn as sns
import splitfolders
#import torch

#print("CUDA Available:", torch.cuda.is_available())
#print("GPU Name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")

sns.set_style('darkgrid')

BASE_MODEL= os.getenv("BASE_MODEL","model/yolov8m.pt")
#model = YOLO('model/yolov8x.pt')
model = YOLO(BASE_MODEL)

height = 640
DATASET_RAW = os.getenv("DATASET_RAW","datasets/Terrorflags/project-2-at-2025-05-23-12-44-f448e586")
DATASET = os.getenv("DATASET","datasets/Terrorflags")
EPOCH = int(os.getenv("EPOCH","40"))

# split training data
def splitdata(datasetpath, splitdataset):
    splitfolders.ratio(datasetpath,splitdataset, seed=1337, group_prefix=True, ratio=(.7, 0.2,0.1))

# if th dataset is not split TODO control by flag
if not os.path.exists(os.path.join(os.path.abspath(DATASET),"train")):
    splitdata(os.path.abspath(DATASET_RAW), os.path.abspath(DATASET))

# Training the model
model.train(data = os.path.abspath(os.path.join(os.path.abspath(DATASET),"data.yaml")),
            epochs = EPOCH,
            imgsz = height,
            seed = 42,
            batch = 8,
            #dropout=0.2,
            workers = 4)

print("finished")
