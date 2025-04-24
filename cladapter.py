
# PARA INTEGRACION CON CHATBOT:
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import LogicAdapter

from chatterbot.conversation import Statement


########################################## INTEGRACION CON EL CHATBOT:

class CustomLogicAdapter(LogicAdapter):
    def __init__(self, chatbot, pipeline, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.model = pipeline  # Usar el modelo entrenado

    def can_process(self, statement):
        # Determinar si este adaptador puede procesar la declaración
        return True

    def process(self, statement, additional_response_selection_parameters):
        try:
            response = self.model.predict([statement.text])[0]
            return Statement(text=response)
        except Exception as e:
            return "Lo siento, no pude procesar tu solicitud."


######################################### FIN DE INTEGRACION CON EL CHATBOT
