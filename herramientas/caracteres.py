import unicodedata

def quita_acentos(cadena):
    return ''.join(c for c in unicodedata.normalize('NFD', cadena) if unicodedata.category(c) != 'Mn')

