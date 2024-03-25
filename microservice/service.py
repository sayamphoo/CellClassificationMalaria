import tensorflow as tf

import io
from PIL import Image

model = tf.keras.models.load_model('../model/malaria_model.h5')
def prediction(image):

    # Read image from bytes
    img = Image.open(io.BytesIO(image))
    img = img.resize((50, 50))
    # Preprocess image
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    img_array = tf.keras.applications.resnet.preprocess_input(img_array)

    # Make prediction
    prediction = model.predict(img_array)
    return prediction
