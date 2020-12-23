# -*- coding: utf-8 -*-


nombre = input("Ingrese su nombre: ")

if nombre == 'maxi':
    print("Imprimo esto porque la evaluacion fue verdadera")
elif nombre == "nombre":
    print("Ah sos chistoso?")
    
numero = input("Ingrese un numero entre el 1 y el 100: ")
numero = int(numero) 

"""Recordar siempre castear los numeros que ingresan por pantalla"""

numero2 = 0

while numero2 != numero:
    numero2 += 1
    print("Iteracion numero ", numero2)

nombre = input("Ingrese su nombre: ")

while nombre != "maxi":
    print("El nombre no es valido, porfavor intentelo nuevamente.")
    nombre = input("Ingrese su nombre: ")
    
valor = input("Ingrese un valor numerico: ")
valor = int (valor)

while valor <= 10:
    if valor == 8:
        print("Valor encontrado")
        break
    else:
        print("El valor es: ", valor)
        valor += 1
        

lista = [1, 2, 3, 4, 5, 6, 7, 8 ,9]
indice = 0
    
for indice, recorrer in enumerate(lista):
    lista[indice] *= 5
    
for recorrer in lista:
    print(recorrer)

String = ["Maximiliano"]

for caracteres in String:
    print(caracteres)
    
for i in range(10):
    print(i)
    
for i in [1, 2, 3, 4, 5]:
    print(i)