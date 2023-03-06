import csv
from colorama import init, Fore
from .util import cxb, clear_console

init()

"""                     PS3 MENU                     """
async def ps3_menu():
    """ Menú PS3 """
    clear_console()
    print('PS3:\n\n1- GAMES\n2- DLCs\n3- THEMES\n4- AVATARS')
    option = input('=')
    if option == '1':
        await ps3_games()
    elif option == '2':
        await ps3_dlcs()
    elif option == '3':
        await ps3_themes()
    elif option == '4':
        await ps3_avatars()
    

"""                        GAMES                       """
async def ps3_games():
    """ PSVITA GAMES """
    filename = "ps3/PS3_GAMES.tsv"
    clear_console()
    print('PS3 GAMES')
    search = input("Nombre: ")
    games = await process_games(filename)
    if games:
        matches = await search_games(games, search)
        if matches:
            clear_console()
            print('PS3 GAMES')
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

            input('\n\n*Enter...')
            clear_console()
            await ps3_menu()
        else:
            print(f"No se encontraron resultados para '{search}'.")
            input('Enter...')
            clear_console()
            print('1- Volver a Intentar\n2- Menú PS3')
            option = input('=')
            if option == '1':
                await ps3_games()
            elif option == '2':
                await ps3_menu()
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



"""                        DLCS                       """
async def ps3_dlcs():
    """ PSVITA DLCS """
    filename = "ps3/PS3_DLCS.tsv"
    clear_console()
    print('PS3 DLCS')
    search = input("Nombre: ")
    games = await process_dlcs(filename)
    if games:
        matches = await search_dlcs(games, search)
        if matches:
            clear_console()
            print('PS3 DLCS')
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

            input('\n\n*Enter...')
            clear_console()
            await ps3_menu()
        else:
            print(f"No se encontraron resultados para '{search}'.")
            input('Enter...')
            clear_console()
            print('1- Volver a Intentar\n2- Menú PS3')
            option = input('=')
            if option == '1':
                await ps3_dlcs()
            elif option == '2':
                await ps3_menu()
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





"""                        THEMES                     """
async def ps3_themes():
    """ PSVITA GAMES """
    filename = "ps3/PS3_THEMES.tsv"
    clear_console()
    print('PS3 THEMES')
    search = input("Nombre: ")
    games = await process_themes(filename)
    if games:
        matches = await search_themes(games, search)
        if matches:
            clear_console()
            print('PS3 THEMES')
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

            input('\n\n*Enter...')
            clear_console()
            await ps3_menu()
        else:
            print(f"No se encontraron resultados para '{search}'.")
            input('Enter...')
            clear_console()
            print('1- Volver a Intentar\n2- Menú PS3')
            option = input('=')
            if option == '1':
                await ps3_themes()
            elif option == '2':
                await ps3_menu()
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


"""                        AVATARS                     """
async def ps3_avatars():
    """ PSVITA GAMES """
    filename = "ps3/PS3_AVATARS.tsv"
    clear_console()
    print('PS3 AVATARS\n')
    search = input("= ")
    games = await process_avatars(filename)
    if games:
        matches = await search_avatars(games, search)
        if matches:
            clear_console()
            print('PS3 AVATARS')
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

            input('\n\n*Enter...')
            clear_console()
            await ps3_menu()
        else:
            print(f"No se encontraron resultados para '{search}'.")
            input('Enter...')
            clear_console()
            print('1- Volver a Intentar\n2- Menú PS3')
            option = input('=')
            if option == '1':
                await ps3_avatars()
            elif option == '2':
                await ps3_menu()
    else:
        print("No se pudo procesar el archivo")
        print('Recuerde colocar los archivos bien en sus respectivas carpetas')
        input('Enter para salir...')

async def process_avatars(filename):
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

async def search_avatars(names, search):
    """ buscar por nombres"""
    results = []
    for name in names:
        if search.lower() in name['Name'].lower() and name not in results:
            results.append(name)
    return results