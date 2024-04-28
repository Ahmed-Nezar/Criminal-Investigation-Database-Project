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
from AddOfficer import AddOfficer
from AddCase import AddCase
from AddCriminal import AddCriminal
from AddSuspect import AddSuspect
from AddVictim import AddVictim
from AddWitness import AddWitness
from DatabaseManagerSQL import DatabaseManagerSQL

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
        self.add_officer = AddOfficer()
        self.add_case = AddCase()
        self.add_criminal = AddCriminal()
        self.add_suspect = AddSuspect()
        self.add_victim = AddVictim()
        self.add_witness = AddWitness()
        self.db_manager = DatabaseManagerSQL()

        self.stacked_widget.addWidget(self.start_menu)
        self.stacked_widget.addWidget(self.login)
        self.stacked_widget.addWidget(self.db_manager)
        self.stacked_widget.addWidget(self.officer_main_menu)
        self.stacked_widget.addWidget(self.cases)
        self.stacked_widget.addWidget(self.criminals)
        self.stacked_widget.addWidget(self.suspects)
        self.stacked_widget.addWidget(self.victims)
        self.stacked_widget.addWidget(self.witnesses)
        self.stacked_widget.addWidget(self.officers)
        self.stacked_widget.addWidget(self.add_officer)
        self.stacked_widget.addWidget(self.add_case)
        self.stacked_widget.addWidget(self.add_criminal)
        self.stacked_widget.addWidget(self.add_suspect)
        self.stacked_widget.addWidget(self.add_victim)
        self.stacked_widget.addWidget(self.add_witness)
        self.stacked_widget.setCurrentWidget(self.start_menu)

        # Start Menu Buttons
        self.start_menu.OfficerMenuBtn.clicked.connect(self.show_login)
        self.start_menu.DatabaseManagerBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.db_manager))
        self.db_manager.BackBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.start_menu))

        # Login Button
        self.login.LoginSubmitBtn.clicked.connect(self.show_officer_menu)

        # Officer Main Menu Buttons
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

        self.officers.AddOfficerBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.add_officer))
        self.add_officer.BackBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.officers))

        self.cases.AddCaseBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.add_case))
        self.add_case.BackBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.cases))

        self.criminals.AddCriminalBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.add_criminal))
        self.add_criminal.BackBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.criminals))

        self.suspects.AddSuspectBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.add_suspect))
        self.add_suspect.BackBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.suspects))

        self.victims.AddVictimBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.add_victim))
        self.add_victim.BackBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.victims))

        self.witnesses.AddWitnessBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.add_witness))
        self.add_witness.BackBtn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.witnesses))


        


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