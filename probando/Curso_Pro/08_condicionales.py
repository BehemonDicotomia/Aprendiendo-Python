#Condicionales 

#Ejercicio 1 

numero = int(input('Ingresa un numero: '))
if numero > 0:
    print('El numero es positivo')
else:
    print('El numero es negativo')

#Ejercicio 2 Ejercicio de mayor o menor de edad
edad = int(input('Ingresa tu edad: '))
if edad >= 18:
    print('Eres mayor de edad')
else: 
    print('Eres menor de edad') 


#Ejercicio 3 vericar si la cadena esta vacia y muestre un mensaje en consecuencia.

cadena = input('Ingresa una cadena: ')

if cadena == '':
    print('La cadena esta vacia')
else: 
    print('La cadena no esta vacia')

#Ejercicio 4  solicitar dos numeros y mostrar cual es mayor o menor
num1 = int(input('Ingresa el primer numero: '))
num2 = int(input('Ingresa el segundo numero: '))

if num1 > num2:
    print(f'El numero mayor es: {num1}')
elif num1 < num2:
    print(f'El numero mayor es: {num2}')
else: 
    print('Los numeros son iguales')

#Ejercicio 5 verificar si un numero es divisible entre 3 y por 5 al mismo tiempo
num = int(input('Ingresa un numero: '))

if num % 3 == 0 and num % 5 == 0:
    print(f'El numero {num} es divisible entre 3 y 5')
else: 
    print(f'El numero {num} no es divisible entre 3 y 5')


#Ejercicio 6 solicitar un numero y verificar si es par o impar 
numero = int(input('Ingresa un numero: '))
             
if numero % 2 == 0:
    print('El numero es par')
else:
    print('El numero es impar')

#Ejercicio 7 determinar si una persona puede votar o no 

edad = int(input('Ingresa tu edad: '))

if edad >= 18:
    print('Puedes votar')
if edad == 16 or edad == 17:
    print('Puedes votar con permiso especial')
else: 
    print('Se desconoce la edad de la persona')

#Ejercicio 8 verificar si la contraseña es correcta 

password = input('Ingresa la contraseña: ')

if password == '123Word':
    print('La contraseña es correcta')
else: 
    print('La contraseña es incorrecta')

#Ejercicio 9 determinar si un numero esta dentro de un rango 

numero = int(input('Ingresa un numero: '))

if  10 <= numero <= 20:
    print('El numero esta dentro del rango')
else: 
    print('El numero no esta dentro del rango')

#Ejercicio 10  simulacion de un semaforo 

print('-----Simulacion de un semaforo-----')
print('')

color = input('Ingresa el color del semaforo (Rojo/Amarillo/Verde): ')

if color.lower() == 'rojo':
    print('Deternerse')
elif color.lower() == 'amarillo':
    print('Precaucion')
elif color.lower() == 'Verde':
    print('Avanzar')
else: 
    print('Color desconocido')
