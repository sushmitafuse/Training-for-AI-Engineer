from tensorflow.keras.models import load_model
import tensorflow_hub as hub

import tokenizer


mapping = {
    0: 'anger',
    1: 'disgust',
    2: 'fear',
    3: 'guilt',
    4: 'joy',
    5: 'sadness',
    6: 'shame'
}


MAX_LEN = 300

print('Emotion detection model loading...')
reloaded_model = load_model('../../checkpoints/bert/emotion_detection_bert.h5', custom_objects={'KerasLayer': hub.KerasLayer})
print('Model loaded')

# Input to bert_encode should be a list
train_input = bert_encode(['I am so scared to go there', 'This is the best day of my life'], tokenizer, max_len=MAX_LEN)
print('Tokenized')

pred = reloaded_model.predict(train_input)

result = []

for value in pred:
  result.append(mapping[np.argmax(value)])

print(result)

