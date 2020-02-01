from tkinter import *

# root window
WIN_SIZE = "800x600"
WIN_TITLE = "ADECUA"
WIN_ICO_PATH = ".\pics\ADECUA.ico"

# Treeview + Listbox
TL_BLK_IID = ["blk1", "blk2", "blk3"]
TL_FLOOR_IID = ["blk1_floor_0", "blk1_floor_1", "blk1_floor_2", "blk1_floor_3",
                "blk2_floor_0", "blk2_floor_1", "blk2_floor_2", "blk2_floor_3",
                "blk3_floor_0", "blk3_floor_1", "blk3_floor_2", "blk3_floor_3"
               ]
TL_FLAT_IID = ["blk1_floor0_flat_1r", "blk1_floor0_flat_2r", "blk1_floor0_flat_3r",
               "blk1_floor1_flat_1r", "blk1_floor1_flat_2r", "blk1_floor1_flat_3r",
               "blk1_floor2_flat_1r", "blk1_floor2_flat_2r", "blk1_floor2_flat_3r",
               "blk1_floor3_flat_1r", "blk1_floor3_flat_2r", "blk1_floor3_flat_3r",

               "blk2_floor0_flat_1r", "blk2_floor0_flat_2r", "blk2_floor0_flat_3r",
               "blk2_floor1_flat_1r", "blk2_floor1_flat_2r", "blk2_floor1_flat_3r",
               "blk2_floor2_flat_1r", "blk2_floor2_flat_2r", "blk2_floor2_flat_3r",
               "blk2_floor3_flat_1r", "blk2_floor3_flat_2r", "blk2_floor3_flat_3r",

               "blk3_floor0_flat_1r", "blk3_floor0_flat_2r", "blk3_floor0_flat_3r",
               "blk3_floor1_flat_1r", "blk3_floor1_flat_2r", "blk3_floor1_flat_3r",
               "blk3_floor2_flat_1r", "blk3_floor2_flat_2r", "blk3_floor2_flat_3r",
               "blk3_floor3_flat_1r", "blk3_floor3_flat_2r", "blk3_floor3_flat_3r",
               ]
TL_FLAT_VAR_IID = ["blk1_floor0_flat1r_1DVar1", "blk1_floor0_flat1r_1DVar2", "blk1_floor0_flat1r_1DVar3",
                   "blk1_floor1_flat1r_1DVar1", "blk1_floor1_flat1r_1DVar2", "blk1_floor1_flat1r_1DVar3",
                   "blk1_floor2_flat1r_1DVar1", "blk1_floor2_flat1r_1DVar2", "blk1_floor2_flat1r_1DVar3",
                   "blk1_floor3_flat1r_1DVar1", "blk1_floor3_flat1r_1DVar2", "blk1_floor3_flat1r_1DVar3",
			       "blk1_floor0_flat2r_1DVar1", "blk1_floor0_flat2r_1DVar2", "blk1_floor0_flat2r_1DVar3",
                   "blk1_floor1_flat2r_1DVar1", "blk1_floor1_flat2r_1DVar2", "blk1_floor1_flat2r_1DVar3",
                   "blk1_floor2_flat2r_1DVar1", "blk1_floor2_flat2r_1DVar2", "blk1_floor2_flat2r_1DVar3",
                   "blk1_floor3_flat2r_1DVar1", "blk1_floor3_flat2r_1DVar2", "blk1_floor3_flat2r_1DVar3",
		  	       "blk1_floor0_flat3r_1DVar1", "blk1_floor0_flat3r_1DVar2", "blk1_floor0_flat3r_1DVar3",
                   "blk1_floor1_flat3r_1DVar1", "blk1_floor1_flat3r_1DVar2", "blk1_floor1_flat3r_1DVar3",
                   "blk1_floor2_flat3r_1DVar1", "blk1_floor2_flat3r_1DVar2", "blk1_floor2_flat3r_1DVar3",
                   "blk1_floor3_flat3r_1DVar1", "blk1_floor3_flat3r_1DVar2", "blk1_floor3_flat3r_1DVar3",
                   "blk2_floor0_flat1r_1DVar1", "blk2_floor0_flat1r_1DVar2", "blk2_floor0_flat1r_1DVar3",
                   "blk2_floor1_flat1r_1DVar1", "blk2_floor1_flat1r_1DVar2", "blk2_floor1_flat1r_1DVar3",
                   "blk2_floor2_flat1r_1DVar1", "blk2_floor2_flat1r_1DVar2", "blk2_floor2_flat1r_1DVar3",
                   "blk2_floor3_flat1r_1DVar1", "blk2_floor3_flat1r_1DVar2", "blk2_floor3_flat1r_1DVar3",
			       "blk2_floor0_flat2r_1DVar1", "blk2_floor0_flat2r_1DVar2", "blk2_floor0_flat2r_1DVar3",
                   "blk2_floor1_flat2r_1DVar1", "blk2_floor1_flat2r_1DVar2", "blk2_floor1_flat2r_1DVar3",
                   "blk2_floor2_flat2r_1DVar1", "blk2_floor2_flat2r_1DVar2", "blk2_floor2_flat2r_1DVar3",
                   "blk2_floor3_flat2r_1DVar1", "blk2_floor3_flat2r_1DVar2", "blk2_floor3_flat2r_1DVar3",
			       "blk2_floor0_flat3r_1DVar1", "blk2_floor0_flat3r_1DVar2", "blk2_floor0_flat3r_1DVar3",
                   "blk2_floor1_flat3r_1DVar1", "blk2_floor1_flat3r_1DVar2", "blk2_floor1_flat3r_1DVar3",
                   "blk2_floor2_flat3r_1DVar1", "blk2_floor2_flat3r_1DVar2", "blk2_floor2_flat3r_1DVar3",
                   "blk2_floor3_flat3r_1DVar1", "blk2_floor3_flat3r_1DVar2", "blk2_floor3_flat3r_1DVar3",
                   "blk3_floor0_flat1r_1DVar1", "blk3_floor0_flat1r_1DVar2", "blk3_floor0_flat1r_1DVar3",
                   "blk3_floor1_flat1r_1DVar1", "blk3_floor1_flat1r_1DVar2", "blk3_floor1_flat1r_1DVar3",
                   "blk3_floor2_flat1r_1DVar1", "blk3_floor2_flat1r_1DVar2", "blk3_floor2_flat1r_1DVar3",
                   "blk3_floor3_flat1r_1DVar1", "blk3_floor3_flat1r_1DVar2", "blk3_floor3_flat1r_1DVar3",
			       "blk3_floor0_flat2r_1DVar1", "blk3_floor0_flat2r_1DVar2", "blk3_floor0_flat2r_1DVar3",
                   "blk3_floor1_flat2r_1DVar1", "blk3_floor1_flat2r_1DVar2", "blk3_floor1_flat2r_1DVar3",
                   "blk3_floor2_flat2r_1DVar1", "blk3_floor2_flat2r_1DVar2", "blk3_floor2_flat2r_1DVar3",
                   "blk3_floor3_flat2r_1DVar1", "blk3_floor3_flat2r_1DVar2", "blk3_floor3_flat2r_1DVar3",
			       "blk3_floor0_flat3r_1DVar1", "blk3_floor0_flat3r_1DVar2", "blk3_floor0_flat3r_1DVar3",
                   "blk3_floor1_flat3r_1DVar1", "blk3_floor1_flat3r_1DVar2", "blk3_floor1_flat3r_1DVar3",
                   "blk3_floor2_flat3r_1DVar1", "blk3_floor2_flat3r_1DVar2", "blk3_floor2_flat3r_1DVar3",
                   "blk3_floor3_flat3r_1DVar1", "blk3_floor3_flat3r_1DVar2", "blk3_floor3_flat3r_1DVar3",

				   "blk1_floor0_flat1r_2DVar1", "blk1_floor0_flat1r_2DVar2", "blk1_floor0_flat1r_2DVar3",
                   "blk1_floor1_flat1r_2DVar1", "blk1_floor1_flat1r_2DVar2", "blk1_floor1_flat1r_2DVar3",
                   "blk1_floor2_flat1r_2DVar1", "blk1_floor2_flat1r_2DVar2", "blk1_floor2_flat1r_2DVar3",
                   "blk1_floor3_flat1r_2DVar1", "blk1_floor3_flat1r_2DVar2", "blk1_floor3_flat1r_2DVar3",
			       "blk1_floor0_flat2r_2DVar1", "blk1_floor0_flat2r_2DVar2", "blk1_floor0_flat2r_2DVar3",
                   "blk1_floor1_flat2r_2DVar1", "blk1_floor1_flat2r_2DVar2", "blk1_floor1_flat2r_2DVar3",
                   "blk1_floor2_flat2r_2DVar1", "blk1_floor2_flat2r_2DVar2", "blk1_floor2_flat2r_2DVar3",
                   "blk1_floor3_flat2r_2DVar1", "blk1_floor3_flat2r_2DVar2", "blk1_floor3_flat2r_2DVar3",
		  	       "blk1_floor0_flat3r_2DVar1", "blk1_floor0_flat3r_2DVar2", "blk1_floor0_flat3r_2DVar3",
                   "blk1_floor1_flat3r_2DVar1", "blk1_floor1_flat3r_2DVar2", "blk1_floor1_flat3r_2DVar3",
                   "blk1_floor2_flat3r_2DVar1", "blk1_floor2_flat3r_2DVar2", "blk1_floor2_flat3r_2DVar3",
                   "blk1_floor3_flat3r_2DVar1", "blk1_floor3_flat3r_2DVar2", "blk1_floor3_flat3r_2DVar3",
                   "blk2_floor0_flat1r_2DVar1", "blk2_floor0_flat1r_2DVar2", "blk2_floor0_flat1r_2DVar3",
                   "blk2_floor1_flat1r_2DVar1", "blk2_floor1_flat1r_2DVar2", "blk2_floor1_flat1r_2DVar3",
                   "blk2_floor2_flat1r_2DVar1", "blk2_floor2_flat1r_2DVar2", "blk2_floor2_flat1r_2DVar3",
                   "blk2_floor3_flat1r_2DVar1", "blk2_floor3_flat1r_2DVar2", "blk2_floor3_flat1r_2DVar3",
			       "blk2_floor0_flat2r_2DVar1", "blk2_floor0_flat2r_2DVar2", "blk2_floor0_flat2r_2DVar3",
                   "blk2_floor1_flat2r_2DVar1", "blk2_floor1_flat2r_2DVar2", "blk2_floor1_flat2r_2DVar3",
                   "blk2_floor2_flat2r_2DVar1", "blk2_floor2_flat2r_2DVar2", "blk2_floor2_flat2r_2DVar3",
                   "blk2_floor3_flat2r_2DVar1", "blk2_floor3_flat2r_2DVar2", "blk2_floor3_flat2r_2DVar3",
			       "blk2_floor0_flat3r_2DVar1", "blk2_floor0_flat3r_2DVar2", "blk2_floor0_flat3r_2DVar3",
                   "blk2_floor1_flat3r_2DVar1", "blk2_floor1_flat3r_2DVar2", "blk2_floor1_flat3r_2DVar3",
                   "blk2_floor2_flat3r_2DVar1", "blk2_floor2_flat3r_2DVar2", "blk2_floor2_flat3r_2DVar3",
                   "blk2_floor3_flat3r_2DVar1", "blk2_floor3_flat3r_2DVar2", "blk2_floor3_flat3r_2DVar3",
                   "blk3_floor0_flat1r_2DVar1", "blk3_floor0_flat1r_2DVar2", "blk3_floor0_flat1r_2DVar3",
                   "blk3_floor1_flat1r_2DVar1", "blk3_floor1_flat1r_2DVar2", "blk3_floor1_flat1r_2DVar3",
                   "blk3_floor2_flat1r_2DVar1", "blk3_floor2_flat1r_2DVar2", "blk3_floor2_flat1r_2DVar3",
                   "blk3_floor3_flat1r_2DVar1", "blk3_floor3_flat1r_2DVar2", "blk3_floor3_flat1r_2DVar3",
			       "blk3_floor0_flat2r_2DVar1", "blk3_floor0_flat2r_2DVar2", "blk3_floor0_flat2r_2DVar3",
                   "blk3_floor1_flat2r_2DVar1", "blk3_floor1_flat2r_2DVar2", "blk3_floor1_flat2r_2DVar3",
                   "blk3_floor2_flat2r_2DVar1", "blk3_floor2_flat2r_2DVar2", "blk3_floor2_flat2r_2DVar3",
                   "blk3_floor3_flat2r_2DVar1", "blk3_floor3_flat2r_2DVar2", "blk3_floor3_flat2r_2DVar3",
			       "blk3_floor0_flat3r_2DVar1", "blk3_floor0_flat3r_2DVar2", "blk3_floor0_flat3r_2DVar3",
                   "blk3_floor1_flat3r_2DVar1", "blk3_floor1_flat3r_2DVar2", "blk3_floor1_flat3r_2DVar3",
                   "blk3_floor2_flat3r_2DVar1", "blk3_floor2_flat3r_2DVar2", "blk3_floor2_flat3r_2DVar3",
                   "blk3_floor3_flat3r_2DVar1", "blk3_floor3_flat3r_2DVar2", "blk3_floor3_flat3r_2DVar3",

				   "blk1_floor0_flat1r_3DVar1", "blk1_floor0_flat1r_3DVar2", "blk1_floor0_flat1r_3DVar3",
                   "blk1_floor1_flat1r_3DVar1", "blk1_floor1_flat1r_3DVar2", "blk1_floor1_flat1r_3DVar3",
                   "blk1_floor2_flat1r_3DVar1", "blk1_floor2_flat1r_3DVar2", "blk1_floor2_flat1r_3DVar3",
                   "blk1_floor3_flat1r_3DVar1", "blk1_floor3_flat1r_3DVar2", "blk1_floor3_flat1r_3DVar3",
			       "blk1_floor0_flat2r_3DVar1", "blk1_floor0_flat2r_3DVar2", "blk1_floor0_flat2r_3DVar3",
                   "blk1_floor1_flat2r_3DVar1", "blk1_floor1_flat2r_3DVar2", "blk1_floor1_flat2r_3DVar3",
                   "blk1_floor2_flat2r_3DVar1", "blk1_floor2_flat2r_3DVar2", "blk1_floor2_flat2r_3DVar3",
                   "blk1_floor3_flat2r_3DVar1", "blk1_floor3_flat2r_3DVar2", "blk1_floor3_flat2r_3DVar3",
		  	       "blk1_floor0_flat3r_3DVar1", "blk1_floor0_flat3r_3DVar2", "blk1_floor0_flat3r_3DVar3",
                   "blk1_floor1_flat3r_3DVar1", "blk1_floor1_flat3r_3DVar2", "blk1_floor1_flat3r_3DVar3",
                   "blk1_floor2_flat3r_3DVar1", "blk1_floor2_flat3r_3DVar2", "blk1_floor2_flat3r_3DVar3",
                   "blk1_floor3_flat3r_3DVar1", "blk1_floor3_flat3r_3DVar2", "blk1_floor3_flat3r_3DVar3",
                   "blk2_floor0_flat1r_3DVar1", "blk2_floor0_flat1r_3DVar2", "blk2_floor0_flat1r_3DVar3",
                   "blk2_floor1_flat1r_3DVar1", "blk2_floor1_flat1r_3DVar2", "blk2_floor1_flat1r_3DVar3",
                   "blk2_floor2_flat1r_3DVar1", "blk2_floor2_flat1r_3DVar2", "blk2_floor2_flat1r_3DVar3",
                   "blk2_floor3_flat1r_3DVar1", "blk2_floor3_flat1r_3DVar2", "blk2_floor3_flat1r_3DVar3",
			       "blk2_floor0_flat2r_3DVar1", "blk2_floor0_flat2r_3DVar2", "blk2_floor0_flat2r_3DVar3",
                   "blk2_floor1_flat2r_3DVar1", "blk2_floor1_flat2r_3DVar2", "blk2_floor1_flat2r_3DVar3",
                   "blk2_floor2_flat2r_3DVar1", "blk2_floor2_flat2r_3DVar2", "blk2_floor2_flat2r_3DVar3",
                   "blk2_floor3_flat2r_3DVar1", "blk2_floor3_flat2r_3DVar2", "blk2_floor3_flat2r_3DVar3",
			       "blk2_floor0_flat3r_3DVar1", "blk2_floor0_flat3r_3DVar2", "blk2_floor0_flat3r_3DVar3",
                   "blk2_floor1_flat3r_3DVar1", "blk2_floor1_flat3r_3DVar2", "blk2_floor1_flat3r_3DVar3",
                   "blk2_floor2_flat3r_3DVar1", "blk2_floor2_flat3r_3DVar2", "blk2_floor2_flat3r_3DVar3",
                   "blk2_floor3_flat3r_3DVar1", "blk2_floor3_flat3r_3DVar2", "blk2_floor3_flat3r_3DVar3",
                   "blk3_floor0_flat1r_3DVar1", "blk3_floor0_flat1r_3DVar2", "blk3_floor0_flat1r_3DVar3",
                   "blk3_floor1_flat1r_3DVar1", "blk3_floor1_flat1r_3DVar2", "blk3_floor1_flat1r_3DVar3",
                   "blk3_floor2_flat1r_3DVar1", "blk3_floor2_flat1r_3DVar2", "blk3_floor2_flat1r_3DVar3",
                   "blk3_floor3_flat1r_3DVar1", "blk3_floor3_flat1r_3DVar2", "blk3_floor3_flat1r_3DVar3",
			       "blk3_floor0_flat2r_3DVar1", "blk3_floor0_flat2r_3DVar2", "blk3_floor0_flat2r_3DVar3",
                   "blk3_floor1_flat2r_3DVar1", "blk3_floor1_flat2r_3DVar2", "blk3_floor1_flat2r_3DVar3",
                   "blk3_floor2_flat2r_3DVar1", "blk3_floor2_flat2r_3DVar2", "blk3_floor2_flat2r_3DVar3",
                   "blk3_floor3_flat2r_3DVar1", "blk3_floor3_flat2r_3DVar2", "blk3_floor3_flat2r_3DVar3",
			       "blk3_floor0_flat3r_3DVar1", "blk3_floor0_flat3r_3DVar2", "blk3_floor0_flat3r_3DVar3",
                   "blk3_floor1_flat3r_3DVar1", "blk3_floor1_flat3r_3DVar2", "blk3_floor1_flat3r_3DVar3",
                   "blk3_floor2_flat3r_3DVar1", "blk3_floor2_flat3r_3DVar2", "blk3_floor2_flat3r_3DVar3",
                   "blk3_floor3_flat3r_3DVar1", "blk3_floor3_flat3r_3DVar2", "blk3_floor3_flat3r_3DVar3"]

TL_BLOCK = ["Bloque 1", "Bloque 2", "Bloque 3"]
TL_FLOOR = ["Planta Baja", "Planta 1ª", "Planta 2ª", "Planta 3ª"]
TL_FLAT = ["1 Dormitorio", "2 Dormitorios", "3 Dormitorios"]
TL_FLAT_VAR = ["1DVar1", "1DVar2", "1DVar3",
                "2DVar1", "2DVar2", "2DVar3",
                "3DVar1", "3DVar2", "3DVar3"]

def addItemsTreeview(Treeview):
    # adding elements to the tree. The previous tree label is indicated
    # to have an event response

    #*************BLOCK1****************
    for i in range(len(TL_BLOCK)):
        Treeview.insert("", END, text=TL_BLOCK[i], iid=TL_BLK_IID[i], tags=("mytag",))
    # Floors
    k = 0
    for i in range(len(TL_BLOCK)):
        for j in range(len(TL_FLOOR)):
            #print("i={}, j={}, k={}".format(i, j, k))
            Treeview.insert(TL_BLK_IID[i], END, text=TL_FLOOR[j], iid=TL_FLOOR_IID[k], tags=("mytag",))
            k += 1
    # Rooms
    k = 0
    for i in range(len(TL_FLOOR_IID)):
        for j in range(len(TL_FLAT)):
            #print("i={}, j={}, k={}".format(i, j, k))
            Treeview.insert(TL_FLOOR_IID[i], END, text=TL_FLAT[j], iid=TL_FLAT_IID[k], tags=("mytag",))
            k += 1

    # Roms variants
    k = 0
    print(len(TL_FLAT_VAR_IID))
    for i in range(len(TL_FLAT_IID)):
        for j in range(len(TL_FLAT_VAR)):
            print("i={}, j={}, k={}".format(i, j, k))
            Treeview.insert(TL_FLAT_IID[i], END, text=TL_FLAT_VAR[j], iid=TL_FLAT_VAR_IID[k], tags=("mytag",))
            k += 1

def addItemsListbox(ListBox):

    ListBox.insert(0, "1DVar1")
    ListBox.insert(1, "1DVar1")
    ListBox.insert(2, "1DVar1")
