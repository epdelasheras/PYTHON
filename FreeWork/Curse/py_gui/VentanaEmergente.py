from tkinter import *
from tkinter import messagebox

root=Tk()

def InfoAdicional():
    messagebox.showinfo("Ventana emergente de Enqique", "Hola has pulsado el boton info")

def WarningAdicional():
    messagebox.showwarning("Ventana emergente de Enqique", "Hola has pulsado el boton warning")

def AskQuestionAdicional():
    valor=messagebox.askquestion("Ventana emergente de Enqique", "Hola has pulsado el boton ask a question?")
    Label(root, text="El valor devuelto por ask a question es: ").pack()
    Label(root, text=valor).pack()

def OkCancelAdicional():
    valor = messagebox.askokcancel("Ventana emergente de Enqique", "Hola has pulsado el boton ask 'OK' o 'Cancel'?")
    if valor==True:
        root.destroy()

def AskRetryCancelAdicional():
    valor = messagebox.askretrycancel("Ventana emergente de Enqique", "No es posible, intentelo de nuevo")
    if valor==False:
        root.destroy()


Button(root, text="Info", command=InfoAdicional).pack()
Button(root, text="Warn", command=WarningAdicional).pack()
Button(root, text="Ask", command=AskQuestionAdicional).pack()
Button(root, text="AskRetry", command=AskRetryCancelAdicional).pack()



root.mainloop()