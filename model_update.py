import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the model
model = load_model('RNN_IMDB.h5')

# Save the model in the current format
model.save('RNN_IMDB_resaved.keras')

model = load_model('RNN_IMDB_resaved.keras')
print("Model re-saved and loaded successfully.")