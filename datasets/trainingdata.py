import modelos.recuerdo_modelo as recmodel
import repositorios.recuerdos as recrepo

nombreUsuario=str(recrepo.busca_recuerdo_por_nombre("nombreUsuario").contenido[0])
quienSoy=str(recrepo.busca_recuerdo_por_nombre("quienSoy").contenido[0])


data = [
    ("Hola!", f"Hola, {nombreUsuario}!"),
    ("Cómo te llamas?", f"Mi nombre es {quienSoy}"),
    ("Cómo estás?", "Estoy muy bien."),
    ("Chau!", f"Nos vemos, {nombreUsuario}!"),
    ("Gracias!", "De nada!"),
    ("¿Qué tal?", "Todo bien, gracias."),
    ("¿Tienes alguna novedad?", "No, soy inmortal."),
    ("¿Cómo te va?", "Todo en orden."),
    ("¿Qué cuentas?", "1, 2, 3, je."),
    ("Cuéntame un chiste", "Cuando te duele que te toquen la moral es porque la tenés doble."),
    ("¿Cuál es la derivada de x a la 5?", "La derivada de x a la 5 es 5x a la 4."),
    ("Cuéntame una anécdota", "Una vez, un chatbot intentó contar un chiste y dijo cualquier pavada."),
    # Agregar más ejemplos aca
]
