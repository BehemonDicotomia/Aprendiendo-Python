# Funciones en Python

#Ejercicio 1 crear una funcion 

def personalized_greeting(name = 'Desconocido'):
    print(f'Hola {name}')

personalized_greeting('Carlos')
personalized_greeting() # Imprime 'Hola Desconocido'

#Ejercicio 2  crear una funcion multiply 

def multiply(a, b):
    return a * b

result = multiply(5, 20)
print(f'El resultado de la multiplicacion es: {result}')

#Ejercicio 3  crear una funcion is_even 

def is_even(number):
    if number % 2 == 0:
       return f'{number} es par {True}'
    else: 
       return f'{number} es impar {False}'

print(is_even(6))

# Ejercicio 4  crear una funcion convert_to_uppercase

texto = input('Ingrese un texto: ')
def convert_to_uppercase(texto):
    return texto.upper()
print(convert_to_uppercase(texto))

#Ejercicio 5 crear una funcion arbitrary_sum 


def arbitrary_sum(*args):
    for i in args:
        return sum(args)

print(arbitrary_sum(1, 2, 35, 676, 7))


#Ejercicio 6 crear una funcion generate_full_greeting

def generate_full_greeting(name, surname):
    return f'Hola {name} {surname}'

print(generate_full_greeting('Carlos', 'Gonzales'))


# Ejercicio 7 crear una funcion power y elevar un numero **2

number1 = int(input('Ingrese un numero: '))
number2 = int(input('Ingrese otro numero: '))

def power(number1, number2):
    return number1 ** number2

print(f' EL numero {number1}, elevado a {number2} da como resultado:  {power(number1, number2)}')

#Ejercicio 8 crear una funcion llamada calculate_averange

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese un numero: '))
num3 = int(input('Ingrese un numero: '))

def calculate_average(*numbers):
    return sum(numbers) / len(numbers)

print(calculate_average(num1, num2, num3))

#Ejercicio 9 crear una funcion llamada count_caraceters

string  = input('Ingrese un texto: ')
def count_characters(string):
    return len(string)
print(count_characters(string))


#Ejercicio 10 crear una funcion llamda  display_message

def display_message(*cadena):
    for i in cadena: 
        print(i.upper())
    

display_message('Hola', 'mundo', 'python')