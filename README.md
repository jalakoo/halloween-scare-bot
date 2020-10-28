# Halloween Scare Bot

Halloween bot incorporating:
- Computer Vision for tracking tricker treaters
- [Pi eyes](https://learn.adafruit.com/animated-snake-eyes-bonnet-for-raspberry-pi) for display eyes onto a monitor (or OLED/TFT displays)
- Audio output for scaring children

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