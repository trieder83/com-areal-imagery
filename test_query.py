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

image_path = "data/ship/test/images/02e39612d_jpg.rf.cc5483bb711f080d12b644ff62cf977a.jpg"
image = cv2.imread(image_path)
print("image read")

# Get the size of the image
height, width, channels = image.shape
print(f"The image has dimensions {width}x{height} and {channels} channels.")


# load trained model
model = YOLO('runs/detect/train12/weights/best.pt')
# yolo11n.pt  yolo11x.pt  yolov8n.pt  yolov8x.pt
#model = YOLO('model/yolov8n.pt') # noboard, nothing, airplain

# Run inference with 
results = model(image_path)

# Check if results is a list
if isinstance(results, list):
    print("is a list")
    # Access the Results object for the first (and likely only) image
    if results:
        #df = results[0].pandas().xyxy[0]
        print(results[0].to_json())
        results[0].show()
        #print(results[0].save_dir)
        results[0].save('runs/detect/predict/')
    else:
        print("No detections found.")
else:
    # If it's a single Results object (which it should be for a single image)
    df = results.pandas().xyxy[0]
    print(df)
    results.show()
    results.save(save_dir='runs/detect/predict')

print("finished")
