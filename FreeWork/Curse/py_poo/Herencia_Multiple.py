'''
Herencia Multiple: Crear una clase a partir de multiples clases superiores.

class Base_uno:
    pass
clasee Base_dos:
    pass
class DerivadoMultiple(Base_uno, Base_dos):
    pass

Herencia Multinivel: las caracteristicas de la clase base y la clase derivada se heredan
en la nueva clase derivada.

class Base:
    pass
class Derivado-uno(Base):
    pass
class Derivado-dos(Derivado-uno):
    pass
'''

class Telefono:
    def __init__(self): #__init__ es un costructor o inicializador de clase
        pass
    def llamar(self):
        print("llamando...")
    def ocupado(self):
        print("Ocupado...")

class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print("Haciendo fotos...")

class Reproduccion:
    def __init__(self):
        pass
    def musica(self):
        print("reproduciendo musica...")
    def video(self):
        print("reproduciendo video...")

class smartphone(Telefono,Camara,Reproduccion):
    def __del__(self): #limpamos recursos una vez se han usado la clase.
        print("telefono apagado")


movil = smartphone()
#print(dir(movil)) #para saber que metodos especiales puedo usar.
print(movil.fotografia())