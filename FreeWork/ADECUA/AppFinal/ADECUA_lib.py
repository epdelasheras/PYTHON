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

# Tree items
WS_ROW_START = 5
NAMESTRUCTURE = "Estructura "
NAMEPROFILE = "Perfil "
NAMEFLOOR = "Planta "

# Floor pic areas
BLK1_X1 = 40
BLK1_X2 = 125
BLK1_Y1 = 115
BLK1_Y2 = 135

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
	lst_ws = []
	for sheet in wb:
		lst_ws.append(sheet.title)

	for n_sheet in range(len(lst_ws)):

		# saving a copy in memory of the currente excel worksheet to process
		ws = wb[lst_ws[n_sheet]]

		# read all ws rows and create a list with all the ws file names.
		lst_fname = []
		for i in range(WS_ROW_START, ws.max_row + 1):
			if (ws["K" + str(i)].value != None):  # skip empty rows
				lst_fname.append(str(ws["K" + str(i)].value)) # list with file names

		# Split every file name string to do an analysis later
		lst_split = []
		for i in range(len(lst_fname)):
			lst_split.append(lst_fname[i].split("-", 3)) # detect max. two of this "-" in the string

		# create a list with every element of every lst_split item
		lst_struct_prof = []
		lst_struct_prof_floor = []
		for i in range(len(lst_split)):
			str_split = lst_split[i]
			lst_struct_prof.append(str_split[0] + "-" + str_split[1])
			lst_struct_prof_floor.append(str_split[0] + "-" + str_split[1]
									 + "-" + str_split[2])

		# Adding structures to the treeview
		Treeview.insert("", END, text=NAMESTRUCTURE + lst_ws[n_sheet],
						iid=lst_ws[n_sheet], tags=("mytag",))

		# Adding profiles to the treeview
		lst_struct_prof_sort = list(set(lst_struct_prof))
		lst_struct_prof_sort.sort()
		for i in range(len(lst_struct_prof_sort)):
			profile = lst_struct_prof_sort[i]
			profile_split = profile.split("-")
			Treeview.insert(profile_split[0], END, text=NAMEPROFILE + profile_split[1],
					iid=profile, tags=("mytag",))

		# Adding floors to the treeview
		lst_struct_prof_floor_sort = list(set(lst_struct_prof_floor))
		lst_struct_prof_floor_sort.sort()
		for i in range(len(lst_struct_prof_floor_sort)):
			floor = lst_struct_prof_floor_sort[i]
			floor_split = floor.split("-")
			Treeview.insert(floor_split[0] + "-" + floor_split[1], END,
						text=NAMEFLOOR + floor_split[2], iid=floor,
						tags=("mytag",))

		# Adding types to the treeview
		for i in range(len(lst_fname)):
			type = lst_fname[i]
			type_split = type.split("-")
			print(type)
			print(type_split)
			Treeview.insert(type_split[0] + "-" + type_split[1] + "-" + type_split[2],
						END, text=type_split[3], iid=type, tags=("mytag",))