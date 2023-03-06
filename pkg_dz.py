import asyncio
from colorama import Fore, init
from files import psv_menu, ps3_menu, clear_console
import os
import time
import shutil
init()

async def main():
    """ instalación """
    print('*Iniciando pkg_dz...')
    time.sleep(2)
    print('*Verificando Directorios...')
    await directorys()
    time.sleep(2)
    print('*Directorios Verificados ')
    print('*Verificando Archivos de Consolas...')
    await archives()
    time.sleep(2)
    print('*Archivos de Consolas Verificados ')
    time.sleep(2)
    clear_console()
    await menu()


    


async def directorys():
    # Verificar si el directorio "ps3" existe
    if os.path.isdir("ps3"):
        print("*Verificando directorio 'ps3'")
    else:
        # Crear el directorio "ps3"
        os.mkdir("ps3")
        print("*Creando el directorio 'ps3'")
    
    # Verificar si el directorio "psv" existe
    if os.path.isdir("psv"):
        print("*Verificando directorio 'psv'")

    else:
        # Crear el directorio "psv"
        os.mkdir("psv")
        print("*Creando el directorio 'psv'")

    return True

import os

async def archives():
    # Verificar si los archivos existen en el directorio "psv"
    archivos_psv = ["PSV_GAMES.tsv", "PSV_DLCS.tsv", "PSV_THEMES.tsv"]
    for archivo in archivos_psv:
        if not os.path.isfile(f"psv/{archivo}"):
            print(f"*Falta el archivo {archivo} en el directorio 'psv'. Visite https://github.com/j3andz/pkg_dz para obtener más información")
    
    # Verificar si los archivos existen en el directorio "ps3"
    archivos_ps3 = ["PS3_GAMES.tsv", "PS3_DLCS.tsv", "PS3_THEMES.tsv", "PS3_AVATARS.tsv"]
    for archivo in archivos_ps3:
        if not os.path.isfile(f"ps3/{archivo}"):
            print(f"*Falta el archivo {archivo} en el directorio 'ps3'. Visite https://github.com/j3andz/pkg_dz para obtener más información")







async def menu():
    """ Menú de Inicio """
    clear_console()
    print('PKG_DZ v1.0\nGitHub: https://github.com/j3andz/pkg_dz\n\n')
    print(Fore.BLUE+'Menú:\n\n1- PSVITA\n2- PS3\n3- Help')
    option = input('=')
    if option == '1':
        await psv_menu()
    elif option == '2':
        await ps3_menu()
    elif option == '3':
        await help_console()

async def help_console():
    clear_console()
    print("""
Para obtener más información acerca del proyecto puedes entrar a los siguientes enlaces:

PKG_DZ v1.0

*Comunidad de Telegram:
https://t.me/PixelDZ

*GitHub del Proyecto
https://github.com/j3andz/pkg_dz
""")
    input(Fore.CYAN+'*Enter para regresar al menú...')
    await menu()

if __name__ == "__main__":
    asyncio.run(main())
    
