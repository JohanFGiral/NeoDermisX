import pandas as pd
import tensorflow as tf
import os
from config import DATASET_PATH, CSV_PATH, IMG_SIZE, BATCH_SIZE
from tensorflow.keras.applications.efficientnet import preprocess_input



def load_dataset():

    df = pd.read_csv(CSV_PATH)

    print(f"CSV cargado: {len(df)} registros encontrados")
    
    print("\nValores en benign_malignant:")
    print(df["benign_malignant"].value_counts())

    # rutas
    df["path"] = df["image_name"].apply(
        lambda x: os.path.join(DATASET_PATH, x + ".jpg")
    )
    
    print("\nEjemplo de rutas:")
    print(df["path"].head())
    print("\n¿Existe la primera imagen?:", os.path.exists(df["path"].iloc[0]))

    # etiquetas
    df["label"] = df["benign_malignant"].map({
        "benign": 0,
        "malignant": 1
    })
    
    print("\nValores en label:")
    print(df["label"].value_counts())

    df = df.dropna(subset=["path", "label"])

    # MEZCLAR DATAFRAME 
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    # DIVIDIR DATASET
    total = len(df)

    train_df = df[:int(0.7 * total)]
    val_df = df[int(0.7 * total):int(0.85 * total)]
    test_df = df[int(0.85 * total):]

    print(f"Train: {len(train_df)}, Val: {len(val_df)}, Test: {len(test_df)}")

    # función imagen
    def create_dataset(dataframe):

        paths = dataframe["path"].values
        labels = dataframe["label"].values

        ds = tf.data.Dataset.from_tensor_slices((paths, labels))

        def load_image(path, label):
            image = tf.io.read_file(path)
            image = tf.image.decode_jpeg(image, channels=3)
            image = tf.image.resize(image, IMG_SIZE)
            image = preprocess_input(image)
            return image, label

        ds = ds.map(load_image, num_parallel_calls=tf.data.AUTOTUNE)
        ds = ds.batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)

        return ds

    train_ds = create_dataset(train_df)
    for img, label in train_ds.take(1):
        print("\nShape de imágenes:", img.shape)
        
        
        print("Labels:", label[:5])
    val_ds = create_dataset(val_df)
    test_ds = create_dataset(test_df)

    return train_ds, val_ds, test_ds

load_dataset()