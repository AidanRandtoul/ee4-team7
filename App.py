#! /usr/bin/python3.3

import sys
from PyQt5 import QtGui
from desktopapp import  Ui_MainWindow
def main():
    app = QtGui.QApplication (sys.argv)
    m = Ui_MainWindow ()
    m.show ()
    sys.exit (app.exec_ () )


if __name__ == '__main__':
    main ()