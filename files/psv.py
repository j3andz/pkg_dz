import csv
from colorama import init, Fore
from .util import cxb, clear_console

init()

"""                     PSVITA MENU                     """
async def psv_menu():
    """ Menú PSVITA """
    clear_console()
    print('PSVITA:\n\n1- GAMES\n2- DLCS\n3- THEMES')
    option = input('=')
    if option == '1':
        await psv_games()
    elif option == '2':
        await psv_dlcs()
    elif option == '3':
        await psv_themes()


"""                        GAMES                       """
async def psv_games():
    """ PSVITA GAMES """
    filename = "psv/PSV_GAMES.tsv"
    search = input("Nombre: ")
    games = await process_games(filename)
    if games:
        matches = await search_games(games, search)
        if matches:
            clear_console()
            print('PSVITA GAMES')
            print(f"Se encontraron {len(matches)} resultados para '{search}':\n\n")
            for match in matches:
                try:
                    title_id = match["Title ID"]
                    region = match["Region"]
                    name = match["Name"]
                    #require_fw_v = match["Required FW"]
                    pkg_link = match["PKG direct link"] #\nRequire Firware Version: {require_fw_v}
                    file_size = match["File Size"]
                    print(Fore.MAGENTA + f'Name: {name}\nTitle ID: {title_id}\nRegion: {region}\nFile Size: {cxb(file_size)}\nPKG Link: '+Fore.GREEN + f'{pkg_link}') 
                    print(Fore.WHITE+"-" * 40)
                except Exception as ex:
                    print(Fore.RED+f"*Error")
                    print(Fore.WHITE+"-" * 40)
            input('*Enter...')
            clear_console()
            print('1- Volver a Intentar\n2- Menú PSVITA')
            option = input('=')
            if option == '1':
                await psv_games()
            elif option == '2':
                await psv_menu()
        else:
            print(f"No se encontraron resultados para '{search}'.")
            input('Enter...')

            clear_console()
            print('1- Volver a Intentar\n2- Menú PSVITA')
            option = input('=')
            if option == '1':
                await psv_games()
            elif option == '2':
                await psv_menu()
    else:
        print("No se pudo procesar el archivo")
        print('Recuerde colocar los archivos bien en sus respectivas carpetas')
        input('Enter para salir...')

async def process_games(filename):
    """ Función para revisar los archivos .tsv """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
            lines = data.split('\n')
            header = lines[0].split('\t')
            result = []
            for line in lines[1:]:
                if line.strip():
                    game_data = {}
                    values = line.split('\t')
                    for i, value in enumerate(values):
                        game_data[header[i]] = value
                    result.append(game_data)
            return result
    except FileNotFoundError:
        print(f"ERROR: El archivo {filename} no existe")
        print('Recuerde colocar los archivos bien en sus respectivas carpetas')
        input('Enter para salir...')

async def search_games(names, search):
    """ buscar por nombres"""
    results = []
    for name in names:
        if search.lower() in name['Name'].lower() and name not in results:
            results.append(name)
    return results





"""                   DLCs              """
async def psv_dlcs():
    """ PSVITA DLCs """
    filename = "psv/PSV_DLCS.tsv"
    search = input("Nombre: ")
    games = await process_dlcs(filename)
    if games:
        matches = await search_dlcs(games, search)
        if matches:
            clear_console()
            print('PSVITA DLCs')
            print(f"Se encontraron {len(matches)} resultados para '{search}':")
            for match in matches:
                try:
                    title_id = match["Title ID"]
                    region = match["Region"]
                    name = match["Name"]
                    #require_fw_v = match["Required FW"]
                    pkg_link = match["PKG direct link"] #\nRequire Firware Version: {require_fw_v}
                    file_size = match["File Size"]
                    print(Fore.MAGENTA + f'Name: {name}\nTitle ID: {title_id}\nRegion: {region}\nPKG Link: '+Fore.GREEN + f'{pkg_link}') 
                    print(Fore.WHITE+"-" * 40)
                except Exception as ex:
                    print(Fore.RED+f"*Error")
                    print(Fore.WHITE+"-" * 40)

            input('\n\n*Enter...')
            clear_console()
            print('1- Reintentar\n2- Menú PSVITA')
            option = input('=')
            if option == '1':
                await psv_dlcs()
            elif option == '2':
                await psv_menu()
        else:
            print(f"No se encontraron resultados para '{search}'.")
            input('\n\n*Enter...')
            clear_console()
            print('1- Reintentar\n2- Menú PSVITA')
            option = input('=')
            if option == '1':
                await psv_dlcs()
            elif option == '2':
                await psv_menu()
    else:
        print("No se pudo procesar el archivo")
        print('Recuerde colocar los archivos bien en sus respectivas carpetas')
        input('Enter para salir...')


async def process_dlcs(filename):
    """ Función para revisar los archivos .tsv """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
            lines = data.split('\n')
            header = lines[0].split('\t')
            result = []
            for line in lines[1:]:
                if line.strip():
                    game_data = {}
                    values = line.split('\t')
                    for i, value in enumerate(values):
                        game_data[header[i]] = value
                    result.append(game_data)
            return result
    except FileNotFoundError:
        print(f"ERROR: El archivo {filename} no existe")
        print('Recuerde colocar los archivos bien en sus respectivas carpetas')
        input('Enter para salir...')

async def search_dlcs(names, search):
    """ buscar por nombres"""
    results = []
    for name in names:
        if search.lower() in name['Name'].lower() and name not in results:
            results.append(name)
    return results

"""                   THEMES          """
async def psv_themes():
    """ PSVITA THEMES """
    filename = "psv/PSV_THEMES.tsv"
    search = input("Nombre: ")
    games = await process_themes(filename)
    if games:
        matches = await search_themes(games, search)
        if matches:
            clear_console()
            print('PSVITA THEMES')
            print(f"Se encontraron {len(matches)} resultados para '{search}':")
            for match in matches:
                try:
                    title_id = match["Title ID"]
                    region = match["Region"]
                    name = match["Name"]
                    #require_fw_v = match["Required FW"]
                    pkg_link = match["PKG direct link"] #\nRequire Firware Version: {require_fw_v}
                    file_size = match["File Size"]
                    print(Fore.MAGENTA + f'Name: {name}\nTitle ID: {title_id}\nRegion: {region}\nPKG Link: '+Fore.GREEN + f'{pkg_link}') 
                    print(Fore.WHITE+"-" * 40)

                except Exception as ex:
                    print(Fore.RED+f"*Error")
                    print(Fore.WHITE+"-" * 40)

            input('\n\n*Enter...')
            clear_console()
            print('1- Reintentar\n2- Menú PSVITA')
            option = input('=')
            if option == '1':
                await psv_themes()
            elif option == '2':
                await psv_menu()
        else:
            print(f"No se encontraron resultados para '{search}'.")
            input('\n\n*Enter...')
            clear_console()
            print('1- Reintentar\n2- Menú PSVITA')
            option = input('=')
            if option == '1':
                await psv_themes()
            elif option == '2':
                await psv_menu()
    else:
        print("No se pudo procesar el archivo")
        print('Recuerde colocar los archivos bien en sus respectivas carpetas')
        input('Enter para salir...')


async def process_themes(filename):
    """ Función para revisar los archivos .tsv """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
            lines = data.split('\n')
            header = lines[0].split('\t')
            result = []
            for line in lines[1:]:
                if line.strip():
                    game_data = {}
                    values = line.split('\t')
                    for i, value in enumerate(values):
                        game_data[header[i]] = value
                    result.append(game_data)
            return result
    except FileNotFoundError:
        print(f"ERROR: El archivo {filename} no existe")
        print('Recuerde colocar los archivos bien en sus respectivas carpetas')
        input('Enter para salir...')

async def search_themes(names, search):
    """ buscar por nombres"""
    results = []
    for name in names:
        if search.lower() in name['Name'].lower() and name not in results:
            results.append(name)
    return results



"""                   UPDATES          """
async def psv_updates():
    """ PSVITA UPDATES """
    filename = "psv/PSV_UPDATES.tsv"
    search = input("Nombre: ")
    games = await process_updates(filename)
    if games:
        matches = await search_updates(games, search)
        if matches:
            clear_console()
            print('PSVITA UPDATES')
            print(f"Se encontraron {len(matches)} resultados para '{search}':")
            for match in matches:
                try:
                    title_id = match["Title ID"]
                    region = match["Region"]
                    name = match["Name"]
                    #require_fw_v = match["Required FW"]
                    pkg_link = match["PKG direct link"] #\nRequire Firware Version: {require_fw_v}
                    file_size = match["File Size"]
                    print(Fore.MAGENTA + f'Name: {name}\nTitle ID: {title_id}\nRegion: {region}\nPKG Link: '+Fore.GREEN + f'{pkg_link}') 
                    print(Fore.WHITE+"-" * 40)

                except Exception as ex:
                    print(Fore.RED+f"*Error")
                    print(Fore.WHITE+"-" * 40)

            input('\n\n*Enter...')
            clear_console()
            print('1- Reintentar\n2- Menú PSVITA')
            option = input('=')
            if option == '1':
                await psv_updates()
            elif option == '2':
                await psv_menu()
        else:
            print(f"No se encontraron resultados para '{search}'.")
            input('\n\n*Enter...')
            clear_console()
            print('1- Reintentar\n2- Menú PSVITA')
            option = input('=')
            if option == '1':
                await psv_updates()
            elif option == '2':
                await psv_menu()
    else:
        print("No se pudo procesar el archivo")
        print('Recuerde colocar los archivos bien en sus respectivas carpetas')
        input('Enter para salir...')


async def process_updates(filename):
    """ Función para revisar los archivos .tsv """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
            lines = data.split('\n')
            header = lines[0].split('\t')
            result = []
            for line in lines[1:]:
                if line.strip():
                    game_data = {}
                    values = line.split('\t')
                    for i, value in enumerate(values):
                        game_data[header[i]] = value
                    result.append(game_data)
            return result
    except FileNotFoundError:
        print(f"ERROR: El archivo {filename} no existe")
        print('Recuerde colocar los archivos bien en sus respectivas carpetas')
        input('Enter para salir...')

async def search_updates(names, search):
    """ buscar por nombres"""
    results = []
    for name in names:
        if search.lower() in name['Name'].lower() and name not in results:
            results.append(name)
    return results