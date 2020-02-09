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
        self.main_window = Frame()
        self.main_window.grid(row=0, column=0)

        # Create and configure LabelFrames and auto-adjust their sizes
        self.lf_treeview = LabelFrame(self.main_window, text="Treeview Selection", labelanchor=N)
        self.lf_treeview.grid(row=0, column=0, sticky="N", padx=20, pady=20)
        self.lf_flatview = LabelFrame(self.main_window, text="Flatview", labelanchor=N)
        self.lf_flatview.grid(row=0, column=1, sticky="N", padx=20, pady=200)
        self.lf_floorview = LabelFrame(self.main_window, text="Floorview", labelanchor=N)
        self.lf_floorview.grid(row=0, column=2, sticky="N", padx=20)
        self.lf_listbox = LabelFrame(self.main_window, text="Listbox", labelanchor=N)
        self.lf_listbox.grid(row=0, column=2, sticky="S", padx=40, pady=300)

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
        self.flat_picCopyResize = self.flat_picCopy.resize((WIDTH_FLATPIC, HEIGHT_FLATPIC), Image.ANTIALIAS)
        self.flat_picTk = ImageTk.PhotoImage(image=self.flat_picCopyResize)
        self.label_flat = Label(self.lf_flatview, image=self.flat_picTk)
        self.label_flat.grid(row=0, column=0, sticky="NEWS")

        # Create label with floor image
        self.floor_pic = Image.open("./pics/floorviews/PlantaBaja.png")
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
        self.floor_picTk = highlightArea(self.label_floor_x, self.label_floor_y)
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
            self.flat_picCopyResize = self.flat_picCopy.resize((WIDTH_FLATPIC, HEIGHT_FLATPIC), Image.ANTIALIAS)
            self.flat_picTk = ImageTk.PhotoImage(image=self.flat_picCopyResize)
            self.label_flat.configure(image=self.flat_picTk)

App()