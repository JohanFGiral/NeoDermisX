import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.preprocessing import image
from flask import jsonify
from app.modules.model_loader import model


def procesar(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    pred_class = np.argmax(prediction)  # 0 = benigno 1 = maligno
    prob = float(prediction[0][pred_class])   # la probabilidad de la clase predicha
    
    if pred_class == 0:
        print(f"Predicción: benigno con probabilidad {prob:.4f}")
        return "BENIGNO", prob
    else:
        print(f"Predicción: maligno con probabilidad {prob:.4f}")
        return "MALIGNO", prob