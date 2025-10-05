from Funciones_Generales import *
from Personaje import *
from Menu import menu

def main():
    """Función principal del programa que maneja el menú y las opciones del usuario.
    """
    matriz_personajes = []
    while True:
        
        opcion = menu()
        
        if opcion == 1:
            matriz_personajes = crear_matriz_de_personajes()
            print("Matriz de personajes creada exitosamente.")
        if len(matriz_personajes) == 0:
            print("Error: Primero debe crear la matriz de personajes.")
            input("Presione Enter para continuar...")
        
        elif opcion == 2:
            if 'matriz_personajes' in locals():
                agregar_personaje(matriz_personajes)
            else:
                print("Error: Primero debe crear la matriz de personajes.")
                
        elif opcion == 3:
            print(matriz_personajes)
            print("Opción 3 seleccionada.")
        elif opcion == 4:
            mostrar_personajes(matriz_personajes)
        elif opcion == 5:
            mostrar_quince_caracteres(matriz_personajes)
            
        elif opcion == 22:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        input("Presione Enter para continuar...")    
        limpiar_pantalla()
        

main()