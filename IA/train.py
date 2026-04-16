from data import load_dataset
from config import EPOCHS
from model import create_model
import tensorflow as tf

def train():
	train_ds, val_ds, test_ds = load_dataset()
	model = create_model()

	model.fit(
		train_ds,
		validation_data=val_ds,
		epochs=3
	)
	# obtener EfficientNet
	#base_model = model.get_layer("base_model")

	# descongelar SOLO últimas capas
	#for layer in base_model.layers[-50:]:
	#	layer.trainable = True

	#recompilar con LR bajo
	model.compile(
		optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
		loss='sparse_categorical_crossentropy',
		metrics=['accuracy']
	)

	model.fit(
		train_ds,
		validation_data=val_ds,
		epochs=1
	)

	loss,acc = model.evaluate(test_ds)
	print(f"Test Loss: {loss:.4f}, Test Accuracy: {acc:.4f}")

	model.save("skin_cancer_model9.h5")