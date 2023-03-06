import os

def cxb(num):
    """ Humanizar Tamaño de Archivos """
    num = float(num);step_unit = 1000.0
    for x in [' bytes', ' KB', ' MB', ' GB', ' TB']:
        if num < step_unit:return "%3.1f%s" % (num, x)
        num /= step_unit


def clear_console():
    """ Eliminar Consola """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")