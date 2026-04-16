#Rutas de imagenes
DATASET_PATH = r"A:\IA deteccion de cancer\NeoDermisX\IA\Dataset\train" #Ruta del dataset de imágenes

#CSV
CSV_PATH = r"A:\IA deteccion de cancer\NeoDermisX\IA\Dataset\train\data_train_balanceado.csv" #Ruta del archivo CSV con las etiquetas de las imágenes

#PARAMETROS DE ENTRENAMIENTO
EPOCHS = 10 #Número de épocas para el entrenamiento del modelo
IMG_SIZE = (224, 224) #Tamaño de las imágenes de entrada
BATCH_SIZE = 32 #Tamaño del lote para el entrenamiento