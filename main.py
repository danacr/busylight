import os
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)
busylight_path = '/home/kali/.local/bin/busylight'


def battery():
    percentage = subprocess.run(
        ['cat', '/sys/class/power_supply/cw2015-battery/capacity'], stdout=subprocess.PIPE).stdout
    status = subprocess.run(
        ['cat', '/sys/class/power_supply/cw2015-battery/status'], stdout=subprocess.PIPE).stdout
    return percentage + "%, " + status


@app.route("/")
def index():
    return render_template('index.html', battery=battery())


@app.route("/control/", methods=['POST'])
def control():
    match request.form.get('action'):
        case "Green":
            subprocess.run([busylight_path, 'on', 'green'], stdout=subprocess.PIPE)
        case "Red":
            subprocess.run([busylight_path, 'on', 'red'], stdout=subprocess.PIPE)
        case "Blink Red":
            subprocess.run([busylight_path, 'blink', 'red'], stdout=subprocess.PIPE)
        case "_":
            subprocess.run([busylight_path, 'off'], stdout=subprocess.PIPE)

    return render_template('index.html', battery=battery())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
