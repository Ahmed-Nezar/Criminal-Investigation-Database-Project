import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget
from StartMenu import StartMenu
from Login import Login
from OfficerMainMenu import OfficerMainMenu
from Cases import Cases
from Criminals import Criminals
from Suspects import Suspects
from Victims import Victims
from Witnesses import Witnesses
from Officers import Officers
import pyodbc
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crime Investigation System")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.start_menu = StartMenu()
        self.login = Login()
        self.officer_main_menu = OfficerMainMenu()
        self.cases = Cases()
        self.criminals = Criminals()
        self.suspects = Suspects()
        self.victims = Victims()
        self.witnesses = Witnesses()
        self.officers = Officers()

        self.stacked_widget.addWidget(self.start_menu)
        self.stacked_widget.addWidget(self.login)
        self.stacked_widget.addWidget(self.officer_main_menu)
        self.stacked_widget.addWidget(self.cases)
        self.stacked_widget.addWidget(self.criminals)
        self.stacked_widget.addWidget(self.suspects)
        self.stacked_widget.addWidget(self.victims)
        self.stacked_widget.addWidget(self.witnesses)
        self.stacked_widget.addWidget(self.officers)

        self.start_menu.OfficerMenuBtn.clicked.connect(self.show_login)
        self.login.LoginSubmitBtn.clicked.connect(self.show_officer_menu)
        self.officer_main_menu.CasesBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.cases))
        self.officer_main_menu.CriminalsBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.criminals))
        self.officer_main_menu.SuspectsBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.suspects))
        self.officer_main_menu.VictimsBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.victims))
        self.officer_main_menu.WitnessesBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.witnesses))
        self.officer_main_menu.OfficersBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.officers))
        self.officer_main_menu.BackBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.start_menu))

        self.cases.BackBtn.clicked.connect(self.BackToOfficerMenu)
        self.criminals.BackBtn.clicked.connect(self.BackToOfficerMenu)
        self.suspects.BackBtn.clicked.connect(self.BackToOfficerMenu)
        self.victims.BackBtn.clicked.connect(self.BackToOfficerMenu)
        self.witnesses.BackBtn.clicked.connect(self.BackToOfficerMenu)
        self.officers.BackBtn.clicked.connect(self.BackToOfficerMenu)


    def show_login(self):
        self.stacked_widget.setCurrentWidget(self.login)

    def show_officer_menu(self):
        if self.login.ValidateLogin():
            self.stacked_widget.setCurrentWidget(self.officer_main_menu)
        else:
            QMessageBox.information(self, "Invalid ID", "The ID you entered is invalid.")
            self.show_login()
            
    def BackToOfficerMenu(self):
        self.stacked_widget.setCurrentWidget(self.officer_main_menu)


def ConnectDatabase():
    try:
        global conn, cursor
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=.;'
                              'Database=Criminal Investigation System;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        print("Connection Established")

    except pyodbc.Error as e:
        print("Error:", e)
    return conn, cursor
    

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())