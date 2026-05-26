# Estructura-proyecto-parqueadero
Proyecto parqueadero // trabajo estructura de datos
El proyecto se divide en dos partes, la primera consta de un genrador de placas en el formato ABC123, el cual genera laqs placas cada 2 segundos
de momento solo se generan las placas, el app. py se testea para ver si funciona el streamlit, sin embargo no se genera conexion aun

para correr el programa se debe abrir la carpeta (se puede descargar desde el repositorio) y en cmd se ejecuta el siguiente comando


python -m streamlit run app.py

este ejecutable abrira desde la terminal el streamlit que nos llevara al programa

caracteristicas del gestor:
- cuenta con temporizador de cada slot
- permite sacar manualmente cada vehiculo
- el generador ocupa nuevamente los slots vacios


para compilar el generador se debe usar el siguiente codigo
g++ generador.cpp placas.cpp -o generador.exe -lws2_32
