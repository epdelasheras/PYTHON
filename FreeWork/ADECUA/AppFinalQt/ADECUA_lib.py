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

def searchLocation(worksheet, tree_item):
    # It is used in "loadPic" method to search the coordinates of the flat.

    wb = openpyxl.load_workbook("./database.xlsx", data_only=True)  # data_only=True to read the cell data instead of the formula
    ws = wb[worksheet]
    for i in range(WS_ROW_START, ws.max_row + 1):
        if (ws["K" + str(i)].value == tree_item):
            return ws["H" + str(i)].value

def addItemsTreeview(Treeview):
    # adding elements to the tree. The previous tree label is indicated
    # to have an event response

    wb = openpyxl.load_workbook("./database.xlsx", data_only=True)  # data_only=True to read the cell data instead of the formula
    # read all ws and create a list
    lst_ws = []
    for sheet in wb:
        lst_ws.append(sheet.title)

    # tuples to return at the end of the method
    ws_fname = []
    ws_fplace = []
    ws_ftipo = []

    #Create main Treeview column
    Treeview.setColumnCount(1)
    Treeview.setHeaderLabel("ARBOL DE SELECCIÓN")

    # Create temporañ workbook excel file to do relation between
    # pictures file names and treewidget items
    wb_temp = openpyxl.Workbook()

    ws_temp = wb_temp.active
    ws_temp.title = "picnames"
    ws_temp_cnt = int(1)

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

        # Adding profiles to the structures
        lst_struct_prof_sort = list(set(lst_struct_prof))
        lst_struct_prof_sort.sort()
        lst_struct_prof_floor_sort = list(set(lst_struct_prof_floor))
        lst_struct_prof_floor_sort.sort()
        for i in range(len(lst_struct_prof_sort)):
            profile = lst_struct_prof_sort[i]
            profile_split = profile.split("-")
            tree_profile = Qt.QTreeWidgetItem(tree_struct, [NAMEPROFILE + profile_split[1]])
            for j in range(len(lst_struct_prof_floor_sort)):
                floor = lst_struct_prof_floor_sort[j]
                floor_split = floor.split("-")
                if re.fullmatch(profile_split[1], floor_split[1]) != None:
                    tree_floors = Qt.QTreeWidgetItem(tree_profile, [NAMEFLOOR + floor_split[2]])
                    for k in range(len(lst_struct_prof_floor)):
                        type = lst_fname[k]
                        type_split = type.split("-")
                        if re.fullmatch(floor, lst_struct_prof_floor[k]) != None:
                            tree_type = Qt.QTreeWidgetItem(tree_floors, [type_split[3]])
                            ws_temp["A" + str(ws_temp_cnt)] = type
                            ws_temp["B"+str(ws_temp_cnt)] = str(tree_type)
                            ws_temp_cnt += 1

        wb_temp.save(filename="temp.xlsx")

        # Create a list with all the filenames to be used in other parts of the program
        ws_fname.append(lst_fname)

        # Create a list with all the coordinates to be used in other parts of the program
        ws_fplace.append(lst_fplace)

        # Create a list with all the tipologies to be used in other parts of the program
        ws_ftipo.append(lst_ftipo)

    return ws_fname, ws_fplace, ws_ftipo

def addItemsListboxRoom(Listbox, file_names):
    # Adding items to the listbox

    # Figure out which is the max. number of rooms in the database
    n_room = []
    for i in range(len(file_names)): #num max. of rows
        for j in range(len(file_names[i])): #num max of cols
            if len(re.findall(r"[0-9]+D", file_names[i][j])) > 0: #skip flat with no rooms
                tipology_room = re.findall(r"[0-9]+D", file_names[i][j])
                if len(tipology_room) > 1:
                    # check for this tipology construction: 3MF_0D.A_DA+3MF_2D.A1_DA
                    room_add = str(int(tipology_room[0][:1]) + int(tipology_room[1][:1])) + "D"
                    n_room.append(room_add)
                else:
                    # check for this tipology construction: 3MF_1D.B
                    n_room.append(tipology_room[0])

    # removing duplicated items of the listbox
    n_room = list(set(n_room))
    n_room.sort()

    # Adding rooms to the listbox
    for i in range(len(n_room)):
        Listbox.insertItem(i, str(i+1) + " Dormitorio/s")

    return n_room

def addItemsListboxRoomPlace(Listbox, file_names, file_places, item):
    # Add tipologies and coordinates to lb_roomplace
    Listbox_add = []
    for i in range(len(file_names)):  # num max. of rows
        for j in range(len(file_names[i])):  # num max of cols
            if re.search(r"\+", file_names[i][j]) != None:
                # check for this tipology construction: 3MF_0D.A_DA+3MF_2D.A1_DA
                tip_room = re.findall(r"[0-9]+D", file_names[i][j])
                tip_room_add = str(int(tip_room[0][:1]) + int(tip_room[1][:1])) + "D"
                if tip_room_add == item:
                    Listbox_add.append(file_names[i][j] + " | " + file_places[i][j])

            else:
                # check for this tipology construction: 3MF_1D.B
                if re.search(item, file_names[i][j]) != None:
                    Listbox_add.append(file_names[i][j] + " | " + file_places[i][j])

                    # Adding rooms and coordinates to Listbox
    Listbox.clear()  # delete listbox items before add new ones.
    for i in range(len(Listbox_add)):
        Listbox.insertItem(i, Listbox_add[i])