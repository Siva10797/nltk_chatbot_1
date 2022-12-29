from flask import Flask, render_template, request
from preprocessing import chatbot_response

app = Flask(__name__,template_folder='template')
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=False)