# metodo es una fucncion dentro de una clase. determina una accion o un comportamiento.


'''
Metodo 1:
    CLASS nombdre de la clase:
        DEF nombre del metodo (SELF):
            SELF.nombre de la variable = ALGORITMO
'''

class Matematica:
    def suma(self):
        self.n1 = 2
        self.n2 = 3

s = Matematica()
s.suma()
print(s.n1 + s.n2)

'''
Metodo 2:
    _init_
'''

class Ropa:
    def __init__(self): #con esto se evita inicializar el metodo.
        self.marca = "willow"
        self.talla = "M"
        self.color = "Rojo"

camisa = Ropa()
print(camisa.color)

#Ejercicio Practico

class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.mul = n1 * n2
        self.div = n1 / n2

operacion = Calculadora(2,3)

print(operacion.mul)
