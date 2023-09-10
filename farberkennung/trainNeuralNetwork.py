import tensorflow as tf
import numpy as np

farben_dict = {
    "rot": [(128, 0, 0), (139, 0, 0), (165, 42, 42), (178, 34, 34), (220, 20, 60), (255, 0, 0), (255, 99, 71), (255, 127, 80), (205, 92, 92), (240, 128, 128), (233, 150, 122), (250, 128, 114), (255, 160, 122), (255, 69, 0), (255, 140, 0), (255, 165, 0), (255, 215, 0), (184, 134, 11), (218, 165, 32), (238, 232, 170)],
    "grün": [(0,250,0),(128, 128, 0), (154, 205, 50), (85, 107, 47), (107, 142, 35), (124, 252, 0), (173, 255, 47), (0, 100, 0), (0, 128, 0), (34, 139, 34), (50, 205, 50), (144, 238, 144), (152, 251, 152), (143, 188, 143), (46, 139, 87), (102, 205, 170), (60, 179, 113), (32, 178, 170)],
    "blau": [(0, 0, 128), (0, 0, 139), (0, 0, 205), (0, 0, 255), (65, 105, 225), (138, 43, 226), (75, 0, 130), (72, 61, 139), (106, 90, 205), (123, 104, 238), (147, 112, 219), (139, 0, 139), (148, 0, 211), (153, 50, 204), (186, 85, 211), (128, 0, 128), (216, 191, 216), (221, 160, 221), (238, 130, 238), (218, 112, 214), (199, 21, 133), (219, 112, 147), (255, 20, 147), (255, 105, 180), (255, 182, 193), (255, 192, 203)],
    "gelb": [(255, 255, 0), (0, 255, 0), (255, 255, 127), (0, 250, 154)],
    "türkis": [(0, 128, 128), (0, 139, 139), (0, 206, 209), (64, 224, 208), (72, 209, 204), (175, 238, 238), (127, 255, 212), (176, 224, 230), (95, 158, 160), (70, 130, 180), (100, 149, 237), (0, 191, 255), (30, 144, 255), (173, 216, 230), (135, 206, 235), (135, 206, 250)],
    "violett": [(128, 0, 128), (139, 0, 139), (148, 0, 211), (153, 50, 204), (186, 85, 211), (218, 112, 214), (199, 21, 133), (219, 112, 147), (255, 20, 147), (255, 105, 180), (255, 182, 193), (255, 192, 203)]
}

test_farben_dict = {
    "rot": [(255, 0, 0), (210, 0, 0), (160, 50, 50), (180, 20, 20), (240, 50, 50), (200, 0, 0), (255, 80, 80), (255, 120, 120), (220, 100, 100), (245, 150, 150)],
    "grün": [(0, 255, 0), (0, 200, 0), (50, 160, 50), (30, 90, 30), (80, 120, 80), (0, 240, 0), (0, 255, 50), (70, 255, 70), (0, 130, 0), (30, 150, 30)],
    "blau": [(0, 0, 255), (0, 0, 210), (0, 0, 160), (0, 0, 180), (50, 80, 240), (50, 0, 160), (0, 0, 100), (20, 40, 120), (30, 50, 190), (40, 70, 210)],
    "gelb": [(255, 255, 0), (200, 200, 0), (255, 255, 100), (200, 255, 150)],
    "türkis": [(0, 255, 255), (0, 210, 210), (50, 180, 180), (80, 200, 200), (120, 220, 220), (150, 255, 255)],
    "violett": [(128, 0, 255), (139, 0, 210), (148, 50, 180), (153, 100, 210), (186, 50, 220), (255, 0, 255)]
}



def load_your_dataset():
    train_tuple_x = []
    train_tuple_y = []
    test_tuple_x = []
    test_tuple_y = []
    for key in farben_dict.keys():
        for value in farben_dict[key]:
            train_tuple_x.append(value)
            train_tuple_y.append(list(farben_dict.keys()).index(key))
    
    for key in test_farben_dict.keys():
        for value in test_farben_dict[key]:
            test_tuple_x.append(value)
            test_tuple_y.append(list(farben_dict.keys()).index(key))
            
    
    return (np.array(train_tuple_x), np.array(train_tuple_y)), (np.array(test_tuple_x), np.array(test_tuple_y))

(x_train, y_train), (x_test, y_test) = load_your_dataset()

# Modellarchitektur
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(3,)),  # Eingabeschicht mit 3 Neuronen für RGB-Werte
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(6, activation='softmax')  # Anzahl der Farbkategorien
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=100, batch_size=32, validation_data=(x_test, y_test))

test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Test Loss: {test_loss}")
print(f"Test Accuracy: {test_accuracy}")

model.save('mein_farbmodell.h5')
