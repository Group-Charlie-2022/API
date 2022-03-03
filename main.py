#!/usr/bin/python3.9
from dotenv import load_dotenv
load_dotenv(dotenv_path="./secret/.env")

from flask_cors import CORS
from flask import Flask, request, session
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
    if not session["history"]:
        session["history"] = []
    history = session["history"]
    answer = answer_question(data, history)
    session["history"].append((data, answer))
    emit("answer", answer)

@app.route("/question", methods=["GET"])
def question_http():
    q = request.args.get("q")
    print(f"Question asked via http: \"{q}\"")
    if not session["history"]:
        session["history"] = []
    history = session["history"]
    answer = answer_question(q, history)
    session["history"].append((q, answer))
    return answer

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=3000)
