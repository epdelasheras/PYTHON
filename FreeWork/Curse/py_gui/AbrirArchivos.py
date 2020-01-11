from tkinter import *
from tkinter import filedialog

root=Tk()

def abreFichero():
    # Devuelve la ruta del archivo que queremos abrir.
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="./", filetypes=(("Ficheros de Excel","*.xlsx"),
                                                                ("Imagenes","*.png"),("Todos los ficheros","*.*")))

    print(fichero)

Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()