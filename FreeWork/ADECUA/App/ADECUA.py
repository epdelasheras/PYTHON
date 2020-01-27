from tkinter import *
from ADECUA_lib import *

class App():
    def __init__(self):
        #Create and configure the window
        self.root = Tk()
        self.root.title("ADECUA") #Config window title
        self.root.iconbitmap(r'.\pics\ADECUA.ico') #Config the icon window
        self.root.state("zoomed") #Execute program with maxmize window

        #Create and configure the Main Frame
        self.mainFrame = Frame(self.root)
        self.mainFrame.grid_configure(sticky="NEWS")  # to grow up in all directions
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(1, weight=1)

        #Create and configure label frames
        self.lfTreeview = LabelFrame(self.mainFrame, text="Treeview Selection", labelanchor=N)
        self.lfTreeview.grid(row=0, column=0, sticky="NW", padx=50, pady=20)
        self.lfFlatview = LabelFrame(self.mainFrame, text="Flatview", labelanchor=N)
        self.lfFlatview.grid(row=0, column=1, sticky="N", padx=100, pady=120)
        self.lfFloorview = LabelFrame(self.mainFrame, text="Floorview", labelanchor=N)
        self.lfFloorview.grid(row=0, column=2, sticky="NE", padx=30, pady=20)
        self.lfListbox = LabelFrame(self.mainFrame, text="Listbox", labelanchor=N)
        self.lfListbox.grid(row=1, column=2, sticky="N", padx=20, pady=20)


        # Creating TreeView and bind selected item event
        self.treeData = createTreeview(self.lfTreeview)
        self.treeData.tag_bind("mytag", "<<TreeviewSelect>>", self.treeItemSelected)

        # Add default image
        self.Dormitorio1_V4 = PhotoImage(file="./pics/flatviews/Dormitorio1_V4.png")
        self.lFlatview = Label(self.lfFlatview, image=self.Dormitorio1_V4)
        self.lFlatview.grid(row=0, column=0)

        self.PlantaBaja = PhotoImage(file="./pics/floorviews/PlantaBaja.png")
        self.lFloorview = Label(self.lfFloorview, image=self.PlantaBaja)
        self.lFloorview.grid(row=0, column=0)

        # Creating listbox and bind clickOptionlist event
        self.listData = Listbox(self.lfListbox, height=4) # Creating listbox
        self.listData.grid(row=0, column=0, sticky="NS")
        self.yscroll = Scrollbar(self.lfListbox, command=self.listData.yview) # Creating vertical scroll
        self.yscroll.grid(row=0, column=2, sticky="NEWS")
        self.listData.config(yscrollcommand=self.yscroll.set) # Enable yscroll on the listbox
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