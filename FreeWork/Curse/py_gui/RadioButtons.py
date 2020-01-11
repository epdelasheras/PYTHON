from tkinter import *

root=Tk()

varOpcion=IntVar()

Label(root, text="Genero:").pack()

def imprimir():
    #print(varOpcion.get()) #rescatamos el valor del radiobutton pulsado.
    if varOpcion.get()==1:
        etiqueta.config(text="Has elegido masculino")
    else:
        etiqueta.config(text="Has elegido femenino")

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()


root.mainloop()