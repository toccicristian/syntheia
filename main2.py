apodo = input("Tu apodo: ")
botname = input("Nombre del bot: ")


# PARA INTEGRACION CON CHATBOT:
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import LogicAdapter



# PARA CLASIFICACION DE TEXTO:
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score



########################################## MODELO DE CLASIFICACION DE TEXTO:

# Ejemplo de datos de entrenamiento
data = [
    ("Hola!", f"Hola, {apodo}"),
    ("Cómo te llamas?", f"Mi nombre es {botname}"),
    ("Cómo estás?", "Estoy muy bien."),
    ("Chau!", f"Nos vemos, {apodo}!"),
    ("Gracias!", "De nada!")
]

# Separar las preguntas y respuestas
questions = [pair[0] for pair in data]
answers = [pair[1] for pair in data]

# Crear un pipeline de clasificación
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(questions, answers, test_size=0.2, random_state=42)

# Entrenar el modelo
pipeline.fit(X_train, y_train)

# Evaluar el modelo
y_pred = pipeline.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

########################################## FIN DE MODELO DE CLASIFICACION DE TEXTO



import sys
from os.path import normpath, expanduser, isfile

comlist = """
    Converse con el chatbot o bien ingrese alguno de los siguientes comandos:
    /ayuda      (esta ayuda)
    /entrenar   (entrena el bot)
                si se especifica ruta a archivo yml utiliza ese archivo
    /exit       (sale del programa)
"""

trainer = False

def selector(comando, datos):
    if comando.lower() == "/ayuda":
        print(f"\n\nComandos:\n{comlist}\n")
        return None

    if comando.lower().startswith("/entrenar ") and isfile(normpath(expanduser(comando.lower().lstrip("/entrenar ")))):
        print(f"***Entrenando con {normpath(expanduser(comando.lower().lstrip('/entrenar ')))}...")
        datos["trainer"].train(normpath(expanduser(comando.lower().lstrip("/entrenar "))))
        print("***Entrenamiento terminado!")
        return None

    if comando.lower() == "/entrenar":
        # Entrenar el chatbot con el corpus de datos de ChatterBot
        print("***Entrenando...")
        datos["trainer"].train("chatterbot.corpus.spanish")
        print("***Entrenamiento terminado!")
        return None

    if comando.lower() == "/exit":
        print("***Programa finalizado")
        sys.exit()

    else:
        # Obtener una respuesta del chatbot
        response = datos["chatbot"].get_response(comando)
        print(f"{datos['botname']}> {response}")
        return None


datos = {"username": apodo, "botname": botname, "trainer": trainer}




# Crear un nuevo chatbot
datos["chatbot"] = ChatBot(
    datos["botname"],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Lo lamento pero no te entiendo.',
            'maximum_similarity_threshold': 0.90
        },
        {
            'import_path': 'cladapter.CustomLogicAdapter',  # Usar el adaptador personalizado definido en este archivo
            'pipeline': pipeline  # Pasar el pipeline aquí
        }
    ]
)

print(f"\n***Creado {datos['botname']}\n")

# Crear un nuevo entrenador para el chatbot
if not datos["trainer"]:
    datos["trainer"] = ChatterBotCorpusTrainer(datos["chatbot"])
    print("***Entrenador creado!")

# Entrenar el chatbot con el corpus de datos de ChatterBot
print("***Entrenando...")
datos["trainer"].train("chatterbot.corpus.spanish")
print("***Entrenamiento terminado!")

print(f"\n\nComandos:\n{comlist}\n")

while True:
    comando = input(f"{datos['username']}> ")
    selector(comando, datos)
