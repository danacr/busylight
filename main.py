import os
from flask import Flask, render_template, Response, request, redirect, url_for
from busylight.lights.embrava import Blynclight

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/green/", methods=['POST'])
def green():
    os.system('/home/kali/.local/bin/busylight on green')

    return render_template('index.html');

@app.route("/red/", methods=['POST'])
def red():
    os.system('/home/kali/.local/bin/busylight on red')

    return render_template('index.html');

@app.route("/blinkred/", methods=['POST'])
def blinkred():
    os.system('/home/kali/.local/bin/busylight blink red')

    return render_template('index.html');

@app.route("/off/", methods=['POST'])
def off():
    os.system('/home/kali/.local/bin/busylight off')

    return render_template('index.html');

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)