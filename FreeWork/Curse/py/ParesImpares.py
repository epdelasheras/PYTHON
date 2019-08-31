#Sperara en pares e impares

lista=[1,2,3,4,5,6,7,8,9,10]

def separar_lista(lista):
    lista.sort()
    lista_par = []
    lista_impar = []
    for i in lista:
        if i % 2 == 0:
            lista_par.append(i)
        else:
            lista_impar.append(i)
    return lista_par,lista_impar

lista_par,lista_impar = separar_lista(lista)
print(lista_par)
print(lista_impar)


