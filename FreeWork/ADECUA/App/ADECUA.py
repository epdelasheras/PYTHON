from ADECUA_lib import *
from tkinter import *
from PIL import Image, ImageTk

class App():
    def __init__(self):
        #Create and configure the window
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.title("ADECUA") #Config window title
        self.root.iconbitmap(r'.\pics\ADECUA.ico') #Config the icon window

        self.mainWindow = Frame()
        self.mainWindow.grid(row=0, column=0)
        self.mainWindow.columnconfigure(0, weight=1)
        self.mainWindow.rowconfigure(1, weight=1)

        # Create and configure label frames
        self.lfTreeview = LabelFrame(self.mainWindow, text="Treeview Selection", labelanchor=N)
        self.lfTreeview.grid(row=0, column=0, sticky="N", padx=20, pady=20)
        self.lfFlatview = LabelFrame(self.mainWindow, text="Flatview", labelanchor=N)
        self.lfFlatview.grid(row=0, column=1, sticky="N", padx=20, pady=200)
        self.lfFloorview = LabelFrame(self.mainWindow, text="Floorview", labelanchor=N)
        self.lfFloorview.grid(row=0, column=2, sticky="N", padx=20)
        self.lfListbox = LabelFrame(self.mainWindow, text="Listbox", labelanchor=N)
        self.lfListbox.grid(row=0, column=2, sticky="S", padx=40, pady=300)

        self.lfTreeview.columnconfigure(0, weight=1)
        self.lfTreeview.rowconfigure(0, weight=1)
        self.lfFlatview.columnconfigure(0, weight=1)
        self.lfFlatview.rowconfigure(0, weight=1)
        self.lfFloorview.columnconfigure(0, weight=1)
        self.lfFloorview.rowconfigure(0, weight=1)
        self.lfListbox.columnconfigure(0, weight=1)
        self.lfListbox.rowconfigure(0, weight=1)

        # Creating TreeView and bind selected item event
        self.treeData = createTreeview(self.lfTreeview)
        self.treeData.tag_bind("mytag", "<<TreeviewSelect>>", self.treeItemSelected)
        self.treeData.grid(row=0, column=0, sticky="NEWS")

        # Add default images
        self.flatPic = Image.open("./pics/flatviews/Dormitorio1_V4.png")
        self.flatPicCopy = self.flatPic.copy()
        self.flatPicTk = ImageTk.PhotoImage(image=self.flatPic)
        self.lFlatview = Label(self.lfFlatview, image=self.flatPicTk)
        self.lFlatview.grid(row=0, column=0, sticky="NEWS")

        self.floorPic = Image.open("./pics/floorviews/PlantaBaja.png")
        self.floorPicTk = ImageTk.PhotoImage(image=self.floorPic)
        self.lFloorview = Label(self.lfFloorview, image=self.floorPicTk)
        self.lFloorview.grid(row=0, column=0, sticky="NEWS")

        # Creating listbox and bind clickOptionlist event
        self.listData = Listbox(self.lfListbox, height=4) # Creating listbox
        self.listData.grid(row=0,column=0, sticky="NEWS")
        self.yscroll = Scrollbar(self.lfListbox) # Creating vertical scroll
        self.yscroll.grid(row=0,column=1, sticky="NS")
        self.listData.config(yscrollcommand=self.yscroll.set) # Enable yscroll on the listbox
        self.yscroll.config(command=self.listData.yview)
        addItemListbox(self.listData)
        self.listData.bind("<<ListboxSelect>>",lambda event: self.clickOptionlist(event))

        self.root.bind("<Configure>", self.resize_handler)  # bind the function to resize window

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

    def resize_handler(self, event):
        # determine the ratio of old width/height to new width/height
        hWindow = self.root.winfo_screenheight()
        wWindow = self.root.winfo_screenwidth()
        wEvent = event.width
        hEvent = event.height


        if self.root.state() == "zoomed":
            if hWindow > hEvent:
                wPicSize = 800
                hPicSize = 300
                print("Window size es: {}x{}".format(wWindow, hWindow))
                print("Event size es: {}x{}".format(wEvent, hEvent))
                print("Pic size es: {}x{}".format(wPicSize, hPicSize))
                self.flatPic = self.flatPicCopy.resize((wPicSize, hPicSize), Image.ANTIALIAS)
                self.flatPicTk = ImageTk.PhotoImage(image=self.flatPic)
                self.lFlatview.configure(image=self.flatPicTk)
        else:
            wPicSize = 400
            hPicSize = 300
            print("Window size es: {}x{}".format(wWindow, hWindow))
            print("Event size es: {}x{}".format(wEvent, hEvent))
            print("Pic size es: {}x{}".format(wPicSize, hPicSize))
            self.flatPic = self.flatPicCopy.resize((wPicSize, hPicSize), Image.ANTIALIAS)
            self.flatPicTk = ImageTk.PhotoImage(image=self.flatPic)
            self.lFlatview.configure(image=self.flatPicTk)

App()