from camera import Camera
from flask import Flask, Response, Request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/<param>')
def index(param=None):
    return render_template('index.html',name = param)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),mimetype='multipart/x-mixed-replace; boundary=frame')

def startServer():
    app.run(host='0.0.0.0', port=90, threaded=True)