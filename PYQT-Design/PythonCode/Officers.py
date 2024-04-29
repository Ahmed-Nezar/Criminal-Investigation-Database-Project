# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'Officers.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Classes.Officer import Officer 


class Officers(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.officers = Officer.get_all()
        self.populate_table()

    def setupUi(self):
        self.setObjectName("Officers")
        self.resize(1007, 678)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.OfficerSearchField = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OfficerSearchField.sizePolicy().hasHeightForWidth())
        self.OfficerSearchField.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.OfficerSearchField.setFont(font)
        self.OfficerSearchField.setObjectName("OfficerSearchField")
        self.horizontalLayout_2.addWidget(self.OfficerSearchField)
        self.OfficerSearchBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OfficerSearchBtn.sizePolicy().hasHeightForWidth())
        self.OfficerSearchBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.OfficerSearchBtn.setFont(font)
        self.OfficerSearchBtn.setObjectName("OfficerSearchBtn")
        self.horizontalLayout_2.addWidget(self.OfficerSearchBtn)
        self.OfficerContactInfoBtn = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.OfficerContactInfoBtn.setFont(font)
        self.OfficerContactInfoBtn.setObjectName("OfficerContactInfoBtn")
        self.horizontalLayout_2.addWidget(self.OfficerContactInfoBtn)
        self.OfficerArrestsBtn = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.OfficerArrestsBtn.setFont(font)
        self.OfficerArrestsBtn.setObjectName("OfficerArrestsBtn")
        self.horizontalLayout_2.addWidget(self.OfficerArrestsBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.OfficerScrollArea = QtWidgets.QScrollArea(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OfficerScrollArea.sizePolicy().hasHeightForWidth())
        self.OfficerScrollArea.setSizePolicy(sizePolicy)
        self.OfficerScrollArea.setWidgetResizable(True)
        self.OfficerScrollArea.setObjectName("OfficerScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 893, 515))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.OfficerScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.OfficerScrollArea, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.AddOfficerBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddOfficerBtn.sizePolicy().hasHeightForWidth())
        self.AddOfficerBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AddOfficerBtn.setFont(font)
        self.AddOfficerBtn.setObjectName("AddOfficerBtn")
        self.horizontalLayout.addWidget(self.AddOfficerBtn)
        self.BackBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BackBtn.sizePolicy().hasHeightForWidth())
        self.BackBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BackBtn.setFont(font)
        self.BackBtn.setObjectName("BackBtn")
        self.horizontalLayout.addWidget(self.BackBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)

        self.retranslateUi()
        
        self.officersTable = QtWidgets.QTableWidget(self)
        self.officersTable.setObjectName("officersTable")
        self.officersTable.setColumnCount(9) # Number of columns
        self.officersTable.setHorizontalHeaderLabels(['OfficerID', 'First Name', 'Last Name', 'Date of Birth',
                                                      'Gender','Badge Number','Rank','SuperID','StationID'])
        self.gridLayout.addWidget(self.officersTable, 2, 0, 1, 1)
        self.OfficerSearchBtn.clicked.connect(self.search_officers)
        
        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.OfficerSearchBtn.setText(_translate("self", "Search"))
        self.OfficerContactInfoBtn.setText(_translate("self", "Contact Info"))
        self.OfficerArrestsBtn.setText(_translate("self", "Arrests"))
        self.label.setText(_translate("self", "Officers"))
        self.AddOfficerBtn.setText(_translate("self", "Add"))
        self.BackBtn.setText(_translate("self", "Back"))
        
    # Add function of populate table with officers
    def populate_table(self):
        self.officersTable.setRowCount(len(self.officers))
        for i, Officer in enumerate(self.officers):
            for j, data in enumerate(Officer):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.officersTable.setItem(i, j, item)
        self.officersTable.resizeColumnsToContents()
        self.officersTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.officersTable.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        
    def search_officers(self):
        search_value = self.OfficerSearchField.text()

        self.OfficerSearchField.clear() 
        if search_value:
            try:
                search_value = int(search_value)
            except:
                QtWidgets.QMessageBox.warning(self, 'Invalid Input', 'Please enter a valid officer ID')
                return
            self.officers = Officer.search(search_value)
            if not self.officers:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("No Officer found")
                msg.setWindowTitle("Search")
                msg.exec_()
            else:
                self.populate_table()
        else:
            self.officers = Officer.get_all()
            self.populate_table()
        


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     self = QtWidgets.QWidget()
#     ui = Ui_self()
#     ui.setupUi(self)
#     self.show()
#     sys.exit(app.exec_())
