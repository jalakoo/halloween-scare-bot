# import settings
import config
# import eyes
from flask import Flask, request
app = Flask(__name__)

# settings.init("foo")
# TEST=""

@app.route("/test")
def test():
    # global TEST
    config.TEST = request.args.get('test')
    return f"TEST={config.TEST}"

@app.route("/start")
def start():
    global SHOULD_RUN
    SHOULD_RUN = True
    # global TEST
    # startEyes()
    # eyes.start_eyes(TEST)
    import eyes
    return "Started app"

@app.route("/stop")
def stop():
    global SHOULD_RUN
    SHOULD_RUN = False
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


if __name__ == "__main__":
    app.run (host = "0.0.0.0", port = 5000)
