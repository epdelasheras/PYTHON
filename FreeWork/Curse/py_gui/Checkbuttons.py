from tkinter import *

root=Tk()

root.title("Ejemplo")

#Creamos variables para cada unos de los checkbuttons
playa=IntVar()
montana=IntVar()
turismorural=IntVar()

#Definimos las funciones para cada uno de los checkbuttons
def opcionesViaje():
    oppcionEscogida=""
    if(playa.get()==1):
            oppcionEscogida+=" playa"
    if(montana.get()==1):
            oppcionEscogida+=" montaña"
    if(turismorural.get()==1):
            oppcionEscogida+=" turimos rural"

    textoFinal.config(text=oppcionEscogida)

foto=PhotoImage(file="mouse.png")
Label(root, image=foto).pack()
frame=Frame(root)
frame.pack()

Label(frame, text="Eligde destinos:", width=50).pack()
Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismorural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()