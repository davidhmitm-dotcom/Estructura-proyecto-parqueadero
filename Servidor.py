parqueadero = []
capacidad = 20
import socket

HOST = '0.0.0.0' 
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Servidor escuchando en el puerto", PORT)

conn, addr = server.accept()
print("Cliente conectado desde:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break

    placa = data.decode().strip()
    if placa in parqueadero:
        parqueadero.remove(placa)
        print(f"{placa} → SALE ")
        print(f"Ocupación: {len(parqueadero)}/{capacidad}")
    else:
        
        if len(parqueadero) < capacidad:
            parqueadero.append(placa)
            print(f"{placa} → ENTRA ")
            print(f"Ocupación: {len(parqueadero)}/{capacidad}")
        else:
            print(f"{placa} → PARQUEADERO LLENO ")
            print(f"Ocupación: {len(parqueadero)}/{capacidad}")

conn.close()
server.close()