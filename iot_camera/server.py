from flask import Flask, Response, Request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/<param>')
def index(param=None):
    return render_template('index.html',name = param)

def startServer():
    app.run(host='0.0.0.0', port=90, threaded=True)