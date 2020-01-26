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
