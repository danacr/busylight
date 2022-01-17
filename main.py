import os
from flask import Flask, render_template, Response, request, redirect, url_for

app = Flask(__name__)
busylight_path = '/home/kali/.local/bin/busylight'


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/control/", methods=['POST'])
def control():
    match request.form.get('action'):
        case "Green":
            os.system(busylight_path + ' on green')
        case "Red":
            os.system('/home/kali/.local/bin/busylight on red')
        case "Blink Red":
            os.system('/home/kali/.local/bin/busylight blink red')
        case "_":
            os.system('/home/kali/.local/bin/busylight off')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
