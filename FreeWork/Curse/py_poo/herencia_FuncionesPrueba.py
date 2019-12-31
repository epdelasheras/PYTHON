#Herencia funciones integradas

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

objeto  = Op_basicas()
print(isinstance(objeto,Op_basicas)) #verifica la herencia, devolvera True
print(isinstance(objeto,Raiz)) #verifica la herencia, devolvera False.

#verifica y revisa la herencia de clase
print(issubclass(Calculadora,Op_basicas))#Devuelve False porque hay que tener en cuenta el nombre subclase
print(issubclass(Op_basicas, Calculadora)) #Devuelve True porque primero se poner la subclase y luego la clase.
print(issubclass(Raiz,Calculadora))
#print((issubclass(Potencia,Calculadora))) # Da un error porque no existe la subclase potencia.