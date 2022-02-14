#!/usr/bin/python3.9
from dotenv import load_dotenv
load_dotenv(dotenv_path="./secret/.env")

from flask_cors import CORS
from flask import Flask, request
from flask_socketio import SocketIO, emit
from question_handler import answer_question

app = Flask(__name__)

CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/heart")
def heartbeat():
    return "beat"

@socketio.on("connect")
def connect(sid):
    print(f"Socket connected: {sid}")

@socketio.on("disconnect")
def disconnect(sid):
    print(f"Socket connected: {sid}")

@socketio.on("question")
def question_socket(data):
    print(f"Question asked via socket: \"{data}\"")
    emit("answer", answer_question(data, None))

@app.route("/question", methods=["GET"])
def question_http():
    q = request.args.get("q")
    print(f"Question asked via http: \"{q}\"")
    return answer_question(q, None)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=3000)
