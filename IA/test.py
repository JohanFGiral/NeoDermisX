import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.preprocessing import image
import pandas as pd

model = load_model(r"A:\IA deteccion de cancer\NeoDermisX\NeoDermisXV1.h5")

df = pd.read_csv(r"A:\IA deteccion de cancer\NeoDermisX\IA\Dataset\val\data_val_balanceado.csv")
imgid=df["image_id"]
resultados = []

for i in range(len(imgid)):
    img_path = f"a:\\IA deteccion de cancer\\NeoDermisX\\IA\\Dataset\\val\\{imgid[i]}.jpg"
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    print("Predicción (probabilidades):", prediction)
    
    # Elegir la clase con mayor probabilidad
    pred_class = np.argmax(prediction)  # 0 = benigno 1 = maligno
    prob = prediction[0][pred_class]   # la probabilidad de la clase predicha
    
    if pred_class == 0:
        resultados.append((imgid[i], df["type"].iloc[i], "benigno", prob))
    else:
        resultados.append((imgid[i], df["type"].iloc[i], "maligno", prob))


for i in resultados:
    print(i)
print(f"CSV cargado: {len(df)} registros encontrados")

df_resultados = pd.DataFrame(resultados, columns=["image_id", "label_real", "prediccion_IA", "prob_maligno"])
df_resultados.to_csv(r"a:\IA deteccion de cancer\NeoDermisX\IA\Dataset\val\resultados_predicciones_modelo10.csv", index=False)
print("Resultados guardados en CSV")