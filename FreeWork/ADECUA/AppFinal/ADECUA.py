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
        self.lf_treeview.grid(row=0, column=0, sticky="N", padx=10, pady=20)
        self.lf_flatview = LabelFrame(self.main_window, text="APARTAMENTO SELECCIONADO", labelanchor=N)
        self.lf_flatview.grid(row=0, column=1, sticky="N", padx=10, pady=150)
        self.lf_labelroom = LabelFrame(self.main_window, text="Nº DORMITORIOS | COORDENADAS", labelanchor=N)
        self.lf_labelroom.grid(row=0, column=1, sticky="NW", padx=10, pady=20)
        self.lf_listroom = LabelFrame(self.main_window, text="SELECCIÓN DORMITORIOS", labelanchor=N)
        self.lf_listroom.grid(row=0, column=1, sticky="NE", padx=10, pady=20)
        self.lf_listroomplace = LabelFrame(self.main_window, text="Nº DORMITORIOS | COORDENADAS", labelanchor=N)
        self.lf_listroomplace.grid(row=0, column=2, sticky="NW", padx=10, pady=20)

        # Creating TreeView and bind selected item event
        self.tree_view = ttk.Treeview(self.lf_treeview, height=35)
        self.tree_view.heading("#0", text="Treeview")
        self.tree_view.column("#0", minwidth=0, width=245, stretch=NO)
        self.file_names, self.file_places, self.file_tipo = addItemsTreeview(self.tree_view)
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
        self.tb_room = Label(self.lf_labelroom, text="", justify="left")
        self.tb_room.grid(row=0, column=0, sticky="NE")

        # Create label with coordinates of the tipology selected
        self.tb_place = Label(self.lf_labelroom, text="", justify="left")
        self.tb_place.grid(row=0, column=1, sticky="NW")

        # Create listbox with number of rooms to choose
        self.lb_room = Listbox(self.lf_listroom, heigh=0)
        self.lb_room.grid(row=0, column=0, sticky="NEWS")
        self.lb_room.bind("<<ListboxSelect>>", self.listboxItemSelRoom)
        self.lb_room_yscrl = Scrollbar(self.lf_listroom, orient=VERTICAL)
        self.lb_room["yscrollcommand"] = self.lb_room_yscrl.set
        self.lb_room_yscrl["command"] = self.lb_room.yview
        self.lb_room_yscrl.grid(row=0, column=1, sticky="NEWS")
        self.n_room = addItemsListboxRoom(self.lb_room, self.file_names)

        # Create listbox with rooms and coordinates
        self.lb_roomplace = Listbox(self.lf_listroomplace, width=60, heigh=40)
        self.lb_roomplace.grid(row=0, column=0, sticky="NEWS")
        self.lb_roomplace.bind("<<ListboxSelect>>", self.listboxItemSelRoomPlace)
        self.lb_roomplace_yscrl = Scrollbar(self.lf_listroomplace, orient=VERTICAL)
        self.lb_roomplace["yscrollcommand"] = self.lb_roomplace_yscrl.set
        self.lb_roomplace_yscrl["command"] = self.lb_roomplace.yview
        self.lb_roomplace_yscrl.grid(row=0, column=1, sticky="NEWS")

        self.root.mainloop()

    # Method executed when a item in lb_roomplace is selected
    def listboxItemSelRoomPlace(self, event):
        item_click = event.widget
        item_sel = item_click.curselection()
        if len(item_sel) > 0:  # to avoid error when other listbox item is selected
            item_str = item_click.get(item_sel[0])
            item_str_split = item_str.split(" | ")
            file_name = item_str_split[0]
            file_name_split = file_name.split("-")
            self.tree_view.item(file_name_split[0], open=True)
            self.tree_view.item(file_name_split[0] + "-" +
                                file_name_split[1], open=True)
            self.tree_view.item(file_name_split[0] + "-" +
                                file_name_split[1] + "-" +
                                file_name_split[2], open=True)
            self.tree_view.selection_set(file_name_split[0] + "-" +
                                         file_name_split[1] + "-" +
                                         file_name_split[2] + "-" +
                                         file_name_split[3])

            if len(file_name_split) == N_ITEMS:  # Only load pics when tipololy tree view is selected
                self.flat_pic = Image.open(PIC_PATH + file_name + PIC_EXTENSION)
                self.flat_picCopy = self.flat_pic.copy()
                self.flat_picCopyResize = self.flat_picCopy.resize((WIDTH_FLATPIC, HEIGHT_FLATPIC), Image.ANTIALIAS)
                self.flat_picTk = ImageTk.PhotoImage(image=self.flat_picCopyResize)
                self.label_flat.configure(image=self.flat_picTk)
                tipology = file_name_split[3]
                tipology_split = tipology.split("_", 1)
                if (len(tipology_split) > 1):  # to avoid the LC1 case
                    if re.search(r"\+", file_name) != None:
                        # check for this tipology construction: 3MF_0D.A_DA+3MF_2D.A1_DA
                        tip_room = re.findall(r"[0-9]+D", file_name)
                        tip_room_add = str(int(tip_room[0][:1]) + int(tip_room[1][:1]))
                        n_rooms = tip_room_add
                    else:  # check for this tipology construction: 3MF_1D.B
                        n_rooms = tipology_split[1][:1]  # save only the integer related with the n_rooms
                    self.tb_room.configure(text=n_rooms + " DORMITORIO/S")
                    coordinates = searchLocation(file_name_split[0], file_name)
                    self.tb_place.configure(text=" | " + coordinates)
                    #print(coordinates)
                else:  # LC1 case selected
                    coordinates = searchLocation(file_name_split[0], file_name)
                    self.tb_place.configure(text=" | " + coordinates)
                    #print(coordinates)

    # Method executed when a item in lb_room is selected
    def listboxItemSelRoom(self, event):
        item_click = event.widget
        item_sel = item_click.curselection()
        #item_str = item_click.get(item_sel[0])
        if len(item_sel) > 0: # to avoid error when other listbox item is selected
            item_search = str(item_sel[0]+1) + "D"
            # check room coincidences
            lb_roomplace_add = []
            for i in range(len(self.file_names)):  # num max. of rows
                for j in range(len(self.file_names[0])):  # num max of cols
                    if re.search(r"\+", self.file_names[i][j]) != None:
                        # check for this tipology construction: 3MF_0D.A_DA+3MF_2D.A1_DA
                        tip_room = re.findall(r"[0-9]+D", self.file_names[i][j])
                        tip_room_add = str(int(tip_room[0][:1]) + int(tip_room[1][:1])) + "D"
                        if tip_room_add == item_search:
                            lb_roomplace_add.append(self.file_names[i][j] + " | " +
                                                    self.file_places[i][j])

                    else:
                        # check for this tipology construction: 3MF_1D.B
                        if re.search(item_search, self.file_names[i][j]) != None:
                            lb_roomplace_add.append(self.file_names[i][j] + " | " +
                                                    self.file_places[i][j])

            # Adding rooms and coordinates to lb_roomplace
            self.lb_roomplace.delete(0, END)  # delete listbox items before add new ones.
            for i in range(len(lb_roomplace_add)):
                self.lb_roomplace.insert(i, lb_roomplace_add[i])

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
                if re.search(r"\+", tree_item) != None:
                    # check for this tipology construction: 3MF_0D.A_DA+3MF_2D.A1_DA
                    tip_room = re.findall(r"[0-9]+D", tree_item)
                    tip_room_add = str(int(tip_room[0][:1]) + int(tip_room[1][:1]))
                    n_rooms = tip_room_add
                else: # check for this tipology construction: 3MF_1D.B
                    n_rooms = tipology_split[1][:1] #save only the integer related with the n_rooms
                self.tb_room.configure(text=n_rooms + " DORMITORIO/S")
                coordinates = searchLocation(tree_item_split[0], tree_item)
                self.tb_place.configure(text=" | " + coordinates)
                #print(coordinates)
            else: # LC1 case selected
                coordinates = searchLocation(tree_item_split[0], tree_item)
                self.tb_place.configure(text=" | " + coordinates)
                #print(coordinates)

App()