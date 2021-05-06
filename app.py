from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from src.models.train_model import load_model
from src.models.predict_model import predict_emotion

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/emotion_data"
mongo = PyMongo(app)

tokenizer, model = load_model()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form.get("text"):
            text = request.form.get("text")
            # mongo.save(text)
            mongo.db.users.insert_one({"text": request.form.get("text")})
            emotion = predict_emotion(text, tokenizer, model)
        return emotion
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)

