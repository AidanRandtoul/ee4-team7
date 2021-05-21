# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desktopapp.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import serial
from time import sleep

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 520)

        self.commQueue = False  # Toggle for command operation mode set to False initially

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 321, 381))
        self.groupBox.setObjectName("groupBox")

        self.commandHistory = QtWidgets.QListWidget(self.groupBox)
        self.commandHistory.setGeometry(QtCore.QRect(10, 20, 301, 351))
        self.commandHistory.setObjectName("commandHistory")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 40, 471, 111))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")

        # -------------- Status Display -------------- #
        # Rover speed display
        self.speedNumber = QtWidgets.QLCDNumber(self.groupBox_2)
        self.speedNumber.setGeometry(QtCore.QRect(30, 40, 121, 41))
        self.speedNumber.setObjectName("speedNumber")

        # Rover inclination display
        self.aoiNumber = QtWidgets.QLCDNumber(self.groupBox_2)
        self.aoiNumber.setGeometry(QtCore.QRect(270, 40, 121, 41))
        self.aoiNumber.setObjectName("aoiNumber")

        # -------------- Command arrows -------------- #
        # Up
        self.arrowUp = QtWidgets.QPushButton(self.centralwidget)
        self.arrowUp.setGeometry(QtCore.QRect(650, 200, 80, 80))
        self.arrowUp.setStyleSheet("border-image: url(:/images/Up Arrow.png);")
        self.arrowUp.setText("")
        self.arrowUp.setObjectName("arrowUp")
        self.arrowUp.clicked.connect(lambda: self.arrowPush("arrowUp"))

        # Down
        self.arrowDown = QtWidgets.QPushButton(self.centralwidget)
        self.arrowDown.setGeometry(QtCore.QRect(650, 300, 80, 80))
        self.arrowDown.setStyleSheet("border-image: url(:/images/Down Arrow.png);")
        self.arrowDown.setText("")
        self.arrowDown.setObjectName("arrowDown")
        self.arrowDown.clicked.connect(lambda: self.arrowPush("arrowDown"))

        # Left
        self.arrowLeft = QtWidgets.QPushButton(self.centralwidget)
        self.arrowLeft.setGeometry(QtCore.QRect(600, 250, 80, 80))
        self.arrowLeft.setStyleSheet("border-image: url(:/images/Left Arrow.png);")
        self.arrowLeft.setText("")
        self.arrowLeft.setObjectName("arrowLeft")
        self.arrowLeft.clicked.connect(lambda: self.arrowPush("arrowLeft"))

        # Right
        self.arrowRight = QtWidgets.QPushButton(self.centralwidget)
        self.arrowRight.setGeometry(QtCore.QRect(700, 250, 80, 80))
        self.arrowRight.setStyleSheet("border-image: url(:/images/Right Arrow.png);")
        self.arrowRight.setText("")
        self.arrowRight.setObjectName("arrowRight")
        self.arrowRight.clicked.connect(lambda: self.arrowPush("arrowRight"))

        # -------------- Command Controls -------------- #
        # Command mode toggle
        self.rtToggle = QtWidgets.QRadioButton(self.centralwidget)
        self.rtToggle.setGeometry(QtCore.QRect(365, 170, 141, 16))
        self.rtToggle.setObjectName("rtToggle")
        self.rtToggle.clicked.connect(self.toggle)

        # Command list
        self.commandList = QtWidgets.QListWidget(self.centralwidget)
        self.commandList.setGeometry(QtCore.QRect(375, 190, 121, 191))
        self.commandList.setObjectName("commandList")

        # Command duration
        self.commDuration = QtWidgets.QSpinBox(self.centralwidget)
        self.commDuration.setGeometry(QtCore.QRect(550, 180, 42, 22))
        self.commDuration.setObjectName("commDuration")

        # Send Button
        self.SendButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendButton.setGeometry(QtCore.QRect(355, 385, 51, 21))
        self.SendButton.setObjectName("SendButton")
        self.SendButton.clicked.connect(self.sendCommands)

        # Clear Button
        self.ClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButton.setGeometry(QtCore.QRect(465, 385, 51, 21))
        self.ClearButton.setObjectName("ClearButton")
        self.ClearButton.clicked.connect(self.clearCommands)

        # Delete Button
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(410, 385, 51, 21))
        self.DeleteButton.setObjectName("DeleteButton")
        self.DeleteButton.clicked.connect(self.deleteCommands)

        # -------------- Dividing Lines -------------- #

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(340, 30, 471, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(330, 40, 20, 395))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(340, 140, 471, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(800, 40, 20, 395))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(340, 425, 471, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)

        # -------------- Labels -------------- #

        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(280, 10, 261, 17))
        self.mainLabel.setObjectName("mainLabel")

        self.speedLabel = QtWidgets.QLabel(self.groupBox_2)
        self.speedLabel.setGeometry(QtCore.QRect(30, 20, 67, 17))
        self.speedLabel.setObjectName("speedLabel")

        self.angleLabel = QtWidgets.QLabel(self.groupBox_2)
        self.angleLabel.setGeometry(QtCore.QRect(260, 20, 141, 17))
        self.angleLabel.setObjectName("angleLabel")

        self.durationLabel = QtWidgets.QLabel(self.centralwidget)
        self.durationLabel.setGeometry(QtCore.QRect(530, 160, 111, 21))
        self.durationLabel.setObjectName("durationLabel")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # -------------- Functionality -------------- #

    def toggle(self):
        self.commQueue = not(self.commQueue)

    def sendCommands(self):
        ser = serial.Serial('COM3', 9600, timeout=1)
        sleep(2)
        items = []

        for index in range(self.commandList.count()):
            command = self.commandList.item(index).text()
            direction, duration = command.split(', ')
            direction = direction[5:]

            ser.write(bytes(direction[0].lower(), 'ascii'))
            items.append([direction, duration])

        ser.write(b's')
        sleep(4)
        print(ser.readlines())
        print(items)
        ser.close()

    def clearCommands(self):
        print("Cleared command queue!")
        self.commandList.clear()

    def deleteCommands(self):
        print("Deleted selected command from queue!")
        model = self.commandList.model()
        for item in self.commandList.selectedItems():
            index = self.commandList.indexFromItem(item)
            model.removeRow(index.row())

    def arrowPush(self, name):
        if self.commQueue:
            self.commandList.addItem("%s, %s" %(name, self.commDuration.text()))
            self.commandList.repaint()
        else:
            print([name[5:], self.commDuration.text()])

        # -------------- #

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainLabel.setText(_translate("MainWindow", "Double Rocker Rover Control Window"))
        self.groupBox.setTitle(_translate("MainWindow", "Command History"))
        self.speedLabel.setText(_translate("MainWindow", "Speed"))
        self.angleLabel.setText(_translate("MainWindow", "Angle of Inclination"))
        self.rtToggle.setText(_translate("MainWindow", "Toggle Command Queue"))
        self.durationLabel.setText(_translate("MainWindow", "Command Duration"))
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
