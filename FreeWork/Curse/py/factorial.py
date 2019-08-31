'''
Determinar el factorial de un numero introducido. Por ejemplo:
4! = 1*2*3*4 = 24
'''

num = int(input('Ingrese un numero: '))
factorial=1
if num < 0 :
    print('Error!! el numero ha de ser positivo')
else:
    for i in range(1,num+1):
        factorial = factorial * i

print(f'el factorial de {num} es: {factorial}')

