# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClientNew.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

'''
Next modifications should be done before insert this window
into the main window:
 - class Ui_MainWindow(object): => class Ui_ClientNew(object):  
 - def setupUi(self): => def setup(self, MainWindow):
 - MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow")) => MainWindow.setWindowTitle(_translate("MainWindow", "ADECUA - Nuevo Cliente"))
 - ui = Ui_MainWindow() => ui = Ui_ClientNew()
 - ui.setupUi(MainWindow) => ui.setup(MainWindow)

''' 

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClientNew(object): 
    def __init__(self, db_ADECUA, windowClientNew):
        self.dbClientNew = db_ADECUA # copy database to a local variable. 
        self.wClientNew = windowClientNew #copy window var to a loca var.
               
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(329, 304)
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
        self.LineName = QtWidgets.QLineEdit(self.centralwidget)
        self.LineName.setGeometry(QtCore.QRect(90, 30, 171, 20))
        self.LineName.setObjectName("LineName")
        self.LineSurname1 = QtWidgets.QLineEdit(self.centralwidget)
        self.LineSurname1.setGeometry(QtCore.QRect(92, 60, 171, 20))
        self.LineSurname1.setObjectName("LineSurname1")
        self.LineSurname2 = QtWidgets.QLineEdit(self.centralwidget)
        self.LineSurname2.setGeometry(QtCore.QRect(90, 90, 171, 20))
        self.LineSurname2.setObjectName("LineSurname2")
        self.LineDNI = QtWidgets.QLineEdit(self.centralwidget)
        self.LineDNI.setGeometry(QtCore.QRect(90, 120, 171, 20))
        self.LineDNI.setObjectName("LineDNI")
        self.LinePhone = QtWidgets.QLineEdit(self.centralwidget)
        self.LinePhone.setGeometry(QtCore.QRect(90, 150, 171, 20))
        self.LinePhone.setObjectName("LinePhone")
        self.LineEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEmail.setGeometry(QtCore.QRect(90, 180, 171, 20))
        self.LineEmail.setObjectName("LineEmail")
        self.labelEmail = QtWidgets.QLabel(self.centralwidget)
        self.labelEmail.setGeometry(QtCore.QRect(20, 180, 47, 13))
        self.labelEmail.setObjectName("labelEmail")
        self.ButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSave.setGeometry(QtCore.QRect(40, 230, 75, 23))
        self.ButtonSave.setObjectName("ButtonSave")
        self.ButtonErase = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonErase.setGeometry(QtCore.QRect(130, 230, 75, 23))
        self.ButtonErase.setObjectName("ButtonErase")
        self.ButtonExit = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonExit.setGeometry(QtCore.QRect(220, 230, 75, 23))
        self.ButtonExit.setObjectName("ButtonExit")
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
        self.labelEmail.setText(_translate("MainWindow", "Email:"))
        self.ButtonSave.setText(_translate("MainWindow", "Guardar"))
        self.ButtonErase.setText(_translate("MainWindow", "Borrar"))
        self.ButtonExit.setText(_translate("MainWindow", "Salir"))

    # mouse click connect functions
        self.ButtonSave.clicked.connect(self.SaveClient)
        self.ButtonErase.clicked.connect(self.EraseLinesClient)
        self.ButtonExit.clicked.connect(self.ExitClient)

    # methods related to the action buttons
        
    def SaveClient(self):
        name = self.LineName.text()
        surname1 = self.LineSurname1.text()
        surname2 = self.LineSurname2.text()
        dni = self.LineDNI.text()
        phone = self.LinePhone.text()        
        email = self.LineEmail.text()        
        self.dbClientNew.insert({'Name': name, 'Surname1': surname1, 'Surname2': surname2, 
                                 'DNI': dni, 'Phone': phone, 'Email': email})
        #get all documents stored in the database
        print (self.dbClientNew.all())

    def EraseLinesClient(self):
        self.LineName.clear()
        self.LineSurname1.clear()
        self.LineSurname2.clear()
        self.LineDNI.clear()
        self.LinePhone.clear()
        self.LineEmail.clear()

    def ExitClient(self):        
        self.wClientNew.hide()

'''
if __name__ == "__main__":  
    import sys 
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ClientNew()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

'''