# IMPORTING ALL THE NECESSERY PYSIDE6 MODULES FOR OUR APPLICATION.
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
import pyodbc
from ui_main1 import Ui_MainWindow
from ui_function import *


# OUR APPLICATION MAIN WINDOW :
# -----> MAIN APPLICATION CLASS
class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ----> SET WINDOW TITLE AND ICON
        applicationName = ""
        ############################################################
        self.setWindowTitle(applicationName)
        ############################################################
        UIFunction.labelTitle(self, applicationName)
        ############################################################
        UIFunction.initStackTab(self)
        ############################################################
        UIFunction.constantFunction(self)
        #############################################################
        self.ui.bn_home.clicked.connect(
            lambda: UIFunction.buttonPressed(self, 'bn_home', connection, cursor))
        # repeat for every button

        #############################################################
        UIFunction.stackPage(self)
        #############################################################
        #############################################################

        #############################################################

        self.ui.bn_bug_start.clicked.connect(
            lambda: UIFunction.buttonPressed(self, 'bn_bug_start', connection, cursor))
        self.ui.bn_cloud_connect.clicked.connect(
            lambda: UIFunction.buttonPressed(self, "bn_cloud_connect", connection, cursor))
        self.ui.bn_cloud_clear.clicked.connect(
            lambda: APFunction.cloudClear(self))

        self.dragPos = self.pos()

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunction.returStatus() == 1:
                UIFunction.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_appname.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    #############################################################


if __name__ == "__main__":
    try:
        # Hena a3ml connect lel database
        print("Connection Established")
        connection.autocommit = True
        cursor = connection.cursor()
    except pyodbc.Error as e:
        print("Connection Failed", e)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

############################################################################################################################################################
