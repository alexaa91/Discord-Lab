import datetime

from practica_02.procesador_comandos import (
    obtener_saludo,
    procesar_comando_recordar,
    calcular_uptime,
    mostrar_ayuda
)

NOMBRE_BOT = "RodrigoBot"
PREFIJO = "!"

hora_inicio = datetime.datetime.now()

def analizar_comando(entrada):
    if not entrada.startswith(PREFIJO):
        return "Comando no reconocido"

    partes = entrada[len(PREFIJO):].split(maxsplit=1)

    comando = partes[0].lower()
    argumento = partes[1] if len(partes) > 1 else ""

    if comando == "saludo":
        return obtener_saludo(NOMBRE_BOT)

    elif comando == "recordar":
        return procesar_comando_recordar(argumento)

    elif comando == "uptime":
        return calcular_uptime(hora_inicio)

    elif comando == "ayuda":
        return mostrar_ayuda()

    elif comando == "salir":
        return "¡Hasta pronto!"

    return "Comando no reconocido"


def main():
    print(obtener_saludo(NOMBRE_BOT))
    print("Escribe !ayuda para ver los comandos disponibles")

    while True:
        entrada = input(f"[{NOMBRE_BOT}] Ingrese comando: ")

        if entrada.lower() == "!salir":
            print("¡Hasta pronto!")
            break

        print(analizar_comando(entrada))


if __name__ == "__main__":
    main()