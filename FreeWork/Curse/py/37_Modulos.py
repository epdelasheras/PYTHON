# los modulos son el equivalente a las librerias en C

# importo modulo de constantes y funciones matematicas.
from math import pi
a = pi
print(a)

from math import factorial
a = factorial(6)
print(a)

from math import log
a = log(8,10)
print(a)

from random import choice
a = choice(['cara', 'cruz'])
print(a)

from random import randrange
a = randrange(5) #obtenemos numeros aleatorioas de 0 a 5
print(a)

from datetime import date
dia = date(2019,6,30)
print(dia)
año = date(2019,12,31)
fin_de_año = (año-dia).days
print('faltan:',fin_de_año,'dias')

from fractions import Fraction
a = Fraction(2,4)
b = Fraction(4,8)
print(Fraction(a+b))

#importo modulo creado

from modulo_pares import pares
a = pares(8)
print(a)


