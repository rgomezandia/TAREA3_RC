#!/usr/bin/python
# -*- coding: utf-8 -*-
# Programa Cliente

import socket
import sys
import re

if len(sys.argv) != 3:
    print ("Agregar la IP del servidor y el puerto donde se ofrece el servicio.")
    sys.exit(0)

IP = sys.argv[1]
PUERTO = int(sys.argv[2])

print ("\nConectandose al servidor ", IP, " en el puerto ", PUERTO, " ...")

try:
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((IP, PUERTO))
except:
    print ("No se puede conectar con el servidor.", IP, " en el puerto ", PUERTO)
    sys.exit(0)

print ("\nConectado, escriba finalizar() para terminar la conección.")
print ("\nDebe enviar el numero de dado y su cantidad de caras separados por un espacio, ambos hasta 100!!.\n\n") #solo como referencia

try:
    while True:
        mensaje = input("Yo >>")
        socket_cliente.send(str.format(mensaje).encode("utf-8"))
        if mensaje == "finalizar()":
            break
        recibido = socket_cliente.recv(1024).decode('utf-8')
        print ("Servidor >> " + recibido)

except socket.error:
    print ("Se perdio la conexion con el servidor.")
except KeyboardInterrupt:
    print ("\nSe interrunpio el cliente con un Control_C.")

finally:
    print ("Terminando conexion con el servidor ...")
    socket_cliente.close()
    print ("Conexion con el servidor terminado.")