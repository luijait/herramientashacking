import requests

url = input('[+] Introduce la URL: ')
archivo = input('[+] Introduce el nombre del archivo que contiene los directorios: ' )

def peticion(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass

lineas = open(archivo, 'r')
for linea in lineas:
        directorio = linea.strip()
        urlalcompleto = url + '/' + directorio
        repuesta = peticion(urlalcompleto)
        print (urlalcompleto)
        if repuesta:
            print("[+] Directorio Descubierto en esta ruta del servidor web " + urlalcompleto)
        else:
            print("No se ha encontrado la url citada")