from tensorflow.keras.models import load_model
import tensorflow_hub as hub
import tokenization

import numpy as np

import tokenize_sentence


mapping = {
    0: 'anger',
    1: 'disgust',
    2: 'fear',
    3: 'guilt',
    4: 'joy',
    5: 'sadness',
    6: 'shame'
}

print("Module url loading...")
print('---------------------------------------------')
# module_url = 'https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/2'
module_url = '../../checkpoints/bert_en_uncased_L-12_H-768_A-12_2'
bert_layer = hub.KerasLayer(module_url, trainable=True)
print('Module loaded')

vocab_file = bert_layer.resolved_object.vocab_file.asset_path.numpy()
do_lower_case = bert_layer.resolved_object.do_lower_case.numpy()
print('FullTokenizer starting')
tokenizer = tokenization.FullTokenizer(vocab_file, do_lower_case)
print('FullTokenizer completed')


MAX_LEN = 300

print('Emotion detection model loading...')
reloaded_model = load_model('/home/nishesh/Desktop/Work/Trainings/Training-for-AI-Engineer/checkpoints/bert/emotion_detection_bert.h5', custom_objects={'KerasLayer': hub.KerasLayer})
print('Model loaded')

# Input to bert_encode should be a list
print('Bert encode called')
train_input = tokenize_sentence.bert_encode(['This is the best day of my life'], tokenizer, max_len=MAX_LEN)
print('Tokenized')

pred = reloaded_model.predict(train_input)
print('Predicted from model')

result = []

for value in pred:
  result.append(mapping[np.argmax(value)])

print(result)

