from tkinter import *
from tkinter import ttk

def createTreeview(Frame):
    treeview = ttk.Treeview(Frame)

    # adding elements to the tree. The previous tree label is indicated
    # to have an event response
    treeview.insert("", END, text="Elemento 1", iid="Main", tags=("mytag",))
    treeview.insert("Main", END, text="Subelemento 1", iid="Sub1", tags=("mytag",))
    treeview.insert("Main", END, text="Subelemento 2", iid="Sub2", tags=("mytag",))

    return treeview

def addItemListbox(ListBox):

    ListBox.insert(0, "Subelemento 1")
    ListBox.insert(1, "Subelemento 2")
    ListBox.insert(2, "Subelemento 3")
    ListBox.insert(3, "Subelemento 4")
    ListBox.insert(4, "Subelemento 5")
    ListBox.insert(5, "Subelemento 6")

    #return listbox
