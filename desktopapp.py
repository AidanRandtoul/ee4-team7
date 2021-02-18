# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desktopapp.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(817, 467)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 261, 17))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 30, 801, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(330, 50, 16, 391))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(340, 170, 471, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 321, 381))
        self.groupBox.setObjectName("groupBox")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 301, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.front = QtWidgets.QWidget()
        self.front.setObjectName("front")
        self.graphicsView = QtWidgets.QGraphicsView(self.front)
        self.graphicsView.setGeometry(QtCore.QRect(10, 40, 281, 111))
        self.graphicsView.setObjectName("graphicsView")
        self.label_2 = QtWidgets.QLabel(self.front)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 91, 17))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.front)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 91, 17))
        self.label_5.setObjectName("label_5")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.front)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 180, 281, 121))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.tabWidget.addTab(self.front, "")
        self.back = QtWidgets.QWidget()
        self.back.setObjectName("back")
        self.label_6 = QtWidgets.QLabel(self.back)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 91, 17))
        self.label_6.setObjectName("label_6")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.back)
        self.graphicsView_3.setGeometry(QtCore.QRect(10, 30, 281, 121))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.label_7 = QtWidgets.QLabel(self.back)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 91, 17))
        self.label_7.setObjectName("label_7")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.back)
        self.graphicsView_4.setGeometry(QtCore.QRect(10, 180, 281, 121))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.tabWidget.addTab(self.back, "")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(350, 30, 461, 141))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 30, 67, 17))
        self.label_3.setObjectName("label_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 70, 121, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber_2.setGeometry(QtCore.QRect(270, 70, 121, 41))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(260, 30, 141, 17))
        self.label_4.setObjectName("label_4")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(350, 190, 451, 231))
        self.listWidget.setObjectName("listWidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(360, 400, 141, 16))
        self.radioButton.setObjectName("radioButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 250, 80, 80))
        self.pushButton.setStyleSheet("border-image: url(:/images/Right Arrow.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 300, 80, 80))
        self.pushButton_2.setStyleSheet("border-image: url(:/images/Down Arrow.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.upButton = QtWidgets.QPushButton(self.centralwidget)
        self.upButton.setGeometry(QtCore.QRect(650, 200, 80, 80))
        self.upButton.setStyleSheet("border-image: url(:/images/Up Arrow.png);")
        self.upButton.setText("")
        self.upButton.setObjectName("upButton")

        def say_hello(self):
            print("Button clicked, Hello!")
        self.upButton.clicked.connect(say_hello)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(600, 250, 80, 80))
        self.pushButton_4.setStyleSheet("border-image: url(:/images/Left Arrow.png);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(370, 200, 121, 191))
        self.listView.setObjectName("listView")
        self.groupBox_2.raise_()
        self.label.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.groupBox.raise_()
        self.listWidget.raise_()
        self.radioButton.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.upButton.raise_()
        self.pushButton_4.raise_()
        self.listView.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 817, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Double Rocker Rover Control Window"))
        self.groupBox.setTitle(_translate("MainWindow", "Motor RPMs"))
        self.label_2.setText(_translate("MainWindow", "Motors 1 & 2"))
        self.label_5.setText(_translate("MainWindow", "Motors 3 & 4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.front), _translate("MainWindow", "Front"))
        self.label_6.setText(_translate("MainWindow", "Motors 5 & 6"))
        self.label_7.setText(_translate("MainWindow", "Motors 7 & 8"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.back), _translate("MainWindow", "Back"))
        self.label_3.setText(_translate("MainWindow", "Speed"))
        self.label_4.setText(_translate("MainWindow", "Angle of Inclination"))
        self.radioButton.setText(_translate("MainWindow", "Toggle Command Queue"))
import Resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
