from camera import Camera
from flask import Flask, Response, request, render_template

app = Flask(__name__)

@app.route('/')
def index(param=None):
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'

def startServer():
    app.run(host='0.0.0.0', port=96, threaded=True)