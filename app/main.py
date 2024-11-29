from flask import Flask, render_template, request
from chatbot import Chatbot

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        user_input = request.form["user_input"]
        bot = Chatbot(user_input)
        return render_template("index.html", response=bot.model())
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)