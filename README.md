# Estructura-proyecto-parqueadero
# Proyecto parqueadero // trabajo estructura de datos
Este proyecto consiste en un sistema inteligente de parqueadero desarrollado con arquitectura cliente-servidor que se divide en dos partes, Un cliente en C++ encargado de generar placas aleatorias y enviarlas mediante sockets TCP y un servidor en Python con Streamlit encargado de recibir las placas, administrar los espacios del parqueadero y mostrar una interfaz gráfica en tiempo real. 

# Características
-	Generación automática de placas: El sistema genera placas aleatorias con formato ABC123
-	Comunicación entre computadores: El cliente y el servidor pueden ejecutarse en computadores distintos dentro de la misma     red local.
-	Interfaz gráfica en tiempo real: La interfaz desarrollada con Streamlit permite visualizar:
  o	Espacios libres y ocupados
  o	Placas de los vehículos
  o	Historial de entradas y salidas
  o	Temporizador por vehículo
  o	Cantidad de espacios ocupados
-	Control manual de vehículos: El usuario puede retirar vehículos manualmente mediante botones dentro de la interfaz.
-	Arquitectura distribuida: El sistema implementa comunicación cliente-servidor usando sockets TCP.

# ¿Cómo funciona?
# Generación de placas:
El cliente en C++ genera placas aleatorias automáticamente cada 2 segundos.
# Envío mediante sockets:
Las placas se envían desde el cliente hacia el servidor utilizando sockets TCP con WinSock2.
# Recepción de datos:
El servidor en Python recibe las placas y verifica si el vehículo entra o sale, actualiza el estado del parqueadero y guarda el historial de movimientos
# Actualización de la interfaz:
Streamlit muestra los cambios en tiempo real:
-	Vehículos actuales
-	Espacios libres
-	Tiempo de permanencia

# Ejecutar
para correr el programa se debe abrir la carpeta (se puede descargar desde el repositorio) y en cmd se ejecuta el siguiente comando

python -m streamlit run app.py

este ejecutable abrira desde la terminal el streamlit que nos llevara al programa

caracteristicas del gestor:
- cuenta con temporizador de cada slot
- permite sacar manualmente cada vehiculo
- el generador ocupa nuevamente los slots vacios

para compilar el generador se debe usar el siguiente codigo
g++ generador.cpp placas.cpp -o generador.exe -lws2_32
