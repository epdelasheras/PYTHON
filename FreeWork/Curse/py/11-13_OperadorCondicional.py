# Comprobar si un número entero es igual, menor o mayor que el otro ingresado


a=int(input('Por favor ingrese el primer numero a comparar: '))
b=int(input('Por favor ingrese el segundo numero a comparar: '))

if a > b:
    print('el numrero '+str(a) + ' es mayor que ' +str(b))
elif b > a:
    print('el numrero ' + str(b) + ' es mayor que ' + str(a))
else:
    print('el numrero ' + str(a) + ' y el numero ' + str(a) + ' son iguales')

print('Fin del ejercicio de la comparacaion de: ',a,b)

