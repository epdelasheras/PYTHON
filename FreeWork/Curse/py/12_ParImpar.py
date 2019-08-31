# Identificar pares e impares

n1=int(input("Por favor introduzca un numero: "))
n2=int(input(f"Por favor introduzca un numero mayor que {n1:} "))

if n2 < n1:
        print(f"Tiene que introducir un 2º num mayor que {n1:}!!")
else:
    for i in range(n1, n2+1):
        if i % 2 == 0:
            print(f'El numero {i} introducido es par')
        else:
            print(f'El numero {i} introducido es impar')
