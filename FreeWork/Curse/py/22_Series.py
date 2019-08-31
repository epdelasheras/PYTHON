# serie 4,3,2,1,4,3,2,1...


n = int(input('Por favor ingrese un numero: '))
c = 0 # controlador de bucle

w=n
while c < n:
    print(w,end=',')
    w -= 1
    c += 1

