# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from my_lib import *
from selenium import webdriver
from instabot import Bot 
from PIL import Image
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(909, 895)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_url_marca = QtWidgets.QLineEdit(self.centralwidget)
        self.line_url_marca.setGeometry(QtCore.QRect(100, 70, 331, 20))
        self.line_url_marca.setObjectName("line_url_marca")
        self.label_step2 = QtWidgets.QLabel(self.centralwidget)
        self.label_step2.setGeometry(QtCore.QRect(20, 780, 241, 16))
        self.label_step2.setObjectName("label_step2")
        self.label_step1 = QtWidgets.QLabel(self.centralwidget)
        self.label_step1.setGeometry(QtCore.QRect(20, 30, 121, 16))
        self.label_step1.setObjectName("label_step1")
        self.label_url_marca = QtWidgets.QLabel(self.centralwidget)
        self.label_url_marca.setGeometry(QtCore.QRect(50, 70, 31, 16))
        self.label_url_marca.setObjectName("label_url_marca")
        self.label_url_as = QtWidgets.QLabel(self.centralwidget)
        self.label_url_as.setGeometry(QtCore.QRect(450, 70, 31, 16))
        self.label_url_as.setObjectName("label_url_as")
        self.label_url_mundo = QtWidgets.QLabel(self.centralwidget)
        self.label_url_mundo.setGeometry(QtCore.QRect(430, 430, 91, 16))
        self.label_url_mundo.setObjectName("label_url_mundo")
        self.label_url_sport = QtWidgets.QLabel(self.centralwidget)
        self.label_url_sport.setGeometry(QtCore.QRect(50, 430, 41, 16))
        self.label_url_sport.setObjectName("label_url_sport")
        self.label_pic_marca = QtWidgets.QLabel(self.centralwidget)
        self.label_pic_marca.setGeometry(QtCore.QRect(140, 100, 251, 291))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pic_marca.sizePolicy().hasHeightForWidth())
        self.label_pic_marca.setSizePolicy(sizePolicy)
        self.label_pic_marca.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_pic_marca.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_pic_marca.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pic_marca.setText("")
        self.label_pic_marca.setScaledContents(True)
        self.label_pic_marca.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pic_marca.setObjectName("label_pic_marca")
        self.label_pic_as = QtWidgets.QLabel(self.centralwidget)
        self.label_pic_as.setGeometry(QtCore.QRect(540, 100, 251, 291))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pic_as.sizePolicy().hasHeightForWidth())
        self.label_pic_as.setSizePolicy(sizePolicy)
        self.label_pic_as.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_pic_as.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_pic_as.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pic_as.setText("")
        self.label_pic_as.setScaledContents(True)
        self.label_pic_as.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pic_as.setObjectName("label_pic_as")
        self.line_url_as = QtWidgets.QLineEdit(self.centralwidget)
        self.line_url_as.setGeometry(QtCore.QRect(500, 70, 331, 20))
        self.line_url_as.setObjectName("line_url_as")
        self.label_pic_sport = QtWidgets.QLabel(self.centralwidget)
        self.label_pic_sport.setGeometry(QtCore.QRect(140, 460, 251, 291))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pic_sport.sizePolicy().hasHeightForWidth())
        self.label_pic_sport.setSizePolicy(sizePolicy)
        self.label_pic_sport.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_pic_sport.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_pic_sport.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pic_sport.setText("")
        self.label_pic_sport.setScaledContents(True)
        self.label_pic_sport.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pic_sport.setObjectName("label_pic_sport")
        self.label_pic_mundo = QtWidgets.QLabel(self.centralwidget)
        self.label_pic_mundo.setGeometry(QtCore.QRect(540, 460, 251, 291))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pic_mundo.sizePolicy().hasHeightForWidth())
        self.label_pic_mundo.setSizePolicy(sizePolicy)
        self.label_pic_mundo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_pic_mundo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_pic_mundo.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pic_mundo.setText("")
        self.label_pic_mundo.setScaledContents(True)
        self.label_pic_mundo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pic_mundo.setObjectName("label_pic_mundo")
        self.line_url_sport = QtWidgets.QLineEdit(self.centralwidget)
        self.line_url_sport.setGeometry(QtCore.QRect(90, 430, 331, 20))
        self.line_url_sport.setObjectName("line_url_sport")
        self.line_url_mundo = QtWidgets.QLineEdit(self.centralwidget)
        self.line_url_mundo.setGeometry(QtCore.QRect(520, 430, 331, 20))
        self.line_url_mundo.setObjectName("line_url_mundo")
        self.label_insta_user = QtWidgets.QLabel(self.centralwidget)
        self.label_insta_user.setGeometry(QtCore.QRect(70, 810, 31, 16))
        self.label_insta_user.setObjectName("label_insta_user")
        self.label_insta_pass = QtWidgets.QLabel(self.centralwidget)
        self.label_insta_pass.setGeometry(QtCore.QRect(70, 840, 31, 16))
        self.label_insta_pass.setObjectName("label_insta_pass")
        self.line_insta_user = QtWidgets.QLineEdit(self.centralwidget)
        self.line_insta_user.setGeometry(QtCore.QRect(110, 810, 141, 20))
        self.line_insta_user.setObjectName("line_insta_user")
        self.line_insta_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.line_insta_pass.setGeometry(QtCore.QRect(110, 840, 141, 20))
        self.line_insta_pass.setObjectName("line_insta_pass")
        self.pushButton_GetPics = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GetPics.setGeometry(QtCore.QRect(170, 30, 75, 23))
        self.pushButton_GetPics.setObjectName("pushButton_GetPics")
        self.pushButton_Login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Login.setGeometry(QtCore.QRect(270, 830, 75, 23))
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.label_step3 = QtWidgets.QLabel(self.centralwidget)
        self.label_step3.setGeometry(QtCore.QRect(440, 780, 101, 16))
        self.label_step3.setObjectName("label_step3")
        self.pushButton_Upload = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Upload.setGeometry(QtCore.QRect(550, 780, 75, 23))
        self.pushButton_Upload.setObjectName("pushButton_Upload")
        self.label_Title = QtWidgets.QLabel(self.centralwidget)
        self.label_Title.setGeometry(QtCore.QRect(310, 10, 301, 16))
        self.label_Title.setObjectName("label_Title")
        self.label_Author = QtWidgets.QLabel(self.centralwidget)
        self.label_Author.setGeometry(QtCore.QRect(720, 860, 181, 16))
        self.label_Author.setObjectName("label_Author")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_step2.setText(_translate("MainWindow", "STEP2: LOGIN INTO YOUR INSTAGRAM ACCOUNT"))
        self.label_step1.setText(_translate("MainWindow", "STEP 1: GET PIC LINKS"))
        self.label_url_marca.setText(_translate("MainWindow", "Marca"))
        self.label_url_as.setText(_translate("MainWindow", "AS"))
        self.label_url_mundo.setText(_translate("MainWindow", "Mundo Deportivo"))
        self.label_url_sport.setText(_translate("MainWindow", "Sport"))
        self.label_insta_user.setText(_translate("MainWindow", "User:"))
        self.label_insta_pass.setText(_translate("MainWindow", "User:"))
        self.pushButton_GetPics.setText(_translate("MainWindow", "Get Pics"))
        self.pushButton_Login.setText(_translate("MainWindow", "Login"))
        self.label_step3.setText(_translate("MainWindow", "STEP3: Upload Pics"))
        self.pushButton_Upload.setText(_translate("MainWindow", "Upload"))
        self.label_Title.setText(_translate("MainWindow", "FRONT PAGE SPORT NEWSPAPERS INSTAGRAM UPLOADER"))
        self.label_Author.setText(_translate("MainWindow", "Powered by Flote (All rights reserved)"))

        # initializing the app.    
        init_app()
        self.bot = Bot()                      

        # mouse click connect functions
        self.pushButton_GetPics.clicked.connect(self.GetLinksAndPics)
        self.pushButton_Login.clicked.connect(self.InstaLogin)
        self.pushButton_Upload.clicked.connect(self.InstaUpload)

    def InstaUpload(self): 
        # Marca
        FrontPageName = "PortadaMarca.jpg"
        FrontPageNameResize = "PortadaMarca_resize.jpg"
        picPath = str(FOLDER) + "/marca/" + FrontPageName
        img_pil = Image.open(picPath)
        img_resize = InstaPicResize(img_pil, 1080, (255, 255, 255))
        img_resize.save(FrontPageNameResize)
        self.bot.upload_photo(FrontPageNameResize, caption =FrontPageName)
        os.remove(FrontPageNameResize + ".REMOVE_ME")        

        # As
        FrontPageName = "PortadaAs.jpg"
        FrontPageNameResize = "PortadaAs_resize.jpg"
        picPath = str(FOLDER) + "/as/" + FrontPageName
        img_pil = Image.open(picPath)
        img_resize = InstaPicResize(img_pil, 1080, (255, 255, 255))
        img_resize.save(FrontPageNameResize)
        self.bot.upload_photo(FrontPageNameResize, caption =FrontPageName)
        os.remove(FrontPageNameResize + ".REMOVE_ME")        

        # Mundo
        FrontPageName = "PortadaMundo.jpg"
        FrontPageNameResize = "PortadaMundo_resize.jpg"
        picPath = str(FOLDER) + "/mundo/" + FrontPageName
        img_pil = Image.open(picPath)
        img_resize = InstaPicResize(img_pil, 1080, (255, 255, 255))
        img_resize.save(FrontPageNameResize)
        self.bot.upload_photo(FrontPageNameResize, caption =FrontPageName)
        os.remove(FrontPageNameResize + ".REMOVE_ME")        

        # Sport
        FrontPageName = "PortadaSport.jpg"
        FrontPageNameResize = "PortadaSport_resize.jpg"
        picPath = str(FOLDER) + "/sport/" + FrontPageName
        img_pil = Image.open(picPath)
        img_resize = InstaPicResize(img_pil, 1080, (255, 255, 255))
        img_resize.save(FrontPageNameResize)
        self.bot.upload_photo(FrontPageNameResize, caption =FrontPageName)
        os.remove(FrontPageNameResize + ".REMOVE_ME")        


    def InstaLogin(self): 
        user = self.line_insta_user.text()
        password = self.line_insta_pass.text()
        print(user)
        print(password)        
        self.bot.login(username = user, password = password) 

    def GetLinksAndPics(self): 

        # launcho chrome
        driver = webdriver.Chrome("chromedriver.exe")

        #------Marca------#
        # download the Frontpage.
        url = URL_MARCA       
        pathToStore = str(FOLDER) + "/marca/"
        wordToFind = KEY_MARCA
        picname = "PortadaMarca"
        pic_download(driver, url, pathToStore, wordToFind, picname)        
        # set link in qline
        self.line_url_marca.setText(URL_MARCA)
        # set pic in qlabel
        load_pic = QtGui.QPixmap(pathToStore + picname + ".jpg")
        self.label_pic_marca.setPixmap(load_pic)

        #------AS------#
        # download the Frontpage.
        url = URL_AS       
        pathToStore = str(FOLDER) + "/as/"
        wordToFind = KEY_AS
        picname = "PortadaAS"
        pic_download(driver, url, pathToStore, wordToFind, picname)        
        # set link in qline
        self.line_url_as.setText(URL_AS)
        # set pic in qlabel
        load_pic = QtGui.QPixmap(pathToStore + picname + ".jpg")
        self.label_pic_as.setPixmap(load_pic)

        #------MUNDO------#
        # download the Frontpage.
        url = URL_MUNDO       
        pathToStore = str(FOLDER) + "/mundo/"
        wordToFind = KEY_MUNDO
        picname = "PortadaMundo"
        pic_download(driver, url, pathToStore, wordToFind, picname)        
        # set link in qline
        self.line_url_mundo.setText(URL_MUNDO)
        # set pic in qlabel
        load_pic = QtGui.QPixmap(pathToStore + picname + ".jpg")
        self.label_pic_mundo.setPixmap(load_pic)

        #------SPORT------#
        # download the Frontpage.
        url = URL_SPORT
        pathToStore = str(FOLDER) + "/sport/"
        wordToFind = KEY_SPORT
        picname = "PortadaSport"
        pic_download(driver, url, pathToStore, wordToFind, picname)        
        # set link in qline
        self.line_url_sport.setText(URL_SPORT)
        # set pic in qlabel
        load_pic = QtGui.QPixmap(pathToStore + picname + ".jpg")
        self.label_pic_sport.setPixmap(load_pic)      
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
