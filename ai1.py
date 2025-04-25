import sys
from os.path import normpath, expanduser, isfile
import os
import logging


ayuda=f"""
    ai1 es un chatbot basico que hace uso de chatterbot.
    SINTAXIS:
    {sys.argv[0]} [opcion]


"""

CUSTOMDATASET=False

logging.getLogger('chatterbot').setLevel(logging.ERROR)
logging.basicConfig(level=logging.ERROR)

if len(sys.argv)>1:
    for arg in sys.argv[1:]:
        if arg == "--logging=info":
            logging.basicConfig(level=logging.info)
        if len([a for a in ['--help','--ayuda','-h'] if a == arg]):
            print(f"{ayuda}")
            sys.exit()
        if arg.startswith("--dataset="):
            if not isfile(normpath(expanduser(arg.lstrip("--dataset=")))):
                print("No se ha encontrado la ruta al dataset expresado en los argumentos.")
                sys.exit()
            if not normpath(expanduser(arg.lstrip("--dataset="))).endswith(".csv") and not normpath(expanduser(arg.lstrip("--dataset="))).endswith(".json"):
                print("El dataset proveido debe ser .csv o .json")

            CUSTOMDATASET=arg.lstrip("--dataset=")


############################################################
# BIBLIOTECA DE RECUERDOS
#
import modelos.recuerdo_modelo as recmodel
import repositorios.recuerdos as recrepo
#
if not recrepo.busca_recuerdo_por_nombre("nombreUsuario"):
    recuerdo_apodo=recmodel.Recuerdo(nombre="nombreUsuario", contenido=[input("Quien sos?\n>"),])
    recrepo.agrega_recuerdo(recuerdo_apodo)
#
#
recuerdo_apodo=recrepo.busca_recuerdo_por_nombre("nombreUsuario")
apodo = recuerdo_apodo.contenido[0]
#
#
if not recrepo.busca_recuerdo_por_nombre("quiensoy"):
    recuerdo_botname=recmodel.Recuerdo(nombre="quiensoy", contenido=[input(f"No recuerdo mi nombre... cuál es?\n{apodo}>"),])
    recrepo.agrega_recuerdo(recuerdo_botname)
#
recuerdo_botname=recrepo.busca_recuerdo_por_nombre("quiensoy")
botname = recuerdo_botname.contenido[0]
#
############################################################



############################################################
#                  DATASET:
#
#INTENTS_FILE="datasets/university_dataset.json"
INTENTS_FILE="datasets/Conversation.csv"
if CUSTOMDATASET:
    INTENTS_FILE=CUSTOMDATASET
#
#
#
############################################################

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(botname, storage_adapter='chatterbot.storage.SQLStorageAdapter') # Crear un nuevo chatbot
trainer = ListTrainer(chatbot)  # Crear un entrenador

#ENTRENAMOS EL CHATBOT SEGÚN SEA JSON O CSV EL INTENTS:

if INTENTS_FILE.lower().endswith(".json"):
    with open(INTENTS_FILE, 'r', encoding='utf-8') as file:
        import json
        intents = json.load(file)
        for intent in intents['intents']:
            trainer.train(intent['patterns'])
            trainer.train(intent['responses'])

else:
    if INTENTS_FILE.lower().endswith(".csv"):
        import pandas as pd

        if os.path.exists(INTENTS_FILE):
            data = pd.read_csv(INTENTS_FILE)
        else:
            data = pd.DataFrame(columns=['question', 'answer'])

    i=1
    for index, row in data.iterrows():
        question = row['question']
        answer = row['answer']
        trainer.train([question, answer]) # Entrenar con la pregunta y la respuesta
        print(f"[{i}/{len(data)}]")
        i=i+1



try:
    while True:
        user_input = input(f"{apodo}>")
        if user_input.lower() in ["salir", "exit"]:
            print("Bot: ¡Hasta luego!")
            break
        response = chatbot.get_response(user_input)
        if response.confidence < 0.6:
            print("Bot: Sorry, i didn't get that. Could you rephrase?")
            if INTENTS_FILE.lower().endswith(".csv"):
                user_feedback = input("Would you like me to learn the answer to this question? (yes/no): ")
                if user_feedback.lower() == 'yes':
                    new_answer = input("which would be the right answer? ")
                    new_data = pd.DataFrame([[user_input, new_answer]], columns=['question', 'answer'])
                    data = pd.concat([data, new_data], ignore_index=True)
                    data.to_csv(INTENTS_FILE, index=False)
                    trainer.train([user_input, new_answer])
        else:
            print(f"{botname}>{response}")

except KeyboardInterrupt:
    print("\nPrograma finalizado!")
    sys.exit()

