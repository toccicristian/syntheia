import herramientas.caracteres as hcaract
import pandas as pd
import os
import modelos.recuerdo_modelo as recuerdo


def selector(entrada, rec_persona, rec_chatbot, chatbot, CUSTOMDATASET, INTENTS_DIR, data, trainer):
    if entrada.lower() in ["salir", "exit"]:
        print("<Proceso terminado>")
        return False
    respuesta = chatbot.get_response(hcaract.quita_acentos(entrada.lower()))
    if respuesta.confidence < 0.6:
        print(f"{rec_chatbot.busca_contenido('nombre')}>Lo siento... no comprendo lo que dijiste...")
        INPUT_INTENTS_FILE=CUSTOMDATASET
        if not INPUT_INTENTS_FILE:
            INPUT_INTENTS_FILE=os.path.join(INTENTS_DIR,rec_persona.nombre+".csv")

        if INPUT_INTENTS_FILE.lower().endswith(".csv"):
            user_feedback = input(f"{rec_chatbot.busca_contenido('nombre')}>Te gustaría enseñarme una respuesta adecuada a esa pregunta?\n{rec_persona.nombre}>")
            if user_feedback.lower() in ['si','bueno','tal vez','capaz','ok','puede ser']:
                new_answer = input(f"{rec_chatbot.busca_contenido('nombre')}>cuál sería una respuesta adecuada?\n{rec_persona.nombre}>")
                new_data = pd.DataFrame([[entrada, new_answer]], columns=['question', 'answer'])
                data = pd.concat([data, new_data], ignore_index=True)
                data.to_csv(INPUT_INTENTS_FILE, index=False)
                trainer.train([entrada, new_answer])
                return f"{rec_chatbot.busca_contenido('nombre')}>Gracias!. Lo voy a tener en cuenta."
            else:
                return f"{rec_chatbot.busca_contenido('nombre')}>Ok... creo que voy a ignorar lo que dijiste entonces!"

    else:
        return f"{rec_chatbot.busca_contenido('nombre')}>{respuesta}"
