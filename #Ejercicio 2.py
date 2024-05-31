#Ejercicio 2

usuarios = {}

def menu():
    print("Bienvenido al sistema de registro de usuarios.")
    print("1. Iniciar sesión")
    print("2. Registrar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")

def iniciar_sesion():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Inicio de sesión exitoso.")
    else:
        print("Error: Nombre de usuario o contraseña incorrectos.")

def registrar_usuario():
    usuario = input("Ingrese un nombre de usuario: ")
    contraseña = input("Ingrese una contraseña: ")
    usuarios[usuario] = contraseña
    print("Usuario registrado exitosamente.")

def eliminar_usuario():
    usuario = input("Ingrese el nombre de usuario que desea eliminar: ")
    if usuario in usuarios:
        contraseña = input("Confirme la contraseña para eliminar este usuario: ")
        if usuarios[usuario] == contraseña:
            del usuarios[usuario]
            print("Usuario eliminado exitosamente.")
        else:
            print("Error: La contraseña no coincide.")
    else:
        print("Error: El usuario especificado no existe.")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        iniciar_sesion()
    elif opcion == "2":
        registrar_usuario()
    elif opcion == "3":
        eliminar_usuario()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")