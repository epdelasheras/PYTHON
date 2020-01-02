#sticky se usa para alinear de acuerdo a los puntos cardinales Este(derecha), Oesto(Izquierda)
#padx & pady se usan para espaciar elementos en pixeles

from tkinter import *

root=Tk()

miFrame=Frame(root,width=1200,height=600)
miFrame.pack()

LabelNombre=Label(miFrame,text="Nombre: ")
#nombreLabel.place(x=100,y=100)
LabelNombre.grid(row=0,column=0,sticky='e',padx=10,pady=10)
LabelApellido=Label(miFrame,text="Apellido: ").grid(row=1,column=0,sticky='e',padx=10,pady=10)
LabelDir=Label(miFrame,text="Direccion de Casa: ").grid(row=2,column=0,sticky='e',padx=10,pady=10)


EntryNombre=Entry(miFrame)
#cuadrotexto.place(x=100,y=100)
EntryNombre.grid(row=0,column=1,padx=10,pady=10)
EntryNombre.config(fg="red",justify="center") #texto escrito en rojo y alineado al centro.
EntryApellido=Entry(miFrame).grid(row=1,column=1,padx=10,pady=10)
EntryDir=Entry(miFrame)
EntryDir.grid(row=2,column=1,padx=10,pady=10)
EntryDir.config(show="*") #Para ocultar los caracteres por ejemplo una contraseña.



root.mainloop()