#set tambien conocidos como conjuntos

#vamos a podemos almacenar info dentro de conjuntos pero si seguir un orden coherente
a = 'python'
print(set(a))

a = [3,4,5,3,6]
print(set(a)) #conversion de listas a conjuntos. Ojo el elemento repetido se pierde! En este caso el 3
a = (3,4,5,3,6)
print(set(a)) #conversion de tuplas a conjuntos. Ojo el elemento repetido se pierde! En este caso el 3

alumno = set()
alumno = ('pepe', 'victor', 'hector')
print(alumno)
#podemos verificar info dentro del conjunto devolviendo true or false
print('victor' in alumno)

set = {2,3,4}
print(set)
set.add(5) #añadimos al final del conjunto el valor mostrado siguiendo una secuencia
print(set)
set.add(7)
print(set)
set.add(10)
set.add(1)
set.add(6)
set.add('a')
set.add('z')#ojo! al tener mezclados numeros con letras, podemos tener el conjunto desordenado
set.add('b')
print(set)