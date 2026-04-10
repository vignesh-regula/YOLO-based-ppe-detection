import os
from ultralytics import YOLO

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../../models/ppe_model.pt")

model = YOLO(MODEL_PATH)

def predict_image(img):
    results = model.predict(source=img, imgsz=640, conf=0.25, iou=0.45, verbose=False)
    return results[0]

def predict_frame(frame):
    results = model.predict(source=frame, imgsz=640, conf=0.25, iou=0.45, verbose=False)
    return results[0]
