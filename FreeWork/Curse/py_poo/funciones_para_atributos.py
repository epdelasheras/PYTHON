#funciones para atributos

class Persona:
    edad = 27
    nombre = 'victor'
    pais = 'brasil'

doctor = Persona()

print('la edad es: ',doctor.edad)
print('la edad es: ',getattr(doctor,'edad'))
print('el doctor tiene una edad?', hasattr(doctor,'edad'))
print('el doctor tiene una edad?', hasattr(doctor,'apellido'))
print('antes era: ',doctor.nombre)
setattr(doctor,'nombre','hector')
print('ahora se llama: ',doctor.nombre)
print(doctor.pais)
delattr(Persona,'pais')