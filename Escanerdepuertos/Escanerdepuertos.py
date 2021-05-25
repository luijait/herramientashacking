import socket 
import sys
from datetime import datetime 
import pyfiglet
ascii_banner = pyfiglet.figlet_format("ESCANER DE PUERTOS BY @LUIJAIT_ASM")
print(ascii_banner)
if len(sys.argv) == 2:
    objetivo = socket.gethostbyname(sys.argv[1])
else:
    print("Introduzca una IP como argumento")  

print("-" * 70)
print("Esceando: " + objetivo )
print("Escaneo ha empezado a esta hora: " + str(datetime.now()))
print("-" * 70)
try:

    for puerto in range(1,100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        conexion = s.connect_ex((objetivo,puerto))
        if conexion ==0:
            print ("Puerto {} esta abierto".format(puerto))
        else:
            print("Puerto {} esta cerrado".format(puerto))
        
    s.close()
except KeyboardInterrupt:
    print("\n Saliendo del programa...")
    sys.exit()
except socket.gaierror:
    print ("\n No se puede conectar con el objetivo")
    sys.exit()
except socket.error:
    print ("\n El objetivo no esta respondiendo")
    sys.exit()