'''
- clase: es una plantilla para crear objetos
- instancia: Un objeto se crea usando el constructor de una clase (__init__).
  una vez que el objeto es creado, se le conoce com una instancia de la clase.

Existen tres tipo de metodos:
 1) Estaticos
 2) clase
 3) Instancia.

*Metodos de clase: @claasmethod. No es necesario usar el __init__ para crearlo.
 No tiene acceso a atributos de instancia.
'''

#Clase y estatico

class Pastel:
    def __init__(self, ingredientes):
        self.ingredientes  = ingredientes

    def __repr__(self):
        return f"pastel({self.ingredientes !r})"

    @classmethod
    def Pastel_chocolate(cls):
        return cls(["harina","leche","chocolate"])

    @classmethod
    def Pastel_vainilla(cls):
        return cls(["harina", "leche", "vainilla"])

print(Pastel.Pastel_chocolate())

#metodo estatico; pueden ser llamados sin tener una instancia de la clase. No me interesa lo exterior.
import  math
class Pastel:
    def __init__(self,ingredientes,tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño

    def __repr__(self):
        return (f"Pastel({self.ingredientes}, "f"{self.tamaño}")

    def area(self):
        return self.tamaño_area(self.tamaño)

    @staticmethod
    def tamaño_area(A):
        return A ** 2*math.pi

nuevo_pastel = Pastel(["harina","azucar","..."],4)
print(nuevo_pastel.ingredientes)
print(nuevo_pastel.tamaño)


