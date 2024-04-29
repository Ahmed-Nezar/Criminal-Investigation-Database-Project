import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

curr_dir = os.path.dirname('systemdb\Classes\Suspect.py')
parent_dir = os.path.dirname(curr_dir)
sys.path.insert(0, parent_dir)
from Classes.Suspect import Suspect


class Suspects(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.suspects =  Suspect.get_all()
        self.populate_table()

    def setupUi(self):
        self.setObjectName("Suspects")
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
        self.SuspectSearchField = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SuspectSearchField.sizePolicy().hasHeightForWidth())
        self.SuspectSearchField.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectSearchField.setFont(font)
        self.SuspectSearchField.setObjectName("SuspectSearchField")
        self.horizontalLayout_2.addWidget(self.SuspectSearchField)
        self.SuspectSearchBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SuspectSearchBtn.sizePolicy().hasHeightForWidth())
        self.SuspectSearchBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectSearchBtn.setFont(font)
        self.SuspectSearchBtn.setObjectName("SuspectSearchBtn")
        self.horizontalLayout_2.addWidget(self.SuspectSearchBtn)
        self.SuspectsCriminalRecordsBtn = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectsCriminalRecordsBtn.setFont(font)
        self.SuspectsCriminalRecordsBtn.setObjectName("SuspectsCriminalRecordsBtn")
        self.horizontalLayout_2.addWidget(self.SuspectsCriminalRecordsBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.AddSuspectBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddSuspectBtn.sizePolicy().hasHeightForWidth())
        self.AddSuspectBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AddSuspectBtn.setFont(font)
        self.AddSuspectBtn.setObjectName("AddSuspectBtn")
        self.horizontalLayout.addWidget(self.AddSuspectBtn)
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

        # Table to display suspects
        self.SuspectTable = QtWidgets.QTableWidget(self)
        self.SuspectTable.setObjectName("SuspectTable")
        self.SuspectTable.setColumnCount(10) # Number of columns
        self.SuspectTable.setHorizontalHeaderLabels(['SuspectID', 'First Name', 'Last Name', 'Gender', 'Date of Birth', 'Phone Record', ' Street', ' Government', ' ZIP', 'Remove'])
        self.gridLayout.addWidget(self.SuspectTable, 2, 0, 1, 1)
        
        self.SuspectSearchBtn.clicked.connect(self.search_suspects)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.SuspectSearchBtn.setText(_translate("self", "Search"))
        self.label.setText(_translate("self", "Suspects"))
        self.AddSuspectBtn.setText(_translate("self", "Add"))
        self.BackBtn.setText(_translate("self", "Back"))
        self.SuspectsCriminalRecordsBtn.setText(_translate("self", "Criminal Records"))
    
    def populate_table(self):
        self.SuspectTable.setRowCount(len(self.suspects))
        for i, suspect in enumerate(self.suspects):
            for j, data in enumerate(suspect):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.SuspectTable.setItem(i, j, item)
            remove_button = QtWidgets.QPushButton("Remove")
            remove_button.clicked.connect(lambda _, suspect=suspect: self.remove_suspect(suspect))
            self.SuspectTable.setCellWidget(i, len(suspect), remove_button)
        self.SuspectTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.SuspectTable.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)


    def search_suspects(self):
        search_value = self.SuspectSearchField.text()
        self.SuspectSearchField.clear() 
        if search_value:
            try:
                search_value = int(search_value)
            except:
                QtWidgets.QMessageBox.warning(self, "Search", "Please enter a valid suspect ID")
                return
            self.suspects = Suspect.search(search_value)
            if not self.suspects:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("No suspects found")
                msg.setWindowTitle("Search")
                msg.exec_()
            else:
                self.populate_table()
        else:
            self.suspects = Suspect.get_all()
            self.populate_table()

    def remove_suspect(self, suspect_row):
        Suspect.delete(suspect_row[0])
        self.suspects = Suspect.get_all()
        self.populate_table()

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     self = QtWidgets.QWidget()
#     ui = Ui_self()
#     ui.setupUi(self)
#     suspects = Suspect.get_all()  
#     ui.populate_table(suspects)
#     ui.SuspectSearchBtn.clicked.connect(ui.search_suspects) 
#     self.show()
#     sys.exit(app.exec_())
