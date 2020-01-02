from tkinter import *

root=Tk()

miframe=Frame(root,width=500,height=400)
miframe.pack()

milabel=Label(miframe,text="Hola mundo", fg="red", font=("Comic Sans MS",18)) #tamaño 18 de color rojo
milabel.place(x=100,y=200) #100 pixeles desde el borde izq de la pantalla hasta el texto. 200 pixeles desde la parte superior hasta el texto.

miImagen=PhotoImage(file="mouse.png")
Label(miframe, image=miImagen).place(x=20,y=10)

root.mainloop()