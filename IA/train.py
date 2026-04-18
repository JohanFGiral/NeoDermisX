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
		epochs= EPOCHS
	)

	loss,acc = model.evaluate(test_ds)
	print(f"Test Loss: {loss:.4f}, Test Accuracy: {acc:.4f}")

	model.save("skin_cancer_model9.h5")