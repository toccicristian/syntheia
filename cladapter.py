
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

    def process(self, statement, additional_response_selection_parameters=None):
        try:
            response_text = self.model.predict([statement.text])[0]
            response_statement = Statement(text=response_text)
            return response_statement

        except Exception as e:
            return Statement(text="Lo siento, no pude procesar tu solicitud.")  # Devuelve un Statement en caso de error


######################################### FIN DE INTEGRACION CON EL CHATBOT


