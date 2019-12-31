#clases y objetos 2

'''
class Persona:
    doctor = 'victor'

print(Persona.doctor)

class Jugadores_A:
    j1 = "Messi"
    j2 = "CR7"

print(Jugadores_A.j2)

class Jugadores_B:
    j3 = 'Marcelo'
    j1 = 'falcao'

print(Jugadores_B.j1)

'''

class Nombre:
    pass #creo la clase pero sin atributos

#Creo objetos
victor = Nombre()
maria = Nombre()

#Creo atributos para los objetos anteiores => objeto.atributo = valor
victor.edad = 30
victor.sexo = 'masculino'
victor.pais = 'bolivia'

maria.edad = 25 #ojo se puedes crear diferente atributos a los de victor si uno desea.
maria.sexo = 'femenino'
maria.pais = 'colombia'

print(victor.edad)
print(maria.edad)