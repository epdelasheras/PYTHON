#Herencia: consiste en crear una nueva clase a partir de otra clase.

class Pokemon:
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    def descripcion(self):
        return "{} es un pokemon de tipo: {}".format(self.nombre,self.tipo)

class Pikachu(Pokemon): #Clase hijo de la calse Pokemon
    def ataque(self,tipoataque):
        return "{} tipo de ataque: {}".format(self.nombre, tipoataque)

class Charmander(Pokemon): #Clase hijo de la calse Pokemon
    def ataque(self,tipoataque):
        return "{} tipo de ataque: {}".format(self.nombre, tipoataque)

nuevo_pokemon = Pikachu("Bobi", "electrico")
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque("impacto trueno"))