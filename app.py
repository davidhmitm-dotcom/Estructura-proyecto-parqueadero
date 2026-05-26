import streamlit as st
import socket
import threading
import time

CAPACIDAD = 20

# ESTRUCTURA
if "parqueadero" not in st.session_state:
    st.session_state.parqueadero = {}  # placa -> tiempo
    st.session_state.historial = []

parqueadero = st.session_state.parqueadero
historial = st.session_state.historial

lock = threading.Lock()

# aqui se enlaza con el servidor
def servidor():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8080))
    server.listen(1)

    print("Esperando conexión...")
    conn, addr = server.accept()
    print("Cliente conectado:", addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break

        placa = data.decode().strip()
        print("📩 Recibido:", placa)

        with lock:
            if placa in parqueadero:
                tiempo_total = int(time.time() - parqueadero[placa])
                historial.append(f"{placa} SALIÓ - {tiempo_total}s")
                del parqueadero[placa]
            else:
                if len(parqueadero) < CAPACIDAD:
                    parqueadero[placa] = time.time()
                    historial.append(f"{placa} ENTRÓ")

    conn.close()
    server.close()

# inicia servidor
if "server_running" not in st.session_state:
    threading.Thread(target=servidor, daemon=True).start()
    st.session_state.server_running = True

st.set_page_config(page_title="Parqueadero", layout="wide")

COLUMNAS = 5

# estructura visual
st.title("GPI controller (gestion de parqueadero)")

ocupacion = len(parqueadero)
st.metric("Vehículos dentro", f"{ocupacion}/{CAPACIDAD}")
st.progress(ocupacion / CAPACIDAD)

st.divider()
st.subheader("Ocupacion de slots en tiempo real")

placas = list(parqueadero.keys())

for i in range(0, CAPACIDAD, COLUMNAS):
    cols = st.columns(COLUMNAS)

    for j in range(COLUMNAS):
        idx = i + j

        with cols[j]:
            if idx < len(placas):
                placa = placas[idx]
                tiempo_entrada = parqueadero[placa]
                tiempo_actual = int(time.time() - tiempo_entrada)

                minutos = tiempo_actual // 60
                segundos = tiempo_actual % 60

                st.error(f"🚗 {placa}")
                st.caption(f"⏱ {minutos}m {segundos}s")

                # boton para sacar manualmente
                if st.button("Sacar", key=f"btn_{placa}_{idx}"):
                    with lock:
                        if placa in parqueadero:
                            tiempo_total = int(time.time() - parqueadero[placa])
                            historial.append(f"{placa} SALIÓ (manual) - {tiempo_total}s")
                            del parqueadero[placa]

                    st.rerun()

            else:
                st.success("Libre")

st.divider()
st.subheader("📋 Historial")
st.write(historial[-10:])

# Auto refresh cada 1 segundo
time.sleep(1)
st.rerun()