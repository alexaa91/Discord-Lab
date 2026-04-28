import datetime
def obtener_saludo(nombre_bot):
    """
    retorna un saludo formateado
    """
    return f"Hola, soy {nombre_bot} y estoy listo para ayudarte"

def procesar_comando_recordar(comando):
    """
    Valida y procesa la acción de recordar un dato
    """
    if not comando:
        return "Error: falta el nombre. Uso !recordar [nombre]"
    else:
        return f"Entendido! Recordaré el nombre: {comando}"

def calcular_uptime(hora_inicio):
    """
    Calculan la diferencia de tiempo entre el inicio y el actual (mostrar actividad del bot)
    """
    ahora = datetime.datetime.now()
    diferencia = ahora - hora_inicio
    segundos = int(diferencia.total_seconds())
    return f"Tiempo de actividad {segundos} segundos"

def mostrar_ayuda():
    """
    Comandos disponibles para el usuario
    """
    return(
        "Comandos dispnibles:\n"
        "!saludo - Muestra un saludo del bot\n"
        "!recordar [nombre] - El bot recordará el nombre proporcionado\n"
        "!uptime - Muestra el tiempo de actividad del bot\n"
        "!ayuda - Muestra esta lista de comandos"
    )

#función principal para probar la funcion

def iniciar_agente():
    NOMBRE_BOT = "RodrigoBot"
    PREFIJO = "!"
    hora_inicio = datetime.datetime.now()

    print(f"{obtener_saludo(NOMBRE_BOT)}")
    print("Escribe !ayuda para ver los comandos disponibles")

    ejecutando = True
    while ejecutando:
        entrada = input(f"[{NOMBRE_BOT}] Ingrese comando: ").strip()

        if not entrada.startswith(PREFIJO):
            print("Comando no reconocido")
            continue

        partes = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = partes[0].lower()
        argumento = partes[1] if len(partes) > 1 else ""

        if comando == "saludo":
            print(obtener_saludo(NOMBRE_BOT))
        elif comando == "ayuda":
            print(mostrar_ayuda())
        elif comando == "salir":
            print("¡Hasta pronto!")
            ejecutando = False
        else:
            print("Comando no reconocido")

def main():
    iniciar_agente()

if __name__ == "__main__":
    main()