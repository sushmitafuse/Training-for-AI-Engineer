import pickle
from tensorflow import keras

model_path = "checkpoints/glove_lstm/Glove_Lstm_Model.h5"
weights_path = "checkpoints/glove_lstm/Glove_Lstm_weights.hdf5"
tokenizer_path = "checkpoints/tokenizer/tokenizer.pickle"

def load_model():
    with open(tokenizer_path, 'rb') as handle:
        tokenizer = pickle.load(handle)

    model = keras.models.load_model(model_path)  
    model.load_weights(weights_path)
    return tokenizer, model