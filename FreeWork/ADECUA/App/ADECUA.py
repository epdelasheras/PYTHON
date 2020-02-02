from ADECUA_lib import *
from tkinter import *
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

class App():
    def __init__(self):
        #Create and configure the window
        self.root = Tk()
        self.root.geometry(WIN_SIZE)
        self.root.title(WIN_TITLE) #Config window title
        self.root.iconbitmap(WIN_ICO_PATH) #Config the icon window

        # Create main frame to place all the widgets inside
        self.main_window = Frame()
        self.main_window.grid(row=0, column=0)
        self.main_window.columnconfigure(0, weight=1)
        self.main_window.rowconfigure(1, weight=1)

        # Create and configure LabelFrames and auto-adjust their sizes
        self.lf_treeview = LabelFrame(self.main_window, text="Treeview Selection", labelanchor=N)
        self.lf_treeview.grid(row=0, column=0, sticky="N", padx=20, pady=20)
        self.lf_flatview = LabelFrame(self.main_window, text="Flatview", labelanchor=N)
        self.lf_flatview.grid(row=0, column=1, sticky="N", padx=20, pady=200)
        self.lf_floorview = LabelFrame(self.main_window, text="Floorview", labelanchor=N)
        self.lf_floorview.grid(row=0, column=2, sticky="N", padx=20)
        self.lf_listbox = LabelFrame(self.main_window, text="Listbox", labelanchor=N)
        self.lf_listbox.grid(row=0, column=2, sticky="S", padx=40, pady=300)
        self.lf_treeview.columnconfigure(0, weight=1)
        self.lf_treeview.rowconfigure(0, weight=1)
        self.lf_flatview.columnconfigure(0, weight=1)
        self.lf_flatview.rowconfigure(0, weight=1)
        self.lf_floorview.columnconfigure(0, weight=1)
        self.lf_floorview.rowconfigure(0, weight=1)
        self.lf_listbox.columnconfigure(0, weight=1)
        self.lf_listbox.rowconfigure(0, weight=1)

        # Creating TreeView and bind selected item event
        self.tree_view = ttk.Treeview(self.lf_treeview)
        self.tree_view.heading("#0", text="Treeview")
        self.tree_view.column("#0", minwidth=0, width=130, stretch=NO)
        addItemsTreeview(self.tree_view)
        self.tree_view.tag_bind("mytag", "<<TreeviewSelect>>", self.treeItemSelected)
        self.tree_view.grid(row=0, column=0, sticky="NEWS")

        # Create label with flat images
        self.flat_pic = Image.open("./pics/flatviews/Dormitorio1_V4.png")
        self.flat_picCopy = self.flat_pic.copy()
        self.flat_picTk = ImageTk.PhotoImage(image=self.flat_pic)
        self.label_flat = Label(self.lf_flatview, image=self.flat_picTk)
        self.label_flat.grid(row=0, column=0, sticky="NEWS")

        # Create label with floor image
        self.floor_pic = Image.open("./pics/floorviews/PlantaBaja.png")
        self.floor_picCopy = self.floor_pic.copy()
        self.floor_picTk = ImageTk.PhotoImage(image=self.floor_pic)
        self.label_floor = Label(self.lf_floorview, image=self.floor_picTk)
        self.label_floor.grid(row=0, column=0, sticky="NEWS")
        self.label_floor.bind("<Motion>", self.labelFloorMotion) # bind mouse movement on pic
        self.label_floor.bind("<Button-1>",lambda event: self.labelFloorLeftClick(event)) # bind the left mouse click on pic

        # Creating listbox and bind clickOptionlist event
        self.list_box = Listbox(self.lf_listbox, height=4) # Creating listbox
        self.list_box.grid(row=0,column=0, sticky="NEWS")
        self.list_box_yscroll = Scrollbar(self.lf_listbox) # Creating vertical scroll
        self.list_box_yscroll.grid(row=0,column=1, sticky="NS")
        self.list_box.config(yscrollcommand=self.list_box_yscroll.set) # Enable listbox_yscroll on the listbox
        self.list_box_yscroll.config(command=self.list_box.yview)
        addItemsListbox(self.list_box)
        self.list_box.bind("<<ListboxSelect>>",lambda event: self.listboxItemSel(event))

        # bind to resize window items
        self.root.bind("<Configure>", self.rootResize)  # bind to windows sizing event
        self.root.mainloop()

    def labelFloorLeftClick(self, event):
        floor_width_ratio = float(WIDTH_FLOORPIC_ZOOM/WIDTH_FLOORPIC_DEFAULT)
        floor_height_ratio = float(HEIGHT_FLOORPIC_ZOOM/HEIGHT_FLOORPIC_DEFAULT)
        print("{},{}".format(floor_width_ratio, floor_height_ratio))
        aux=self.root.winfo_reqwidth()
        print(aux)
        print(((self.label_floor_x) * floor_width_ratio))
        if self.root.winfo_reqwidth() > 900:
            if (int((self.label_floor_x)/floor_width_ratio) > 20 and
                int((self.label_floor_x)/floor_width_ratio) < 60 and
                int((self.label_floor_y)/floor_height_ratio) > 60 and
                int((self.label_floor_y)/floor_height_ratio) < 80):

                print("Portal1, Vivienda A, zoom")
        else:
            if (self.label_floor_x > 20 and
                self.label_floor_x < 60 and
                self.label_floor_y > 60 and
                self.label_floor_y < 80):
                print("Portal1, Vivienda A, default")

    def labelFloorMotion(self, event):
        self.label_floor_x = event.x
        self.label_floor_y = event.y
        #print('{}, {}'.format(self.label_floor_x, self.label_floor_y))

    # TreeView method to identify item selected
    def treeItemSelected(self, event):
        """Item from tree_view selected."""
        #selected_items = self.tree_view.selection()
        #print(self.tree_view.item(selected_items)["text"])
        #print(self.tree_view.item(selected_items)["text"])
        tree_coords = (self.tree_view.winfo_pointerx() - self.tree_view.winfo_rootx(),
                       self.tree_view.winfo_pointery() - self.tree_view.winfo_rooty())
        tree_item = self.tree_view.identify('item', *tree_coords)
        print(tree_item)


    # ListBox method to identify the item selected
    def listboxItemSel(self, event):
        list = event.widget
        selection = list.curselection()
        value = list.get(selection[0])  # get the string from the item selected on the listbox


    # method to adjust pic sizes according main window size
    def rootResize(self, event):
        # determine the ratio of old width/height to new width/height
        hWindow = self.root.winfo_screenheight()
        wWindow = self.root.winfo_screenwidth()
        wEvent = event.width
        hEvent = event.height
        if self.root.state() == "zoomed":
            if hWindow > hEvent:
                # Resize flat pic
                self.flat_pic = self.flat_picCopy.resize((WIDTH_FLATPIC_ZOOM, HEIGHT_FLATPIC_ZOOM), Image.ANTIALIAS)
                self.flat_picTk = ImageTk.PhotoImage(image=self.flat_pic)
                self.label_flat.configure(image=self.flat_picTk)
                # Resize floor pic
                self.floor_pic = self.floor_picCopy.resize((WIDTH_FLOORPIC_ZOOM, HEIGHT_FLOORPIC_ZOOM), Image.ANTIALIAS)
                self.floor_picTk = ImageTk.PhotoImage(image=self.floor_pic)
                self.label_floor.configure(image=self.floor_picTk)
        else:
            # Resize flat pic
            self.flat_pic = self.flat_picCopy.resize((WIDTH_FLATPIC_DEFAULT, HEIGHT_FLATPIC_DEFAULT), Image.ANTIALIAS)
            self.flat_picTk = ImageTk.PhotoImage(image=self.flat_pic)
            self.label_flat.configure(image=self.flat_picTk)
            # Resize floor pic
            self.floor_pic = self.floor_picCopy.resize((WIDTH_FLOORPIC_DEFAULT, HEIGHT_FLOORPIC_DEFAULT), Image.ANTIALIAS)
            self.floor_picTk = ImageTk.PhotoImage(image=self.floor_pic)
            self.label_floor.configure(image=self.floor_picTk)

App()