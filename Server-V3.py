import re
import socket
import sys
import netifaces as ni
from random import randint, uniform, random

if len(sys.argv) != 2:
    print ("Agregar el puerto donde se va a ofrecer el servicio.")
    sys.exit(0)

ni.ifaddresses('ens3')
IP = ni.ifaddresses('ens3')[ni.AF_INET][0]['addr']
PUERTO = int(sys.argv[1])

print ("\nServicio se va a configurar en la ip: ",IP," y el puerto: ", PUERTO, " ...")

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace del socket con la IP y el puerto
socket_servidor.bind((IP, PUERTO))

# Escuchar conexiones entrantes con el metodo listen,
# El parametro indica el numero de conexiones entrantes que vamos a aceptar
socket_servidor.listen(2)

print ("Servicio configurado.\n")

try:
    while True:
        print ("Esperando conexión de un cliente ...")
        # Instanciar objeto socket_cliente para recibir datos,
        # direccion_cliente recibe la tupla de conexion: IP y puerto
        socket_cliente, direccion_cliente = socket_servidor.accept()
        print ("Cliente conectado desde: ", direccion_cliente)

        while True:
            try:
                recibido = socket_cliente.recv(1024).decode('utf-8')
                print (direccion_cliente[0] + " >> ", recibido)
                if recibido == "finalizar()":
                    print ("Cliente finalizo la conexion.")
                    print ("Cerrando la conexion con el cliente ...")
                    socket_cliente.close()
                    print ("Conexion con el cliente cerrado.")
                    break
                
                lista = recibido.split(" ")
                try:
                    dados = int(lista[1])
                    cantidad = int(lista[0])
                except:
                    print("Usted ingreso algo indebido")
                    print ("Cerrando el servicio ...")
                    socket_servidor.close()
                    print ("Servicio cerrado, Adios!")
                cadena = ""
                sumador = 0
                
                print("\nCARAS DEL DADOS "+str(dados)+" NUMERO DE DADOS "+str(cantidad)+"\n\n")
                
                for x in range(cantidad):
                    numero_dado = randint(1,dados)
                    sumador = sumador + numero_dado
                    if(x==cantidad-1):
                        cadena = cadena + str(numero_dado)
                    else:
                        cadena = cadena + str(numero_dado) + "+"
                cadena = cadena + "=" + str(sumador)  
                
                
                respuesta_servidor =  direccion_cliente[0] + " envio: " + cadena #UN ERROR AQUI
                socket_cliente.send(str.format(respuesta_servidor).encode("utf-8"))
            except socket.error:
                print ("Conexion terminada abruptamente por el cliente.")
                print ("Cerrando conexion con el cliente ...")
                socket_cliente.close()
                print ("Conexion con el cliente cerrado.")
                break
            except KeyboardInterrupt:
                print ("\n∫Se interrunpio el cliente con un Control_C.")
                print ("Cerrando conexion con el cliente ...")
                socket_cliente.close()
                print ("Conexion con el cliente cerrado.")
                break

except KeyboardInterrupt:
    print ("\nSe interrumpio el servidor con un Control_C.")
    print ("Cerrando el servicio ...")
    socket_servidor.close()
    print ("Servicio cerrado, Adios!")
