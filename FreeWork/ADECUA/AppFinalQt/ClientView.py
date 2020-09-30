# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClientView.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from tinydb import TinyDB, Query

class Ui_ClientView(object):
    def __init__(self, clientSel, dbClientManage, dbTableFlatFavClientManage, dbTableFlatBookClientManage,
                dbTableFlatBuyClientManage, windowClientView):
        self.dbClientView = dbClientManage # copy database to a local variable. 
        self.windowClientView = windowClientView #copy window var to a loca var.
        self.clientData = clientSel
        # copy database tables to local variables
        self.dbTableFlatFavClientView = dbTableFlatFavClientManage
        self.dbTableFlatBookClientView = dbTableFlatBookClientManage
        self.dbTableFlatBuyClientView = dbTableFlatBuyClientManage

        #print(self.clientData.doc_id)
        #print(self.dbTableFlatFavClientView.all())

        
        
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 750)
        MainWindow.setMaximumSize(QtCore.QSize(750, 750))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LabelName = QtWidgets.QLabel(self.centralwidget)
        self.LabelName.setGeometry(QtCore.QRect(20, 30, 61, 21))
        self.LabelName.setObjectName("LabelName")
        self.LabelSurname1 = QtWidgets.QLabel(self.centralwidget)
        self.LabelSurname1.setGeometry(QtCore.QRect(20, 60, 61, 21))
        self.LabelSurname1.setObjectName("LabelSurname1")
        self.LabelSurname2 = QtWidgets.QLabel(self.centralwidget)
        self.LabelSurname2.setGeometry(QtCore.QRect(20, 90, 61, 21))
        self.LabelSurname2.setObjectName("LabelSurname2")
        self.LabelDNI = QtWidgets.QLabel(self.centralwidget)
        self.LabelDNI.setGeometry(QtCore.QRect(20, 120, 61, 21))
        self.LabelDNI.setObjectName("LabelDNI")
        self.LabelPhone = QtWidgets.QLabel(self.centralwidget)
        self.LabelPhone.setGeometry(QtCore.QRect(20, 150, 61, 21))
        self.LabelPhone.setObjectName("LabelPhone")
        self.lineNameView = QtWidgets.QLineEdit(self.centralwidget)
        self.lineNameView.setEnabled(False)
        self.lineNameView.setGeometry(QtCore.QRect(80, 30, 311, 20))
        self.lineNameView.setObjectName("lineNameView")
        self.lineSurname1View = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSurname1View.setEnabled(False)
        self.lineSurname1View.setGeometry(QtCore.QRect(80, 60, 311, 20))
        self.lineSurname1View.setObjectName("lineSurname1View")
        self.lineSurname2View = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSurname2View.setEnabled(False)
        self.lineSurname2View.setGeometry(QtCore.QRect(80, 90, 311, 20))
        self.lineSurname2View.setObjectName("lineSurname2View")
        self.lineDNIView = QtWidgets.QLineEdit(self.centralwidget)
        self.lineDNIView.setEnabled(False)
        self.lineDNIView.setGeometry(QtCore.QRect(80, 120, 311, 20))
        self.lineDNIView.setObjectName("lineDNIView")
        self.linePhoneView = QtWidgets.QLineEdit(self.centralwidget)
        self.linePhoneView.setEnabled(False)
        self.linePhoneView.setGeometry(QtCore.QRect(80, 150, 311, 20))
        self.linePhoneView.setObjectName("linePhoneView")
        self.ButtonEdit = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonEdit.setGeometry(QtCore.QRect(430, 60, 75, 23))
        self.ButtonEdit.setObjectName("ButtonEdit")
        self.ButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSave.setGeometry(QtCore.QRect(430, 90, 75, 23))
        self.ButtonSave.setObjectName("ButtonSave")
        self.ButtonExit = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonExit.setGeometry(QtCore.QRect(430, 120, 75, 23))
        self.ButtonExit.setObjectName("ButtonExit")
        #self.listFlatFav = QtWidgets.QListWidget(self.centralwidget)
        self.listFlatFav = ListFavWidget(self.centralwidget)
        self.listFlatFav.setGeometry(QtCore.QRect(20, 260, 681, 121))
        self.listFlatFav.setObjectName("listFlatFav")
        self.LabelFlatFav = QtWidgets.QLabel(self.centralwidget)
        self.LabelFlatFav.setGeometry(QtCore.QRect(300, 230, 161, 21))
        self.LabelFlatFav.setObjectName("LabelFlatFav")
        #self.listFlatBook = QtWidgets.QListWidget(self.centralwidget)
        self.listFlatBook = ListBookWidget(self.centralwidget)
        self.listFlatBook.setGeometry(QtCore.QRect(20, 420, 681, 121))
        self.listFlatBook.setObjectName("listFlatBook")
        self.LabelFlatBook = QtWidgets.QLabel(self.centralwidget)
        self.LabelFlatBook.setGeometry(QtCore.QRect(300, 390, 181, 21))
        self.LabelFlatBook.setObjectName("LabelFlatBook")
        #self.listFlatBuy = QtWidgets.QListWidget(self.centralwidget)
        self.listFlatBuy = ListBuyWidget(self.centralwidget)
        self.listFlatBuy.setGeometry(QtCore.QRect(20, 590, 681, 121))
        self.listFlatBuy.setObjectName("listFlatBuy")
        self.LabelFlatBuy = QtWidgets.QLabel(self.centralwidget)
        self.LabelFlatBuy.setGeometry(QtCore.QRect(300, 560, 181, 21))
        self.LabelFlatBuy.setObjectName("LabelFlatBuy")
        self.LabelEmail = QtWidgets.QLabel(self.centralwidget)
        self.LabelEmail.setGeometry(QtCore.QRect(20, 180, 61, 21))
        self.LabelEmail.setObjectName("LabelEmail")
        self.lineEmailView = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEmailView.setEnabled(False)
        self.lineEmailView.setGeometry(QtCore.QRect(80, 180, 311, 20))
        self.lineEmailView.setObjectName("lineEmailView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LabelName.setText(_translate("MainWindow", "Nombre:"))
        self.LabelSurname1.setText(_translate("MainWindow", "Apellido 1:"))
        self.LabelSurname2.setText(_translate("MainWindow", "Apellido 2:"))
        self.LabelDNI.setText(_translate("MainWindow", "DNI:"))
        self.LabelPhone.setText(_translate("MainWindow", "Teléfono:"))
        self.lineNameView.setText(_translate("MainWindow", "NameView"))
        self.lineSurname1View.setText(_translate("MainWindow", "Surname1View"))
        self.lineSurname2View.setText(_translate("MainWindow", "Surname2View"))
        self.lineDNIView.setText(_translate("MainWindow", "SurnameDNIView"))
        self.linePhoneView.setText(_translate("MainWindow", "PhoneView"))
        self.ButtonEdit.setText(_translate("MainWindow", "Editar"))
        self.ButtonSave.setText(_translate("MainWindow", "Guardar"))
        self.ButtonExit.setText(_translate("MainWindow", "Salir"))
        self.LabelFlatFav.setText(_translate("MainWindow", "Lista de Favoritos"))
        self.LabelFlatBook.setText(_translate("MainWindow", "Lista de Reservas"))
        self.LabelFlatBuy.setText(_translate("MainWindow", "Lista de Compras"))
        self.LabelEmail.setText(_translate("MainWindow", "Email:"))
        self.lineEmailView.setText(_translate("MainWindow", "EmailView"))
        
        # Edit line widgets with data client
        self.lineNameView.setText(_translate("MainWindow", self.clientData['Name']))
        self.lineSurname1View.setText(_translate("MainWindow", self.clientData['Surname1']))
        self.lineSurname2View.setText(_translate("MainWindow", self.clientData['Surname2']))
        self.lineDNIView.setText(_translate("MainWindow", self.clientData['DNI']))
        self.linePhoneView.setText(_translate("MainWindow", self.clientData['Phone']))
        self.lineEmailView.setText(_translate("MainWindow", self.clientData['Email']))

        # Mouse click connect functions
        self.ButtonEdit.clicked.connect(self.ClientViewEdit)
        self.ButtonSave.clicked.connect(self.ClientViewSave)
        self.ButtonExit.clicked.connect(self.ClientViewExit)
        self.listFlatFav.right_click.connect(self.ClientListFavRightMenu)
        self.listFlatBook.right_click.connect(self.ClientListBookRightMenu)
        self.listFlatBuy.right_click.connect(self.ClientListBuyRightMenu)

        # Adding items to the list boxes
        self.ClientListAddItems()

# methods related to the action buttons
   
    def ClientListFavRightMenu(self): 
    # when righ click is over widget item...
        item_sel = self.listFlatFav.selectedItems()     
        if item_sel: 
            if self.listFlatFav.action == self.listFlatFav.viewAction:                        
                print ("Ver piso")
            elif self.listFlatFav.action == self.listFlatFav.moveToBookAction:
                print ("Mover a lista de reservas")
            elif self.listFlatFav.action == self.listFlatFav.moveToBuyAction:
                print ("Mover a lista de compras")
            elif self.listFlatFav.action == self.listFlatFav.removeAction:
                print ("Quitar de la lista")
                removeItem(item_sel, self.dbTableFlatFavClientView, self.listFlatFav)


    def ClientListBookRightMenu(self): 
        pass

    def ClientListBuyRightMenu(self):
        pass

    def ClientListAddItems(self):
    # add items to the list boxes
        # add items to the fav list.
        flatFav = Query()        
        docs = self.dbTableFlatFavClientView.search(flatFav.Id == str(self.clientData.doc_id)) # search in the table
        lflatFav = []
        # create a list with the items to add to the listbox.
        for doc in docs:
            listFlatFavTxt = 'Apartamento: ' + str(doc['Picname']) + ' | ' + 'Habitaciones: ' +\
                              str(doc['NumRoom']) + ' | ' + 'Coordenadas: ' + str(doc['Coordinates'])
            lflatFav.append(listFlatFavTxt)   
        # set and sort list (just in case the user makes click over the same item several times).
        lflatFav_sort = list(set(lflatFav))
        lflatFav_sort.sort()       
        # Adding rooms to the listbox
        for i in range(len(lflatFav_sort)):
            self.listFlatFav.insertItem(i, lflatFav_sort[i])

        # add items to the book list.
        flatBook = Query()        
        docs = self.dbTableFlatBookClientView.search(flatBook.Id == str(self.clientData.doc_id)) # search in the table
        lflatBook = []
        # create a list with the items to add to the listbox.
        for doc in docs:
            listFlatBookTxt = 'Apartamento: ' + str(doc['Picname']) + ' | ' + 'Habitaciones: ' +\
                              str(doc['NumRoom']) + ' | ' + 'Coordenadas: ' + str(doc['Coordinates'])
            lflatBook.append(listFlatBookTxt)   
        # set and sort list (just in case the user makes click over the same item several times).
        lflatBook_sort = list(set(lflatBook))
        lflatBook_sort.sort()       
        # Adding rooms to the listbox
        for i in range(len(lflatBook_sort)):
            self.listFlatBook.insertItem(i, lflatBook_sort[i])

        # add items to the Buy list.
        flatBuy = Query()        
        docs = self.dbTableFlatBuyClientView.search(flatBuy.Id == str(self.clientData.doc_id)) # search in the table
        lflatBuy = []
        # create a list with the items to add to the listbox.
        for doc in docs:
            listFlatBuyTxt = 'Apartamento: ' + str(doc['Picname']) + ' | ' + 'Habitaciones: ' +\
                              str(doc['NumRoom']) + ' | ' + 'Coordenadas: ' + str(doc['Coordinates'])
            lflatBuy.append(listFlatBuyTxt)   
        # set and sort list (just in case the user makes click over the same item several times).
        lflatBuy_sort = list(set(lflatBuy))
        lflatBuy_sort.sort()       
        # Adding rooms to the listbox
        for i in range(len(lflatBuy_sort)):
            self.listFlatBuy.insertItem(i, lflatBuy_sort[i])
        
    def ClientViewEdit(self):
    # when edit button is clicked...
        self.lineNameView.setEnabled(True)
        self.lineSurname1View.setEnabled(True)
        self.lineSurname2View.setEnabled(True)
        self.lineDNIView.setEnabled(True)
        self.linePhoneView.setEnabled(True)
        self.lineEmailView.setEnabled(True)

    def ClientViewSave(self):
    # when save button is clicked...
        self.dbClientView.update({'Name': self.lineNameView.text()}, doc_ids = [self.clientData.doc_id])
        self.dbClientView.update({'Surname1': self.lineSurname1View.text()}, doc_ids = [self.clientData.doc_id])
        self.dbClientView.update({'Surname2': self.lineSurname2View.text()}, doc_ids = [self.clientData.doc_id])
        self.dbClientView.update({'DNI': self.lineDNIView.text()}, doc_ids = [self.clientData.doc_id])
        self.dbClientView.update({'Phone': self.linePhoneView.text()}, doc_ids = [self.clientData.doc_id])
        self.dbClientView.update({'Email': self.lineEmailView.text()}, doc_ids = [self.clientData.doc_id])
        print(self.dbClientView.all())

    def ClientViewExit(self):
    # when exit button is clicked...
        self.windowClientView.hide()       

#-------------------------CLASSES---------------------------

# Class to handle right click button action over listFav widget
class ListFavWidget(QtWidgets.QListWidget):          
    # Handling mouse clicks on treeview
    right_click = QtCore.pyqtSignal()               

    def mousePressEvent(self, event):
        super(ListFavWidget, self).mousePressEvent(event)                    
        if event.button() == QtCore.Qt.RightButton:            
            menu = QtWidgets.QMenu()
            self.viewAction = menu.addAction("Ver") 
            self.moveToBookAction = menu.addAction("Mover a reservas")   
            self.moveToBuyAction = menu.addAction("Mover a compras")
            self.removeAction = menu.addAction("Quitar")               
            self.action = menu.exec_(event.globalPos())          
            self.right_click.emit()

# Class to handle right click button action over listBook widget
class ListBookWidget(QtWidgets.QListWidget):          
    # Handling mouse clicks on treeview
    right_click = QtCore.pyqtSignal()               

    def mousePressEvent(self, event):
        super(ListBookWidget, self).mousePressEvent(event)                    
        if event.button() == QtCore.Qt.RightButton:            
            menu = QtWidgets.QMenu()
            self.viewAction = menu.addAction("Ver") 
            self.moveToBookAction = menu.addAction("Mover a Favoritos")   
            self.moveToBuyAction = menu.addAction("Mover a compras")
            self.removeAction = menu.addAction("Quitar")               
            self.action = menu.exec_(event.globalPos())          
            self.right_click.emit()

# Class to handle right click button action over listBuy widget
class ListBuyWidget(QtWidgets.QListWidget):          
    # Handling mouse clicks on treeview
    right_click = QtCore.pyqtSignal()               

    def mousePressEvent(self, event):
        super(ListBuyWidget, self).mousePressEvent(event)                    
        if event.button() == QtCore.Qt.RightButton:            
            menu = QtWidgets.QMenu()
            self.viewAction = menu.addAction("Ver") 
            self.moveToBookAction = menu.addAction("Mover a favoritos")   
            self.moveToBuyAction = menu.addAction("Mover a reservas")
            self.removeAction = menu.addAction("Quitar")               
            self.action = menu.exec_(event.globalPos())          
            self.right_click.emit()

#----------------------------METHODS--------------------------

def removeItem (item_sel, dbTableFlatClientView, listFlat):
    # remove listbox selected item from the listbox
    for i in item_sel:
        listFlat.takeItem(listFlat.row(i))
    # drop item from the database
    item_text = item_sel[0].text()
    item_text_split = item_text.split('|')
    item_flat = item_text_split[0]
    item_flat_split = item_flat.split(':')
    picname_text = item_flat_split[1][1:-1]   
    picname_query = Query()
    docs = dbTableFlatClientView.search(picname_query.Picname == picname_text)    
    for doc in docs:        
        dbTableFlatClientView.remove(doc_ids = [doc.doc_id])
    