# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from my_lib import *
from selenium import webdriver
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1006, 967)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_url_as = QtWidgets.QLineEdit(self.centralwidget)
        self.line_url_as.setGeometry(QtCore.QRect(100, 70, 331, 20))
        self.line_url_as.setObjectName("line_url_as")
        self.label_step2 = QtWidgets.QLabel(self.centralwidget)
        self.label_step2.setGeometry(QtCore.QRect(20, 780, 241, 16))
        self.label_step2.setObjectName("label_step2")
        self.label_step1 = QtWidgets.QLabel(self.centralwidget)
        self.label_step1.setGeometry(QtCore.QRect(20, 30, 121, 16))
        self.label_step1.setObjectName("label_step1")
        self.label_url_as = QtWidgets.QLabel(self.centralwidget)
        self.label_url_as.setGeometry(QtCore.QRect(50, 70, 31, 16))
        self.label_url_as.setObjectName("label_url_as")
        self.label_url_marca = QtWidgets.QLabel(self.centralwidget)
        self.label_url_marca.setGeometry(QtCore.QRect(450, 70, 31, 16))
        self.label_url_marca.setObjectName("label_url_marca")
        self.label_url_mundo = QtWidgets.QLabel(self.centralwidget)
        self.label_url_mundo.setGeometry(QtCore.QRect(430, 430, 91, 16))
        self.label_url_mundo.setObjectName("label_url_mundo")
        self.label_url_sport = QtWidgets.QLabel(self.centralwidget)
        self.label_url_sport.setGeometry(QtCore.QRect(50, 430, 41, 16))
        self.label_url_sport.setObjectName("label_url_sport")
        self.label_pic_as = QtWidgets.QLabel(self.centralwidget)
        self.label_pic_as.setGeometry(QtCore.QRect(140, 100, 251, 291))
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
        self.label_pic_marca = QtWidgets.QLabel(self.centralwidget)
        self.label_pic_marca.setGeometry(QtCore.QRect(540, 100, 251, 291))
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
        self.line_url_marca = QtWidgets.QLineEdit(self.centralwidget)
        self.line_url_marca.setGeometry(QtCore.QRect(500, 70, 331, 20))
        self.line_url_marca.setObjectName("line_url_marca")
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
        self.label_insta_user.setGeometry(QtCore.QRect(20, 840, 31, 16))
        self.label_insta_user.setObjectName("label_insta_user")
        self.label_insta_pass = QtWidgets.QLabel(self.centralwidget)
        self.label_insta_pass.setGeometry(QtCore.QRect(20, 870, 31, 16))
        self.label_insta_pass.setObjectName("label_insta_pass")
        self.line_insta_user = QtWidgets.QLineEdit(self.centralwidget)
        self.line_insta_user.setGeometry(QtCore.QRect(60, 840, 141, 20))
        self.line_insta_user.setObjectName("line_insta_user")
        self.line_insta_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.line_insta_pass.setGeometry(QtCore.QRect(60, 870, 141, 20))
        self.line_insta_pass.setObjectName("line_insta_pass")
        self.pushButton_GetPics = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GetPics.setGeometry(QtCore.QRect(170, 30, 75, 23))
        self.pushButton_GetPics.setObjectName("pushButton_GetPics")
        self.pushButton_Login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Login.setGeometry(QtCore.QRect(220, 860, 75, 23))
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.label_step3 = QtWidgets.QLabel(self.centralwidget)
        self.label_step3.setGeometry(QtCore.QRect(370, 780, 111, 16))
        self.label_step3.setObjectName("label_step3")
        self.pushButton_Upload = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Upload.setGeometry(QtCore.QRect(510, 780, 75, 23))
        self.pushButton_Upload.setObjectName("pushButton_Upload")
        self.label_Title = QtWidgets.QLabel(self.centralwidget)
        self.label_Title.setGeometry(QtCore.QRect(310, 10, 511, 31))
        self.label_Title.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_Title.setLineWidth(2)
        self.label_Title.setTextFormat(QtCore.Qt.AutoText)
        self.label_Title.setObjectName("label_Title")
        self.label_Author = QtWidgets.QLabel(self.centralwidget)
        self.label_Author.setGeometry(QtCore.QRect(800, 920, 191, 20))
        self.label_Author.setObjectName("label_Author")
        self.label_post = QtWidgets.QLabel(self.centralwidget)
        self.label_post.setGeometry(QtCore.QRect(470, 810, 41, 16))
        self.label_post.setObjectName("label_post")
        self.label_hashtag = QtWidgets.QLabel(self.centralwidget)
        self.label_hashtag.setGeometry(QtCore.QRect(760, 780, 81, 16))
        self.label_hashtag.setObjectName("label_hashtag")
        self.text_post = QtWidgets.QTextEdit(self.centralwidget)
        self.text_post.setGeometry(QtCore.QRect(360, 830, 271, 71))
        self.text_post.setObjectName("text_post")
        self.text_hashtag = QtWidgets.QTextEdit(self.centralwidget)
        self.text_hashtag.setGeometry(QtCore.QRect(640, 800, 341, 111))
        self.text_hashtag.setObjectName("text_hashtag")
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
        self.label_url_as.setText(_translate("MainWindow", "As"))
        self.label_url_marca.setText(_translate("MainWindow", "Marca"))
        self.label_url_mundo.setText(_translate("MainWindow", "Mundo Deportivo"))
        self.label_url_sport.setText(_translate("MainWindow", "Sport"))
        self.label_insta_user.setText(_translate("MainWindow", "User:"))
        self.label_insta_pass.setText(_translate("MainWindow", "User:"))
        self.pushButton_GetPics.setText(_translate("MainWindow", "Get Pics"))
        self.pushButton_Login.setText(_translate("MainWindow", "Login"))
        self.label_step3.setText(_translate("MainWindow", "STEP3: UPLOAD PICS"))
        self.pushButton_Upload.setText(_translate("MainWindow", "Upload"))
        self.label_Title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">FRONT PAGE SPORT NEWSPAPERS INSTAGRAM UPLOADER</span></p></body></html>"))
        self.label_Author.setText(_translate("MainWindow", "Powered by Flote (flote21@gmail.com)"))
        self.label_post.setText(_translate("MainWindow", "Post"))
        self.label_hashtag.setText(_translate("MainWindow", "# hashtags"))

        # mouse click connect functions
        self.pushButton_GetPics.clicked.connect(self.getLinksAndPics)
        self.pushButton_Login.clicked.connect(self.loginWebsites)
        self.pushButton_Upload.clicked.connect(self.uploadPics)

        # load fix message in status bar
        self.status_label = QtWidgets.QLabel()
        MainWindow.statusBar().addPermanentWidget(self.status_label, 100)
        self.status_label.setText(("Here are the instructions..."))

        # Set default username & pass
        self.line_insta_user.setText("portatest")
        self.line_insta_pass.setText("kikazo")

        # show default post and hashtags
        date = time.strftime("%d/%m/%y")
        post = "Portadas de hoy " + str(date)        
        self.text_post.setPlainText(post)
        hashtags = "#portadas #portad_as_ymas #diarioas#diariomarca\
                    #diariosport #mundodeportivo #deporte#futbol\
                    #laligasantander #uefachampionsleague #championsleague\
                    #realmadridcf #zidane #sergioramos #benzema #modric\
                    #cristianoronaldo #fcbarcelona #koeman #messi #pedri\
                    #neymar #atleticodemadrid #simeone #marcosllorente\
                    #oblak #jaofelix #luissuarez #hazard"
        self.text_hashtag.setPlainText(hashtags)

        kk = self.text_hashtag.toPlainText()
        print(kk)
    
    def uploadPics(self): 
        self.status_label.setText(("Pics uploading, wait..."))
        studioCreatorUpload(self.driver, self.text_post, self.text_hashtag)
        time.sleep(5)
        instagramLogout(self.driver)         
        self.status_label.setText(("Pics upload successfully!"))

    def loginWebsites(self): 
    # Method used to login into the websited
        self.status_label.setText(("Login into the website, wait"))
        # load studio creator webpage
        window_before, self.driver = studioCreatorLogin()                      
        # Get user/pass from the GUI cells.
        username = self.line_insta_user.text()
        password = self.line_insta_pass.text()
        print(username)
        print(password)  
        instagramLogin(self.driver, username, password)
        # Wait 3sec until the old windows is loaded
        time.sleep(3)
        # Switch to the old window
        self.driver.switch_to_window(window_before)
        self.status_label.setText(("Login successfully, go to next step"))  

    def getLinksAndPics(self): 
    # Method used to dwonload pics from the website
        self.status_label.setText(("Downloading pics, wait"))
        # launch chrome
        driver_webpic = webdriver.Chrome("chromedriver.exe", options=chromeOptions())
        driver_webpic.implicitly_wait(2)
        # create folder to save the pics
        createFolderPics()

        #------AS------#
        # download the Frontpage.
        url = URL_AS       
        pathToStore = str(FOLDER) + "/as/"
        wordToFind = KEY_AS
        picname = "PortadaAS"
        downloadPic(driver_webpic, url, pathToStore, wordToFind, picname)        
        # set link in qline
        self.line_url_as.setText(URL_AS)
        # set pic in qlabel
        load_pic = QtGui.QPixmap(pathToStore + picname + ".jpg")
        self.label_pic_as.setPixmap(load_pic)
        
        #------Marca------#
        # download the Frontpage.
        url = URL_MARCA       
        pathToStore = str(FOLDER) + "/marca/"
        wordToFind = KEY_MARCA
        picname = "PortadaMarca"
        downloadPic(driver_webpic, url, pathToStore, wordToFind, picname)        
        # set link in qline
        self.line_url_marca.setText(URL_MARCA)
        # set pic in qlabel
        load_pic = QtGui.QPixmap(pathToStore + picname + ".jpg")
        self.label_pic_marca.setPixmap(load_pic)

        #------MUNDO------#
        # download the Frontpage.
        url = URL_MUNDO       
        pathToStore = str(FOLDER) + "/mundo/"
        wordToFind = KEY_MUNDO
        picname = "PortadaMundo"
        downloadPic(driver_webpic, url, pathToStore, wordToFind, picname)        
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
        downloadPic(driver_webpic, url, pathToStore, wordToFind, picname)        
        # set link in qline
        self.line_url_sport.setText(URL_SPORT)
        # set pic in qlabel
        load_pic = QtGui.QPixmap(pathToStore + picname + ".jpg")
        self.label_pic_sport.setPixmap(load_pic)

        # Close the window website
        driver_webpic.close()  

        self.status_label.setText(("Pics downloaded successfully, go to next step"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
