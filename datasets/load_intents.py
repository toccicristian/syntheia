import json
import random


INTENTFILE="university_dataset.json"



# Cargar el archivo intents.json
with open(INTENTFILE, 'r', encoding='utf-8') as file:
    intents = json.load(file)

def get_response(user_input):
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if user_input.lower() == pattern.lower():
                return random.choice(intent['responses'])
    return "Lo siento, no entendí eso."

# Ejemplo de uso
while True:
    user_input = input("Tú: ")
    if user_input.lower() in ["salir", "exit"]:
        print("Bot: ¡Hasta luego!")
        break
    response = get_response(user_input)
    print(f"Bot: {response}")
