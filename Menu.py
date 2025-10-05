from Funciones_Generales import *

def menu() -> int:
    """Menu de opciones del programa.

    Returns:
        int: Opción seleccionada por el usuario.
    """
    print("\nMenú de opciones:\n")
    print("1- Crear matriz")
    print("2- Agregar personaje")
    print("22- Salir")
    return ingreso_entero("Seleccione una opción: ", "Error: Opción no válida.", 1, 22)