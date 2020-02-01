from ADECUA_lib import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class App():
    def __init__(self):
        #Create and configure the window
        self.root = Tk()
        self.root.geometry(WIN_SIZE)
        self.root.title(WIN_TITLE) #Config window title
        self.root.iconbitmap(WIN_ICO_PATH) #Config the icon window

        # Create main frame to place all the widgets inside
        self.mainWindow = Frame()
        self.mainWindow.grid(row=0, column=0)
        self.mainWindow.columnconfigure(0, weight=1)
        self.mainWindow.rowconfigure(1, weight=1)

        # Create and configure LabelFrames and auto-adjust their sizes
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
        self.treeData = ttk.Treeview(self.lfTreeview)
        self.treeData.heading("#0", text="Treeview")
        self.treeData.column("#0", minwidth=0, width=200, stretch=NO)
        addItemsTreeview(self.treeData)
        self.treeData.tag_bind("mytag", "<<TreeviewSelect>>", self.treeItemSelected)
        self.treeData.grid(row=0, column=0, sticky="NEWS")


        # Create label with flat images
        self.flatPic = Image.open("./pics/flatviews/Dormitorio1_V4.png")
        self.flatPicCopy = self.flatPic.copy()
        self.flatPicTk = ImageTk.PhotoImage(image=self.flatPic)
        self.lFlat = Label(self.lfFlatview, image=self.flatPicTk)
        self.lFlat.grid(row=0, column=0, sticky="NEWS")

        # Create label with floor image
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
        addItemsListbox(self.listData)
        self.listData.bind("<<ListboxSelect>>",lambda event: self.clickOptionlist(event))

        self.root.bind("<Configure>", self.resize_handler)  # bind to windows sizing event
        self.root.mainloop()

    def treeItemSelected(self, event):
        """Item from treeData selected."""
        selected_items = self.treeData.selection()
        #print(self.treeData.item(selected_items)["text"])
        print(self.treeData.item(selected_items)["text"])

    # method related to the item selected on the listData
    def clickOptionlist(self, event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])  # get the string from the item selected on the listbox
        print(value)
        if str(value) == TL_FLAT_VAR[0]:
            self.treeData.item(TL_FLAT_VAR[0], open=True)
            self.treeData.selection_set(TL_FLAT_VAR[0])
        elif str(value) == TL_FLAT_VAR[1]:
            self.treeData.item(TL_FLAT_VAR[1], open=True)
            self.treeData.selection_set(TL_FLAT_VAR[1])

    def resize_handler(self, event):
        # determine the ratio of old width/height to new width/height
        hWindow = self.root.winfo_screenheight()
        wWindow = self.root.winfo_screenwidth()
        wEvent = event.width
        hEvent = event.height


        if self.root.state() == "zoomed":
            if hWindow > hEvent:
                wPicSize = 600
                hPicSize = 400
                #print("Window size es: {}x{}".format(wWindow, hWindow))
                #print("Event size es: {}x{}".format(wEvent, hEvent))
                #print("Pic size es: {}x{}".format(wPicSize, hPicSize))
                self.flatPic = self.flatPicCopy.resize((wPicSize, hPicSize), Image.ANTIALIAS)
                self.flatPicTk = ImageTk.PhotoImage(image=self.flatPic)
                self.lFlat.configure(image=self.flatPicTk)
        else:
            wPicSize = 400
            hPicSize = 300
            #print("Window size es: {}x{}".format(wWindow, hWindow))
            #print("Event size es: {}x{}".format(wEvent, hEvent))
            #print("Pic size es: {}x{}".format(wPicSize, hPicSize))
            self.flatPic = self.flatPicCopy.resize((wPicSize, hPicSize), Image.ANTIALIAS)
            self.flatPicTk = ImageTk.PhotoImage(image=self.flatPic)
            self.lFlat.configure(image=self.flatPicTk)

App()