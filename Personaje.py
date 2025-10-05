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
    
    
    nuevo_personaje = ingresar_informacion_personaje(matriz)
    
    tamanio_inicial = len(matriz)
    matriz.append(nuevo_personaje)
    if tamanio_inicial == len(matriz):
        print("Error: No se pudo agregar el personaje.")
        return False
    else:
        print("Personaje agregado exitosamente.")
        return True
    
def ingresar_informacion_personaje(matriz : list) -> list:
    """Solicita al usuario que ingrese información para un nuevo personaje.
    Args:
        matriz (list): Matriz principal de personajes.

    Returns:
        list: Lista con la información del nuevo personaje.
    """
    # Solicitar y validar cada dato del personaje
    nombre_heroe = ingreso_string("Nombre del héroe: ","Error: El nombre no puede estar vacío ni exceder los 50 caracteres.", 1, 50)
    alias = ingreso_string("Alias: ","Error: El alias no puede estar vacío ni exceder los 30 caracteres.", 1, 30)
    raza = ingreso_de_informacion_especifica(matriz, 2, "Ingrese la raza: ", "Error: Raza no válida.")
    genero = ingreso_de_informacion_especifica(matriz, 3, "Ingrese el género: ", "Error: Género no válido.")
    poder = ingreso_entero("Ingrese el poder (1-100): ","Error: Debe ingresar un número entre 1 y 100.", 1, 100)
    inteligencia = ingreso_entero("Ingrese el inteligencia (1-100): ","Error: Debe ingresar un número entre 1 y 100.", 1, 100)
    velocidad = ingreso_entero("Ingrese el velocidad (1-100): ","Error: Debe ingresar un número entre 1 y 100.", 1, 100)
    
    return [nombre_heroe, alias, raza, genero, poder, inteligencia, velocidad]
    
def ingreso_de_informacion_especifica(matriz: list, indice: int, mensaje: str, mensaje_error: str) -> str:
    """Solicita al usuario que ingrese una raza y la valida.

    Args:
        matriz (list): Matriz principal de personajes.
        indice (int): Índice de la columna que contiene la información buscada.
        mensaje (str): Mensaje que se muestra al usuario para solicitar el ingreso.
        mensaje_error (str): Mensaje que se muestra en caso de error.

    Returns:
        str: Raza ingresada y validada.
    """
    limpiar_pantalla()
    lista = conseguir_cadena_unicas(matriz, indice)
    print("Opciones disponibles:")
    for elemento in lista:
        print(f"- {elemento}")
    data = input(mensaje)
    data = validar_string_lista(data, mensaje_error, lista)
    return data

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

def mostrar_personajes(matriz: list) -> bool:
    """Muestra la matriz de personajes en un formato legible.

    Args:
        matriz (list): Matriz principal de personajes.
    Returns:
        bool: True si la matriz se mostró correctamente, False si estaba vacía.
    """
    if len(matriz) == 0:
        print("La matriz está vacía.")
        return False
    
    for personaje in matriz:
        mostrar_personaje(personaje)
    return True
        
def mostrar_personaje(personaje: list) -> None:
    """Muestra la información de un personaje en un formato legible.

    Args:
        personaje (list): Lista con la información del personaje.
    """
    print(f"Nombre del héroe: {personaje[0]}")
    print(f"Alias: {personaje[1]}")
    print(f"Raza: {personaje[2]}")
    print(f"Género: {personaje[3]}")
    print(f"Poder: {personaje[4]}")
    print(f"Inteligencia: {personaje[5]}")
    print(f"Velocidad: {personaje[6]}")
    print("-" * 40)
    
def mostrar_quince_caracteres(matriz: list) -> None:
    """Muestra los primeros 15 caracteres de cada cadena en la matriz.

    Args:
        matriz (list): Matriz principal de personajes.
    """
    for fila in matriz:
        mostrar_personaje_quince_caracteres(fila)
        

def mostrar_personaje_quince_caracteres(personaje: list) -> None:
    """Muestra los primeros 15 caracteres de cada atributo de un personaje.

    Args:
        personaje (list): Lista que representa un personaje.
    """
    # data = ""
    # for i in range(len(personaje)):
    #     data += str(personaje[i]) + ","
    # print (data[:15] + "...")
    print(f"{personaje[0][:15]},{personaje[1][:15]},{personaje[2][:15]},{personaje[3][:15]},{str(personaje[4])[:15]},{str(personaje[5])[:15]},{str(personaje[6])[:15]} ...")
