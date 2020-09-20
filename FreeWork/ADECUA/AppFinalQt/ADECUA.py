# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ADECUA.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ADECUA_lib import *
from ClientNew import *
from ClientManage import *
from tinydb import TinyDB, Query
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 797)
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
        #self.tree_widget = QtWidgets.QTreeWidget(self.splitter_2)
        self.tree_widget = TreeWidget(self.splitter_2)
        self.tree_widget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.tree_widget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tree_widget.setUniformRowHeights(True)
        self.tree_widget.setAnimated(False)
        self.tree_widget.setObjectName("tree_widget")
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
        self.menuClient = QtWidgets.QMenu(self.menubar)
        self.menuClient.setObjectName("menuClient")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.file_open = QtWidgets.QAction(MainWindow)
        self.file_open.setObjectName("file_open")
        self.file_quit = QtWidgets.QAction(MainWindow)
        self.file_quit.setObjectName("file_quit")
        self.client_new = QtWidgets.QAction(MainWindow)
        self.client_new.setObjectName("client_new")
        self.client_manage = QtWidgets.QAction(MainWindow)
        self.client_manage.setObjectName("client_manage")
        self.menuFile.addAction(self.file_open)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.file_quit)
        self.menuClient.addAction(self.client_new)
        self.menuClient.addAction(self.client_manage)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuClient.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADECUA"))
        self.lb_room.setSortingEnabled(True)
        self.lb_roomplace.setSortingEnabled(True)
        self.menuFile.setTitle(_translate("MainWindow", "Archivo"))
        self.menuClient.setTitle(_translate("MainWindow", "Cliente"))
        self.file_open.setText(_translate("MainWindow", "Abrir"))
        self.file_quit.setText(_translate("MainWindow", "Salir"))
        self.client_new.setText(_translate("MainWindow", "Nuevo"))
        self.client_manage.setText(_translate("MainWindow", "Gestionar"))             
        

        # load default GUI settings
        self.excelFileName = "./database.xlsx"
        self.qtwidget_struct, self.qtwidget_profile, self.qtwidget_floor, self.qtwidget_type, \
        self.tree_struct, self.tree_profile, self.tree_floor, self.tree_type, self.tree_picname = \
        defGuiConfig(self.tb_room, self.flat_pic, self.tree_widget, self.lb_room, self.excelFileName)
        MainWindow.statusBar().showMessage(" Se han cargado " +  str(len(self.tree_picname)) + " viviendas")
        MainWindow.setWindowIcon(QtGui.QIcon(PIC_PATH+WIN_TITLE+PIC_EXTENSION))               

        # mouse click connect functions         
        self.tree_widget.right_click.connect(self.AdecuaTreeItemRightMenu)
        self.tree_widget.itemClicked.connect(self.AdecuaTreeItemSel)
        self.tree_widget.itemExpanded.connect(self.AdecuaTreeItemSel)        
        self.lb_room.clicked.connect(self.AdecuaListRoomSel)
        self.lb_roomplace.clicked.connect(self.AdecuaListRoomPlaceSel)
        self.file_open.triggered.connect(self.AdecuaMenuArhiveOpen)
        self.file_quit.triggered.connect(self.AdecuaMenuArhiveQuit)
        self.client_new.triggered.connect(self.AdecuaMenuClientNew)             
        self.client_manage.triggered.connect(self.AdecuaMenuClientManage)             

        # create database
        self.db_ADECUA = TinyDB("ADECUA_DB.json")           

    #-- Menu methods --#
    
    def AdecuaMenuClientNew(self):
        self.windowClientNew=QtWidgets.QMainWindow()
        self.ui=Ui_ClientNew(self.db_ADECUA, self.windowClientNew)        
        self.ui.setup(self.windowClientNew)
        self.windowClientNew.show()        

    def AdecuaMenuClientManage(self):        
        self.windowClientManage=QtWidgets.QMainWindow()
        self.ui=Ui_ClientManage(self.db_ADECUA, self.windowClientManage, MainWindow)
        self.ui.setup(self.windowClientManage)
        self.windowClientManage.show()
    
    def AdecuaMenuArhiveOpen(self):
        # Open excel file
        dialog = QtWidgets.QFileDialog()
        dialog.setWindowTitle("Abrir fichero")        
        dialog.setNameFilter('Excel files (*.xlsx)')
        dialog.setDirectory(QtCore.QDir.currentPath())
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.excelFileName = str(dialog.selectedFiles()[0])
        else:
            return None       

        # clean all listbox and tree view
        self.tree_widget.clear()  
        self.lb_room.clear()
        self.lb_roomplace.clear()
        
        # load new items into treeview
        self.qtwidget_struct, self.qtwidget_profile, self.qtwidget_floor, self.qtwidget_type, \
        self.tree_struct, self.tree_profile, self.tree_floor, self.tree_type, self.tree_picname = \
        defGuiConfig(self.tb_room, self.flat_pic, self.tree_widget, self.lb_room, self.excelFileName)
        MainWindow.statusBar().showMessage(" Se han cargado " +  str(len(self.tree_picname)) + " viviendas")        

    def AdecuaMenuArhiveQuit(self):
        sys.exit()        

    #-- Widget methods --#
    
    def AdecuaTreeItemRightMenu(self): 
    # when righ click is over tree item...                
        item_sel = self.tree_widget.selectedItems()
        if item_sel:                                      
            # check if user makes right click over the right tree item
            mouse_pos = False
            for i in range(len(self.qtwidget_type)):
                if self.qtwidget_type[i] == item_sel[0]:                    
                    flat_sel_temp = self.tree_picname[i]
                    mouse_pos = True

            # only launch the action when the user makes click over the right item.            
            if mouse_pos == True:
                # read statusbar string
                statusBarText = self.statusbar.currentMessage()
                # filtering the string to get the doc_id of the data base                
                statusBarText_split = statusBarText.split('[')                
                #db_id = statusBarText_split[1][:-1]
                # execute code only if a client is selected.
                if len(statusBarText_split) > 1:                    
                    item_sel = self.tree_widget.selectedItems()        

                    # Getting info from the selected item
                    print(flat_sel_temp)
                    flat_sel_temp_split = flat_sel_temp.split("-", 1)
                    location, n_room = givemeNroomLocation(flat_sel_temp_split[0], flat_sel_temp, self.excelFileName)
                    print(location)
                    print(n_room)
                    #

                    if self.tree_widget.action == self.tree_widget.favAction:                        
                        print ("Favorito")                        
                    elif self.tree_widget.action == self.tree_widget.bookAction:
                        print ("Reserva")
                    elif self.tree_widget.action == self.tree_widget.buyAction:
                        print ("Compra")  
                else:    
                    popupWarningWindow("Error en la seleccion de cliente");                 
                                           
            # if the user does not make click over the right item...
            else:  
                popupWarningWindow("Seleccion incorrecta")
    
    def AdecuaTreeItemSel(self):
    # when one item is selected...
        item_sel = self.tree_widget.selectedItems()
        #print(item_sel)
        if item_sel:
            #item_sel_txt = item_sel[0].text(0)
            #print(item_sel_txt)
            #print(item_sel[0])
            treeViewLoadImageAndLocation(item_sel, self.flat_pic, self.tb_room,\
                                         self.qtwidget_type, self.tree_picname,\
                                         self.excelFileName)
        
        # to set horizontal scrollbar on tree widget
        self.tree_widget.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tree_widget.header().setStretchLastSection(False)


    def AdecuaListRoomSel(self):
    # when one item is selected...
        #item_sel = str(self.lb_room.currentRow() + 1) + "D"
        #print(item_sel)
        item_sel = self.lb_room.selectedItems()
        item = item_sel[0].text()
        lbRoomPlaceAddItems(item, self.lb_roomplace, self.excelFileName)

    def AdecuaListRoomPlaceSel(self):
    # when one item is selected...
        item_sel = str(self.lb_roomplace.currentItem().text())
        #print(item_sel)
        expandTreeItem(self.tree_struct, self.tree_profile, self.tree_floor, self.tree_type,\
                       self.qtwidget_struct, self.qtwidget_profile, self.qtwidget_floor,\
                       self.qtwidget_type, self.tree_widget, item_sel)
        self.AdecuaTreeItemSel()

# Class to handle right click button action over tree widget
class TreeWidget(QtWidgets.QTreeWidget):          
    # Handling mouse clicks on treeview
    right_click = QtCore.pyqtSignal()               

    def mousePressEvent(self, event):
        super(TreeWidget, self).mousePressEvent(event)                    
        if event.button() == QtCore.Qt.RightButton:            
            menu = QtWidgets.QMenu()
            self.favAction = menu.addAction("Añadir a favoritos") 
            self.bookAction = menu.addAction("Reservar")   
            self.buyAction = menu.addAction("Comprar")   
            self.action = menu.exec_(event.globalPos())          
            self.right_click.emit()

if __name__ == "__main__":
    #import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)     
    MainWindow.show()
    sys.exit(app.exec_())
