'''
Ejemplo serie fibonacci

1+1=2
1+2=3
2+3=5
3+5=8
5+8=13
8+13=21

'''

n=int(input('Introduce numero de iteracione: '))
w1=1
w2=1
i=0

while i<n:
    s=w1+w2
    i+=1
    w2=w1
    w1=s
    print(f'{s}')


