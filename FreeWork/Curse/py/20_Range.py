# range (a,b,c) => Crea una lista que empieza en a, termina antes de b y se incrementa en c.
# si no pongo nada en c, por defecto se incrementa en 1

n=int(input('Numero para hacer la tabla de multiplicar: '))

for i in range(1,11):
    print(n, 'x' ,i, '=',n*i, )

valores=int(input('¿Cuantos valores va a introducir? \n'))
primero=int(input('Esciba el primer numero: '))


for i in range(valores-1): #Contador descendente
    numero = int(input(f'Escriba un numero mas grande que el {primero}: '))
    if numero > primero:
        print(f'El {numero} es mas grande que el {primero}')
        primero = numero
    else:
        print(f'Error el {numero} no es mas grande que el {primero}')
        break



