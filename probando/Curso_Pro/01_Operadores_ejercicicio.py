# Operadores Ejercicios de python 

suma = 15 + 25 
resta = 50 - 22
MUltiplicacion = 8 * 7
Division = 100 / 20

print(f'''
El resultado de la suma es: {suma}
EL resultado de la resta es: {resta}
El resultado de la multiplicación es: {MUltiplicacion}
El resultado de la división es: {Division:.0f}
''')

#Ejercicio 2 

# Resto de un numero 
remainder = 37 % 5
print(f'El resto de 37 / 5 es: {remainder}')


numero = 7
print( str(7) + ' Es mi numero favorito') 

'''palabra = 'Python' * 10

print(palabra)'''

a, b  = 12, 8 

resultado = a > b
print(resultado)

c, d = 'apples', 'banana'
print(c > d)
# entre c y d quien tiene mayor mayor alfabetico, en este caso es apples por comenzar con a

print(10 > 5 and 10 < 20)

print(7 < 3 or 7 > 5)

print(not(5 > 20))

print((5 * 3) + 2 > 10 and (5 * 3) + 2  < 20)