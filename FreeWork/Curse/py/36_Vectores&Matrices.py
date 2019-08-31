
'''
tenemos que instalar una libreria o modulo que nos permita manejar mejor los vectores.
Ese modulo se llama numpy y para instalarlo hay que seguir los siguientes pasos:
1) File => Settings
2) Project Interpreter => clik en + y se abre una ventana donde podremos seleccionar el modulo.
'''

import numpy as np

vector = np.array([6,5,6,5,6]) #todos los elementos del vector han de ser del mismo tipo
print(vector)
vector = np.array([6,5,6.5,5,6]) #cuando uno de los elementos del vector es diferente, el resto se convierten a ese tipo diferente
print(vector)
vector = np.array([6,5,6,5,6])
print(vector.astype(str))  #convrierte el tipo de dato de un vector

# operaciones con vectores
a = np.array([6,5,6,5])
b = np.array([8,7,6,3])
print(a+b)
print(a-b)
print(a*b)
print(a<b)


vector = np.array([6,5,7,8,9])
print(vector[3]) #obtien un elemento de un vector
print(vector.max()) #devuelve el mayor elemento de un array
print(vector.argmax()) #devuelve el max valor del vector
print(vector.argmin()) #devuelve el min valor del vector
print(vector.sum()) #suma todos los elementos del vector
print(vector.prod()) #multiplica todos los elemetos del vector

matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("vector : ",vector)
print("matriz: \n",matriz)
matriz_a = np.array([[1,2,3],[4,5,6],[7,8,9]])
matriz_b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\n",matriz_a+matriz_b)
print(vector.size)
print(matriz.size)

