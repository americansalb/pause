from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def pause_response():
    time.sleep(5)
    return "Done"
