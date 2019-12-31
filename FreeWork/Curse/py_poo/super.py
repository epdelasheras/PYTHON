#La funcion o metodo super() se utiliza para llamar a metodos definidos.

class Mamifero:
    def __init__(self,nombre):
        print(nombre,'Es un animal de sangre caliente')

class Leon(Mamifero):
    def __init__(self):
        print('El leon es un animal de 4 patas')
        super().__init__('Simba') #LLamo a un metodo padre o superior desde un metodo hijo.
        #Mamifero.__init__(self,'Simba')

nuevo_leon = Leon()