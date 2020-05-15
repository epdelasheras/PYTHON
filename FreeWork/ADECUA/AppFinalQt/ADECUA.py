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

        # load default image in flat_pic label
        load_pic = QtGui.QPixmap(PIC_PATH + "Diseño Base y Variante 1_2.jpg")
        load_pic = load_pic.scaled(WIDTH_FLATPIC, HEIGHT_FLATPIC,
                             #QtCore.Qt.KeepAspectRatioByExpanding,
                             #QtCore.Qt.KeepAspectRatio,
                             QtCore.Qt.IgnoreAspectRatio,
                             QtCore.Qt.SmoothTransformation)
        self.flat_pic.setPixmap(load_pic)

        # Add tree items
        #self.tree_view.expandToDepth(0)
        #self.tree_view.setCurrentItem(adios)
        self.file_names, self.file_places, self.file_tipo = addItemsTreeview(self.tree_view)
        self.tree_view.itemClicked.connect(self.TreeItemSel)
        self.tree_view.itemExpanded.connect(self.TreeItemSel)
        self.tree_view_selitems = []

        #Add number of rooms to choose to the listbox
        self.n_room = addItemsListboxRoom(self.lb_room, self.file_names)
        self.lb_room.clicked.connect(self.ListRoomSel)

    def TreeItemSel(self):
    # when one item is selected...
        item_sel = self.tree_view.selectedItems()
        if item_sel:
            item_sel_txt = item_sel[0].text(0)
            print(item_sel[0])
            #print(item_sel_txt)
            wb_temp = openpyxl.load_workbook("./temp.xlsx", data_only=True)  # data_only=True to read the cell data instead of the formula
            ws_temp = wb_temp.active
            for i in range(1, ws_temp.max_row + 1):
                if ws_temp["B"+str(i+1)].value == str(item_sel[0]):
                    print(ws_temp["B" + str(i + 1)].value)
                    picname = ws_temp["A"+str(i+1)].value
                    print(picname)
                    print(PIC_PATH + picname + ".jpg")
                    load_pic = QtGui.QPixmap(PIC_PATH + picname + ".jpg")
                    load_pic = load_pic.scaled(WIDTH_FLATPIC, HEIGHT_FLATPIC,
                                               # QtCore.Qt.KeepAspectRatioByExpanding,
                                               # QtCore.Qt.KeepAspectRatio,
                                               QtCore.Qt.IgnoreAspectRatio,
                                               QtCore.Qt.SmoothTransformation)
                    self.flat_pic.setPixmap(load_pic)

    def ListRoomSel(self):
    # when one item is selected...
        item_search = str(self.lb_room.currentRow() + 1) + "D"
        print(item_search)
        addItemsListboxRoomPlace(self.lb_roomplace, self.file_names,
                                 self.file_places, item_search)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())