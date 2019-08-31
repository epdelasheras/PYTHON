#usando diccionarios y funciones.

notas = {"victor":7, "chema":8, "crespo":3}
print(notas.clear()) #borra el diccionario
notas = {"victor":7, "chema":8, "crespo":3}
notas_2 = notas.copy() #copia el diccionario en otra variable
print(notas_2)

#crea un nuevo diccionario basado en las claves de la lista con un mismo valor
notas = dict.fromkeys(["victor", "chema", "crespo"],100)
print(notas)

#regresa el valor de la clave
notas = {"victor":7, "chema":8, "crespo":3}
valor = notas.get("victor")
print(valor)

#devuelve una lista de pares basado en claves y valor
items = notas.items()
print(items)

#devuelve una lista con las claves
keys = notas.keys()
print(keys)

#añade los pares claves dentro de un valor de dic1 al dic2
dic1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
dic2 = {'e':6, 'g':7, 'h':8, 'i':9, 'j':10}
dic1.update(dic2)
print(dic1) #ojo la clave 'e' aparece reemplazada con el valor del dic2

#devuelve una lista con valores
value = dic1.values()
print(value)

#elimina una clave+valor especifica del dic
dic1.pop('b') #le pasamos como parametro la clave
print(dic1)


