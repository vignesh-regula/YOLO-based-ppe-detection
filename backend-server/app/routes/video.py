from flask import Blueprint, request, jsonify, Response
import os, uuid, cv2
from ..services.yolo_service import predict_frame

video_bp = Blueprint("video", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@video_bp.route("/upload", methods=["POST"])
def upload_videos():
    saved_videos = {}

    for key in request.files:
        file = request.files[key]
        filename = f"{uuid.uuid4().hex}.mp4"
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)
        saved_videos[key] = filename

    return jsonify(saved_videos)


def generate_video_stream(video_filename):
    video_path = os.path.join(UPLOAD_FOLDER, video_filename)
    cap = cv2.VideoCapture(video_path)

    while True:
        success, frame = cap.read()
        if not success:
            break

        r = predict_frame(frame)

        if r.boxes is not None:
            boxes = r.boxes.xyxy.cpu().numpy()
            confs = r.boxes.conf.cpu().numpy()
            cls_idxs = r.boxes.cls.cpu().numpy()
            names = r.names

            for (x1, y1, x2, y2), conf, cls_idx in zip(boxes, confs, cls_idxs):
                x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
                label = names[int(cls_idx)]
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.putText(frame, f"{label} {conf:.2f}",
                            (x1, y1-5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0,255,0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +
               frame_bytes + b'\r\n')

    cap.release()


@video_bp.route("/stream/<video_filename>")
def stream_video(video_filename):
    return Response(generate_video_stream(video_filename),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
