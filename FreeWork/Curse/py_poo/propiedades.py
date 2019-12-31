#Propiedades()
class Empleado:
    def __init__(self,nombre,salario):
        self.__nombre = nombre
        self.__salario = salario


    def __getnombre(self): #encapsulo el metodo poniendo __
        return self.__nombre
    def __getsalario(self):
        return self.__salario

    def __setnombre(self,nombre):
        self.__nombre = nombre
    def __setsalario(self,salario):
        self.__salario = salario

    def __delnombre(self):
        del self.__nombre
    def __delsalario(self):
        del self.__salario

    #creo propiedades dentro de la clase
    nombre = property(fget=__getnombre,
                      fset=__setnombre,
                      fdel=__delnombre,
                      doc="soy la propiedad del 'nombre'")

    salario = property(fget=__getsalario)

empleado1 = Empleado("Victor",2000)
empleado1.nombre = "Sara"
print(empleado1.nombre,empleado1.salario)
help(empleado1)