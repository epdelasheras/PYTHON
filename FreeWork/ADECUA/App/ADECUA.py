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
        self.lfTreeview = LabelFrame(self.mainFrame, text="Treeview Selection")
        self.lfTreeview.grid(row=0, column=0, sticky="NW", padx=20, pady=20)
        self.lfFlatview = LabelFrame(self.mainFrame, text="Flat view", padx=20, pady=50)
        self.lfFlatview.grid(row=0, column=1, sticky="N")


        # Creating TreeView and bind selected item event
        self.treeData = createTreeview(self.lfTreeview)
        self.treeData.tag_bind("mytag", "<<TreeviewSelect>>", self.treeItemSelected)

        # Add default image
        self.bed1 = PhotoImage(file="./pics/flatviews/bed1.png")
        self.lFlatview = Label(self.lfFlatview, image=self.bed1)
        self.lFlatview.grid(row=0, column=0, padx=20, pady=20)


        self.root.mainloop()

    def treeItemSelected(self, event):
        """Item from treeData selected."""
        selected_items = self.treeData.selection()
        print(self.treeData.item(selected_items)["text"])


App()