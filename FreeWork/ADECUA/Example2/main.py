from tkinter import *
from tkinter import ttk


class Application(ttk.Frame):

    def __init__(self, main_window):

        super().__init__(main_window)#create a superfunction to save code in othe classes
        main_window.title("Vista de árbol en Tkinter")

        self.treeview = ttk.Treeview(self)

        # Creating new tree labels
        self.treeview.tag_bind("mytag", "<<TreeviewSelect>>",
                               self.item_selected)

        # adding elements to the tree. The previous tree label is indicated
        # to have an event response
        item = self.treeview.insert("", END, text="Elemento 1",
                                    tags=("mytag",))
        self.treeview.insert(item, END, text="Subelemento 1",
                             tags=("mytag",))
        self.treeview.insert(item, END, text="Subelemento 2",


                             tags=("mytag",))


        self.treeview.pack()

        self.pack()

    def item_selected(self, event):
        """Item seleccionado."""
        selected_items = self.treeview.selection()
        print(selected_items)

    def item_opened(self, event):
        """Item abierto."""
        print("Abierto.")

    def item_closed(self, event):
        """Item cerrado."""
        print("Cerrado.")


main_window = Tk()
app = Application(main_window)
app.mainloop()