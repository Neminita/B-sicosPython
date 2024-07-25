# Ciclo que mantiene una cantidad de repeticiones para una condición o valor#

A = "Mensaje de ejemplo"

# Contador i #

for i in range(20):
    i += 1
    print(f"({i}) {A}")

print("------------------------------")

print("***Tablas de Multiplicar!***")
B = int(input("Ingrese un número: "))


print(f"--Tabla del {B}--")

for i in range(10):
    i += 1
    resultado = B * i
    print(f"{B} x {i} = {resultado}")
