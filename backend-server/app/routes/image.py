from flask import Blueprint, request, jsonify
import numpy as np
import cv2
from ..services.yolo_service import predict_image

image_bp = Blueprint("image", __name__)

@image_bp.route("/predict", methods=["POST"])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image']
    np_arr = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    r = predict_image(img)

    boxes = []
    if r.boxes is not None:
        xyxy = r.boxes.xyxy.cpu().numpy()
        confs = r.boxes.conf.cpu().numpy()
        cls_idxs = r.boxes.cls.cpu().numpy()
        names = r.names

        for (x1, y1, x2, y2), conf, cls_idx in zip(xyxy, confs, cls_idxs):
            boxes.append({
                "box": [float(x1), float(y1), float(x2), float(y2)],
                "score": float(conf),
                "class": int(cls_idx),
                "label": names[int(cls_idx)]
            })

    return jsonify({"detections": boxes})
