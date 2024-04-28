# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'AddWitness.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class AddWitness(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("AddWitness")
        self.resize(1007, 678)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 3, 1, 1)
        self.WitnessGenderFIeld = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.WitnessGenderFIeld.setFont(font)
        self.WitnessGenderFIeld.setObjectName("WitnessGenderFIeld")
        self.gridLayout.addWidget(self.WitnessGenderFIeld, 9, 2, 1, 1)
        self.WitnessDOBField = QtWidgets.QDateEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.WitnessDOBField.setFont(font)
        self.WitnessDOBField.setObjectName("WitnessDOBField")
        self.gridLayout.addWidget(self.WitnessDOBField, 8, 2, 1, 1)
        self.WitnessLastNameField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.WitnessLastNameField.setFont(font)
        self.WitnessLastNameField.setObjectName("WitnessLastNameField")
        self.gridLayout.addWidget(self.WitnessLastNameField, 7, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 10, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)
        self.WitnessIDField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.WitnessIDField.setFont(font)
        self.WitnessIDField.setObjectName("WitnessIDField")
        self.gridLayout.addWidget(self.WitnessIDField, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 12, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.WitnessAgeField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.WitnessAgeField.setFont(font)
        self.WitnessAgeField.setObjectName("WitnessAgeField")
        self.gridLayout.addWidget(self.WitnessAgeField, 10, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.BackBtn = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BackBtn.setFont(font)
        self.BackBtn.setObjectName("BackBtn")
        self.gridLayout.addWidget(self.BackBtn, 13, 0, 1, 1)
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.AddWitnessDataBtn = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AddWitnessDataBtn.setFont(font)
        self.AddWitnessDataBtn.setObjectName("AddWitnessDataBtn")
        self.gridLayout.addWidget(self.AddWitnessDataBtn, 13, 2, 1, 1)
        self.WitnessFirstNameField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.WitnessFirstNameField.setFont(font)
        self.WitnessFirstNameField.setObjectName("WitnessFirstNameField")
        self.gridLayout.addWidget(self.WitnessFirstNameField, 6, 2, 1, 1)
        self.WitnessAddressField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.WitnessAddressField.setFont(font)
        self.WitnessAddressField.setObjectName("WitnessAddressField")
        self.gridLayout.addWidget(self.WitnessAddressField, 11, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 11, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 3, 3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 4, 1, 1, 1)

        self.retranslateUi()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_10.setText(_translate("self", "Age"))
        self.label_9.setText(_translate("self", "Gender"))
        self.label_2.setText(_translate("self", "Witness ID"))
        self.label_5.setText(_translate("self", "First Name"))
        self.label_3.setText(_translate("self", "DOB"))
        self.label_6.setText(_translate("self", "Last Name"))
        self.BackBtn.setText(_translate("self", "Back"))
        self.label.setText(_translate("self", "Add Witness"))
        self.AddWitnessDataBtn.setText(_translate("self", "Add"))
        self.label_4.setText(_translate("self", "Address"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     self = QtWidgets.QWidget()
#     ui = Ui_self()
#     ui.setupUi(self)
#     self.show()
#     sys.exit(app.exec_())
