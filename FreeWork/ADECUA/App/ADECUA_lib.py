from tkinter import *
import cv2
from PIL import Image, ImageTk

# root window attributes
WIN_SIZE = "1366x768"
WIN_TITLE = "ADECUA"
WIN_ICO_PATH = ".\pics\ADECUA.ico"

# Pic sizes
WIDTH_FLATPIC = 700
HEIGHT_FLATPIC = 500
WIDTH_FLOORPIC = 380
HEIGHT_FLOORPIC = 380

# Floor pic areas
BLK1_X1 = 40
BLK1_X2 = 125
BLK1_Y1 = 115
BLK1_Y2 = 135

# Floor Area ids
AREA3 = "1DVar"


# Treeview + Listbox
TL_BLK_IID = ["blk1", "blk2", "blk3"]
TL_FLOOR_IID = ["blk1_floor0", "blk1_floor1", "blk1_floor2", "blk1_floor3",
                "blk2_floor0", "blk2_floor1", "blk2_floor2", "blk2_floor3",
                "blk3_floor0", "blk3_floor1", "blk3_floor2", "blk3_floor3"
               ]
TL_FLAT_IID = ["blk1_floor0_flat1r", "blk1_floor0_flat2r", "blk1_floor0_flat3r",
               "blk1_floor1_flat1r", "blk1_floor1_flat2r", "blk1_floor1_flat3r",
               "blk1_floor2_flat1r", "blk1_floor2_flat2r", "blk1_floor2_flat3r",
               "blk1_floor3_flat1r", "blk1_floor3_flat2r", "blk1_floor3_flat3r",

               "blk2_floor0_flat1r", "blk2_floor0_flat2r", "blk2_floor0_flat3r",
               "blk2_floor1_flat1r", "blk2_floor1_flat2r", "blk2_floor1_flat3r",
               "blk2_floor2_flat1r", "blk2_floor2_flat2r", "blk2_floor2_flat3r",
               "blk2_floor3_flat1r", "blk2_floor3_flat2r", "blk2_floor3_flat3r",

               "blk3_floor0_flat1r", "blk3_floor0_flat2r", "blk3_floor0_flat3r",
               "blk3_floor1_flat1r", "blk3_floor1_flat2r", "blk3_floor1_flat3r",
               "blk3_floor2_flat1r", "blk3_floor2_flat2r", "blk3_floor2_flat3r",
               "blk3_floor3_flat1r", "blk3_floor3_flat2r", "blk3_floor3_flat3r",
               ]

TL_FLAT_VAR_IID = ["blk1_floor0_flat1r_1DVar1", "blk1_floor0_flat1r_1DVar2", "blk1_floor0_flat1r_1DVar3",
				   "blk1_floor0_flat1r_2DVar1", "blk1_floor0_flat1r_2DVar2", "blk1_floor0_flat1r_2DVar3",
				   "blk1_floor0_flat1r_3DVar1", "blk1_floor0_flat1r_3DVar2", "blk1_floor0_flat1r_3DVar3",
				   "blk1_floor0_flat2r_1DVar1", "blk1_floor0_flat2r_1DVar2", "blk1_floor0_flat2r_1DVar3",
				   "blk1_floor0_flat2r_2DVar1", "blk1_floor0_flat2r_2DVar2", "blk1_floor0_flat2r_2DVar3",
				   "blk1_floor0_flat2r_3DVar1", "blk1_floor0_flat2r_3DVar2", "blk1_floor0_flat2r_3DVar3",
				   "blk1_floor0_flat3r_1DVar1", "blk1_floor0_flat3r_1DVar2", "blk1_floor0_flat3r_1DVar3",
				   "blk1_floor0_flat3r_2DVar1", "blk1_floor0_flat3r_2DVar2", "blk1_floor0_flat3r_2DVar3",
				   "blk1_floor0_flat3r_3DVar1", "blk1_floor0_flat3r_3DVar2", "blk1_floor0_flat3r_3DVar3",
				   "blk1_floor1_flat1r_1DVar1", "blk1_floor1_flat1r_1DVar2", "blk1_floor1_flat1r_1DVar3",
				   "blk1_floor1_flat1r_2DVar1", "blk1_floor1_flat1r_2DVar2", "blk1_floor1_flat1r_2DVar3",
				   "blk1_floor1_flat1r_3DVar1", "blk1_floor1_flat1r_3DVar2", "blk1_floor1_flat1r_3DVar3",
				   "blk1_floor1_flat2r_1DVar1", "blk1_floor1_flat2r_1DVar2", "blk1_floor1_flat2r_1DVar3",
				   "blk1_floor1_flat2r_2DVar1", "blk1_floor1_flat2r_2DVar2", "blk1_floor1_flat2r_2DVar3",
				   "blk1_floor1_flat2r_3DVar1", "blk1_floor1_flat2r_3DVar2", "blk1_floor1_flat2r_3DVar3",
				   "blk1_floor1_flat3r_1DVar1", "blk1_floor1_flat3r_1DVar2", "blk1_floor1_flat3r_1DVar3",
				   "blk1_floor1_flat3r_2DVar1", "blk1_floor1_flat3r_2DVar2", "blk1_floor1_flat3r_2DVar3",
				   "blk1_floor1_flat3r_3DVar1", "blk1_floor1_flat3r_3DVar2", "blk1_floor1_flat3r_3DVar3",
				   "blk1_floor2_flat1r_1DVar1", "blk1_floor2_flat1r_1DVar2", "blk1_floor2_flat1r_1DVar3",
				   "blk1_floor2_flat1r_2DVar1", "blk1_floor2_flat1r_2DVar2", "blk1_floor2_flat1r_2DVar3",
				   "blk1_floor2_flat1r_3DVar1", "blk1_floor2_flat1r_3DVar2", "blk1_floor2_flat1r_3DVar3",
				   "blk1_floor2_flat2r_1DVar1", "blk1_floor2_flat2r_1DVar2", "blk1_floor2_flat2r_1DVar3",
				   "blk1_floor2_flat2r_2DVar1", "blk1_floor2_flat2r_2DVar2", "blk1_floor2_flat2r_2DVar3",
				   "blk1_floor2_flat2r_3DVar1", "blk1_floor2_flat2r_3DVar2", "blk1_floor2_flat2r_3DVar3",
				   "blk1_floor2_flat3r_1DVar1", "blk1_floor2_flat3r_1DVar2", "blk1_floor2_flat3r_1DVar3",
				   "blk1_floor2_flat3r_2DVar1", "blk1_floor2_flat3r_2DVar2", "blk1_floor2_flat3r_2DVar3",
				   "blk1_floor2_flat3r_3DVar1", "blk1_floor2_flat3r_3DVar2", "blk1_floor2_flat3r_3DVar3",
				   "blk1_floor3_flat1r_1DVar1", "blk1_floor3_flat1r_1DVar2", "blk1_floor3_flat1r_1DVar3",
				   "blk1_floor3_flat1r_2DVar1", "blk1_floor3_flat1r_2DVar2", "blk1_floor3_flat1r_2DVar3",
				   "blk1_floor3_flat1r_3DVar1", "blk1_floor3_flat1r_3DVar2", "blk1_floor3_flat1r_3DVar3",
				   "blk1_floor3_flat2r_1DVar1", "blk1_floor3_flat2r_1DVar2", "blk1_floor3_flat2r_1DVar3",
				   "blk1_floor3_flat2r_2DVar1", "blk1_floor3_flat2r_2DVar2", "blk1_floor3_flat2r_2DVar3",
				   "blk1_floor3_flat2r_3DVar1", "blk1_floor3_flat2r_3DVar2", "blk1_floor3_flat2r_3DVar3",
				   "blk1_floor3_flat3r_1DVar1", "blk1_floor3_flat3r_1DVar2", "blk1_floor3_flat3r_1DVar3",
				   "blk1_floor3_flat3r_2DVar1", "blk1_floor3_flat3r_2DVar2", "blk1_floor3_flat3r_2DVar3",
				   "blk1_floor3_flat3r_3DVar1", "blk1_floor3_flat3r_3DVar2", "blk1_floor3_flat3r_3DVar3",

				   "blk2_floor0_flat1r_1DVar1", "blk2_floor0_flat1r_1DVar2", "blk2_floor0_flat1r_1DVar3",
				   "blk2_floor0_flat1r_2DVar1", "blk2_floor0_flat1r_2DVar2", "blk2_floor0_flat1r_2DVar3",
				   "blk2_floor0_flat1r_3DVar1", "blk2_floor0_flat1r_3DVar2", "blk2_floor0_flat1r_3DVar3",
				   "blk2_floor0_flat2r_1DVar1", "blk2_floor0_flat2r_1DVar2", "blk2_floor0_flat2r_1DVar3",
				   "blk2_floor0_flat2r_2DVar1", "blk2_floor0_flat2r_2DVar2", "blk2_floor0_flat2r_2DVar3",
				   "blk2_floor0_flat2r_3DVar1", "blk2_floor0_flat2r_3DVar2", "blk2_floor0_flat2r_3DVar3",
				   "blk2_floor0_flat3r_1DVar1", "blk2_floor0_flat3r_1DVar2", "blk2_floor0_flat3r_1DVar3",
				   "blk2_floor0_flat3r_2DVar1", "blk2_floor0_flat3r_2DVar2", "blk2_floor0_flat3r_2DVar3",
				   "blk2_floor0_flat3r_3DVar1", "blk2_floor0_flat3r_3DVar2", "blk2_floor0_flat3r_3DVar3",
				   "blk2_floor1_flat1r_1DVar1", "blk2_floor1_flat1r_1DVar2", "blk2_floor1_flat1r_1DVar3",
				   "blk2_floor1_flat1r_2DVar1", "blk2_floor1_flat1r_2DVar2", "blk2_floor1_flat1r_2DVar3",
				   "blk2_floor1_flat1r_3DVar1", "blk2_floor1_flat1r_3DVar2", "blk2_floor1_flat1r_3DVar3",
				   "blk2_floor1_flat2r_1DVar1", "blk2_floor1_flat2r_1DVar2", "blk2_floor1_flat2r_1DVar3",
				   "blk2_floor1_flat2r_2DVar1", "blk2_floor1_flat2r_2DVar2", "blk2_floor1_flat2r_2DVar3",
				   "blk2_floor1_flat2r_3DVar1", "blk2_floor1_flat2r_3DVar2", "blk2_floor1_flat2r_3DVar3",
				   "blk2_floor1_flat3r_1DVar1", "blk2_floor1_flat3r_1DVar2", "blk2_floor1_flat3r_1DVar3",
				   "blk2_floor1_flat3r_2DVar1", "blk2_floor1_flat3r_2DVar2", "blk2_floor1_flat3r_2DVar3",
				   "blk2_floor1_flat3r_3DVar1", "blk2_floor1_flat3r_3DVar2", "blk2_floor1_flat3r_3DVar3",
				   "blk2_floor2_flat1r_1DVar1", "blk2_floor2_flat1r_1DVar2", "blk2_floor2_flat1r_1DVar3",
				   "blk2_floor2_flat1r_2DVar1", "blk2_floor2_flat1r_2DVar2", "blk2_floor2_flat1r_2DVar3",
				   "blk2_floor2_flat1r_3DVar1", "blk2_floor2_flat1r_3DVar2", "blk2_floor2_flat1r_3DVar3",
				   "blk2_floor2_flat2r_1DVar1", "blk2_floor2_flat2r_1DVar2", "blk2_floor2_flat2r_1DVar3",
				   "blk2_floor2_flat2r_2DVar1", "blk2_floor2_flat2r_2DVar2", "blk2_floor2_flat2r_2DVar3",
				   "blk2_floor2_flat2r_3DVar1", "blk2_floor2_flat2r_3DVar2", "blk2_floor2_flat2r_3DVar3",
				   "blk2_floor2_flat3r_1DVar1", "blk2_floor2_flat3r_1DVar2", "blk2_floor2_flat3r_1DVar3",
				   "blk2_floor2_flat3r_2DVar1", "blk2_floor2_flat3r_2DVar2", "blk2_floor2_flat3r_2DVar3",
				   "blk2_floor2_flat3r_3DVar1", "blk2_floor2_flat3r_3DVar2", "blk2_floor2_flat3r_3DVar3",
				   "blk2_floor3_flat1r_1DVar1", "blk2_floor3_flat1r_1DVar2", "blk2_floor3_flat1r_1DVar3",
				   "blk2_floor3_flat1r_2DVar1", "blk2_floor3_flat1r_2DVar2", "blk2_floor3_flat1r_2DVar3",
				   "blk2_floor3_flat1r_3DVar1", "blk2_floor3_flat1r_3DVar2", "blk2_floor3_flat1r_3DVar3",
				   "blk2_floor3_flat2r_1DVar1", "blk2_floor3_flat2r_1DVar2", "blk2_floor3_flat2r_1DVar3",
				   "blk2_floor3_flat2r_2DVar1", "blk2_floor3_flat2r_2DVar2", "blk2_floor3_flat2r_2DVar3",
				   "blk2_floor3_flat2r_3DVar1", "blk2_floor3_flat2r_3DVar2", "blk2_floor3_flat2r_3DVar3",
				   "blk2_floor3_flat3r_1DVar1", "blk2_floor3_flat3r_1DVar2", "blk2_floor3_flat3r_1DVar3",
				   "blk2_floor3_flat3r_2DVar1", "blk2_floor3_flat3r_2DVar2", "blk2_floor3_flat3r_2DVar3",
				   "blk2_floor3_flat3r_3DVar1", "blk2_floor3_flat3r_3DVar2", "blk2_floor3_flat3r_3DVar3",

				   "blk3_floor0_flat1r_1DVar1", "blk3_floor0_flat1r_1DVar2", "blk3_floor0_flat1r_1DVar3",
				   "blk3_floor0_flat1r_2DVar1", "blk3_floor0_flat1r_2DVar2", "blk3_floor0_flat1r_2DVar3",
				   "blk3_floor0_flat1r_3DVar1", "blk3_floor0_flat1r_3DVar2", "blk3_floor0_flat1r_3DVar3",
				   "blk3_floor0_flat2r_1DVar1", "blk3_floor0_flat2r_1DVar2", "blk3_floor0_flat2r_1DVar3",
				   "blk3_floor0_flat2r_2DVar1", "blk3_floor0_flat2r_2DVar2", "blk3_floor0_flat2r_2DVar3",
				   "blk3_floor0_flat2r_3DVar1", "blk3_floor0_flat2r_3DVar2", "blk3_floor0_flat2r_3DVar3",
				   "blk3_floor0_flat3r_1DVar1", "blk3_floor0_flat3r_1DVar2", "blk3_floor0_flat3r_1DVar3",
				   "blk3_floor0_flat3r_2DVar1", "blk3_floor0_flat3r_2DVar2", "blk3_floor0_flat3r_2DVar3",
				   "blk3_floor0_flat3r_3DVar1", "blk3_floor0_flat3r_3DVar2", "blk3_floor0_flat3r_3DVar3",
				   "blk3_floor1_flat1r_1DVar1", "blk3_floor1_flat1r_1DVar2", "blk3_floor1_flat1r_1DVar3",
				   "blk3_floor1_flat1r_2DVar1", "blk3_floor1_flat1r_2DVar2", "blk3_floor1_flat1r_2DVar3",
				   "blk3_floor1_flat1r_3DVar1", "blk3_floor1_flat1r_3DVar2", "blk3_floor1_flat1r_3DVar3",
				   "blk3_floor1_flat2r_1DVar1", "blk3_floor1_flat2r_1DVar2", "blk3_floor1_flat2r_1DVar3",
				   "blk3_floor1_flat2r_2DVar1", "blk3_floor1_flat2r_2DVar2", "blk3_floor1_flat2r_2DVar3",
				   "blk3_floor1_flat2r_3DVar1", "blk3_floor1_flat2r_3DVar2", "blk3_floor1_flat2r_3DVar3",
				   "blk3_floor1_flat3r_1DVar1", "blk3_floor1_flat3r_1DVar2", "blk3_floor1_flat3r_1DVar3",
				   "blk3_floor1_flat3r_2DVar1", "blk3_floor1_flat3r_2DVar2", "blk3_floor1_flat3r_2DVar3",
				   "blk3_floor1_flat3r_3DVar1", "blk3_floor1_flat3r_3DVar2", "blk3_floor1_flat3r_3DVar3",
				   "blk3_floor2_flat1r_1DVar1", "blk3_floor2_flat1r_1DVar2", "blk3_floor2_flat1r_1DVar3",
				   "blk3_floor2_flat1r_2DVar1", "blk3_floor2_flat1r_2DVar2", "blk3_floor2_flat1r_2DVar3",
				   "blk3_floor2_flat1r_3DVar1", "blk3_floor2_flat1r_3DVar2", "blk3_floor2_flat1r_3DVar3",
				   "blk3_floor2_flat2r_1DVar1", "blk3_floor2_flat2r_1DVar2", "blk3_floor2_flat2r_1DVar3",
				   "blk3_floor2_flat2r_2DVar1", "blk3_floor2_flat2r_2DVar2", "blk3_floor2_flat2r_2DVar3",
				   "blk3_floor2_flat2r_3DVar1", "blk3_floor2_flat2r_3DVar2", "blk3_floor2_flat2r_3DVar3",
				   "blk3_floor2_flat3r_1DVar1", "blk3_floor2_flat3r_1DVar2", "blk3_floor2_flat3r_1DVar3",
				   "blk3_floor2_flat3r_2DVar1", "blk3_floor2_flat3r_2DVar2", "blk3_floor2_flat3r_2DVar3",
				   "blk3_floor2_flat3r_3DVar1", "blk3_floor2_flat3r_3DVar2", "blk3_floor2_flat3r_3DVar3",
				   "blk3_floor3_flat1r_1DVar1", "blk3_floor3_flat1r_1DVar2", "blk3_floor3_flat1r_1DVar3",
				   "blk3_floor3_flat1r_2DVar1", "blk3_floor3_flat1r_2DVar2", "blk3_floor3_flat1r_2DVar3",
				   "blk3_floor3_flat1r_3DVar1", "blk3_floor3_flat1r_3DVar2", "blk3_floor3_flat1r_3DVar3",
				   "blk3_floor3_flat2r_1DVar1", "blk3_floor3_flat2r_1DVar2", "blk3_floor3_flat2r_1DVar3",
				   "blk3_floor3_flat2r_2DVar1", "blk3_floor3_flat2r_2DVar2", "blk3_floor3_flat2r_2DVar3",
				   "blk3_floor3_flat2r_3DVar1", "blk3_floor3_flat2r_3DVar2", "blk3_floor3_flat2r_3DVar3",
				   "blk3_floor3_flat3r_1DVar1", "blk3_floor3_flat3r_1DVar2", "blk3_floor3_flat3r_1DVar3",
				   "blk3_floor3_flat3r_2DVar1", "blk3_floor3_flat3r_2DVar2", "blk3_floor3_flat3r_2DVar3",
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
    #print(len(TL_FLAT_VAR_IID))
    for i in range(len(TL_FLAT_IID)):
        for j in range(len(TL_FLAT_VAR)):
            #print("i={}, j={}, k={}".format(i, j, k))
            Treeview.insert(TL_FLAT_IID[i], END, text=TL_FLAT_VAR[j], iid=TL_FLAT_VAR_IID[k], tags=("mytag",))
            k += 1

def addItemsListbox(list_box, block, floor, flat):
    # Adding elements to the listbox

    if block == TL_BLOCK[0]: # Block-1
        if floor == TL_FLOOR[0]: # Ground floor
            if flat == TL_FLAT[0]: # 1-bedroom
                list_box.insert(0, "1DVar1")
                list_box.insert(1, "1DVar2")
                list_box.insert(2, "1DVar3")
                return
            elif flat == TL_FLAT[1]: # 2-bedroom
                list_box.insert(3, "2DVar1")
                list_box.insert(4, "2DVar2")
                list_box.insert(5, "2DVar3")
            else: # 3-beedroom
                list_box.insert(6, "3DVar1")
                list_box.insert(7, "3DVar2")
                list_box.insert(8, "3DVar3")

def loadNewFlatPic(tv_iid_split):
	flat_pic = Image.open("./pics/flatviews/" + tv_iid_split[3] + ".png")
	flat_picCopy = flat_pic.copy()
	flat_pic_resize = flat_picCopy.resize((WIDTH_FLATPIC, HEIGHT_FLATPIC), Image.ANTIALIAS)
	flat_picTk = ImageTk.PhotoImage(image=flat_pic_resize)
	return flat_picTk


# to identify the area selected on the Floor pic.
def areaId(label_floor_x, label_floor_y)
	if (label_floor_x > BLK1_X1 and
		label_floor_x < BLK1_X2 and
		label_floor_y > BLK1_Y1 and
		label_floor_y < BLK1_Y2):
	return AREA3


# make a rectangle on the floor image
def highlightArea(label_floor_x, label_floor_y):
	floor_picCv2 = cv2.imread("./pics/floorviews/PlantaBaja.png") # load image in open cv format
	floor_picCv2Copy = floor_picCv2.copy() # create a copy of the previous image
    # draw a rectangle over the image
	x, y, w, h = 10, 10, 10, 10  # Rectangle parameters
	cv2.rectangle(floor_picCv2Copy, (x, y), (x + w, y + h), (0, 200, 0), -1)  # A filled rectangle
	alpha = 0.4  # Transparency factor.
	floor_picCv2Mod = cv2.addWeighted(floor_picCv2Copy, alpha, floor_picCv2, 1 - alpha, 0)  # image with the rectangle

    # OpenCV represents images in BGR order; however PIL represents
    # images in RGB order, so we need to swap the channels
	b, g, r = cv2.split(floor_picCv2Mod)
	floor_picCv2_RGB = cv2.merge((r, g, b))

	# Convert the Image object into a TkPhoto object
	floor_pic = Image.fromarray(floor_picCv2_RGB)

	floor_picCopy = floor_pic.copy()
	floor_picCopyResize = floor_picCopy.resize((WIDTH_FLOORPIC, HEIGHT_FLOORPIC), Image.ANTIALIAS)
	floor_picTk = ImageTk.PhotoImage(image=floor_picCopyResize)
	return floor_picTk



