import controladores.selector
import sys

def prompt(persona, rbot, chatbot, CUSTOMDATASET, INTENTS_DIR, data, trainer):
    try:
        respuesta=True
        while respuesta:
            entrada = input(f"{persona.nombre}>")
            respuesta=controladores.selector.selector(entrada, persona, rbot, chatbot, CUSTOMDATASET, INTENTS_DIR, data, trainer)
            if(respuesta):
                print(f"{respuesta}")

    except KeyboardInterrupt:
        print("\nPrograma finalizado!")
        sys.exit()
