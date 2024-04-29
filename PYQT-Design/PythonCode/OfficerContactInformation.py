# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'OfficerContactInfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from Classes.OfficerContactInfo import OfficerContactInfo


class OfficerContactInformation(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.contact_infos_records = OfficerContactInfo.return_view()
        self.populate_table()

    def setupUi(self):
        self.setObjectName("OfficerArrests")
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
        self.OfficerContactSearchField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.OfficerContactSearchField.setFont(font)
        self.OfficerContactSearchField.setObjectName("OfficerContactSearchField")
        self.horizontalLayout_3.addWidget(self.OfficerContactSearchField)
        self.OfficerContactSearchBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OfficerContactSearchBtn.sizePolicy().hasHeightForWidth())
        self.OfficerContactSearchBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.OfficerContactSearchBtn.setFont(font)
        self.OfficerContactSearchBtn.setObjectName("OfficerContactSearchBtn")
        self.horizontalLayout_3.addWidget(self.OfficerContactSearchBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.OfficerContactScrollArea = QtWidgets.QScrollArea(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OfficerContactScrollArea.sizePolicy().hasHeightForWidth())
        self.OfficerContactScrollArea.setSizePolicy(sizePolicy)
        self.OfficerContactScrollArea.setWidgetResizable(True)
        self.OfficerContactScrollArea.setObjectName("OfficerContactScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 893, 515))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.OfficerContactScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.OfficerContactScrollArea, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)

        # Table to display contact_infos
        self.OfficerContactInfoTable = QtWidgets.QTableWidget(self)
        self.OfficerContactInfoTable.setObjectName("OfficerContactInfoTable")
        self.OfficerContactInfoTable.setColumnCount(4) # Number of columns
        self.OfficerContactInfoTable.setHorizontalHeaderLabels(['Officer ID','Officer Name', 'Email', 'Phone'])
        self.gridLayout.addWidget(self.OfficerContactInfoTable, 2, 0, 1, 1)

        self.OfficerContactSearchBtn.clicked.connect(self.search_table)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label.setText(_translate("self", "Officer Contact Info"))
        self.BackBtn.setText(_translate("self", "Back"))
        self.OfficerContactSearchBtn.setText(_translate("self", "Search"))

    def populate_table(self):
        self.contact_infos_records = OfficerContactInfo.return_view()
        self.OfficerContactInfoTable.setRowCount(len(self.contact_infos_records))
        for i, contact_info in enumerate(self.contact_infos_records):
            for j, data in enumerate(contact_info):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.OfficerContactInfoTable.setItem(i, j, item)
            self.OfficerContactInfoTable.resizeColumnsToContents()

    def search_table(self):
        self.contact_infos_records = OfficerContactInfo.return_view()
        search_value = self.OfficerContactSearchField.text()
        self.OfficerContactSearchField.clear()
        
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
            contact_infos = []
            for contact_info in self.contact_infos_records:
                if search_value in contact_info:
                    contact_infos.append(contact_info)
            if contact_infos == []:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("No Criminal Records found")
                msg.setWindowTitle("Search")
                msg.exec_()
            else:
                self.OfficerContactInfoTable.setRowCount(len(contact_infos))
        
                for i, contact_info in enumerate(contact_infos):
                    for j, data in enumerate(contact_info):
                        item = QtWidgets.QTableWidgetItem(str(data))
                        self.OfficerContactInfoTable.setItem(i, j, item)
                self.OfficerContactInfoTable.resizeColumnsToContents()
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
