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
        self.root.resizable(0, 0)

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
        self.tree_view.tag_bind("mytag", "<<TreeviewSelect>>", self.treeItemSel)
        self.tree_view.grid(row=0, column=0, sticky="NEWS")

        # Creating listbox and bind clickOptionlist event
        self.list_box = Listbox(self.lf_listbox, height=4) # Creating listbox
        self.list_box.grid(row=0,column=0, sticky="NEWS")
        self.list_box_yscroll = Scrollbar(self.lf_listbox) # Creating vertical scroll
        self.list_box_yscroll.grid(row=0,column=1, sticky="NS")
        self.list_box.config(yscrollcommand=self.list_box_yscroll.set) # Enable listbox_yscroll on the listbox
        self.list_box_yscroll.config(command=self.list_box.yview)
        self.list_box.bind("<<ListboxSelect>>", lambda event: self.listboxItemSel(event))

        # Create label with flat images
        self.flat_pic = Image.open("./pics/flatviews/1DVar1.png")
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
        self.label_floor.bind("<Button-1>", lambda event: self.labelFloorLeftClick(event, # bind leftmouse clickon pic
                                                         self.lf_listbox, self.list_box))

        # bind to resize window items
        self.root.bind("<Configure>", self.rootResize)  # bind to windows sizing event
        self.root.mainloop()

    # Method executed when the user makes left clik on an specific part of the floor picture
    def labelFloorLeftClick(self, event, lf_listbox, list_box):
        floor_width_ratio = float(WIDTH_FLOORPIC_ZOOM/WIDTH_FLOORPIC_DEFAULT)
        floor_height_ratio = float(HEIGHT_FLOORPIC_ZOOM/HEIGHT_FLOORPIC_DEFAULT)
        if self.root.winfo_reqwidth() > WIDTH_LABELFLOOR:
            if (int((self.label_floor_x)/floor_width_ratio) > BLK1_X1 and
                int((self.label_floor_x)/floor_width_ratio) < BLK1_X2 and
                int((self.label_floor_y)/floor_height_ratio) > BLK1_Y1 and
                int((self.label_floor_y)/floor_height_ratio) < BLK1_Y2):
                # show listbox and specific items
                addItemsListbox(list_box, TL_BLOCK[0], TL_FLOOR[0], TL_FLAT[0])
                self.tl_iid = TL_FLAT_IID[0] # used in treeview to expand the item
        else:
            if (self.label_floor_x > BLK1_X1 and
                self.label_floor_x < BLK1_X2 and
                self.label_floor_y > BLK1_Y1 and
                self.label_floor_y < BLK1_Y2):
                # show listbox and specific items
                addItemsListbox(list_box, TL_BLOCK[0], TL_FLOOR[0], TL_FLAT[0])
                self.tl_iid = TL_FLAT_IID[0]  # used in treeview to expand the item

    # Method which return the coordenates of the mouse over the floor pic.
    def labelFloorMotion(self, event):
        self.label_floor_x = event.x
        self.label_floor_y = event.y
        #print('{}, {}'.format(self.label_floor_x, self.label_floor_y))

    # Method used to identify an item selected on the Listbox.
    def listboxItemSel(self, event):
        list = event.widget
        cur_selection = list.curselection()
        item_selected = list.get(cur_selection[0])  # get the string from the item selected on the listbox
        #print(item_selected)
        tv_iid = str(self.tl_iid) + "_" + str(item_selected) # add the las wod of the string
        tv_iid_split = tv_iid.split("_") # split string and store it in a list

        # open item from the treeview selected in the listbox
        self.tree_view.item(tv_iid_split[0], open=True)# open block
        self.tree_view.item(tv_iid_split[0]+"_"+tv_iid_split[1], open=True)# open block + floor
        self.tree_view.item(tv_iid_split[0]+"_"+tv_iid_split[1]+"_"+tv_iid_split[2], open=True)# open block + floor + flat
        self.tree_view.selection_set(tv_iid)

        # change label flat picture
        self.flat_picTk = loadNewFlatPic(tv_iid_split)
        self.label_flat.configure(image=self.flat_picTk)

        # highlight specific area on the floor pic
        self.floor_picTk = highlightArea(self.label_floor)
        self.label_floor.configure(image=self.floor_picTk)

    # Method used to identify item selected on the Treeview.
    def treeItemSel(self, event):
        #selected_items = self.tree_view.selection()
        #print(self.tree_view.item(selected_items)["text"])
        #print(self.tree_view.item(selected_items)["text"])
        tree_coords = (self.tree_view.winfo_pointerx() - self.tree_view.winfo_rootx(),
                       self.tree_view.winfo_pointery() - self.tree_view.winfo_rooty())
        tree_item = self.tree_view.identify('item', *tree_coords)
        #print(tree_item)
        tree_item_split = tree_item.split("_")
        #print(tree_item_split)
        # change label flat picture
        tl_flat_var_iid_split = TL_FLAT_VAR_IID[0].split("_") # to figure out when the room variant is selected
        if len(tree_item_split) == len(tl_flat_var_iid_split): # check if the number of elements is ok
            self.flat_pic = Image.open("./pics/flatviews/"+tree_item_split[3]+".png")
            self.flat_picCopy = self.flat_pic.copy()
            self.flat_pic_resize = self.flat_picCopy.resize((WIDTH_FLATPIC_ZOOM, HEIGHT_FLATPIC_ZOOM), Image.ANTIALIAS)
            self.flat_picTk = ImageTk.PhotoImage(image=self.flat_pic_resize)
            self.label_flat.configure(image=self.flat_picTk)

    # method to adjust pic sizes according main window size
    def rootResize(self, event):
        # determine the ratio of old width/height to new width/height
        hWindow = self.root.winfo_screenheight()
        wWindow = self.root.winfo_screenwidth()
        wEvent = event.width
        hEvent = event.height
        #print(self.root.state())
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
            self.root.state('zoomed')

            '''
            Resize flat pic
            self.flat_pic = self.flat_picCopy.resize((WIDTH_FLATPIC_DEFAULT, HEIGHT_FLATPIC_DEFAULT), Image.ANTIALIAS)
            self.flat_picTk = ImageTk.PhotoImage(image=self.flat_pic)
            self.label_flat.configure(image=self.flat_picTk)
            # Resize floor pic
            self.floor_pic = self.floor_picCopy.resize((WIDTH_FLOORPIC_DEFAULT, HEIGHT_FLOORPIC_DEFAULT),
                                                       Image.ANTIALIAS)
            self.floor_picTk = ImageTk.PhotoImage(image=self.floor_pic)
            self.label_floor.configure(image=self.floor_picTk)
            '''

App()