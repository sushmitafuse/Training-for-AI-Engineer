from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/emotion_data"
mongo = PyMongo(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form.get("text"):
            # text = request.form.get("text")
            # mongo.save(text)
            mongo.db.users.insert_one({"text": request.form.get("text")})
        return "Done"
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
