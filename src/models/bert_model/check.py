from tensorflow.keras.models import load_model
import tensorflow_hub as hub

print('Emotion detection model loading...')
reloaded_model = load_model('../../../checkpoints/bert/emotion_detection_bert.h5', custom_objects={'KerasLayer': hub.KerasLayer})
print('Model loaded')
