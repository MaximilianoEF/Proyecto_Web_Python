# -*- coding: utf-8 -*-

numero = 10

variable = 5

print(numero+variable)

print(type(numero))

nombre = "maxi"

apellido = 'franco'

print(nombre+ " "+apellido)

numero = "Maxi"

nombre = 10

print(nombre+variable)

print(numero+" "+apellido)

print("hola \nMundo!!")

print("C:\nombres\variables")

print(r"C:\nombres\variables")

print("""De esta manera
nos ahorramos a nun
pero no a \tuna que es para tabular""")

print(numero[0])

print(numero[1])

print(numero[2])

print(numero[3])

variable = "Alvaro"

print(variable[2:5])

print(variable[:5])

print(variable[2:])

print(len(variable))

lista = [numero, variable, nombre, apellido, -8]

print(lista[0])

print(lista[1])

print(lista[2])

print(lista[3])

print(lista[4])

print(lista[0]+" "+lista[3])

lista[4] = 10

print(lista[4])

lista.append("casa")

print(lista[5])

lista.append(lista[5]+" de "+lista[0])

print(lista[6])

par = [0, 2, 4, 6, 8, 10]

inpar = [1, 3, 5, 7, 9]

anidadas = [lista, par, inpar]

print(anidadas[:])

print(len(lista))

lista.insert(1, "Soquete")

print(lista[:])

anidadas.extend(lista)

print(anidadas[:])

numeros = [0, 4, 7, 1, 9, 5, 8]

numeros.sort()

print(numeros)

numeros.reverse()

print(numeros)

print(lista.index("Maxi"))

numeros.pop(2)

print(numeros)

del numeros[0]

print(numeros)

entrada = input()

entrada = int(entrada)

entrada += 3

print(entrada)

nombre = input("Ingrese su nombre: ")

print("Tu nombre es "+nombre)

2 + 2 == 4

"Operadores Logicos"

not True

True and True

False or True

1 != 2

2 > 1

2 < 3

2 >= 2

3 <= 3

"Expresiones anidadas"


primero = 8

segundo = 10

primero * segundo - 4**primero or not (primero % segundo) == 0 
"El ** es elevado"

primero * segundo - 4**primero >= 8 or not (primero % segundo) == 0 

valor = 10

valor += 10

valor -= 10

