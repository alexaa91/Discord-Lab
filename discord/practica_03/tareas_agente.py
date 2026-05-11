import datetime

def agregar_tarea(lista_tareas, descripcion)
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