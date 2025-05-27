from flask import Flask, request, jsonify
import cv2
import numpy as np
from ultralytics import YOLO
import base64
from PIL import Image
import io
import os
#import torch

app = Flask(__name__)

#print("CUDA Available:", torch.cuda.is_available())
#print("GPU Name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")

# Load YOLO model (assumes model file exists in the same directory)
# You can change this to your specific model path
#model = YOLO('model/yolov8x.pt')
MODEL_PATH = os.getenv(YOLO_MODEL, "runs/detect/train27/weights/best.pt")
MODEL = os.path.abspath(MODEL_PATH)

model = YOLO(MODEL)  # or 'yolov8s.pt', 'yolov8m.pt', etc.
#model = YOLO('yolov8m.pt')  # or 'yolov8s.pt', 'yolov8m.pt', etc.

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if image is provided
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400

        image_file = request.files['image']

        if image_file.filename == '':
            return jsonify({'error': 'No image selected'}), 400

        # Read image directly from memory
        image_bytes = image_file.read()

        # Convert bytes to PIL Image
        image = Image.open(io.BytesIO(image_bytes))

        # Convert PIL Image to numpy array for OpenCV
        image_array = np.array(image)

        # Convert RGB to BGR if needed (PIL uses RGB, OpenCV uses BGR)
        if len(image_array.shape) == 3 and image_array.shape[2] == 3:
            image_array = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)

        # Run YOLO prediction
        results = model(image_array)

        # Parse results
        predictions = []
        for result in results:
            boxes = result.boxes
            if boxes is not None:
                for box in boxes:
                    # Get bounding box coordinates
                    x1, y1, x2, y2 = box.xyxy[0].tolist()

                    # Get confidence score
                    confidence = float(box.conf[0])

                    # Get class ID and name
                    class_id = int(box.cls[0])
                    class_name = model.names[class_id]

                    prediction = {
                        'class_id': class_id,
                        'class_name': class_name,
                        'confidence': round(confidence, 4),
                        'bbox': {
                            'x1': round(x1, 2),
                            'y1': round(y1, 2),
                            'x2': round(x2, 2),
                            'y2': round(y2, 2)
                        }
                    }
                    predictions.append(prediction)

        # Return JSON response
        response = {
            'status': 'success',
            'predictions': predictions,
            'total_detections': len(predictions)
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'model_loaded': True})

if __name__ == '__main__':
    print("Starting YOLO Flask API...")
    print("Endpoints:")
    print("  POST /predict - Upload image for object detection")
    print("  GET /health - Health check")
    app.run(debug=True, host='0.0.0.0', port=5000)
