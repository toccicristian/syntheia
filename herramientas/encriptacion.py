import hashlib
import os


def hashear(cadena=str()):
    return hashlib.sha256(str(cadena).encode('utf-8')).hexdigest()



