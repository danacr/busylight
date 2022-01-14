from flask import Flask, render_template, Response, request, redirect, url_for
from busylight.lights.embrava import Blynclight

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/green/", methods=['POST'])
def green():
    light = Blynclight.first_light()

    light.on((255, 255, 255))
    return render_template('index.html');

@app.route("/off/", methods=['POST'])
def off():
    light = Blynclight.first_light()

    light.off()
    return render_template('index.html');

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)