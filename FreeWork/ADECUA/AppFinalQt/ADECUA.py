# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ADECUA.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ADECUA_lib import *
import openpyxl

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Create and configure the "MainWindow"
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(MAINWIN_WIDTH, MAINWIN_HEIGHT)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        #grid layout for the central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # horizontal layout for all MainWindow widgets
        self.layout_hsplitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layout_hsplitter.sizePolicy().hasHeightForWidth())
        self.layout_hsplitter.setSizePolicy(sizePolicy)
        self.layout_hsplitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.layout_hsplitter.setAutoFillBackground(False)
        self.layout_hsplitter.setOrientation(QtCore.Qt.Horizontal)
        self.layout_hsplitter.setObjectName("layout_hsplitter")

        # create tree view
        self.tree_view = QtWidgets.QTreeWidget(self.layout_hsplitter)
        self.tree_view.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_view.sizePolicy().hasHeightForWidth())
        self.tree_view.setSizePolicy(sizePolicy)
        self.tree_view.setMinimumSize(QtCore.QSize(0, 0))
        self.tree_view.setMaximumSize(QtCore.QSize(200, 16777215))
        self.tree_view.setBaseSize(QtCore.QSize(0, 0))
        self.tree_view.setObjectName("tree_view")

        # vertical layout for some widgets
        self.layout_vsplitter = QtWidgets.QSplitter(self.layout_hsplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layout_vsplitter.sizePolicy().hasHeightForWidth())
        self.layout_vsplitter.setSizePolicy(sizePolicy)
        self.layout_vsplitter.setOrientation(QtCore.Qt.Vertical)
        self.layout_vsplitter.setObjectName("layout_vsplitter")

        # create tb_room label        
        self.tb_room = QtWidgets.QLabel(self.layout_vsplitter)
        self.tb_room.setMaximumSize(QtCore.QSize(280, 100))
        self.tb_room.setObjectName("tb_room")

        # create lb_room widget
        self.lb_room = QtWidgets.QListWidget(self.layout_vsplitter)
        self.lb_room.setMaximumSize(QtCore.QSize(280, 100))
        self.lb_room.setObjectName("lb_room")

        # create lb_roomplace widget
        self.lb_roomplace = QtWidgets.QListWidget(self.layout_vsplitter)
        self.lb_roomplace.setMaximumSize(QtCore.QSize(280, 16777215))
        self.lb_roomplace.setObjectName("lb_roomplace")

        # create flat_pic widget
        self.flat_pic = QtWidgets.QLabel(self.layout_hsplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flat_pic.sizePolicy().hasHeightForWidth())
        self.flat_pic.setSizePolicy(sizePolicy)
        self.flat_pic.setObjectName("flat_pic")
        self.gridLayout.addWidget(self.layout_hsplitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        # create top menu MainWindow
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.file_open = QtWidgets.QAction(MainWindow)
        self.file_open.setObjectName("file_open")
        self.file_quit = QtWidgets.QAction(MainWindow)
        self.file_quit.setObjectName("file_quit")
        self.menuFile.addAction(self.file_open)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.file_quit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        #Set widgets titles
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", WIN_TITLE))
        self.tb_room.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "Archivo"))
        self.file_open.setText(_translate("MainWindow", "Abrir"))
        self.file_quit.setText(_translate("MainWindow", "Salir"))

        # Customization of the label which shows Nroom and coodinates
        self.tb_room.setStyleSheet(" font-size: 14px; qproperty-alignment: AlignCenter; "
                                   "border: 1px solid black; ")
        self.tb_room.setText("Coordenadas|NºHabitaciones")

        # load default image in flat_pic label
        load_pic = QtGui.QPixmap(PIC_PATH + "Diseño Base y Variante 1_2.jpg")
        load_pic = load_pic.scaled(WIDTH_FLATPIC, HEIGHT_FLATPIC,
                             QtCore.Qt.IgnoreAspectRatio,
                             QtCore.Qt.SmoothTransformation)
        self.flat_pic.setPixmap(load_pic)

        # Add tree items and connect tree_view with mouse click
        self.tree_widget_items = addItemsTreeview(self.tree_view)
        self.tree_view.itemClicked.connect(self.TreeItemSel)
        self.tree_view.itemExpanded.connect(self.TreeItemSel)
        self.tree_view_selitems = []

        # Add number of rooms to choose to the listbox and connect lb_room with mouse click
        lbRoomAddItems(self.lb_room)
        self.lb_room.clicked.connect(self.ListRoomSel)

        # Connect lb_roomplace with mouse click
        self.lb_roomplace.clicked.connect(self.ListRoomPlaceSel)

    def TreeItemSel(self):
    # when one item is selected...
        item_sel = self.tree_view.selectedItems()
        print(item_sel)
        if item_sel:
            #item_sel_txt = item_sel[0].text(0)
            #print(item_sel_txt)
            print(item_sel[0])
            treeViewLoadImageAndLocation(item_sel, self.flat_pic, self.tb_room)

    def ListRoomSel(self):
    # when one item is selected...
        item_sel = str(self.lb_room.currentRow() + 1) + "D"
        #print(item_sel)
        lbRoomPlaceAddItems(item_sel, self.lb_roomplace)

    def ListRoomPlaceSel(self):
    # when one item is selected...
        item_sel = str(self.lb_roomplace.currentItem().text())
        print(item_sel)
        lbRoomPlaceLoadImageAndLocation(item_sel, self.flat_pic, self.tb_room)

        wb_temp = openpyxl.load_workbook("./temp.xlsx", data_only=True)  # data_only=True to read the cell data instead of the formula
        ws_temp = wb_temp.active
        for i in range(1, ws_temp.max_row + 1):
            if ws_temp["A" + str(i)].value == item_sel:
                treeitem = ws_temp["B" + str(i)].value
                print(treeitem)

        for i in range(len(self.tree_widget_items)):
            if treeitem == str(self.tree_widget_items[i]):
                print(self.tree_widget_items[i])
                self.tree_view.setItemExpanded(self.tree_widget_items[i], True)
        #self.tree_view.setCurrentItem(item_sel)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())