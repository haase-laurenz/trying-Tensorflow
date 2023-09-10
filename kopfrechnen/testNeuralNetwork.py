import tensorflow as tf
import numpy as np
import random as rd
import time

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

# Laden des trainierten Modells
model = tf.keras.models.load_model('mein_kopfrechnenModell')

runs=0
correct=0

while runs<500:
    
    
    quest,answer=generateQuestAndAnswer()
    term1=quest[0]
    operator_val=quest[1]
    term2=quest[2]
    
    input_data = np.array([[term1, operator_val, term2]])
    # Vorhersage mit dem Modell durchführen
    predictions = model.predict(input_data)
    
    
    # Ergebnis ausgeben
    if operator_val == 0:
        operator_str = "+"
    elif operator_val == 1:
        operator_str = "-"
    else:
        operator_str = "*"

    result = int(predictions[0][0])
    
    if result==answer:
        correct+=1
    runs+=1
    
    print(f'Die vorhergesagte Operation ist: {term1} {operator_str} {term2} = {result}')
    print(f'{correct}/{runs} Antworten richtig: {correct/runs}%')
    