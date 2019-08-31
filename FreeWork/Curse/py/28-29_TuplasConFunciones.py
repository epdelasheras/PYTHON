a = (4,5)
b = (5,6)
(a,b) = (b,a) #intercambiamos valores entre tuplas
print(a[1]) #imprimo el valor de la pos1 de la tupla a

print(a)

a = (4,6,9,6,19)
lista = list (a) #convertir tupla a lista
print(lista)

a = [4,6,9,6,19] #convertir lista a tupla
tupla = tuple(a)
print(tupla)

a = (4,6,9,6,19)
print(len(a)) #calcula la longitud de una tupla
print(max(a)) #devuelve el valor max de una tupla
print(min(a)) #devuelve el valor min de una tupla