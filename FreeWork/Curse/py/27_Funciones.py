#Tabla de multiplicar
def tab_mul(n):
    for i in range(1,10+1):
        print(n," x ",i, "= ",i*n)

n=int(input("Introduce numero: "))
tab_mul(n)

#Retorno de una funcion
def cadena():
    return ("curso de python")

print(cadena())


