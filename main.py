import os
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)
busylight_path = '/home/kali/.local/bin/busylight'


def battery():
    percentage = subprocess.run(
        ['cat', '/sys/class/power_supply/cw2015-battery/capacity'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    status = subprocess.run(
        ['cat', '/sys/class/power_supply/cw2015-battery/status'], stdout=subprocess.PIPE).stdout.decode('utf-8').lower()
    return percentage + "%, " + status


@app.route("/", methods=['GET', 'POST'])
def control():
    if request.method == 'POST':
        match request.form.get('action'):
            case "Green":
                subprocess.run([busylight_path, 'on', 'green'],
                               stdout=subprocess.PIPE)
            case "Red":
                subprocess.run([busylight_path, 'on', 'red'],
                               stdout=subprocess.PIPE)
            case "Blue":
                subprocess.run([busylight_path, 'on', 'blue'],
                               stdout=subprocess.PIPE)
            case "Yellow":
                subprocess.run([busylight_path, 'on', 'orange'],  # Orange looks more like yellow than yellow
                               stdout=subprocess.PIPE)
            case "Purple":
                subprocess.run([busylight_path, 'on', 'purple'],
                               stdout=subprocess.PIPE)
            case "White":
                subprocess.run([busylight_path, 'on', 'white'],
                               stdout=subprocess.PIPE)
            case "Blink Red":
                subprocess.run([busylight_path, 'blink', 'red'],
                               stdout=subprocess.PIPE)
            case "Off":
                subprocess.run([busylight_path, 'off'], stdout=subprocess.PIPE)
    return render_template('index.html', battery=battery())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
