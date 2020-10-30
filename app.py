import config
import speech
import os
from pathlib import Path
AUDIO_PLAYER = speech.Speech(os.path.join(
    os.getcwd(), 'bin', 'audio'), "vomit_candy.wav", "come_closer.wav")

from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/test")
def test():
    # global TEST
    config.TEST = request.args.get('test')
    return f"TEST={config.TEST}"

@app.route("/audio_test")
def audio_test():
    AUDIO_PLAYER.complete_then_play("vomit_candy.wav")
    resp = jsonify(success=True)
    return resp

@app.route("/play_audio", methods=['POST'])
def play_audio():
    body = request.json
    audio_file = body['file']
    AUDIO_PLAYER.complete_then_play(audio_file)
    resp = jsonify(success=True)
    return resp

@app.route("/start")
def start():
    config.SHOULD_RUN = True
    # global TEST
    # startEyes()
    # eyes.start_eyes(TEST)
    import eyes
    return "Started app"

@app.route("/stop")
def stop():
    config.SHOULD_RUN = False
    return "Stopped app"

@app.route("/human", methods = ['POST'])
def human_detected():
    response = jsonify({"human":"detected"})
    return response

@app.route("/look", methods = ['POST'])
def look():
    body = request.json
    config.DEST_X = body['DEST_X']
    config.DEST_Y = body['DEST_Y']
    response = jsonify(body)
    return response

@app.route("/aai_track", methods = ['POST'])
def aai_track():
    body = request.json
    x = body['X']
    y = body['Y']
    w = body['W']
    h = body['H']
    # print(f'app.py: aai_track: x:{x}, y:{y}, w:{w}, h:{h}')
    return "received"


if __name__ == "__main__":
    app.run (host = "0.0.0.0", port = 5000)
