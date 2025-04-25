class Recuerdo:
    def __init__(self, nombre="", contenido=[]):
        self.__nombre=nombre
        self.__contenido=contenido

    @property
    def nombre (self):
        return self.__nombre

    @nombre.setter
    def nombre (self, nombre=""):
        self.__nombre = nombre

    @property
    def contenido (self):
        return self.__contenido

    @contenido.setter
    def contenido (self, contenido):
        self.__contenido = contenido
