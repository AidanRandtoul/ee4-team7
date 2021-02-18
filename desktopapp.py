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
        MainWindow.resize(845, 520)
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
        self.line_2.setGeometry(QtCore.QRect(330, 40, 20, 431))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(340, 140, 471, 20))
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
        self.graphOneTwo = QtWidgets.QGraphicsView(self.front)
        self.graphOneTwo.setGeometry(QtCore.QRect(10, 40, 281, 111))
        self.graphOneTwo.setObjectName("graphOneTwo")
        self.label_2 = QtWidgets.QLabel(self.front)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 91, 17))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.front)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 91, 17))
        self.label_5.setObjectName("label_5")
        self.graphThreeFour = QtWidgets.QGraphicsView(self.front)
        self.graphThreeFour.setGeometry(QtCore.QRect(10, 180, 281, 121))
        self.graphThreeFour.setObjectName("graphThreeFour")
        self.tabWidget.addTab(self.front, "")
        self.back = QtWidgets.QWidget()
        self.back.setObjectName("back")
        self.label_6 = QtWidgets.QLabel(self.back)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 91, 17))
        self.label_6.setObjectName("label_6")
        self.graphFiveSix = QtWidgets.QGraphicsView(self.back)
        self.graphFiveSix.setGeometry(QtCore.QRect(10, 40, 281, 111))
        self.graphFiveSix.setObjectName("graphFiveSix")
        self.label_7 = QtWidgets.QLabel(self.back)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 91, 17))
        self.label_7.setObjectName("label_7")
        self.graphSevenEight = QtWidgets.QGraphicsView(self.back)
        self.graphSevenEight.setGeometry(QtCore.QRect(10, 180, 281, 121))
        self.graphSevenEight.setObjectName("graphSevenEight")
        self.tabWidget.addTab(self.back, "")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 40, 471, 111))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 67, 17))
        self.label_3.setObjectName("label_3")
        self.speedNumber = QtWidgets.QLCDNumber(self.groupBox_2)
        self.speedNumber.setGeometry(QtCore.QRect(30, 40, 121, 41))
        self.speedNumber.setObjectName("speedNumber")
        self.aoiNumber = QtWidgets.QLCDNumber(self.groupBox_2)
        self.aoiNumber.setGeometry(QtCore.QRect(270, 40, 121, 41))
        self.aoiNumber.setObjectName("aoiNumber")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(260, 20, 141, 17))
        self.label_4.setObjectName("label_4")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(350, 160, 451, 301))
        self.listWidget.setObjectName("listWidget")
        self.rtToggle = QtWidgets.QRadioButton(self.centralwidget)
        self.rtToggle.setGeometry(QtCore.QRect(365, 170, 141, 16))
        self.rtToggle.setObjectName("rtToggle")

        # Command arrows
        self.arrowRight = QtWidgets.QPushButton(self.centralwidget)
        self.arrowRight.setGeometry(QtCore.QRect(700, 230, 80, 80))
        self.arrowRight.setStyleSheet("border-image: url(:/images/Right Arrow.png);")
        self.arrowRight.setText("")
        self.arrowRight.setObjectName("arrowRight")
        self.arrowDown = QtWidgets.QPushButton(self.centralwidget)
        self.arrowDown.setGeometry(QtCore.QRect(650, 280, 80, 80))
        self.arrowDown.setStyleSheet("border-image: url(:/images/Down Arrow.png);")
        self.arrowDown.setText("")
        self.arrowDown.setObjectName("arrowDown")
        self.arrowUp = QtWidgets.QPushButton(self.centralwidget)
        self.arrowUp.setGeometry(QtCore.QRect(650, 180, 80, 80))
        self.arrowUp.setStyleSheet("border-image: url(:/images/Up Arrow.png);")
        self.arrowUp.setText("")
        self.arrowUp.setObjectName("arrowUp")
        self.arrowLeft = QtWidgets.QPushButton(self.centralwidget)
        self.arrowLeft.setGeometry(QtCore.QRect(600, 230, 80, 80))
        self.arrowLeft.setStyleSheet("border-image: url(:/images/Left Arrow.png);")
        self.arrowLeft.setText("")
        self.arrowLeft.setObjectName("arrowLeft")

        # Command list object
        self.commandList = QtWidgets.QListWidget(self.centralwidget)
        self.commandList.setGeometry(QtCore.QRect(375, 190, 121, 191))
        self.commandList.setObjectName("commandList")

        # Command duration object
        self.commDuration = QtWidgets.QSpinBox(self.centralwidget)
        self.commDuration.setGeometry(QtCore.QRect(550, 180, 42, 22))
        self.commDuration.setObjectName("commDuration")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(530, 160, 111, 21))
        self.label_8.setObjectName("label_8")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(800, 40, 20, 431))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.SendButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendButton.setGeometry(QtCore.QRect(355, 385, 51, 21))
        self.SendButton.setObjectName("SendButton")
        self.ClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButton.setGeometry(QtCore.QRect(465, 385, 51, 21))
        self.ClearButton.setObjectName("ClearButton")
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(410, 385, 51, 21))
        self.DeleteButton.setObjectName("DeleteButton")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(340, 460, 471, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.groupBox_2.raise_()
        self.label.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.groupBox.raise_()
        self.listWidget.raise_()
        self.rtToggle.raise_()
        self.arrowRight.raise_()
        self.arrowDown.raise_()
        self.arrowUp.raise_()
        self.arrowLeft.raise_()
        self.commandList.raise_()
        self.commDuration.raise_()
        self.label_8.raise_()
        self.line_4.raise_()
        self.SendButton.raise_()
        self.ClearButton.raise_()
        self.DeleteButton.raise_()
        self.line_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.SendButton.clicked.connect(self.addToList)
        self.ClearButton.clicked.connect(self.clearCommands)
        self.DeleteButton.clicked.connect(self.deleteCommands)

    def sendCommands(self):
        print("Sent commands to the rover!")
        

    def clearCommands(self):
        print("Cleared command queue!")
        self.commandList.clear()

    def deleteCommands(self):
        print("Deleted last command from queue!")
        model = self.commandList.model()
        for item in self.commandList.selectedItems():
            index = self.commandList.indexFromItem(item)
            model.removeRow(index.row())
    

    def addToList(self):
        print("adding item")
        self.commandList.insertItem(0, "test")
        self.commandList.insertItem(1, "two")
        self.commandList.repaint()


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
        self.rtToggle.setText(_translate("MainWindow", "Toggle Command Queue"))
        self.label_8.setText(_translate("MainWindow", "Command Duration"))
        self.SendButton.setText(_translate("MainWindow", "Send"))
        self.ClearButton.setText(_translate("MainWindow", "Clear"))
        self.DeleteButton.setText(_translate("MainWindow", "Delete"))
import Resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())