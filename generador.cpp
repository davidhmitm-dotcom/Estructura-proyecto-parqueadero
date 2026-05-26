#include <iostream>
#include <cstdlib>
#include <ctime>
#include <winsock2.h>
#include "placas.h"

#pragma comment(lib, "ws2_32.lib")

using namespace std;

int main() {
    srand(time(0));

    WSADATA wsa;
    SOCKET clientSocket;
    sockaddr_in server;

    WSAStartup(MAKEWORD(2,2), &wsa);

    clientSocket = socket(AF_INET, SOCK_STREAM, 0);

    server.sin_family = AF_INET;
    server.sin_port = htons(8080);
    server.sin_addr.s_addr = inet_addr("192.168.1.18");

    if (connect(clientSocket, (struct sockaddr*)&server, sizeof(server)) != 0) {
        cout << "Error al conectar" << endl;
        return 1;
    }

    cout << "Conectado al servidor\n" << endl;

    while (true) {
        string placa = generarPlaca();  //  AQUÍ SE USA
        cout << "Enviando: " << placa << endl;

        send(clientSocket, placa.c_str(), placa.length(), 0);

        Sleep(2000);
    }

    closesocket(clientSocket);
    WSACleanup();

    return 0;
}