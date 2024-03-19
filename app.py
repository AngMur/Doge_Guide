from flask import Flask, render_template, request

from chatbot import ChatBot

cb = ChatBot()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    input = request.form["msg"]
    return cb.get_response(input)


if __name__ == '__main__':
    app.run()
