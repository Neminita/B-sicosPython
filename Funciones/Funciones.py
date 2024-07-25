
# Funciones que permiten mantener código limpio y resumido, almacenando dentro de sí para posteriormente ser llamadas #

# Con parámetros #

def Boleta(pago, resultado, resumen):
    if pago == True:
        print("Su pago ha sido cancelado con éxito!")
        print(f"Su total es : $ {resultado}")
        print("------------------")
        print(resumen)
    else:
        print("Porfavor cancele su compra..")


def Menu(compra, codigo, pago):
    print("Bienvenido!")
    print("1. Comprar")
    print("2. Salir")
    op = int(input("Ingresse su opción: "))
    if op == 1:
        print("1. Alfajor de caramelo : $ 500")
        print("2. Bebida CCU : $ 1.000")
        op2 = int(input("Haga su opción: "))
        if op2 == 1:
            compra  = 500
            resumen = "Alfajor de caramelo"
        else:
            compra = 1000
            resumen = "Bebida CCU"
        print(f"Su total es: {compra}")
        confirm = int(input("Porfavor ingrese el código para su facturación:"))
        if confirm == codigo:
            pago == True
            resultado = compra
            Boleta(pago, resultado, resumen)  
        else:
            pago == False
    else:
        print("Ha salido de la tienda exitósamente!")
