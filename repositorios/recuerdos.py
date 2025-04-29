import json
import modelos.recuerdo_modelo
from os.path import isfile, normpath, expanduser


ARCHIVO_RECUERDOS="recuerdos.json"


def recordar_todo ():
    recuerdos=[]
    if not isfile(normpath(expanduser(ARCHIVO_RECUERDOS))):
        return recuerdos

    with open (ARCHIVO_RECUERDOS, "r") as ar_rec:
        rec=ar_rec.read()

    try:
        recdiclist = json.loads(rec)
    except UnicodeDecodeError:
        return recuerdos

    for r in recdiclist:
        recuerdo=modelos.recuerdo_modelo.Recuerdo()
        recuerdo.__dict__=r
        recuerdos.append(recuerdo)
    return recuerdos


def obtener_maximo_codigo_de_recuerdo():
    recuerdos=recordar_todo()
    codigomax=0
    if len(recuerdos)==0:
        return False

    for recuerdo in recuerdos:
        if int(recuerdo.codigo)>codigomax:
            codigomax = int(recuerdo.codigo)
    return codigomax


def guardar_recuerdos (recuerdos=[]):
    recdic_list=[]
    for r in recuerdos:
        recdic_list.append(r.__dict__)
    ar_w=open(normpath(expanduser(ARCHIVO_RECUERDOS)),'w')
    json.dump(recdic_list, ar_w)
    ar_w.close()


def agrega_recuerdo(recuerdo=modelos.recuerdo_modelo.Recuerdo()):
    recuerdos=recordar_todo()
    codigomax=obtener_maximo_codigo_de_recuerdo()
    recuerdo.codigo=int(0)
    if codigomax is not False:
        recuerdo.codigo=int(codigomax)+1

    recuerdos.append(recuerdo)
    guardar_recuerdos(recuerdos)


def actualiza_recuerdo(recuerdo=modelos.recuerdo_modelo.Recuerdo()):
    recuerdos=recordar_todo()
    resultado=[]
    for re in recuerdos:
        if int(recuerdo.codigo) == int(re.codigo):
            resultado.append(recuerdo)
        else:
            resultado.append(re)

    guardar_recuerdos(resultado)
    return True


def busca_recuerdo_por_nombre(criterio=''):
    recuerdos=recordar_todo()
    for recuerdo in recuerdos:
        if str(recuerdo.nombre).lower() == criterio.lower():
            return recuerdo
    return False

def busca_recuerdo_por_nombre_y_caracteristicas(nombre='', caracteristicas=[]):
    recuerdos=recordar_todo()
    for recuerdo in recuerdos:
        if str(recuerdo.nombre).lower() == nombre.lower() and set(caracteristicas) <= set(recuerdo.caracteristicas):
            return recuerdo

    return False



