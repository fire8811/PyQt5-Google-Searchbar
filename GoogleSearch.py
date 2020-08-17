# Opens default browser and Google searches text in the window's searchbar
#
# Created by: Jenson Jones using PyQt5 UI code generator 5.15.0


from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser,requests, bs4

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(768, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(680, 500, 113, 32))
        self.closeButton.setObjectName("closeButton")
        
        self.searchbar = QtWidgets.QLineEdit(self.centralwidget)
        self.searchbar.setGeometry(QtCore.QRect(190, 160, 391, 31))
        self.searchbar.setObjectName("searchbar")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(290, 100, 261, 41))
        
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(590, 160, 140, 31))
        self.checkBox.setObjectName("checkBox")
        
        self.launchButton = QtWidgets.QPushButton(self.centralwidget)
        self.launchButton.setGeometry(QtCore.QRect(390, 210, 81, 32))
        self.launchButton.setAutoFillBackground(False)
        self.launchButton.setDefault(True)
        self.launchButton.setFlat(False)
        self.launchButton.setObjectName("launchButton")
       
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(300, 210, 81, 32))
        self.clearButton.setAutoFillBackground(False)
        self.clearButton.setDefault(False)
        self.clearButton.setFlat(False)
        self.clearButton.setObjectName("clearButton")
       
        MainWindow.setCentralWidget(self.centralwidget)
       
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
       
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionFavorites = QtWidgets.QAction(MainWindow)
        self.actionFavorites.setObjectName("actionFavorites")
        self.menuFile.addAction(self.actionFavorites)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #********** CLICK EVENT TRIGGERS **********
        self.launchButton.clicked.connect(self.launchClicked)
        self.clearButton.clicked.connect(self.clearClicked)
        self.searchbar.returnPressed.connect(self.launchClicked) #if return is pressed go to launchClicked

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.closeButton.setText(_translate("MainWindow", "Close"))
        self.label1.setText(_translate("MainWindow", "Enter Google Request:"))
        self.checkBox.setText(_translate("MainWindow", "Go to First Result"))
        self.launchButton.setText(_translate("MainWindow", "Go!"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionFavorites.setText(_translate("MainWindow", "Favorites"))
        self.actionFavorites.setStatusTip(_translate("MainWindow", "Your bookmarked links"))
        self.actionFavorites.setShortcut(_translate("MainWindow", "Ctrl+F"))

    def firstResult(self):
        from googlesearch import search

        if (self.checkBox.isChecked()):
            userInput = self.searchbar.text()

            for j in search(userInput, tld="com", num=1, stop=1, pause=2): #get the first result Google returns
                res = j
                webbrowser.open(res) #open first google search result in default browswer

        else:
            pass   

    def launchClicked(self):
        userInput = self.searchbar.text() #get text in searchbar
        print(userInput)

        if(self.checkBox.isChecked()):
            self.firstResult()
        else:
            googleUrl = "https://google.com/?#q="
            webbrowser.open(googleUrl+userInput, new=2) #open result to google

    def clearClicked(self): #clears the text in the searchbar
        self.searchbar.setText("") #needs to be "" and not " " or else it doesn't work for some reason
        self.searchbar.repaint()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

