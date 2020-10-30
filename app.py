import config
import speech
import os
import random
import datetime
from pathlib import Path
AUDIO_PLAYER = speech.Speech(os.path.join(
    os.getcwd(), 'bin', 'audio'), "vomit_candy.wav", "come_closer.wav")

from flask import Flask, request, jsonify
app = Flask(__name__)

CLOSE_AREA_THRESHOLD = 70000
FAR_SOUNDS = ["come_here.wav", "come_closer.wav",
                "i_can_see_you.wav", "i_have_something_for_you.wav"]
CLOSE_SOUNDS = ["laugh.wav", "happy_halloween.wav", "happy_halloween_laugh.wav"]
LAST_AUDIO = datetime.datetime.now()

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

def aai_transform(w,h,x,y):
	""" A function to translate x,y coordinates from Always AI screen
	to a Pyeye screen given the AI screen w,h,x and y 
	Input: 4 ints, return 2 ints """

	PI_w, PI_h = 60,60
	# The PI screen has 0,0 in the center; the translate values
	# shift the AI x,y coordiate to the correct location.
	PI_translate_y = 30 
	PI_translate_x = 30

	new_y = ((PI_h/h)*y)+PI_translate_y
	new_x = ((PI_w/w)*w)+PI_translate_x

	return new_x, new_y

def aai_translate(x,y,w,h):
    """
    pi eyes expect x and y range between -30 to 30
    aai track from upper-left 0,0 to lower,right max_width, max_height
    This function converts the incoming aai data to conform to pi eyes
    """
    half_width = w/2
    adjusted_x = x - half_width
    new_x = adjusted_x * (30/half_width)

    half_height = h/2
    adjusted_y = y - half_width
    new_y = adjusted_y * (30/half_height)

    return new_x, new_y

def process_audio(area, close_threshold):
    '''
    Decide what audio file to play in response to how close
    someone is to the camera - using the bounding box area
    of the person detected from the computer vision detection
    service
    '''
    global LAST_AUDIO
    if area is None:
        return
    global AUDIO_PLAYER
    is_near = False
    audio_file = random.choice(FAR_SOUNDS)
    if int(area) < close_threshold:
        is_near = True
        audio_file = random.choice(CLOSE_SOUNDS)
    LAST_AUDIO = datetime.datetime.now()
    AUDIO_PLAYER.complete_then_play(audio_file)
    
    
def can_play_audio_again(sec):
    global LAST_AUDIO
    if LAST_AUDIO is None:
        LAST_AUDIO = datetime.datetime.now()
        return True
    now = datetime.datetime.now()
    if now > LAST_AUDIO + datetime.timedelta(seconds = sec):
        return True
    return False

@app.route("/aai_track", methods = ['POST'])
def aai_track():
    body = request.json
    x = body['X']
    y = body['Y']
    w = body['W']
    h = body['H']
    # result = aai_transform(w, h, x, y)
    result = aai_translate(x,y,w,h)
    config.DEST_X = result[0]
    config.DEST_Y = result[1]

    a = body['A']
    if can_play_audio_again(2) == True:
        process_audio(a, CLOSE_AREA_THRESHOLD)
    # print(f'app.py: aai_track: x:{x}, y:{y}, w:{w}, h:{h}')
    return "received"


if __name__ == "__main__":
    app.run (host = "0.0.0.0", port = 5000)
