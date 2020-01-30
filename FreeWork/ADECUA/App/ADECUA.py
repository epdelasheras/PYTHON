from tkinter import *
from ADECUA_lib import *

class App():
    def __init__(self):
        #Create and configure the window
        self.root = Tk()
        self.root.title("ADECUA") #Config window title
        self.root.iconbitmap(r'.\pics\ADECUA.ico') #Config the icon window
        self.root.state("zoomed") #Execute program with maxmize window

        # Create and configure label frames
        self.lfTreeview = LabelFrame(self.root, text="Treeview Selection", labelanchor=N)
        self.lfTreeview.place(x=20, y=80)
        self.lfFlatview = LabelFrame(self.root, text="Flatview", labelanchor=N)
        self.lfFlatview.place(x=500, y=200)
        self.lfFloorview = LabelFrame(self.root, text="Floorview", labelanchor=N)
        self.lfFloorview.place(x=1300, y=200, relx=0)
        self.lfListbox = LabelFrame(self.root, text="Listbox", labelanchor=N)
        self.lfListbox.place(x=1300, y=600)


        # Creating TreeView and bind selected item event
        self.treeData = createTreeview(self.lfTreeview)
        self.treeData.tag_bind("mytag", "<<TreeviewSelect>>", self.treeItemSelected)
        self.treeData.pack()

        # Add default images
        self.Dormitorio1_V4 = PhotoImage(file="./pics/flatviews/Dormitorio1_V4.png")
        self.lFlatview = Label(self.lfFlatview, image=self.Dormitorio1_V4)
        self.lFlatview.pack()

        self.PlantaBaja = PhotoImage(file="./pics/floorviews/PlantaBaja.png")
        self.lFloorview = Label(self.lfFloorview, image=self.PlantaBaja)
        self.lFloorview.pack()


        # Creating listbox and bind clickOptionlist event
        self.listData = Listbox(self.lfListbox, height=4) # Creating listbox
        self.listData.pack(side=LEFT)
        self.yscroll = Scrollbar(self.lfListbox) # Creating vertical scroll
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.listData.config(yscrollcommand=self.yscroll.set) # Enable yscroll on the listbox
        self.yscroll.config(command=self.listData.yview)
        addItemListbox(self.listData)
        self.listData.bind("<<ListboxSelect>>",lambda event: self.clickOptionlist(event))


        self.root.mainloop()

    def treeItemSelected(self, event):
        """Item from treeData selected."""
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


App()