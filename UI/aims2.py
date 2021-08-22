# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aims2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from . import stylesheet

class Ui_MainWindow(object):
    def __init__(self):
        self.sizeX = 900
        self.sizeY = 600
    def setupUi(self, MainWindow):
        
        #   MAIN WINDOW
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(self.sizeX, self.sizeY)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        
        palette = QtGui.QPalette()
        stylesheet.style_main_window(palette)
        MainWindow.setPalette(palette)
        
        MainWindow.setToolTip("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #~~~~~~~~~TAB WIDGET~~~~~~#
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, self.sizeX, self.sizeY))
        
        palette = QtGui.QPalette()
        stylesheet.style_tab_widget(palette)       
        self.tabWidget.setPalette(palette)
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")
        
        #~~~ADD ALBUM TAB~~~#
        
        self.AddAlbum = QtWidgets.QWidget()
        self.AddAlbum.setAutoFillBackground(True)
        self.AddAlbum.setObjectName("AddAlbum")
        #ARTIST NAME ENTRY
        self.ArtistName = QtWidgets.QLineEdit(self.AddAlbum)
        self.ArtistName.setGeometry(QtCore.QRect(330, 200, 241, 20))
        self.ArtistName.setCursorPosition(0)
        self.ArtistName.setObjectName("ArtistName")
        #ALBUM TITLE ENTRY
        self.lineEdit = QtWidgets.QLineEdit(self.AddAlbum)
        self.lineEdit.setGeometry(QtCore.QRect(330, 260, 241, 20))
        self.lineEdit.setFrame(True)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setObjectName("lineEdit")
        #SEARCH BUTTON
        self.pushButton = QtWidgets.QPushButton(self.AddAlbum)
        self.pushButton.setGeometry(QtCore.QRect(400, 340, 101, 31))
        
        palette = QtGui.QPalette()
        stylesheet.style_pushbutton(palette)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.AddAlbum)
        self.label.setGeometry(QtCore.QRect(420, 180, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.AddAlbum)
        self.label_2.setGeometry(QtCore.QRect(420, 240, 71, 21))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.AddAlbum, "")
        #END OF ADD ALBUM TAB
        
        #~~~~Warehouse Tab~~~~
        self.MyWareHouse = QtWidgets.QWidget()
        self.MyWareHouse.setObjectName("MyWareHouse")
        self.MyWareHouse.setStyleSheet("background-color:rgb(148, 166, 187)")
        self.tabWidget.addTab(self.MyWareHouse, "")
        #TableWidget
        self.load_table_button = QtWidgets.QPushButton(self.MyWareHouse)
        self.load_table_button.setGeometry(QtCore.QRect(400, 300, 100, 30))
        self.load_table_button.setText("Load Inventory")
        palette = QtGui.QPalette()
        stylesheet.style_pushbutton(palette)
        self.load_table_button.setStyleSheet("background-color:rgb(180, 180, 180)")
        
        
        
        #~~~~Shop Tab
        self.MyShop = QtWidgets.QWidget()
        self.MyShop.setObjectName("MyShop")
        
        
        #~~~~Orders Tab
        self.MyOrders = QtWidgets.QWidget()
        self.MyOrders.setObjectName("MyOrders")
        
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "A.I.M.S"))
        self.ArtistName.setText(_translate("MainWindow", "Enter Artist Name"))
        self.lineEdit.setText(_translate("MainWindow", "Enter Album Title"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Artist Name"))
        self.label_2.setText(_translate("MainWindow", "Album Name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AddAlbum), _translate("MainWindow", "Add Album"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MyWareHouse), _translate("MainWindow", "My Warehouse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MyShop), _translate("MainWindow", "My Shop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MyOrders), _translate("MainWindow", "My Orders"))
    
    
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.tabWidget.setCurrentWidget(ui.AddAlbum)
    MainWindow.show()
    sys.exit(app.exec_())
