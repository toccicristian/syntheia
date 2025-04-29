class Recuerdo:
    def __init__(self, nombre="", caracteristicas=[], contenido={}):
        self.__codigo=False
        self.__nombre=nombre
        self.__caracteristicas=caracteristicas
        self.__contenido=contenido

    @property
    def codigo (self):
        return self.__codigo

    @codigo.setter
    def codigo (self, codigo=False):
        self.__codigo=codigo

    @property
    def nombre (self):
        return self.__nombre

    @nombre.setter
    def nombre (self, nombre=""):
        self.__nombre = nombre

    @property
    def caracteristicas (self):
        return self.__caracteristicas

    @caracteristicas.setter
    def caracteristicas (self, caracteristicas=[]):
        self.__caracteristicas=caracteristicas

    @property
    def contenido (self):
        return self.__contenido

    @contenido.setter
    def contenido (self, contenido):
        self.__contenido = contenido

    def busca_contenido(self, palabra_clave):
        if len([llave for llave in self.__contenido if llave.lower() == palabra_clave.lower()])>0:
            return self.__contenido[palabra_clave.lower()]

        return False

    def agrega_contenido (self, nombre, cosas):
        if len([llave for llave in self.__contenido if llave.lower() == nombre.lower()])>0:
            return False

        self.__contenido[nombre]=cosas
        return True

    def actualiza_contenido (self, nombre, cosas):
        self.__contenido[nombre]=cosas
        return True

    def busca_caracteristica(self, caracteristica):
        if len([c for c in self.__caracteristicas if c.lower() == caracteristica.lower()])>0:
            return True

        return False

