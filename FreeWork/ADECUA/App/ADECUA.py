from ADECUA_lib import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import openpyxl

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

        # Create and configure LabelFrames and auto-adjust their sizes
        self.lf_treeview = LabelFrame(self.main_window, text="Treeview Selection", labelanchor=N)
        self.lf_treeview.grid(row=0, column=0, sticky="N", padx=20, pady=20)
        self.lf_flatview = LabelFrame(self.main_window, text="Flatview", labelanchor=N)
        self.lf_flatview.grid(row=0, column=1, sticky="N", padx=20, pady=200)
        self.lf_floorview = LabelFrame(self.main_window, text="Floorview", labelanchor=N)
        self.lf_floorview.grid(row=0, column=2, sticky="N", padx=20)

        # Creating TreeView and bind selected item event
        self.tree_view = ttk.Treeview(self.lf_treeview, height=35)
        self.tree_view.heading("#0", text="Treeview")
        self.tree_view.column("#0", minwidth=0, width=150, stretch=NO)
        addItemsTreeview(self.tree_view)
        self.tree_view.tag_bind("mytag", "<<TreeviewSelect>>", self.treeItemSel)
        self.tree_view.grid(row=0, column=0, sticky="NEWS")

        # Create label with flat images
        self.flat_pic = Image.open("./pics/blk1floor0flat1rvar1.png")
        self.flat_picCopy = self.flat_pic.copy()
        self.flat_picCopyResize = self.flat_picCopy.resize((WIDTH_FLATPIC, HEIGHT_FLATPIC), Image.ANTIALIAS)
        self.flat_picTk = ImageTk.PhotoImage(image=self.flat_picCopyResize)
        self.label_flat = Label(self.lf_flatview, image=self.flat_picTk)
        self.label_flat.grid(row=0, column=0, sticky="NEWS")

        # Create label with floor image
        self.floor_pic = Image.open("./pics/blk1floor0.png")
        self.floor_picCopy = self.floor_pic.copy()
        self.floor_picCopyResize = self.floor_picCopy.resize((WIDTH_FLOORPIC, HEIGHT_FLOORPIC), Image.ANTIALIAS)
        self.floor_picTk = ImageTk.PhotoImage(image=self.floor_picCopyResize)
        self.label_floor = Label(self.lf_floorview, image=self.floor_picTk)
        self.label_floor.grid(row=0, column=0, sticky="NEWS")
        self.label_floor.bind("<Motion>", self.labelFloorMotion) # bind mouse movement on pic
        self.label_floor.bind("<Button-1>", lambda event: self.labelFloorLeftClick(event, # bind leftmouse clickon pic
                                                          self.list_box))

        self.root.mainloop()

    # Method executed when the user makes left clik on an specific part of the floor picture
    def labelFloorLeftClick(self, event, list_box):
        self.floor_area_id = areaId(self.label_floor_x, self.label_floor_y)
        if list_box.size() != 0: # delete listbox items before adding new ones.
            list_box.delete(0,"end")
        if self.floor_area_id == AREA_ID[0]: # Add to the listbox specific variants
            addItemsListbox(list_box, AREA_ID[0])
            self.tl_iid = TL_FLAT_IID[0]  # expand the treeview with the variants

    # Method which return the coordenates of the mouse over the floor pic.
    def labelFloorMotion(self, event):
        self.label_floor_x = event.x
        self.label_floor_y = event.y
        #print('{}, {}'.format(self.label_floor_x, self.label_floor_y))

    # Method used to identify item selected on the Treeview.
    def treeItemSel(self, event):
        # get the tree selected item
        tree_coords = (self.tree_view.winfo_pointerx() - self.tree_view.winfo_rootx(),
                       self.tree_view.winfo_pointery() - self.tree_view.winfo_rooty())
        tree_item = self.tree_view.identify('item', *tree_coords)

        print(tree_item)
        print(len(tree_item))

        #change pics according to the tree item selected
        if len(tree_item) == 10: #Change floor pic
            self.floor_pic = Image.open("./pics/" + tree_item + ".png")
            self.floor_picCopy = self.floor_pic.copy()
            self.floor_picCopyResize = self.floor_picCopy.resize((WIDTH_FLOORPIC, HEIGHT_FLOORPIC), Image.ANTIALIAS)
            self.floor_picTk = ImageTk.PhotoImage(image=self.floor_picCopyResize)
            self.label_floor.configure(image=self.floor_picTk)
        elif len(tree_item) == 20: #change flat pic
            self.flat_pic = Image.open("./pics/" + tree_item + ".png")
            self.flat_picCopy = self.flat_pic.copy()
            self.flat_picCopyResize = self.flat_picCopy.resize((WIDTH_FLATPIC, HEIGHT_FLATPIC), Image.ANTIALIAS)
            self.flat_picTk = ImageTk.PhotoImage(image=self.flat_picCopyResize)
            self.label_flat.configure(image=self.flat_picTk)


'''
        # highlight specific area on the floor pic
        self.floor_picTk = highlightArea(self.label_floor_x, self.label_floor_y)
        self.label_floor.configure(image=self.floor_picTk)
'''

App()