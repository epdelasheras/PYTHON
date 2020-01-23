from tkinter import *
from py_lib import *

class Application():
    def __init__(self):
        root = Tk()
        root.title("ADECUA")

        # Treeview frame
        self.tvFrame = Frame(root)
        self.tvFrame.grid(row=0, column=0)

        # Listbox frame
        self.lbFrame = Frame(root)
        self.lbFrame.grid(row=0, column=1)

        # Car image frame
        self.carFrame = Frame(root)
        self.carFrame.grid(row=0, column=2)
        self.carPic = PhotoImage(file="./pics/car.png")
        self.carLabel = Label(self.carFrame, image=self.carPic)
        self.carLabel.grid(row=0, column=0)

        # Creating TreeView and bind selected item event
        self.treeData = createTreeview(self.tvFrame)
        self.treeData.tag_bind("mytag", "<<TreeviewSelect>>", self.treeItemSelected)

        # Creating listbox and bind clickOptionlist event
        self.listData = createListbox(self.lbFrame)
        self.listData.bind("<<ListboxSelect>>",lambda event:
                           self.clickOptionlist(event))

        root.mainloop()

    # method related to the item selected on the treeData
    def treeItemSelected(self, event):
        """Item seleccionado."""
        selected_items = self.treeData.selection()
        print(self.treeData.item(selected_items)["text"])

    # method related to the item selected on the listData
    def clickOptionlist(self, event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])  # get the string from the item selected on the listbox
        print(value)
        if str(value) == "Subelemento 1":
            self.treeData.item("Main", open=True)
            self.treeData.selection_set("Sub1")
        elif str(value) == "Subelemento 2":
            self.treeData.item("Main", open=True)
            self.treeData.selection_set("Sub2")

Application()