
# Operadores simples y entre variables#

# Suma #

print(24+30)

A = 56

B = 30

print(A + B)

# Resta #

print(30-21)

C = 50

D = 30

print(C - D)

# Multiplicación #

print(6 * 8)

E = 5

F = 10

print(E * F)

#  División #

print(6 / 3)

G = 10

H = 5

print(H / G)

# Módulo, es decir lo que sobra de una división #

print(4 % 71)

I = 7

J = 54

print(I % J)

# Conjunto #

print((A + H)* G - (I % B))

# Números ingresados por el usuario #

numero = int(input('Ingrese número: '))
numero2 = int(input('Ingrese otro número: '))

print(f"La suma entre los números {numero} y {numero2} es:",numero+numero2)
print(f"La resta entre los números {numero} y {numero2} es:",numero-numero2)
print(f"La multiplicación entre los números {numero} y {numero2} es:",numero*numero2)
print(f"La división entre los números {numero} y {numero2} es:",numero/numero2)
print(f"El módulo entre los números {numero} y {numero2} es:",numero%numero2)