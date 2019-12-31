#f-string
# format %

'''
curso = "python"
print("tutoriales de %s"%curso)

nombre = "Victor"
edad = 25

print("hola soy %s y tengo %s años."%(nombre,edad))

#str.format
print("que tal soy {} y tengo {} años".format(nombre,edad))

#f-string
print(f"hola soy {nombre} y tengo {edad} años")
'''

class Estudiante:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self): #usar este metodo cuando queramos visualizar algo directamente. Todos los datos son considerados string aunque se hayan declarado atributos tipo int.
        return f"El estudiante {self.nombre} {self.apellido} tiene {self.edad} años"

nuevo_estudiante = Estudiante("Enrique","Perez",25)
print(f"{nuevo_estudiante}")

class Estudiante:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __repr__(self): #equivalente al metodo __str__ pero con este metodo se conservan los tipos de datos si son int o string o float
        return f"El estudiante {self.nombre} {self.apellido} tiene {self.edad} años"

otro_estudiante = Estudiante("Enrique","Perez",25)
print(f"{otro_estudiante !r}")
