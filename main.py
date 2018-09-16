from flask import Flask
import os
from PIL import Image
import numpy as np
import cv2
from keras.models import load_model

app = Flask(__name__)

@app.route("/hello")
def hello_world():

    #-- keras が起動出来ているか確認する --#
    #model = load_model('./shiogao_model2.h5')
    #print(model.summary())
    #-----#

    return "hello world!"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
