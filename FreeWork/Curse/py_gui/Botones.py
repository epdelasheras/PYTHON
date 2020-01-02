
from tkinter import *

root=Tk()


def CodigoBoton(texto):
    Label(root, text=texto).pack()

BotonEnvio=Button(root,text="Enviar",command=lambda:CodigoBoton("Juan")) #lamda se usa para solo ejecutar la funcion cuando se pulse el boton
BotonEnvio.pack()



root.mainloop()