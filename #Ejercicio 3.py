#Ejercicio 3

biblioteca = {}

def menu():
    print("Bienvenido a la biblioteca.")
    print("1. Añadir libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Salir")

def añadir_libro():
    titulo = input("Ingrese el título del libro: ")
    biblioteca[titulo] = {"titulo": titulo}
    print("Libro añadido exitosamente.")

def buscar_libro():
    titulo = input("Ingrese el título del libro que desea buscar: ")
    if titulo in biblioteca:
        print("El libro", titulo, "está en la biblioteca.")
    else:
        print("El libro", titulo, "no está en la biblioteca.")

def eliminar_libro():
    titulo = input("Ingrese el título del libro que desea eliminar: ")
    if titulo in biblioteca:
        del biblioteca[titulo]
        print("Libro eliminado exitosamente.")
    else:
        print("El libro", titulo, "no está en la biblioteca.")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        añadir_libro()
    elif opcion == "2":
        buscar_libro()
    elif opcion == "3":
        eliminar_libro()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")