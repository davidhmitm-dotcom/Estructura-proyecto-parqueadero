#include "placas.h"
#include <cstdlib>
#include <string>

std::string generarPlaca() {
    std::string placa = "";

    for (int i = 0; i < 3; i++) {
        placa += 'A' + rand() % 26;
    }

    for (int i = 0; i < 3; i++) {
        placa += '0' + rand() % 10;
    }

    return placa;
}