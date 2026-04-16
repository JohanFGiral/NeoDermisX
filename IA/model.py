import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import EfficientNetB0
from config import IMG_SIZE

def create_model():
    #se incluye modelo preentrenado EfficientNetB0 sin la parte superior (clasificación) y se congela para evitar que se actualicen sus pesos durante el entrenamiento
	base_model = EfficientNetB0(
		weights="imagenet", 
		include_top=False, 
		input_shape=IMG_SIZE + (3,)
	)

	base_model.trainable = False
	x = base_model.output
	x = layers.GlobalAveragePooling2D()(x) # se remplaza flatten por global average pooling para reducir la dimensionalidad de las características extraídas por el modelo base
	x = layers.Dense(128, activation="relu")(x) # capa densa con 128 neuronas y activación ReLU para aprender representaciones más complejas
	output = layers.Dense(2, activation="softmax")(x) # capa de salida con 2 neuronas y activación softmax para clasificación binaria

	model = models.Model(inputs=base_model.input, outputs=output)

	model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
	)

	return model