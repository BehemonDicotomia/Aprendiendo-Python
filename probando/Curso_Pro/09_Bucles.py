#Bucles en Python

# Ejercicio 1 usando while para imprimir los numeros del 1 al 10 

numero = 1

while numero <= 10: 
    print(numero)
    numero += 1
else: 
    print('El bucle ha terminado')


#Ejercicio 2 

lista = [10, 20, 30, 40, 50]

for elemento in lista:
    print(elemento)
else:
    print('El bucle termina')


#Ejercicio 3 usando while crear un programa que sume un numero hasta que llegue a 100

suma = 0 
numero = 1
while suma < 100:
    suma += numero
    print(f'La suma es: { suma}')

#Ejercicio 4 usando for recorrer una cadena 

cadena = 'Python'

for letra in cadena: 
    print(letra)
else:
    print('-----Fin del bucle----')

#Ejercicio 5 usando while encontrar el primer numero divisible por 7  entre 1  y 50 

numero_2 = 1 

while numero_2 <= 50:
    if numero_2 % 7 == 0:
        print(f'El primer numero divisible por 7 es: {numero_2}')
        break
    numero_2 += 1
else:
    print('No se encontro un numero divisible por 7')


#Ejercicio 6 usando for recorrer un diccionario e imprimir sus claves 

diccionario = {'name': 'Brais', 'age': 37, 'country': 'Galicia'}

for clave in diccionario.keys():
    print(clave)
else:
    print('-----Fin del bucle----')


#Ejercicio 7  crear un bucle que imprima los numeros pares del 1 al 20 

numero = 0
while numero < 20:
    numero += 2
    print(numero)
print('---Fin de este while----')

#Ejercicio 8  usar for para imprimir los numeros del 1 al 10 con range() y en orden inverso

for i in range(10, 0, -1):
    print(i) 

#Ejercicio 9  para contar cuntas veces se repite un elemento en una lista



LISTA = [30, 10, 30, 20, 30, 40]

for i in LISTA:
    if i == 30:
        print(f'El numero 30 se repite {LISTA.count(i)} veces')
else: 
    print('-----Fin del bucle----')


#Ejercicio 10 

lista = ['name', 'age', 37, 'Brais', 'country', 'Galicia']

for i in lista: 
    print(i)
    if i == 'Brais':
        print('El bucle se detiene')
        break
