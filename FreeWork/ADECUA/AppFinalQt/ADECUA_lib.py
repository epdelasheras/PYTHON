from tkinter import *
from typing import List

import openpyxl
from PyQt5 import QtCore, QtGui, QtWidgets, Qt

# root window attributes
MAINWIN_WIDTH = 1400
MAINWIN_HEIGHT = 800
WIN_TITLE = "ADECUA"
PIC_EXTENSION = ".jpg"
PIC_PATH = "./pics/"

# Pic sizes
WIDTH_FLATPIC = 900
HEIGHT_FLATPIC = 700
WIDTH_FLOORPIC = 380
HEIGHT_FLOORPIC = 380

# Tree items
N_ITEMS = 4 # when tipology tree view is selected, tree_view_split = 4 items
WS_ROW_START = 5
NAMESTRUCTURE = "Estructura "
NAMEPROFILE = "Perfil "
NAMEFLOOR = "Planta "


def defGuiConfig(tb_room, flat_pic, tree_widget, lb_room):

    # Customization of the label which shows Nroom and coodinates
    tb_room.setStyleSheet(" font-size: 14px; qproperty-alignment: AlignCenter; "
                               "border: 1px solid black; ")
    tb_room.setText("Coordenadas|NºHabitaciones")

    # load default image in flat_pic label
    load_pic = QtGui.QPixmap(PIC_PATH + "Diseño Base y Variante 1_2.jpg")
    load_pic = load_pic.scaled(WIDTH_FLATPIC, HEIGHT_FLATPIC,
                               QtCore.Qt.IgnoreAspectRatio,
                               QtCore.Qt.SmoothTransformation)
    flat_pic.setPixmap(load_pic)



    # Add number of rooms to choose to the listbox and connect lb_room with mouse click
    lbRoomAddItems(lb_room)

    # Add tree items and connect tree_widget with mouse click
    qtwidget_struct, qtwidget_profile, qtwidget_floor, qtwidget_type, tree_struct, tree_profile, \
    tree_floor, tree_type, tree_picname = addItemsTreeview(tree_widget)

    return qtwidget_struct, qtwidget_profile, qtwidget_floor, qtwidget_type, tree_struct, \
           tree_profile, tree_floor, tree_type, tree_picname


def givemeNroomLocation(worksheet, tree_item):
    # It is used in "loadPic" method to search the coordinates of the flat.
    wb = openpyxl.load_workbook("./database.xlsx", data_only=True)  # data_only=True to read the cell data instead of the formula
    ws = wb[worksheet]
    for i in range(WS_ROW_START, ws.max_row + 1):
        if (ws["K" + str(i)].value == tree_item):
            return ws["H" + str(i)].value, ws["I" + str(i)].value

def treeViewLoadImageAndLocation(item_sel, flat_pic, tb_room, qtwidget_type, tree_picname):
    # It is used to load images and coordinates into flat pic label and tb_room from tree_widget widget
    for i in range(len(qtwidget_type)):
        if qtwidget_type[i] == item_sel[0]:
            picname = tree_picname[i]
            load_pic = QtGui.QPixmap(PIC_PATH + picname + ".jpg")
            load_pic = load_pic.scaled(WIDTH_FLATPIC, HEIGHT_FLATPIC,
                                       QtCore.Qt.IgnoreAspectRatio,
                                       QtCore.Qt.SmoothTransformation)
            flat_pic.setPixmap(load_pic)
            picname_split = picname.split("-", 1)
            #print(picname_split)
            location, n_room = givemeNroomLocation(picname_split[0], picname)
            #print(location, n_room)
            tb_room.setText(str(location) + " | " + str(n_room) + " dormitorio/s")

def expandTreeItem(tree_struct, tree_profile, tree_floor, tree_type, qtwidget_struct, qtwidget_profile,
                   qtwidget_floor,qtwidget_type, tree_widget, item_sel):
    #It is used to expand a specific item on the tree_widget

    item_sel_split = item_sel.split("-")
    #print(item_sel_split)

    item_struct = NAMESTRUCTURE + item_sel_split[0]
    item_profile = NAMEPROFILE + item_sel_split[1]
    item_floor = NAMEFLOOR + item_sel_split[2]
    item_type = item_sel_split[3]

    #print(item_struct)
    #print(item_profile)
    #print(item_floor)

    # collapse the complete tree before expanding a new item
    tree_widget.collapseAll()

    # un-select all items
    for i in range(len(tree_type)):
        qtwidget_type[i].setSelected(False)

    # expanding every item on tree one by one
    for i in range(len(tree_struct)):
        if tree_struct[i] == item_struct:
            qtwidget_struct[i].setExpanded(True)

    for i in range(len(tree_profile)):
        if tree_profile[i] == item_profile:
            qtwidget_profile[i].setExpanded(True)

    for i in range(len(tree_floor)):
        if tree_floor[i] == item_floor:
            qtwidget_floor[i].setExpanded(True)

    for i in range(len(tree_type)):
        if tree_type[i] == item_type:
            qtwidget_type[i].setSelected(True)

def addItemsTreeview(Treeview):
    # adding elements to the tree. The previous tree label is indicated
    # to have an event response

    wb = openpyxl.load_workbook("./database.xlsx", data_only=True)  # data_only=True to read the cell data instead of the formula
    # read all ws and create a list
    lst_ws = []
    for sheet in wb:
        lst_ws.append(sheet.title)

    #Create main Treeview column
    Treeview.setColumnCount(1)
    Treeview.setHeaderLabel("ARBOL DE SELECCIÓN")
    # Create tuplas with all treewidgets
    lst_struct_widget = []
    lst_profile_widget = []
    lst_floor_widget = []
    lst_type_widget = []

    # Create tuplas with the text of all treewidgets
    lst_struct_txt = []
    lst_profile_txt = []
    lst_floor_txt = []
    lst_type_txt = []
    lst_picname = []

    # Loop to read all worsheets of the excel book
    for n_sheet in range(len(lst_ws)):

        # saving a copy in memory of the current excel worksheet to process
        ws = wb[lst_ws[n_sheet]]

        # read all ws rows and create a list with all the ws file names.
        lst_fname = []
        lst_fplace = []
        lst_ftipo = []
        for i in range(WS_ROW_START, ws.max_row + 1):
            if (ws["K" + str(i)].value != None):  # skip empty rows
                lst_fname.append(str(ws["K" + str(i)].value)) # list with file names
                lst_fplace.append(str(ws["H" + str(i)].value)) # list with coordinates
                lst_ftipo.append(str(ws["F" + str(i)].value)) # list with tiplogies

        # Split every file name string to do an analysis later
        lst_fname_split = []
        for i in range(len(lst_fname)):
            lst_fname_split.append(lst_fname[i].split("-"))

        # create a list with every element of every lst_fname_split item
        lst_struct_prof = []
        lst_struct_prof_floor = []
        for i in range(len(lst_fname_split)):
            str_split = lst_fname_split[i]
            lst_struct_prof.append(str_split[0] + "-" + str_split[1])
            lst_struct_prof_floor.append(str_split[0] + "-" + str_split[1]
                                     + "-" + str_split[2])

        # Adding structures to the treeview
        tree_struct = Qt.QTreeWidgetItem(Treeview, [NAMESTRUCTURE + lst_ws[n_sheet]])
        lst_struct_widget.append(tree_struct) # add item widget to tupla
        lst_struct_txt.append(NAMESTRUCTURE + lst_ws[n_sheet])  # add widget text to tupla

        # Adding profiles to the structures
        lst_struct_prof_sort = list(set(lst_struct_prof))
        lst_struct_prof_sort.sort()
        lst_struct_prof_floor_sort = list(set(lst_struct_prof_floor))
        lst_struct_prof_floor_sort.sort()
        for i in range(len(lst_struct_prof_sort)):
            profile = lst_struct_prof_sort[i]
            profile_split = profile.split("-")
            tree_profile = Qt.QTreeWidgetItem(tree_struct, [NAMEPROFILE + profile_split[1]])
            lst_profile_widget.append(tree_profile)  # add item widget to tupla
            lst_profile_txt.append(NAMEPROFILE + profile_split[1]) # add widget text to tupla
            for j in range(len(lst_struct_prof_floor_sort)):
                floor = lst_struct_prof_floor_sort[j]
                floor_split = floor.split("-")
                if re.fullmatch(profile_split[1], floor_split[1]) != None:
                    tree_floors = Qt.QTreeWidgetItem(tree_profile, [NAMEFLOOR + floor_split[2]])
                    lst_floor_widget.append(tree_floors)  # add item widget to tupla
                    lst_floor_txt.append(NAMEFLOOR + floor_split[2])  # add widget text to tupla
                    for k in range(len(lst_struct_prof_floor)):
                        type = lst_fname[k]
                        type_split = type.split("-")
                        if re.fullmatch(floor, lst_struct_prof_floor[k]) != None:
                            #print(type_split)
                            tree_type = Qt.QTreeWidgetItem(tree_floors, [type_split[3]])
                            lst_type_widget.append(tree_type) # add item widget to tupla
                            lst_type_txt.append(type_split[3])  # add widget text to tupla
                            lst_picname.append(type)

    return lst_struct_widget, lst_profile_widget, lst_floor_widget, lst_type_widget, \
           lst_struct_txt, lst_profile_txt, lst_floor_txt, lst_type_txt, lst_picname


def lbRoomAddItems(Listbox):
    # Adding items to the listbox

    wb = openpyxl.load_workbook("./database.xlsx", data_only=True)  # data_only=True to read the cell data instead of the formula
    # read all ws and create a list
    lst_ws = []
    for sheet in wb:
        lst_ws.append(sheet.title)

    # create list with number of rooms
    lst_nrooms = []

    # create a var to figure out if there are LCXX types in the excel file
    lc_cnt = int(0)

    # Loop to read all worsheets of the excel book
    for n_sheet in range(len(lst_ws)):
        # saving a copy in memory of the current excel worksheet to process
        ws = wb[lst_ws[n_sheet]]
        for i in range(WS_ROW_START, ws.max_row + 1):
            if re.match(r"[0-9]", str(ws["I" + str(i)].value)) != None:
                lst_nrooms.append(ws["I" + str(i)].value)
            elif str(ws["I" + str(i)].value) == "-" :
                lc_cnt += 1

    # set and sort list
    lst_nrooms_sort = list(set(lst_nrooms))
    lst_nrooms_sort.sort()

    # Adding rooms to the listbox
    for i in range(len(lst_nrooms_sort)):
        Listbox.insertItem(i, str(i+1) + " Dormitorio/s")

    # check for the LCxx types
    if lc_cnt > 0:
        Listbox.insertItem(i+1, "- Dormitorio/s")

def lbRoomPlaceAddItems(item, Listbox):
    # Add tipologies and coordinates to lb_roomplace

    wb = openpyxl.load_workbook("./database.xlsx", data_only=True)  # data_only=True to read the cell data instead of the formula
    # read all ws and create a list
    lst_ws = []
    for sheet in wb:
        lst_ws.append(sheet.title)

    Listbox.clear()  # delete listbox items before add new ones.

    # print(item[:1])

    # list to save items read from the excel file
    lst_item = []

    # Loop to read all worsheets of the excel book
    for n_sheet in range(len(lst_ws)):
        # saving a copy in memory of the current excel worksheet to process
        ws = wb[lst_ws[n_sheet]]
        for i in range(WS_ROW_START, ws.max_row + 1):
            #print(str(ws["I" + str(i)].value))
            if item[:1] == str(ws["I" + str(i)].value):
                lst_item.append(ws["K" + str(i)].value)

    # add sorting items to the listbox
    lst_item.sort()
    for i in range(len(lst_item)):
        Listbox.insertItem(i, lst_item[i])