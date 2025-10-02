from Funciones_Generales import *
from Personaje import *
from Menu import menu

def main():
    """Función principal del programa que maneja el menú y las opciones del usuario.
    """
    while True:
        limpiar_pantalla()
        match menu():
            case 1:
                print("Crear matriz")
            case 2:
                print("Agregar personaje")
            case 22:
                print("Salir")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")
                continue

matriz_personajes = crear_matriz_de_personajes()
lista_razas = conseguir_cadena_unicas(matriz_personajes, 2)
lista_genero = conseguir_cadena_unicas(matriz_personajes, 3)


for raza in lista_razas:
    print(raza)
    
input("Presione Enter para continuar...\n\n")

limpiar_pantalla()
print("\n\n\n")
for genero in lista_genero:
    print(genero)