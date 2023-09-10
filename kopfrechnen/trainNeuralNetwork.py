import tensorflow as tf
import numpy as np
import random as rd

def generateQuestAndAnswer():
    
    term1=rd.randint(0,10)
    term2=rd.randint(0,10)
    operator=rd.randint(0,2)
    
    if operator==0:
        answer=term1+term2
    elif operator==1:
        answer=term1-term2
    else:
        answer=term1*term2
    
    return (term1,operator,term2),answer

def load_your_dataset():
    
    train_tuple_q=[]
    train_a=[]
    test_tuple_q=[]
    test_a=[]
    
    for i in range(2000):
        
        train_quest,train_ans=generateQuestAndAnswer()
        train_tuple_q.append(train_quest)
        train_a.append(train_ans)
    
    for i in range(10000):
        
        test_quest,test_ans=generateQuestAndAnswer()
        test_tuple_q.append(test_quest)
        test_a.append(test_ans)
    
    
    return (np.array(train_tuple_q), np.array(train_a)), (np.array(test_tuple_q), np.array(test_a))



(x_train, y_train), (x_test, y_test) = load_your_dataset()

# Modellarchitektur
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(3,)),  # Eingabeschicht mit 3 Neuronen für RGB-Werte
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)  # Anzahl der Farbkategorien
])

model.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics=['mae'])

model.fit(x_train, y_train, epochs=1000, batch_size=32, validation_data=(x_test, y_test))

test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Test Loss: {test_loss}")
print(f"Test Accuracy: {test_accuracy}")

model.save('mein_kopfrechnenModell')