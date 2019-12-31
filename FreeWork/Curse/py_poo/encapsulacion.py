#Encapsulacion es la oculatacion de de datos del estado interno para proteger la integridad de un objeto.

class Cliente:
    def __init__(self):
        self.__codigo = 4321 #valor encapsulado.

    def __cuenta(self):
        print('cuenta de procesamiento')

    def getcodigo(self): #necesito un nuevo metodo para desencapsular el codigo
        return self.__codigo

persona = Cliente()
#objecto._nombreclase__nombreatributo
print(persona._Cliente__codigo)
persona._Cliente__cuenta() #no es necesario poner el print.
