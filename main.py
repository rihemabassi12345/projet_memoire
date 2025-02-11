import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import cv2

# ==== 1️⃣ Chargement des données (supposons que vous avez des images classées dans des dossiers) ====
CHEMIN_DONNEES = "datasets/"  # Indiquez le bon chemin ici
TAILLE_IMG = 48  # Taille d'image souhaitée

def charger_images(chemin_donnees):
    X, Y = [], []
    labels = os.listdir(chemin_donnees)  # Noms des classes
    mapping_labels = {label: i for i, label in enumerate(labels)}

    for label in labels:
        chemin_label = os.path.join(chemin_donnees, label)
        for nom_img in os.listdir(chemin_label):
            chemin_img = os.path.join(chemin_label, nom_img)
            img = cv2.imread(chemin_img, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (TAILLE_IMG, TAILLE_IMG))
            X.append(img)
            Y.append(mapping_labels[label])

    X = np.array(X).reshape(-1, TAILLE_IMG, TAILLE_IMG, 1) / 255.0  # Normalisation des données
    Y = np.array(Y)
    return X, Y, mapping_labels

# Chargement des données
X_train, Y_train, mapping_labels = charger_images(CHEMIN_DONNEES)

# ==== 2️⃣ Construction d'un modèle simple ====
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation="relu", input_shape=(TAILLE_IMG, TAILLE_IMG, 1)),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D(2, 2),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(len(mapping_labels), activation="softmax")  # Nombre de classes pour la classification
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.summary()

# ==== 3️⃣ Entraînement du modèle ====
model.fit(X_train, Y_train, epochs=10, batch_size=32)

# ==== 4️⃣ Sauvegarde du modèle ====
CHEMIN_MODELE_H5 = "models/emotion_model.h5"
os.makedirs("models", exist_ok=True)
model.save(CHEMIN_MODELE_H5)
print(f"✅ Le modèle a été sauvegardé dans {CHEMIN_MODELE_H5}")

# ==== 5️⃣ Conversion du modèle en TFLite ====
CHEMIN_MODELE_TFLITE = "models/emotion_model.tflite"

convertisseur = tf.lite.TFLiteConverter.from_keras_model(model)
modele_tflite = convertisseur.convert()

with open(CHEMIN_MODELE_TFLITE, "wb") as f:
    f.write(modele_tflite)
print(f"✅ Le modèle a été converti en TFLite et sauvegardé dans {CHEMIN_MODELE_TFLITE}")
