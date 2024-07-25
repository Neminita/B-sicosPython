
# Condición para mantener si pasa un evento o si no #

nombre = str(input("Ingrese su nombre: "))
print(f"Bienvenido/a {nombre}!")

print("--------------------------------------")
print("**Comparativa de números**")

A = int(input("Ingrese un número: "))

B = int(input("Ingrese el segundo número: "))

if A < B:
    print(f"{A} se mantiene menor al número {B}")
else:
    print(f"{A} es mayor que {B}")

print("--------------------------------------")

print("**Calculador de mayoría de edad**")
edad = int(input("Ingrese su edad: "))

diferencia1 = 18 - edad
diferencia2 = edad - 18

if edad < 18:
    print(f"Para ser mayor de edad te quedan: {diferencia1} año/s!")
elif edad == 18:
    print("Recién éste año cumpliste 18!")
else:
    print(f"Hace {diferencia2} años que eres mayor de edad!")
