import os
import json
import numpy as np

from flask import Flask
from flask import request, jsonify

import tensorflow as tf
from urllib.request import urlretrieve
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import Xception
from tensorflow.keras.applications.xception import preprocess_input
from tensorflow.keras.applications.xception import decode_predictions

loaded_model = None

app = Flask(__name__)


def load_model():
    """
    Load model and tensorflow graph
    into global variables.
    """

    # global variables
    global loaded_model

    loaded_model = Xception(weights='imagenet')
    print("Model loaded.")

def load_image_from_url(url, target_size=(299, 299)):
    path, response = urlretrieve(url, filename='/tmp/temp_img')
    img = image.load_img(path, target_size=target_size)
    img_tensor = np.expand_dims(image.img_to_array(img), axis=0)
    return img, img_tensor

def preprocess(data):
    url = data.decode('utf-8')
    img, img_tensor = load_image_from_url(url)
    img_scaled = preprocess_input(img_tensor)
    return img_scaled


@app.route('/', methods=["POST"])
def predict():
    """
    Generate predictions with the model
    when receiving data as a POST request
    """
    if request.method == "POST":
        # get url from the request
        data = request.data

        # preprocess the data
        processed = preprocess(data)

        # run predictions
        preds = loaded_model.predict(processed)

        # obtain predicted classes from predicted probabilities
        result = decode_predictions(preds, top=1)[0][0][1]

        # print in backend
        print("Received data:", data)
        print("Predicted labels:", result)

        return jsonify(result)


if __name__ == "__main__":
    print("* Loading model and starting Flask server...")
    load_model()
    app.run(host='0.0.0.0', debug=True)


# Test this with the following command:
# curl -d 'http://bit.ly/2wb7uqN' -H "Content-Type: application/json" -X POST http://localhost:5000
