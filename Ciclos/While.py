# Ciclo de mientras esté esta condición, ejecuta lo que se le ingrese #
login = False

print("***Creación de usuarios***")

usuario = str(input("Ingrese su nombre de usuario: "))

contrasenna = int(input("Ingrese contraseña en números: "))
print("------------------------------")

while login == False:

    print("***Inicio de sesión***")

    A = str(input("Ingrese usuario creado: "))
    B = int(input("Ingrese contraseña creada: "))

    if A == usuario and B == contrasenna:
        login = True
    else:
        print("El usuario o la contraseña son erróneas..")
        login = False
        break  

    while login == True:
        print("Bienvenido a su sesión!")
        print("--------------------------")
        print("1. Actualizar contraseña")
        print("2. Actualizar usuario")
        print("3. Salir")
        op = int(input("¿Qué desea hacer hoy? :"))
        if op == 1:
            contrasenna = int(input("Ingrese contraseña nueva numérica: "))
        elif op == 2:
            usuario = str(input("Ingrese usuario nuevo: "))
        else:
            print("Ha cerrado la sesión exitosamente, vuelva pronto!")
            break
    login = False
