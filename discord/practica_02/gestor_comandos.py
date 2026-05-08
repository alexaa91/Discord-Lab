import datetime

def analizar_comando(entrada_usuario):
    """
    Segunda fase del agente: Procesamiento de comandos y lógica dinamica
    Aquí el alumno aprende a separar la acción de los datos
    """

    mensaje = entrada_usuario.lower().strip()

    #simulación de comandos prefijados(como se usan en Discord: !ayuda, !ejemplo)
    if mensaje.startswith("!"):
        partes = mensaje.split(" ", 1)
        comando = partes[0]
        argumento = partes[1] if len(partes) > 1 else None

        #Lógica de comandos
        if comando == "!definir":
            return buscar_en_diccionario(argumento)
        
        elif comando == "!validar":
            return validar_variable(argumento)
        
        elif comando == "!hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f"La hora actual del servidor es: {ahora}"
        
        elif comando ==  "!ahora":
            return ("Comandos disponibles: \n"
            "1. '!definir <termino>' - Busca conceptos en Python \n"
            "2. '!validar <nombre>' - Revisa si un nombre de variable es válido. \n"
            "3. '!hora' - Muestra la hora del sistema")
def buscar_en_diccionario(termino):


def validar_variable(nombre):
