# Halloween Scare Bot

Halloween bot incorporating:
- Computer Vision for tracking tricker treaters
- [Pi eyes](https://learn.adafruit.com/animated-snake-eyes-bonnet-for-raspberry-pi) for display eyes onto a monitor (or OLED/TFT displays)
- Audio output for scaring children

## Archtiecture
This flask server controls the pi-eyes and audio effects.

The computer vision docker image is a separate app that will pass detection info this app for processing.

## Running
1. ssh to device (ie `ssh pi@raspberrypi.local`)
2. goto this app's folder
3. Run one of the flask run options (see below) or `./start.sh`

## Virtual Env
Official docs: https://docs.python.org/3/tutorial/venv.html
Save requirements.txt: `pip freeze > requirements.txt`
Install from requirements.txt: `python3 -m pip install -r requirements.txt`
Create: `python3 -m venv <virtual_bin>`
Activate: `source venv/bin/activate`
Deactivate: `deactivate`

## Flask
run: `python3 app.py`
run w/ external network access: `flask run --host=0.0.0.0`

## Troubleshooting
PROBLEM:
```
Git 'fatal: Unable to write new index file'
```
SOLUTION:
1. duplicate .git/index file
2. delete original
3. rename copy to .git/index