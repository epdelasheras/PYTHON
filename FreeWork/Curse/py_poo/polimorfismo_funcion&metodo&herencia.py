#Polimorfismo por función.

class Tomate:
    def tipo(self):
        print('Vegetal')
    def color(self):
        print('Rojo')

class Manzana:
    def tipo(self):
        print('Fruta')
    def color(self):
        print('Verde')

def funcion(objeto):
    objeto.tipo()
    objeto.color()

nuevo_tomate = Tomate()
funcion(nuevo_tomate) #Con la nueva version de python no hace falta poner print

nueva_manzana = Manzana()
funcion(nueva_manzana)

#Polimorfismo con metodos: funciona bien cuando tenemos varias clases

class Colombia:
    def capital(self):
        print('Bogota')
    def idioma(self):
        print('Español')

class Francia:
    def capital(self):
        print('Paris')
    def idioma(self):
        print('Frances')

colombiano = Colombia()
frances = Francia()

#el polimorfismo por metodo tiene sentido usarlo con mas de un objeto. Si solo hay un objeto no tiene sentido
for pais in (colombiano,frances):
    pais.capital()
    pais.idioma()

#Polimorfismo con herencia

class Aves:
    def volar(self):
        print('La mayoria de las aves pueden volar pero algunas no')

class Aguila(Aves):
    def volar(self):
        print('Las aguilas pueden volar')

class Gallina(Aves):
    def volar(self):
        print('Las gallinas no pueden volar')

obj_ave = Aves()
obj_aguila = Aguila()
obj_gallina = Gallina()
obj_ave.volar()
obj_aguila.volar()
obj_gallina.volar()



