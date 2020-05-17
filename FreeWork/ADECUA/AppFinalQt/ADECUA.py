# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ADECUA.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ADECUA_lib import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.tree_widget = QtWidgets.QTreeWidget(self.splitter_2)
        self.tree_widget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.tree_widget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tree_widget.setUniformRowHeights(True)
        self.tree_widget.setAnimated(False)
        self.tree_widget.setObjectName("treeWidget")
        self.tree_widget.headerItem().setText(0, "1")
        self.flat_pic = QtWidgets.QLabel(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flat_pic.sizePolicy().hasHeightForWidth())
        self.flat_pic.setSizePolicy(sizePolicy)
        self.flat_pic.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.flat_pic.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.flat_pic.setFrameShape(QtWidgets.QFrame.Box)
        self.flat_pic.setText("")
        self.flat_pic.setScaledContents(True)
        self.flat_pic.setAlignment(QtCore.Qt.AlignCenter)
        self.flat_pic.setObjectName("flat_pic")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tb_room = QtWidgets.QLabel(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_room.sizePolicy().hasHeightForWidth())
        self.tb_room.setSizePolicy(sizePolicy)
        self.tb_room.setMaximumSize(QtCore.QSize(280, 100))
        self.tb_room.setFrameShape(QtWidgets.QFrame.Box)
        self.tb_room.setText("")
        self.tb_room.setObjectName("tb_room")
        self.lb_room = QtWidgets.QListWidget(self.splitter)
        self.lb_room.setMaximumSize(QtCore.QSize(280, 100))
        self.lb_room.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.lb_room.setResizeMode(QtWidgets.QListView.Adjust)
        self.lb_room.setItemAlignment(QtCore.Qt.AlignLeading)
        self.lb_room.setObjectName("lb_room")
        self.lb_roomplace = QtWidgets.QListWidget(self.splitter)
        self.lb_roomplace.setMaximumSize(QtCore.QSize(280, 16777215))
        self.lb_roomplace.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.lb_roomplace.setResizeMode(QtWidgets.QListView.Adjust)
        self.lb_roomplace.setItemAlignment(QtCore.Qt.AlignLeading)
        self.lb_roomplace.setObjectName("lb_roomplace")
        self.horizontalLayout.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
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
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADECUA"))
        self.lb_room.setSortingEnabled(True)
        self.lb_roomplace.setSortingEnabled(True)
        self.menuFile.setTitle(_translate("MainWindow", "Archivo"))
        self.file_open.setText(_translate("MainWindow", "Abrir"))
        self.file_quit.setText(_translate("MainWindow", "Salir"))

        # load default GUI settings
        self.qtwidget_struct, self.qtwidget_profile, self.qtwidget_floor, self.qtwidget_type, \
        self.tree_struct, self.tree_profile, self.tree_floor, self.tree_type, self.tree_picname = \
        defGuiConfig(self.tb_room, self.flat_pic, self.tree_widget, self.lb_room)

        # mouse click connect functions
        self.tree_widget.itemClicked.connect(self.TreeItemSel)
        self.tree_widget.itemExpanded.connect(self.TreeItemSel)
        self.lb_room.clicked.connect(self.ListRoomSel)
        self.lb_roomplace.clicked.connect(self.ListRoomPlaceSel)
        self.file_open.triggered.connect(self.MenuArhiveOpen)
        self.file_quit.triggered.connect(self.MenuArhiveQuit)

    def MenuArhiveOpen(self):
        dialog = QtWidgets.QMessageBox()
        dialog.setIcon(QtWidgets.QMessageBox.Warning)
        dialog.setText("Esta opción aun no esta implementada")
        dialog.addButton(QtWidgets.QMessageBox.Ok)
        dialog.exec()

    def MenuArhiveQuit(self):
        self.close

    def TreeItemSel(self):
    # when one item is selected...
        item_sel = self.tree_widget.selectedItems()
        #print(item_sel)
        if item_sel:
            #item_sel_txt = item_sel[0].text(0)
            #print(item_sel_txt)
            #print(item_sel[0])
            treeViewLoadImageAndLocation(item_sel, self.flat_pic, self.tb_room,\
                                         self.qtwidget_type, self.tree_picname)

    def ListRoomSel(self):
    # when one item is selected...
        #item_sel = str(self.lb_room.currentRow() + 1) + "D"
        #print(item_sel)
        item_sel = self.lb_room.selectedItems()
        item = item_sel[0].text()
        lbRoomPlaceAddItems(item, self.lb_roomplace)

    def ListRoomPlaceSel(self):
    # when one item is selected...
        item_sel = str(self.lb_roomplace.currentItem().text())
        #print(item_sel)
        expandTreeItem(self.tree_struct, self.tree_profile, self.tree_floor, self.tree_type,\
                       self.qtwidget_struct, self.qtwidget_profile, self.qtwidget_floor,\
                       self.qtwidget_type, self.tree_widget, item_sel)

        self.TreeItemSel()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
