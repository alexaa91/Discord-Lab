import datetime

from practica_03.agente_logica import (
    ejecutar_suma,
    ejecutar_multiplicacion,
    buscar_en_diccionario,
    validar_variable,
    obtener_fecha_completa,
    historial_comandos
)

def analizar_comando(entrada_usuario):
    mensaje = entrada_usuario.lower().strip()

    if mensaje.startswith("!"):
        partes = mensaje.split(" ", 1)
        comando = partes[0]
        argumento = partes[1] if len(partes) > 1 else None

        if len(historial_comandos) >= 5:
            historial_comandos.pop(0)

        historial_comandos.append(comando)

        if comando == "!definir":
            return buscar_en_diccionario(argumento)

        elif comando == "!validar":
            return validar_variable(argumento)

        elif comando == "!hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f"Hora actual: {ahora}"

        elif comando == "!historial":
            respuesta = "Últimos comandos:\n"

            for i, cmd in enumerate(historial_comandos, 1):
                respuesta += f"{i}. {cmd}\n"

            return respuesta

        elif comando == "!sumar":
            return ejecutar_suma(argumento)

        elif comando == "!multiplicar":
            return ejecutar_multiplicacion(argumento)

        elif comando == "!fecha":
            return obtener_fecha_completa()

        elif comando == "!ayuda":
            return (
                "Comandos disponibles:\n"
                "!definir\n"
                "!validar\n"
                "!hora\n"
                "!historial\n"
                "!sumar\n"
                "!multiplicar\n"
                "!fecha"
            )

        else:
            return f"El comando '{comando}' no existe."

    return "Usa '!' para comandos."


if __name__ == "__main__":
    while True:
        entrada = input("Alumno >> ")

        if entrada.lower() in ["salir", "exit"]:
            break

        print("Bot >>", analizar_comando(entrada))

    