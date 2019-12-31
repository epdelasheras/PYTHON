#herencia ejemplo practico.

class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    # Creo el siguiente atributo
    def ingresardato(self): #Creo este metodo
         self.datos = [int(input("Ingresar datos "+str(i+1)+" = ")) for i in range(self.n)]

class Op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2) #solo se pueden introducir dos valores.

    def suma(self):
        a,b = self.datos
        s = a + b
        print("El resultado es: ",s)

    def resta(self):
        a,b = self.datos
        r = a - b
        print("El resultado es: ",r)

class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)

    def cuadrada(self):
        import math
        a, = self.datos
        print("El resulado es: ",math.sqrt(a))


ejemplo = Op_basicas() #Creo el objeto
print(ejemplo.ingresardato())
print(ejemplo.suma())

ejemplo2 = Raiz()
print(ejemplo2.ingresardato())
print(ejemplo2.cuadrada())
