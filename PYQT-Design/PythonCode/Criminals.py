import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Classes.Criminal import Criminal 

curr_dir = os.path.dirname('systemdb\Classes\Criminal.py')
parent_dir = os.path.dirname(curr_dir)
sys.path.insert(0, parent_dir)



class Criminals(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.criminals = Criminal.get_all()
        self.populate_table()

    def setupUi(self):
        self.setObjectName("Criminals")
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
        self.CriminalSearchField = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CriminalSearchField.sizePolicy().hasHeightForWidth())
        self.CriminalSearchField.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CriminalSearchField.setFont(font)
        self.CriminalSearchField.setObjectName("CriminalSearchField")
        self.horizontalLayout_2.addWidget(self.CriminalSearchField)
        self.CriminalSearchBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CriminalSearchBtn.sizePolicy().hasHeightForWidth())
        self.CriminalSearchBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CriminalSearchBtn.setFont(font)
        self.CriminalSearchBtn.setObjectName("CriminalSearchBtn")
        self.horizontalLayout_2.addWidget(self.CriminalSearchBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.CriminalScrollArea = QtWidgets.QScrollArea(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CriminalScrollArea.sizePolicy().hasHeightForWidth())
        self.CriminalScrollArea.setSizePolicy(sizePolicy)
        self.CriminalScrollArea.setWidgetResizable(True)
        self.CriminalScrollArea.setObjectName("CriminalScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 893, 515))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.CriminalScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.CriminalScrollArea, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.AddCriminalBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddCriminalBtn.sizePolicy().hasHeightForWidth())
        self.AddCriminalBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AddCriminalBtn.setFont(font)
        self.AddCriminalBtn.setObjectName("AddCriminalBtn")
        self.horizontalLayout.addWidget(self.AddCriminalBtn)
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
        
        self.CriminalsTable = QtWidgets.QTableWidget(self)
        self.CriminalsTable.setObjectName("CriminalsTable")
        self.CriminalsTable.setColumnCount(5) # Number of columns
        self.CriminalsTable.setHorizontalHeaderLabels(['CriminalID', 'First Name', 'Last Name', 'Status', 'Description',])
        self.gridLayout.addWidget(self.CriminalsTable, 2, 0, 1, 1)
        self.CriminalSearchBtn.clicked.connect(self.search_criminals)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.CriminalSearchBtn.setText(_translate("self", "Search"))
        self.label.setText(_translate("self", "Criminals"))
        self.AddCriminalBtn.setText(_translate("self", "Add"))
        self.BackBtn.setText(_translate("self", "Back"))
        
    def populate_table(self):
        self.CriminalsTable.setRowCount(len(self.criminals))
        for i, criminal in enumerate(self.criminals):
            for j, data in enumerate(criminal):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.CriminalsTable.setItem(i, j, item)
        self.CriminalsTable.resizeColumnsToContents()


    def search_criminals(self):
        search_value = self.CriminalSearchField.text()
        self.CriminalSearchField.clear() 
        if search_value:
            self.criminals = Criminal.search(search_value)
            if not self.criminals:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("No suspects found")
                msg.setWindowTitle("Search")
                msg.exec_()
            else:
                self.populate_table()
        else:
            self.criminals = Criminal.get_all()
            self.populate_table()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     self = QtWidgets.QWidget()
#     ui = Ui_self()
#     ui.setupUi(self)
#     self.show()
#     sys.exit(app.exec_())