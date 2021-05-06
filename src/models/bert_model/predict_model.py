from tensorflow.keras.models import load_model
import tensorflow_hub as hub
from . import tokenization

import numpy as np

from . import tokenize_sentence


mapping = {
    0: 'anger',
    1: 'disgust',
    2: 'fear',
    3: 'guilt',
    4: 'joy',
    5: 'sadness',
    6: 'shame'
}

def load_bert():
# module_url = 'https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/2'
  reloaded_model = load_model('/home/sushmita/Documents/7batch /Training-for-AI-Engineer/checkpoints/bert/emotion_detection_bert.h5', custom_objects={'KerasLayer': hub.KerasLayer})
  return reloaded_model



def predict_bert(sentence,model):
# Input to bert_encode should be a list
  module_url = '/home/sushmita/Documents/7batch /Training-for-AI-Engineer/checkpoints/bert_en_uncased_L-12_H-768_A-12_2'
  bert_layer = hub.KerasLayer(module_url, trainable=True)
  vocab_file = bert_layer.resolved_object.vocab_file.asset_path.numpy()
  do_lower_case = bert_layer.resolved_object.do_lower_case.numpy()
  tokenizer = tokenization.FullTokenizer(vocab_file, do_lower_case)
  MAX_LEN = 300
  train_input = tokenize_sentence.bert_encode(list(sentence), tokenizer, max_len=MAX_LEN)
  pred = model.predict(train_input)
  result = []
  for value in pred:
    result.append(mapping[np.argmax(value)])
  return result[0]
  
