'''
vectores son conjuntos de datos del mismo tipo con el mismo tamaño.
se usan para almacenar principalmente datos numericos
'''

#ej1: imprimir hasta 'n' multiplos de 'm'
n = int(input('ingrese el tamaño del vector: '))
m = int(input('ingrese el numero de multiplos: '))
A = []
for i in range (0,n):
    A.append(i*m)

print(A)

#ej2: Imprimir num impares a 3
B = [1,4,8,9,30,9,13]
C = []
for i in B:
    if i > 3 and i % 2!=0:
        C.append(i)
print(C)

#ej3: calcular 10 numeros aletorios

import random

def vector_aleatorio(num):
    vector = [0]*num
    for j in range(num):
        vector[j] = random.randint(0,10) # genera num aleatorios entre 0 y 10
    return(vector)

num = int(input('Cuantos numeros aleatorios quieres imprimir: '))

aleatorio = vector_aleatorio(num)

print (aleatorio)





