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


def guardar_recuerdos (recuerdos=[]):
    recdic_list=[]
    for r in recuerdos:
        recdic_list.append(r.__dict__)
    ar_w=open(normpath(expanduser(ARCHIVO_RECUERDOS)),'w')
    json.dump(recdic_list, ar_w)
    ar_w.close()


def agrega_recuerdo(recuerdo=modelos.recuerdo_modelo.Recuerdo()):
    recuerdos=recordar_todo()
    recuerdos.append(recuerdo)
    guardar_recuerdos(recuerdos)


def busca_recuerdo_por_nombre(criterio=''):
    recuerdos=recordar_todo()
    for recuerdo in recuerdos:
        if str(recuerdo.nombre).lower() == criterio.lower():
            return recuerdo
    return False



