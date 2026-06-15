import datetime
import discord
import os
import re
from dotenv import load_dotenv
from practica_01.gestor_comandos import buscar_en_diccionario, validar_variable

hora_inicio = datetime.datetime.now()

def mostrar_bienvenida():
    """Retorna la lista de comandos disponibles."""
    return (
        "📜 Bot de Gestión de Tareas (Modo Estructurado):\n"
        "📜 Primeros pasos Agente Discord UX:\n"
        "📜 Esccriba !Exit para salir del Agente:\n"
        "📜 Escriba buscar 'Termino' para buscar en el diccionario:"
    )

def calcular_uptime(hora_inicio):

    """
    Calcula la diferencia de tiempo entre el inicio y el actual
    """
    ahora = datetime.datetime.now()
    diferencia = ahora - hora_inicio
    segundos = int(diferencia.total_seconds())

    return f"Tiempo de actividad: {segundos} segundos"

def main(entrada):

        PREFIJO = "!"

        if not entrada.startswith(PREFIJO):
            if entrada:
                print("Recuerda usar '!' para comandos.")

        cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)

        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""

        if comando == "exit":
            print("Saliendo del gestor...")
            return "Saliendo del gestor..."

        elif comando == "inicio":
            print(mostrar_bienvenida())
            return mostrar_bienvenida()

        elif comando == "uptime":
            print(calcular_uptime(hora_inicio))
            return calcular_uptime(hora_inicio)

        elif comando == "buscar":
            return buscar_en_diccionario(argumento)

        else:
            print(f" Error: Comando '!{comando}' no reconocido.")
            return f" Error: Comando '!{comando}' no reconocido."
        
        print("-" * 20)


# --- CONFIGURACIÓN DE DISCORD ---

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Definir los "intents" (permisos) necesarios
intents = discord.Intents.default()
intents.message_content = True  # Necesario para leer el contenido de los mensajes

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Sincronizado como {client.user} (ID: {client.user.id})')
    print('------')

@client.event
async def on_message(message):
    # Evitar que el bot se responda a sí mismo
    if message.author == client.user:
        return
    
    # 3. Procesamiento: Pasamos el contenido del mensaje a nuestra lógica
    print(f"Mensaje recibido de {message.author}: {message.content}")

      # Solo procesamos si el mensaje empieza con un prefijo (opcional, pero recomendado)
    if message.content.startswith('!'):
        resultado = main(message.content)

        print(f"Resultado del procesamiento: {resultado}")
        
        # 4. Respuesta: El bot escribe el resultado en el mismo canal
        await message.channel.send(f" *Bot Procesador:* {resultado}")
    
# Ejecutar el bot
if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print("ERROR: No se encontró el TOKEN en el archivo .env")