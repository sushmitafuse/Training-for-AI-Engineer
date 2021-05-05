import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

emotions = {0: 'anger', 1:'disgust', 2:'fear', 3:'guilt', 4:'joy', 5:'sad', 6:'shame'}

    
    
def predict_emotion(text, tokenizer, model):
    tokenizedSeq = tokenizer.texts_to_sequences([text])
    padSeq = pad_sequences(tokenizedSeq,maxlen=len(tokenizedSeq[0]))
    sentiment_value = np.argmax(model.predict(padSeq))
    sentiment = emotions[sentiment_value]
    return sentiment

