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
    def __init__(self, db_ADECUA):
        self.dbClientNew = db_ADECUA
        self.dbClientNew.insert({'Nombre': 'Enrique', 'Piso': 'DB-P3-02-2MP_1D.A'})
        self.dbClientNew.insert({'Nombre': 'Jose', 'Piso': 'DB-P3-03_Atico-3MF_0D.C&3MF_3D.A1'})        
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(491, 304)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LineName = QtWidgets.QLineEdit(self.centralwidget)
        self.LineName.setGeometry(QtCore.QRect(100, 30, 151, 21))
        self.LineName.setObjectName("LineName")
        self.LabelName = QtWidgets.QLabel(self.centralwidget)
        self.LabelName.setGeometry(QtCore.QRect(20, 30, 61, 21))
        self.LabelName.setObjectName("LabelName")
        self.LineSurname1 = QtWidgets.QLineEdit(self.centralwidget)
        self.LineSurname1.setGeometry(QtCore.QRect(100, 60, 151, 21))
        self.LineSurname1.setText("")
        self.LineSurname1.setObjectName("LineSurname1")
        self.LabelSurname1 = QtWidgets.QLabel(self.centralwidget)
        self.LabelSurname1.setGeometry(QtCore.QRect(20, 60, 61, 21))
        self.LabelSurname1.setObjectName("LabelSurname1")
        self.ButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSave.setGeometry(QtCore.QRect(60, 240, 75, 23))
        self.ButtonSave.setObjectName("ButtonSave")
        self.ButtonErase = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonErase.setGeometry(QtCore.QRect(160, 240, 91, 23))
        self.ButtonErase.setObjectName("ButtonErase")
        self.ButtonExit = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonExit.setGeometry(QtCore.QRect(270, 240, 75, 23))
        self.ButtonExit.setObjectName("ButtonExit")
        self.LabelSurname2 = QtWidgets.QLabel(self.centralwidget)
        self.LabelSurname2.setGeometry(QtCore.QRect(20, 90, 61, 21))
        self.LabelSurname2.setObjectName("LabelSurname2")
        self.LabelDNI = QtWidgets.QLabel(self.centralwidget)
        self.LabelDNI.setGeometry(QtCore.QRect(20, 120, 61, 21))
        self.LabelDNI.setObjectName("LabelDNI")
        self.LineSurname2 = QtWidgets.QLineEdit(self.centralwidget)
        self.LineSurname2.setGeometry(QtCore.QRect(100, 90, 151, 21))
        self.LineSurname2.setText("")
        self.LineSurname2.setObjectName("LineSurname2")
        self.LineDNI = QtWidgets.QLineEdit(self.centralwidget)
        self.LineDNI.setGeometry(QtCore.QRect(100, 120, 151, 21))
        self.LineDNI.setText("")
        self.LineDNI.setObjectName("LineDNI")
        self.LabelPhone = QtWidgets.QLabel(self.centralwidget)
        self.LabelPhone.setGeometry(QtCore.QRect(20, 150, 61, 21))
        self.LabelPhone.setObjectName("LabelPhone")
        self.LinePhone = QtWidgets.QLineEdit(self.centralwidget)
        self.LinePhone.setGeometry(QtCore.QRect(100, 150, 151, 21))
        self.LinePhone.setText("")
        self.LinePhone.setObjectName("LinePhone")
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
        self.ButtonSave.setText(_translate("MainWindow", "Guardar"))
        self.ButtonErase.setText(_translate("MainWindow", "Borrar campos"))
        self.ButtonExit.setText(_translate("MainWindow", "Salir"))
        self.LabelSurname2.setText(_translate("MainWindow", "Apellido 2:"))
        self.LabelDNI.setText(_translate("MainWindow", "DNI:"))
        self.LabelPhone.setText(_translate("MainWindow", "Teléfono:"))

    # mouse click connect functions
        self.ButtonSave.clicked.connect(self.SaveClient)
        

    def SaveClient(self):
        name = self.LineName.text()
        print(name)
        #get all documents stored in the database
        #print (self.dbClientNew.all())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ClientNew()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
