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

def iniciar_agente():

def main():
    procesar_comando_recordar()
    procesar_comando_recordar()
    calcular_uptime()
    mostrar_ayuda()
    iniciar_agente()

if __name__ == "__main__":
    main()