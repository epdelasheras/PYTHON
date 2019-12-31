'''
Un polimorfismo es cuando un clase superior define diferentes comportamientos. Es la capacidad
que tienes los objetos en diferentes clases para usar un comportamiento o atributo del mismo
nombre pero con diferente valor.

class Auto:
    rueda = 4 #objeto
    def desplazamiento(self): #metodo
        print('El auto se esta desplazando sobre 4 ruedas')

class Muto:
    rueda = 2
    def desplazamiento(self):
        print('La moto se esta desplazando sobre 2 ruedas')
'''

class Animales: #Clase
    def __init__(self,nombre): #Constructor
        self.nombre = nombre #Atributo
    def tipo_animal(self): #Metodo
        pass

class Leon(Animales):
    def tipo_animal(self):
        print('animal salvaje')


class Perro(Animales):
    def tipo_animal(self):
        print('animal domestico')

nuevo_animal1=Leon('SIMBA')
nuevo_animal1.tipo_animal()

nuevo_animal2=Perro('PLUTO')
nuevo_animal2.tipo_animal()

