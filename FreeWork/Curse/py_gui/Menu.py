from tkinter import *

root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

#Creo elementos del menu
archivoMenu=Menu(barraMenu, tearoff=0) #tearoff = 0 quita el separador por defecto.
archivoEdicion=Menu(barraMenu)
archivoHerramientas=Menu(barraMenu)
archivoAyuda=Menu(barraMenu)

#Tenemos que especifar el texto que va a salir en el menu por cada uno de los elementos
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

#Añdimos elementos de submenu para archivoMenu
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator() #Añadimos separador.
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")


root.mainloop()