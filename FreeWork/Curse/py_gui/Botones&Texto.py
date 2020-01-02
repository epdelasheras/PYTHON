from tkinter import *

root=Tk()

miFrame=Frame(root,width=1200,height=600)
miFrame.pack()

miNombre=StringVar()

EntryNombre=Entry(miFrame, textvariable=miNombre)
EntryNombre.grid(row=0,column=1)
Label(miFrame, text="Mi nombre: ").grid(row=0,column=0,padx=10, pady=10)

LabelText=Label(miFrame,text="Comentario: ")
LabelText.grid(row=1,column=0,padx=10,pady=10)

TextComentario=Text(miFrame,width=30,height=10)
TextComentario.grid(row=1,column=1)

'''Scrollbar metodo
view => Se le indica que es un scroll vertical.
sticky ="nsew" => adaptamos el tamaño del scroll al tamaño de la ventana de texto.
yscrollcommand=scrollVert.set => la barra de progreso del scroll se queda apuntando a la linea de texto que se esta editando.
'''

ScrollVert=Scrollbar(miFrame,command=TextComentario.yview)
ScrollVert.grid(row=0,column=2,sticky="nsew")
TextComentario.config(yscrollcommand=ScrollVert.set) #ojo porque esto se configura en la ventana de texto!!!

def CodigoBoton(texto):
    miNombre.set(texto)

BotonEnvio=Button(root,text="Enviar",command=lambda:CodigoBoton("Juan")) #lamda se usa para solo ejecutar la funcion cuando se pulse el boton
BotonEnvio.pack()

root.mainloop()