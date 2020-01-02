
from tkinter import *

root=Tk()


def CodigoBoton(texto):
    Label(root, text=texto).pack()

Button(root,text="Enviar",command=lambda:CodigoBoton("Juan")).pack() #lamda se usa para solo ejecutar la funcion cuando se pulse el boton

root.mainloop()