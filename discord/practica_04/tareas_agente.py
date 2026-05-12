import datetime

def agregar_tarea(lista_tareas, descripcion):
    """
    Agregar una tarea a la lista si cumple los requisitos
    """

    if len(descripcion) < 3:
        return "Error, longitud inválida"
    
    #Crear formato para tareas
    fecha = datetime.datetime.now().strftime("%H:%M")
    nueva_tarea = f"{descripcion} - {fecha}"
    lista_tareas.append(nueva_tarea)
    return f"Tarea agregada con exito"

def listar_tareas(lista_tareas):
    """
    Formatea la lista de tareas para su visualizacion
    """
    if not lista_tareas:
        return "No hay tarea"
    
    #agregar una variable llamada resultado
    resultado = "Listado de tareas: \n"

    #iterar la lista de tareas y formatear la salida
    for i, tarea in enumerate(lista_tareas, start=1):
        resultado += f"{i}. {tarea}\n"
    return resultado

def eliminar_tarea(lista_tareas, indice):
    """
    Elimina tarea por su numero de indice
    """
    if not indice.isdigit():
        return "Error, el indice debe ser un numero"
    
    indice = int(indice) - 1

    #agregamos la lógica para preguntar si el elemento está en la lista y eliminarlo
    if 0 <= indice < len(lista_tareas):
        tarea_eliminada = lista_tareas.pop(indice)
    else:
        return "Error: No existe la tarea"
    return f"Tarea eliminada: {tarea_eliminada}"

def main():
    tareas = []
    PREFIJO = "!"

    print("Bienvenido al gestor de tareas.")
    activa = True
    while activa:
        entrada = input(">>>").strip()

        if not entrada.startswith(PREFIJO):
            print("Error: Comando no reconocido")
            continue

        #procesamiento de la entrada
        cuerpo = entrada[len(PREFIJO):].spli(maxsplit=1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""

        #selección de acción
        if comando == "add":
            resultado = agregar_tarea(tareas, argumento)
        elif comando == "list":
            print(listar_tareas(tareas))
            
        elif comando == "del":
            print(eliminar_tarea(tareas, argumento))
            
        else:
            print(f" Error: Comando '!{comando}' no reconocido.")
        
        print("-" * 20)

if __name__ == "__main__":
    main()



