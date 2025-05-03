import time

def mes_nombre(numero):
    return ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Nociembre","Diciembre"][numero+1]

def dia_nombre(numero):
    return ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"][numero]


def obtiene_fecha():
    return f"{ dia_nombre(time.localtime().tm_wday) } {time.localtime().tm_mday} de { mes_nombre(time.localtime().tm_mon) } del año {time.localtime().tm_year}"


def obtiene_hora():
    return f"{time.localtime().tm_hour}:{time.localtime().tm_min}"
