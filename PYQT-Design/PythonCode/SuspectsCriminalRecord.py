# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'Suspect'sCriminalRecord.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from Classes.CriminalRecord import CriminalRecord


class SuspectsCriminalRecord(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.criminal_records = CriminalRecord.return_view()
        self.populate_table()

    def setupUi(self):
        self.setObjectName("SuspectCriminalRecord")
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.SuspectCriminalRecordSearchField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectCriminalRecordSearchField.setFont(font)
        self.SuspectCriminalRecordSearchField.setObjectName("SuspectCriminalRecordSearchField")
        self.horizontalLayout_3.addWidget(self.SuspectCriminalRecordSearchField)
        self.SuspectCriminalRecordSearchBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SuspectCriminalRecordSearchBtn.sizePolicy().hasHeightForWidth())
        self.SuspectCriminalRecordSearchBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectCriminalRecordSearchBtn.setFont(font)
        self.SuspectCriminalRecordSearchBtn.setObjectName("SuspectCriminalRecordSearchBtn")
        self.horizontalLayout_3.addWidget(self.SuspectCriminalRecordSearchBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.SuspectScrollArea = QtWidgets.QScrollArea(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SuspectScrollArea.sizePolicy().hasHeightForWidth())
        self.SuspectScrollArea.setSizePolicy(sizePolicy)
        self.SuspectScrollArea.setWidgetResizable(True)
        self.SuspectScrollArea.setObjectName("SuspectScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 893, 515))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.SuspectScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.SuspectScrollArea, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)

        # Table to display suspects
        self.SuspectTable = QtWidgets.QTableWidget(self)
        self.SuspectTable.setObjectName("SuspectTable")
        self.SuspectTable.setColumnCount(4) # Number of columns
        self.SuspectTable.setHorizontalHeaderLabels(['SuspectID', 'Name', 'Criminal Record', 'CaseID'])
        self.gridLayout.addWidget(self.SuspectTable, 2, 0, 1, 1)

        self.SuspectCriminalRecordSearchBtn.clicked.connect(self.search_table)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label.setText(_translate("self", "Suspect\'s Criminal Record"))
        self.BackBtn.setText(_translate("self", "Back"))
        self.SuspectCriminalRecordSearchBtn.setText(_translate("Form", "Search"))

    def populate_table(self):
        self.criminal_records = CriminalRecord.return_view()
        self.SuspectTable.setRowCount(len(self.criminal_records))
        
        for i, suspect in enumerate(self.criminal_records):
            for j, data in enumerate(suspect):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.SuspectTable.setItem(i, j, item)
        self.SuspectTable.resizeColumnsToContents()

    def search_table(self):
        self.criminal_records = CriminalRecord.return_view()
        search_value = self.SuspectCriminalRecordSearchField.text()
        self.SuspectCriminalRecordSearchField.clear()
        
        if search_value:
            try:
                search_value = int(search_value)
            except ValueError:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Invalid Input")
                msg.setWindowTitle("Search")
                msg.exec_()
                return
            suspects = []
            for suspect in self.criminal_records:
                if search_value in suspect:
                    suspects.append(suspect)
            if suspects == []:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("No Criminal Records found")
                msg.setWindowTitle("Search")
                msg.exec_()
            else:
                self.SuspectTable.setRowCount(len(suspects))
        
                for i, suspect in enumerate(suspects):
                    for j, data in enumerate(suspect):
                        item = QtWidgets.QTableWidgetItem(str(data))
                        self.SuspectTable.setItem(i, j, item)
                self.SuspectTable.resizeColumnsToContents()
        else:
            
            self.populate_table()
               


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     self = QtWidgets.QWidget()
#     ui = Ui_self()
#     ui.setupUi(self)
#     self.show()
#     sys.exit(app.exec_())
