from tkinter import *
import cv2
from PIL import Image, ImageTk
import openpyxl

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

AREA_ID = ["A", "B", "C", "ALL"]
# "A" => "1DVar1", "1DVar2", "1DVar3"
# "B" => "2DVar1", "2DVar2", "2DVar3"
# "C" => "3DVar1", "3DVar2", "3DVar3"
# "ALL" => "1DVar1", "1DVar2", "1DVar3", "2DVar1", "2DVar2", "2DVar3","3DVar1", "3DVar2", "3DVar3"

# Next matrix is to build the listbox and treeview according to the floor area selected
# [column, row]

def addItemsListbox(list_box, area_id):
    # Adding elements to the listbox
	if area_id == AREA_ID[0]:  # 1-bedroom
		list_box.insert(0, "1DVar1")
		list_box.insert(1, "1DVar2")
		list_box.insert(2, "1DVar3")
		return
	elif area_id == AREA_ID[1]:  # 2-bedroom
		list_box.insert(3, "2DVar1")
		list_box.insert(4, "2DVar2")
		list_box.insert(5, "2DVar3")
	else:  # 3-beedroom
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
def areaId(label_floor_x, label_floor_y):
	if (label_floor_x > BLK1_X1 and label_floor_x < BLK1_X2 and label_floor_y > BLK1_Y1 and label_floor_y < BLK1_Y2):
		return AREA_ID[0]

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

def addItemsTreeview(Treeview):
    # adding elements to the tree. The previous tree label is indicated
    # to have an event response

	wb = openpyxl.load_workbook("./database.xlsx", data_only=True)  # data_only=True to read the cell data instead of the formula
	# read all ws and create a list
	lst_blk = []
	for sheet in wb:
		lst_blk.append(sheet.title)

	# Add blocks to the treeview.
	for i in range(len(lst_blk)):
		Treeview.insert("", END, text="Bloque " + str(i + 1), iid=lst_blk[i], tags=("mytag",))

	# Add
	for sheet in range(len(lst_blk)):
		ws = wb[lst_blk[sheet]]
		# Adding floors to the treeview
		lst_floor = []
		for i in range(2, ws.max_row+1):
			lst_floor.append(str(ws["A"+str(i)].value))
		lst_floor_mod = list(set(lst_floor))  # remove duplicate items
		lst_floor_mod.sort()  # sort list items
		for i in range(len(lst_floor_mod)):
			Treeview.insert(lst_blk[sheet], END, text="Planta " + str(i),
							iid=lst_blk[sheet] + lst_floor_mod[i], tags=("mytag",))

		# Adding rooms to the treeview
		lst_cnt_floor = []
		for i in range(len(lst_floor_mod)):
			cnt_floor = 0
			for j in range(len(lst_floor)):
				if lst_floor_mod[i] == lst_floor[j]:
					cnt_floor += 1
			lst_cnt_floor.append(cnt_floor)

		print(lst_cnt_floor)
		for i in range(len(lst_cnt_floor)):
			lst_room = []
			for j in range(lst_cnt_floor[i]):
				lst_room.append(str(ws["B" + str(j+2)].value))
			lst_room_mod = list(set(lst_room))  # remove duplicate items
			lst_room_mod.sort()  # sort list items
			print(lst_room)
			print(lst_room_mod)
			for i in range(len(lst_floor_mod)):




'''
	# Create Block tree items
	list_blk = []
	for i in range(2, ws.max_row): # read the block column and skiip the first row
		list_blk.append(str(ws["A"+str(i)].value))
	list_blk_mod = list(set(list_blk)) #remove duplicate items
	list_blk_mod.sort() # sort list items
	for i in range(len(list_blk_mod)): #fill tree view with items
		Treeview.insert("", END, text="Bloque "+str(i+1), iid=list_blk_mod[i], tags=("mytag",))

	# Create Floor tree items
	list_floor = []
	for i in range(2, ws.max_row): # read the block column and skiip the first row
		list_floor.append(str(ws["B"+str(i)].value))
	for i in range(len(list_blk_mod)): # fill tree view with items
		for j in range(len(list_blk)):
			if list_blk_mod[i] == list_blk[j]:
				list_floor_mod = list(set(list_floor))  # create list with items for every block

		list_floor_mod.sort()  # sort list items
		for k in range(len(list_floor_mod)):
			Treeview.insert(list_blk_mod[i], END, text="Planta " + str(i),
							iid=list_blk_mod[i] + list_floor_mod[k], tags=("mytag",))
							
	# Create room tree items
	list_room = []
	for i in range(2, ws.max_row): # read the block column and skiip the first row
		list_room.append(str(ws["C"+str(i)].value))
	list_room_mod = list(set(list_room)) #remove duplicate items
	list_room_mod.sort() # sort list items
	for k in range(len(list_blk_mod)): #fill tree view with items
		for j in range(len(list_floor_mod)):
			for i in range(len(list_room_mod)):
				Treeview.insert(list_blk_mod[k]+list_floor_mod[j], END, text=str(i)+" habitacion/es ",
							    iid=list_blk_mod[k]+list_floor_mod[j]+list_room_mod[i],
							    tags=("mytag",))

	# Create variants tree items
	list_var = []
	for i in range(2, ws.max_row): # read the block column and skiip the first row
		list_var.append(str(ws["D"+str(i)].value))
	list_var_mod = list(set(list_var)) #remove duplicate items
	list_var_mod.sort() # sort list items
	for l in range(len(list_blk_mod)): #fill tree view with items
		for k in range(len(list_floor_mod)):
			for j in range(len(list_room_mod)):
				for i in range(len(list_var_mod)):
					Treeview.insert(list_blk_mod[l]+list_floor_mod[k]+list_room_mod[j], END, text="var "+str(i),
									iid=list_blk_mod[l]+list_floor_mod[k]+list_room_mod[j]+list_var_mod[i],
								    tags=("mytag",))
'''