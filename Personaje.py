from Funciones_Generales import *
from utn_fra.datasets import (
    lista_nombre_heroes_pp, lista_alias_pp,
    lista_razas_pp, lista_generos_pp,
    lista_poderes_pp, lista_inteligencias_pp,
    lista_velocidades_pp
 )

def crear_matriz_de_personajes() -> list:
    """Crea una matriz de personajes a partir de listas predefinidas.

    Returns:
        list: Matriz principal de personajes.
    """
    
    matriz_personajes = []
    cantidad_personajes = len(lista_nombre_heroes_pp)
    # Se toman los datos de cada lista y se agrupan en una 
    # sublista por personaje y se agrega a la matriz principal.
    for i in range(cantidad_personajes):
        personaje = [
            lista_nombre_heroes_pp[i],
            lista_alias_pp[i],
            lista_razas_pp[i],
            lista_generos_pp[i],
            lista_poderes_pp[i],
            lista_inteligencias_pp[i],
            lista_velocidades_pp[i]
        ]
        matriz_personajes.append(personaje)

    return matriz_personajes

def agregar_personaje(matriz: list) -> bool:
    """Agrega un nuevo personaje a la matriz de personajes.

    Args:
        matriz (list): Matriz principal de personajes.

    """
    print("Ingrese los datos del nuevo personaje:")
    
    nombre_heroe = ingreso_string("Nombre del héroe: ","Error: El nombre no puede estar vacío ni exceder los 50 caracteres.", 1, 50)
    alias = ingreso_string("Alias: ","Error: El alias no puede estar vacío ni exceder los 30 caracteres.", 1, 30)
    # Falta crear funcion para conseguir la lista de razas y crear el ingreso y validacion de la raza
    lista_razas = conseguir_cadena_unicas(matriz,2)
    mensaje_raza = f"Ingrese raza : {lista_razas}"
    raza = ingreso_string("Raza: ","Error: La raza no puede estar vacía ni exceder los 20 caracteres.", lista_razas)
    # -----------------------------------------------------
    genero = input("Género: ")
    poder = ingreso_entero("Ingrese el poder (1-100): ","Error: Debe ingresar un número entre 1 y 100.", 1, 100)
    inteligencia = ingreso_entero("Ingrese el inteligencia (1-100): ","Error: Debe ingresar un número entre 1 y 100.", 1, 100)
    velocidad = ingreso_entero("Ingrese el velocidad (1-100): ","Error: Debe ingresar un número entre 1 y 100.", 1, 100)

    nuevo_personaje = [
        nombre_heroe,
        alias,
        raza,
        genero,
        poder,
        inteligencia,
        velocidad
    ]
    tamanio_inicial = len(matriz)
    matriz.append(nuevo_personaje)
    if tamanio_inicial == len(matriz):
        print("Error: No se pudo agregar el personaje.")
        return False
    else:
        print("Personaje agregado exitosamente.")
        return True
    
    
def conseguir_cadena_unicas(matriz: list, columna: int) -> list:
    """Obtiene una lista de cadenas únicas de una columna específica en la matriz.

    Args:
        matriz (list): Matriz principal de personajes.
        columna (int): Índice de la columna de la cual se extraerán las cadenas.

    Returns:
        list: Lista de cadenas únicas.
    """
    cadenas_unicas = []
    for fila in matriz:
        valor = fila[columna]
        if valor not in cadenas_unicas:
            cadenas_unicas.append(valor)
    return cadenas_unicas