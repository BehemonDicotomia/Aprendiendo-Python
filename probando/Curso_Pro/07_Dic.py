#Diccionarios Ejercicios 


my_dic = dict()
print(my_dic)

#Los diccionarios son estructuras de datos que almacenan pares de clave-valor.

#Ejercicio 1 crear un diccionario con su clave y valor 

dict = {'name': 'Marcos', 'age': 24, 'country': 'Mexico'}
print(dict)

#Ejercicio 2 accerder a un valor clave del diccionario 

print(dict['name'])

#Ejercicio 3 añadir una nueva clave job 

dict['job'] = 'programador'
print(dict)

#Ejercicio 4 modificar el valor de una clave

dict['age'] = 38
print(dict)

#Ejercicio 5 eliminar una clave del diccionario 

del dict['country']
print(dict)

#Ejercicio 6 crear un diccionario con claves y valores que sean cuadrados
cuadrados = {x: x**2 for x in range(1, 6)}
print(cuadrados)

#otra forma de hacerlo 

cuadrados = {1:1, 2:4, 3:9, 4:16, 5:25}
print(cuadrados)

#Ejercicio 7 verificar si la clave age existe en el diccionario 

my_dic = {'name': 'Brais', 'age': 37, 'country': 'Galicia'}

print('age' in my_dic)

#Ejercicio 8 imprimir solamente las claves del diccionario 

llaves = my_dic.keys()
print(llaves) 


#Ejercicio 9 convertir las claves de un diccionario en una lista e imprimirla 
llaves = list(my_dic.keys())
print(llaves)

#Ejercicio 10  crear un diccionario con el metodo fromkeys()

claves = ['name', 'age', 'job']
claves = dict.fromkeys(claves)
print(claves.fromkeys(claves, 'Desconocido'))