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
        self.root.iconbitmap(PIC_PATH + WIN_TITLE + ".ico") #Config the icon window
        self.root.iconbitmap(PIC_PATH + WIN_TITLE + ".ico")  # Config the icon window

        # Create main frame to place all the widgets inside
        self.main_window = Frame()
        self.main_window.grid(row=0, column=0)

        # Create and configure LabelFrames and auto-adjust their sizes
        self.lf_treeview = LabelFrame(self.main_window, text="ARBOL DE SELECCIÓN", labelanchor=N)
        self.lf_treeview.grid(row=0, column=0, sticky="N", padx=20, pady=20)
        self.lf_flatview = LabelFrame(self.main_window, text="APARTAMENTO SELECCIONADO", labelanchor=N)
        self.lf_flatview.grid(row=0, column=1, sticky="N", padx=20, pady=200)
        self.lf_roomview = LabelFrame(self.main_window, text="Nº DORMITORIOS", labelanchor=N)
        self.lf_roomview.grid(row=0, column=2, sticky="N", padx=20)

        # Creating TreeView and bind selected item event
        self.tree_view = ttk.Treeview(self.lf_treeview, height=35)
        self.tree_view.heading("#0", text="Treeview")
        self.tree_view.column("#0", minwidth=0, width=150, stretch=NO)
        addItemsTreeview(self.tree_view)
        self.tree_view.tag_bind("mytag", "<<TreeviewSelect>>", self.treeItemSel)
        self.tree_view.grid(row=0, column=0, sticky="NEWS")

        # Create label with flat images
        self.flat_pic = Image.open("./pics/Diseño Base y Variante 1_2.jpg")
        self.flat_picCopy = self.flat_pic.copy()
        self.flat_picCopyResize = self.flat_picCopy.resize((WIDTH_FLATPIC, HEIGHT_FLATPIC), Image.ANTIALIAS)
        self.flat_picTk = ImageTk.PhotoImage(image=self.flat_picCopyResize)
        self.label_flat = Label(self.lf_flatview, image=self.flat_picTk)
        self.label_flat.grid(row=0, column=0, sticky="NEWS")

        # Create label with number of rooms text box
        self.tb_room = Label(self.lf_roomview, text="", justify="left")
        self.tb_room.grid(row=0, column=0, sticky="NEWS")

        self.root.mainloop()

    # Method used to identify item selected on the Treeview.
    def treeItemSel(self, event):
        # get the tree selected item
        tree_coords = (self.tree_view.winfo_pointerx() - self.tree_view.winfo_rootx(),
                       self.tree_view.winfo_pointery() - self.tree_view.winfo_rooty())
        tree_item = self.tree_view.identify('item', *tree_coords)

        tree_item_split = tree_item.split("-")

        if len(tree_item_split) == N_ITEMS: # Only load pics when tipololy tree view is selected
            self.flat_pic = Image.open(PIC_PATH + tree_item + PIC_EXTENSION)
            self.flat_picCopy = self.flat_pic.copy()
            self.flat_picCopyResize = self.flat_picCopy.resize((WIDTH_FLATPIC, HEIGHT_FLATPIC), Image.ANTIALIAS)
            self.flat_picTk = ImageTk.PhotoImage(image=self.flat_picCopyResize)
            self.label_flat.configure(image=self.flat_picTk)
            tipology = tree_item_split[3]
            tipology_split = tipology.split("_",1)
            if (len(tipology_split)>1): # to avoid the LC1 case
                n_rooms = tipology_split[1][:1] #save only the integer related with the n_rooms
                self.tb_room.configure(text=n_rooms + " dormitorio/s")
                coordinates = searchLocation(tree_item_split[0], tree_item)
                print(coordinates)
            else: # LC1 case selected
                coordinates = searchLocation(tree_item_split[0], tree_item)
                print(coordinates)



App()