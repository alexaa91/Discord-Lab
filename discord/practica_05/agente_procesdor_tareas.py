from tareas_agente import (
    agregar_tarea,
    listar_tareas,
    eliminar_tarea
)

tareas = []

def analizar_comando(entrada):
    if not entrada.startswith("!"):
        return "Error: Comando no reconocido"

    partes = entrada[1:].split(maxsplit=1)

    comando = partes[0].lower()
    argumento = partes[1] if len(partes) > 1 else ""

    if comando == "add":
        return agregar_tarea(tareas, argumento)

    elif comando == "list":
        return listar_tareas(tareas)

    elif comando == "del":
        return eliminar_tarea(tareas, argumento)

    elif comando == "ayuda":
        return (
            "Comandos disponibles:\n"
            "!add [tarea]\n"
            "!list\n"
            "!del [número]"
        )

    return f"Error: Comando '!{comando}' no reconocido."


def main():
    print("Gestor de tareas iniciado")
    print("Escribe !ayuda para ver los comandos")

    while True:
        entrada = input(">>> ").strip()

        if entrada.lower() == "!salir":
            print("Hasta luego")
            break

        print(analizar_comando(entrada))
        print("-" * 20)

if __name__ == "__main__":
    main()
    