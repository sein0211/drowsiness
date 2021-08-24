from flask import Blueprint
from flask import render_template, Response
import cv2

bp = Blueprint('camera', __name__, url_prefix='/camera')

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()
        return frame

def generate(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n'
               + cv2.imencode('.jpg', cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))[1].tobytes()+ b'\r\n')

@bp.route('/')
def camera():
    return render_template('camera.html')

@bp.route('/video_feed')
def video_feed():
    return Response(generate(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')