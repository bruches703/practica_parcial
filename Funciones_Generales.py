import os
def limpiar_pantalla():
    """Limpia la pantalla
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def ingreso_entero(mensaje: str, mensaje_error: str,
                    minimo: int = None,
                    maximo: int = None) -> int:
    """
    Solicita al usuario que ingrese un número entero dentro de un rango específico.
    
    Args:
        mensaje (str): Mensaje que se muestra al usuario para solicitar el ingreso.
        mensaje_error (str): Mensaje que se muestra en caso de error.
        minimo (int, optional): Valor mínimo permitido. Si no se especifica, no hay límite inferior.
        maximo (int, optional): Valor máximo permitido. Si no se especifica, no hay límite superior.
    
    Returns:
        int: Número entero ingresado por el usuario que cumple con las condiciones.
    """
    numero = input(mensaje)
    numero = convertir_entero(numero)
    numero = validacion_entero(numero, mensaje_error, minimo, maximo)
    return numero

def ingreso_string(mensaje: str, mensaje_error: str,
                    largo_min: int = None,
                    largo_max: int = None) -> str:
    """Ingresa una cadena de texto y valida su longitud.

    Args:
        mensaje (str): Mensaje que se muestra al usuario para solicitar el ingreso.
        mensaje_error (str): Mensaje que se muestra en caso de error.
        largo_min (int, optional): minimo permitido. Defaults to None.
        largo_max (int, optional): maximo permitido. Defaults to None.

    Returns:
        str: Cadena de texto validada.
    """
    cadena = input(mensaje)
    cadena = validar_string(cadena, mensaje_error, largo_min, largo_max)
    
def validacion_entero(numero: int, mensaje_error: str,  minimo: int = None, maximo: int = None) -> int:
    """
    Valida si un número entero cumple con las condiciones especificadas.
    
    Args:
        numero (int): Número entero a validar.
        minimo (int, optional): Valor mínimo permitido. Si no se especifica, no hay límite inferior.
        maximo (int, optional): Valor.maxcdnimo permitido. Si no se especifica, no hay límite superior.
        mensaje_error (str): Mensaje que se muestra en caso de error.
    
    Returns:
        int: Número entero validado.
    """
    while numero == -1 or (minimo is not None and numero < minimo) or (maximo is not None and numero > maximo):
        print(mensaje_error)
        numero = convertir_entero(input("Reingrese: "))
    return numero

def validar_string(cadena: str, mensaje_error: str, largo_min: int = None, largo_max: int = None) -> str:
    """Valida si una cadena de texto cumple con las condiciones especificadas.

    Args:
        cadena (str): Cadena de texto a validar.
        mensaje_error (str): Mensaje que se muestra en caso de error.
        largo_min (int, optional): minimo permitido. Defaults to None.
        largo_max (int, optional): maximo permitido. Defaults to None.

    Returns:
        str: Cadena de texto validada.
    """
    while (largo_min is not None and len(cadena) < largo_min) or (largo_max is not None and len(cadena) > largo_max):
        print(mensaje_error)
        cadena = input("Reingrese: ")
    return cadena

def convertir_entero(numero: str) -> int:
    """
    Verifica si una cadena de texto puede ser convertida a un número entero.
    
    Args:
        numero (str): Cadena de texto a verificar.
    
    Returns:
        int: devuelve el numero entero si es posible convertirlo, de lo contrario devuelve -1.
    """
    try:
        int(numero)
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return -1
    
    return int(numero)