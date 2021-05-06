from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from src.models.train_model import load_model
from src.models.predict_model import predict_emotion
from src.models.bert_model.predict_model import load_bert, predict_bert
from src.models.bert_model import tokenization
import numpy as np
from src.models.bert_model import tokenize_sentence

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/emotion_data"
mongo = PyMongo(app)

tokenizer, model = load_model()
bert_model = load_bert()


# @app.route("/")
# def home():
#     return "This is home"

@app.route("/glove", methods=["GET", "POST"])
def rnn_predict():
    if request.method == "POST":
        if request.form.get("text"):
            text = request.form.get("text")
            # mongo.save(text)
            mongo.db.users.insert_one({"text": request.form.get("text")})
            emotion = predict_emotion(text, tokenizer, model)
        return emotion
    else:
        return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def bert_predict():
    if request.method == "POST":
        if request.form.get("text"):
            text = request.form.get("text")
            # mongo.save(text)
            mongo.db.users.insert_one({"text": request.form.get("text")})
            emotion = predict_bert(text, bert_model)
            print("The predicted emotion is",emotion)
        return emotion
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
