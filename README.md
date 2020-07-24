# Conexión Cliente Servidor



### Acerca de este Trabajo

Esta es una implementación en Python del Juego de Dados en una aplicación cliente - servidor, donde el cliente envía la cantidad de dados y la cantidad de caras de esto, para obtener la suma resultante


### Parametros del Cliente   

1. __DirecciónIP__ : Este parametro debe ser una diracción de la forma "127.0.0.1"
2. __Puerto__: Es el puerto por donde establecerá una conexión con el Servidor. Ejemplo: 9090

### Parametros del Servidor   

1. __Puerto__: Es el puerto por donde establecerá una conexión con el Cliente. Ejemplo: 9090

### Instrucciones para correr el programa en una terminal linux

~~~
$ git clone https://github.com/rgomezandia/TAREA3_RC.git
~~~

~~~
$ cd TAREA3_RC-master
~~~

### Ejecutar Cliente
~~~
 $ python3 Server-V3.py "__DirecciónIP__" "__Puerto__"
~~~

### Ejecutar Servidor
~~~
 $ python3 Client-V3.py "__Puerto__"
~~~
