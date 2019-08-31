
# del => borra los elementos dentro de una lista

curso = 'python'
lista_nueva = list(curso)
print(lista_nueva)

del lista_nueva[0]
print(lista_nueva)

#in => verifica si un elemento esta dentro de una lista
print('y' in curso)
print('a' in curso)

if 'y' in lista_nueva:
    print('y es parte de la lista')