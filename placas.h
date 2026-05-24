#ifndef PLACAS_H
#define PLACAS_H

#include <string>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

extern "C" EXPORT std::string generarPlaca();

#endif