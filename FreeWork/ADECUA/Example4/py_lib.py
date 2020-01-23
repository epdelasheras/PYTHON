from tkinter import *
from tkinter import ttk

def createTreeview(Frame):
    treeview = ttk.Treeview(Frame)

    # adding elements to the tree. The previous tree label is indicated
    # to have an event response
    treeview.insert("", END, text="Elemento 1", iid="Main", tags=("mytag",))
    treeview.insert("Main", END, text="Subelemento 1", iid="Sub1", tags=("mytag",))
    treeview.insert("Main", END, text="Subelemento 2", iid="Sub2", tags=("mytag",))

    treeview.pack()

    return treeview

def createListbox(Frame):
    # Creating listbox
    listbox = Listbox(Frame, height=4)
    listbox.grid(row=0, column=0, sticky=N + S)
    # Creating vertical scroll
    yscroll = Scrollbar(Frame, command=listbox.yview)
    yscroll.grid(row=0, column=2, sticky="nsew")
    # Enable yscroll on the listbox
    listbox.config(yscrollcommand=yscroll.set)

    listbox.insert(0, "Subelemento 1")
    listbox.insert(1, "Subelemento 2")
    listbox.insert(2, "Subelemento 3")
    listbox.insert(3, "Subelemento 4")
    listbox.insert(4, "Subelemento 5")
    listbox.insert(5, "Subelemento 6")

    return listbox

