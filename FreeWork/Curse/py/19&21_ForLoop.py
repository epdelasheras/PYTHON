# Estructura for en python => calcular el numero de vocales de una frase.

frase = str(input('Por favor introduzca una frase:'))
cnt=0

for i in frase:
    if i == 'a' or i=='e' or i=='i' or i=='o' or i=='u':
        cnt+=1
    elif i == 'A' or i=='E' or i=='I' or i=='O' or i=='U':
        cnt += 1

print('El numero de vocales que tiene la frase es: ',cnt)

