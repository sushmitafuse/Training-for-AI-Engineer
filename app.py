from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from src.models.train_model import load_model
from src.models.predict_model import predict_emotion
from src.models.bert_model.predict_model import load_bert, predict_bert
from src.models.bert_model import tokenization
import numpy as np
from src.models.bert_model import tokenize_sentence

from bson.json_util import dumps
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/emotion_data"
mongo = PyMongo(app)

tokenizer, model = load_model()
# bert_model = load_bert()


# @app.route("/")
# def home():
#     return "This is home"

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        if request.form.get("text"):
            text = request.form.get("text")
            # mongo.save(text)
            model_name = str(request.form.get("model_name"))
            if model_name == "LSTM":
                emotion, max_value = predict_emotion(text, tokenizer, model)
            else:
                emotion, max_value = predict_bert(text, bert_model)
            
            mongo.db.users.insert_one({"text": request.form.get("text"), "model": model_name, "emotion": emotion, "confidence": max_value})
        return render_template("result.html", emotion=emotion)
    else:
        return render_template("index.html")


@app.route('/users', methods=['GET'])
def user_list():
    if request.method == 'GET':
        query = request.args
        data = mongo.db.users.find(query)
        data = list(data)

        return render_template("records.html", data=data)


@app.route('/users/<user_id>/', methods=['GET'])
def user(user_id):
    data = []
    if request.method == 'GET':
        try:
            user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
            data.append(user)

        except:
            return "<h2>Record Not Found</h2>"

        return render_template("records.html", data=data)
    

@app.route('/users/delete/<user_id>', methods=['POST'])
def delete_user(user_id):
    db_response = mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    if db_response.deleted_count == 1:
        return redirect(url_for('user_list'))
    else:
        return "<h2>Record Not Found</h2>"


 

# @app.route("/bert", methods=["GET", "POST"])
# def bert_predict():
#     if request.method == "POST":
#         if request.form.get("text"):
#             text = request.form.get("text")
#             # mongo.save(text)
#             mongo.db.users.insert_one({"text": request.form.get("text")})
#             emotion = predict_bert(text, bert_model)
#             print("The predicted emotion is",emotion)
#         return emotion
#     else:
#         return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
