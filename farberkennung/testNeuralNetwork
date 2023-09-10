import tensorflow as tf
import numpy as np

# Ihr trainiertes Modell laden
model = tf.keras.models.load_model('mein_farbmodell.h5')

# RGB-Werte vom Benutzer eingeben lassen
red = int(input("Geben Sie den Rotwert ein (0-255): "))
green = int(input("Geben Sie den Grünwert ein (0-255): "))
blue = int(input("Geben Sie den Blauwert ein (0-255): "))

# Eingabe in das Modell formatieren
input_data = np.array([[red, green, blue]])

# Vorhersage der Farbkategorie
predictions = model.predict(input_data)

# Liste der Farbkategorien
color_categories = ["rot", "grün", "blau", "gelb", "türkis", "violett"]

# Anzeigen der Vorhersage und Wahrscheinlichkeitsverteilung
predicted_color = color_categories[np.argmax(predictions)]
probability_distribution = predictions[0]

print(f"Die vorhergesagte Farbkategorie ist: {predicted_color}")
print("Wahrscheinlichkeitsverteilung:")
for category, probability in zip(color_categories, probability_distribution):
    print(f"{category}: {probability * 100:.2f}%")
