# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClientManage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import re
from PyQt5 import QtCore, QtGui, QtWidgets
from tinydb import TinyDB, Query, where
from ClientView import *
from ADECUA_lib import *

class Ui_ClientManage(object):
    def __init__(self, db_ADECUA, db_ADECUA_TableFlatFav, db_ADECUA_TableFlatBook,
                 db_ADECUA_TableFlatBuy, windowClientManage, status_label,
                 MainWindow, tree_widget_list):
        self.ClientMngDb = db_ADECUA # copy database to a local variable. 
        self.ClientMngWin = windowClientManage #copy window var to a loca var.
        self.ClientMngAdecuaWin = MainWindow # copy Adecua mainwindow to a local var 
        self.ClientMngAdecuaStatusLabel = status_label # copy status label to a local var
        self.ClientMngAdecuaTreeWidLst = tree_widget_list # copy widget to local var
        # copy database tables to local variables
        self.ClientMngDbTableFlatFav = db_ADECUA_TableFlatFav
        self.ClientMngDbTableFlatBook = db_ADECUA_TableFlatBook
        self.ClientMngDbTableFlatBuy = db_ADECUA_TableFlatBuy

    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(482, 481)
        MainWindow.setMaximumSize(QtCore.QSize(482, 482))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LineDNI = QtWidgets.QLineEdit(self.centralwidget)
        self.LineDNI.setGeometry(QtCore.QRect(70, 20, 151, 21))
        self.LineDNI.setObjectName("LineDNI")
        self.LinePhone = QtWidgets.QLineEdit(self.centralwidget)
        self.LinePhone.setGeometry(QtCore.QRect(70, 50, 151, 21))
        self.LinePhone.setText("")
        self.LinePhone.setObjectName("LinePhone")
        self.LineEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEmail.setGeometry(QtCore.QRect(70, 80, 151, 21))
        self.LineEmail.setText("")
        self.LineEmail.setObjectName("LineEmail")
        self.ButtonSearchDNI = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSearchDNI.setGeometry(QtCore.QRect(260, 20, 141, 23))
        self.ButtonSearchDNI.setObjectName("ButtonSearchDNI")
        self.listClient = QtWidgets.QListWidget(self.centralwidget)
        self.listClient.setGeometry(QtCore.QRect(30, 150, 441, 251))
        self.listClient.setObjectName("listClient")
        self.ButtonSelect = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSelect.setGeometry(QtCore.QRect(30, 430, 101, 23))
        self.ButtonSelect.setObjectName("ButtonSelect")
        self.ButtonView = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonView.setGeometry(QtCore.QRect(140, 430, 101, 23))
        self.ButtonView.setObjectName("ButtonView")
        self.ButtonSearchPhone = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSearchPhone.setGeometry(QtCore.QRect(260, 50, 141, 23))
        self.ButtonSearchPhone.setObjectName("ButtonSearchPhone")
        self.ButtonSearchEmail = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSearchEmail.setGeometry(QtCore.QRect(260, 80, 141, 23))
        self.ButtonSearchEmail.setObjectName("ButtonSearchEmail")
        self.ButtonErase = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonErase.setGeometry(QtCore.QRect(250, 430, 101, 23))
        self.ButtonErase.setObjectName("ButtonErase")
        self.ButtonExit = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonExit.setGeometry(QtCore.QRect(360, 430, 91, 23))
        self.ButtonExit.setObjectName("ButtonExit")
        self.ButtonShowAll = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonShowAll.setGeometry(QtCore.QRect(170, 120, 151, 23))
        self.ButtonShowAll.setObjectName("ButtonShowAll")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ButtonSearchDNI.setText(_translate("MainWindow", "Buscar por DNI"))
        self.ButtonSelect.setText(_translate("MainWindow", "Seleccionar"))
        self.ButtonView.setText(_translate("MainWindow", "Ver"))
        self.ButtonSearchPhone.setText(_translate("MainWindow", "Buscar por Telf."))
        self.ButtonSearchEmail.setText(_translate("MainWindow", "Buscar por Email"))
        self.ButtonErase.setText(_translate("MainWindow", "Borrar"))
        self.ButtonExit.setText(_translate("MainWindow", "Salir"))
        self.ButtonShowAll.setText(_translate("MainWindow", "Mostrar todos los clientes"))

        # mouse click connect functions
        self.ButtonSearchDNI.clicked.connect(self.ClientMngSearchDNI)
        self.ButtonSearchPhone.clicked.connect(self.ClientMngSearchPhone)
        self.ButtonSearchEmail.clicked.connect(self.ClientMngSearchEmail)
        self.ButtonView.clicked.connect(self.ClientMng2View)        
        self.ButtonExit.clicked.connect(self.ClientMngExit)      
        self.ButtonSelect.clicked.connect(self.ClientMngSelect)      
        self.ButtonErase.clicked.connect(self.ClientMngErase)
        self.ButtonShowAll.clicked.connect(self.ClientMngShowAll)

# methods related to the action buttons 
        
    def ClientMngErase(self):
        item_sel = self.listClient.selectedItems()                
        
        if item_sel:
            item_curr = str(self.listClient.currentItem().text())                    
            # filtering the string to get the doc_id of the data base.
            item_split = item_curr.split('[')                
            db_id = item_split[1][:-1]
            # remove item from the database.
            self.ClientMngDb.remove(doc_ids = [int(db_id)])
            # remove item from the listbox.
            self.listClient.takeItem(self.listClient.currentRow())    
            # drop tables linked to this client
            #print (len(self.ClientMngDbTableFlatFav.all()))
            #print (len(self.ClientMngDbTableFlatBook.all()))
            #print (len(self.ClientMngDbTableFlatBuy.all()))
            if len(self.ClientMngDbTableFlatFav.all()) > 0:
                self.ClientMngDbTableFlatFav.remove(doc_ids = [int(db_id)])
            if len(self.ClientMngDbTableFlatBook.all()) > 1:
                self.ClientMngDbTableFlatBook.remove(doc_ids = [int(db_id)])
            if len(self.ClientMngDbTableFlatBuy.all()) > 1:
                self.ClientMngDbTableFlatBuy.remove(doc_ids = [int(db_id)])                                  
        else:
            dialog = QtWidgets.QMessageBox()
            dialog.setWindowTitle(WIN_TITLE)
            dialog.setWindowIcon(QtGui.QIcon(PIC_PATH+WIN_TITLE+PIC_EXTENSION))
            dialog.setIcon(QtWidgets.QMessageBox.Warning)
            dialog.setText("No ha seleccionado ningun cliente")
            dialog.addButton(QtWidgets.QMessageBox.Ok)
            dialog.exec()        

    def ClientMngSelect(self):
        item_sel = self.listClient.selectedItems()
        if item_sel:
            item_curr = str(self.listClient.currentItem().text())                    
            # filtering the string to get the doc_id of the data base
            item_split = item_curr.split('[')                
            db_id = item_split[1][:-1]
            #save data of the current selected client for future argument function
            doc = self.ClientMngDb.get(doc_id=int(db_id))
            clientTemp =  "Cliente: " +\
                          doc['Surname1'] + ", " + doc['Surname2'] + ", " +\
                          doc['Name'] + " | " + doc['DNI'] + " | " + doc['Phone'] + " | "+\
                          doc['Email'] + " | " + " [" + str(doc.doc_id) + "]"                           
            self.ClientMngAdecuaStatusLabel.setText(clientTemp)
        else:
            dialog = QtWidgets.QMessageBox()
            dialog.setWindowTitle(WIN_TITLE)
            dialog.setWindowIcon(QtGui.QIcon(PIC_PATH+WIN_TITLE+PIC_EXTENSION))
            dialog.setIcon(QtWidgets.QMessageBox.Warning)
            dialog.setText("No ha seleccionado ningun cliente")
            dialog.addButton(QtWidgets.QMessageBox.Ok)
            dialog.exec()          
    
    def ClientMngExit(self):
        self.ClientMngWin.hide()
    
    def ClientMng2View(self):
        item_sel = self.listClient.selectedItems()
        #print(item_sel)
        if item_sel:
            item_curr = str(self.listClient.currentItem().text())        
            # filtering the string to get the doc_id of the data base
            item_split = item_curr.split('[')                
            db_id = item_split[1][:-1]
            #save data of the current selected client for future argument function
            clientSel = self.ClientMngDb.get(doc_id=int(db_id))          
            # open a new window
            self.windowClientView=QtWidgets.QMainWindow()
            self.ui=Ui_ClientView(clientSel, self.ClientMngDb, self.ClientMngDbTableFlatFav,
                                  self.ClientMngDbTableFlatBook, self.ClientMngDbTableFlatBuy,
                                  self.windowClientView, self.ClientMngAdecuaWin,  
                                  self.ClientMngAdecuaTreeWidLst)        
            self.ui.setup(self.windowClientView)
            self.windowClientView.show()        
        else:
            dialog = QtWidgets.QMessageBox()
            dialog.setWindowTitle(WIN_TITLE)
            dialog.setWindowIcon(QtGui.QIcon(PIC_PATH+WIN_TITLE+PIC_EXTENSION))
            dialog.setIcon(QtWidgets.QMessageBox.Warning)
            dialog.setText("No ha seleccionado ningun cliente")
            dialog.addButton(QtWidgets.QMessageBox.Ok)
            dialog.exec()
    
    def ClientMngShowAll(self):
        docs = self.ClientMngDb.all()
        # create a temp list with the fields to show in the listbox        
        lClient = []      
        for doc in docs:
            clientTemp =  doc['Surname1'] + ", " + doc['Surname2'] + ", " +\
                          doc['Name'] + " | " + doc['DNI'] + " | " + doc['Phone'] + " | "+\
                          doc['Email'] + " | " + " [" + str(doc.doc_id) + "]"  
            lClient.append(clientTemp) 
            
        # add items to the listbox
        self.listClient.clear()
        for i in range(len(lClient)):    
            self.listClient.insertItem(i, lClient[i])
    
    def ClientMngSearchDNI(self):
        # get value from the textbox
        dni2search = self.LineDNI.text()
        
        # search for any match in database
        docs = self.ClientMngDb.search(where('DNI') == dni2search)
        if not docs:        
            dialog = QtWidgets.QMessageBox()
            dialog.setWindowTitle(WIN_TITLE)
            dialog.setWindowIcon(QtGui.QIcon(PIC_PATH+WIN_TITLE+PIC_EXTENSION))
            dialog.setIcon(QtWidgets.QMessageBox.Warning)
            dialog.setText("No existe este valor")
            dialog.addButton(QtWidgets.QMessageBox.Ok)
            dialog.exec()          

        # create a temp list with the fields to show in the listbox        
        lClient = []      
        for doc in docs:
            clientTemp =  doc['Surname1'] + ", " + doc['Surname2'] + ", " +\
                          doc['Name'] + " | " + doc['DNI'] + " | " + doc['Phone'] + " | "+\
                          doc['Email'] + " | " + " [" + str(doc.doc_id) + "]"  
            lClient.append(clientTemp) 
            
        # add items to the listbox
        self.listClient.clear()
        for i in range(len(lClient)):    
            self.listClient.insertItem(i, lClient[i])

    def ClientMngSearchPhone(self):    
        # get value from the textbox
        phone2search = self.LinePhone.text()
        
        # search for any match in database
        docs = self.ClientMngDb.search(where('Phone') == phone2search)
        if not docs:
            dialog = QtWidgets.QMessageBox()
            dialog.setWindowTitle(WIN_TITLE)
            dialog.setWindowIcon(QtGui.QIcon(PIC_PATH+WIN_TITLE+PIC_EXTENSION))
            dialog.setIcon(QtWidgets.QMessageBox.Warning)
            dialog.setText("No existe este valor")
            dialog.addButton(QtWidgets.QMessageBox.Ok)
            dialog.exec()          

        # create a temp list with the fields to show in the listbox
        lClient = []      
        for doc in docs:
            clientTemp =  doc['Surname1'] + ", " + doc['Surname2'] + ", " +\
                          doc['Name'] + " | " + doc['DNI'] + " | " + doc['Phone'] + " | "+\
                          doc['Email'] + " | " + " [" + str(doc.doc_id) + "]"  
            lClient.append(clientTemp) 
            
        # add items to the listbox
        self.listClient.clear()
        for i in range(len(lClient)):    
            self.listClient.insertItem(i, lClient[i])

    def ClientMngSearchEmail(self):
        # get value from the textbox
        email2search = self.LineEmail.text()
        
        # search for any match in database.
        docs = self.ClientMngDb.search(where('Email') == email2search)
        if not docs:
            dialog = QtWidgets.QMessageBox()
            dialog.setWindowTitle(WIN_TITLE)
            dialog.setWindowIcon(QtGui.QIcon(PIC_PATH+WIN_TITLE+PIC_EXTENSION))
            dialog.setIcon(QtWidgets.QMessageBox.Warning)
            dialog.setText("No existe este valor")
            dialog.addButton(QtWidgets.QMessageBox.Ok)
            dialog.exec()          

        # create a temp list with the fields to show in the listbox
        lClient = []      
        for doc in docs:
            clientTemp =  doc['Surname1'] + ", " + doc['Surname2'] + ", " +\
                          doc['Name'] + " | " + doc['DNI'] + " | " + doc['Phone'] + " | "+\
                          doc['Email'] + " | " + " [" + str(doc.doc_id) + "]"  
            lClient.append(clientTemp) 
            
        # add items to the listbox
        self.listClient.clear()
        for i in range(len(lClient)):    
            self.listClient.insertItem(i, lClient[i])
