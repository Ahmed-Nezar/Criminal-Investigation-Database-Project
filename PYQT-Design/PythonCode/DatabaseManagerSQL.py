from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem



class DatabaseManagerSQL(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("DatabaseManagerSQL")
        self.resize(1007, 678)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.OutSQLScrollArea = QtWidgets.QScrollArea(self)
        self.OutSQLScrollArea.setWidgetResizable(True)
        self.OutSQLScrollArea.setObjectName("OutSQLScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 928, 446))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.OutSQLScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.OutSQLScrollArea, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.SQLField = QtWidgets.QTextEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQLField.sizePolicy().hasHeightForWidth())
        self.SQLField.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SQLField.setFont(font)
        self.SQLField.setObjectName("SQLField")
        self.gridLayout.addWidget(self.SQLField, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ExecuteSQLBtn = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ExecuteSQLBtn.setFont(font)
        self.ExecuteSQLBtn.setObjectName("ExecuteSQLBtn")
        self.horizontalLayout.addWidget(self.ExecuteSQLBtn)
        self.BackBtn = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BackBtn.setFont(font)
        self.BackBtn.setObjectName("BackBtn")
        self.horizontalLayout.addWidget(self.BackBtn)
        spacerItem1 = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 2, 1, 1)

        self.retranslateUi()
        self.ExecuteSQLBtn.clicked.connect(self.execute_sql_query)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label.setText(_translate("self", "Write SQL Query"))
        self.ExecuteSQLBtn.setText(_translate("self", "Execute"))
        self.BackBtn.setText(_translate("self", "Back"))

    def execute_sql_query(self):
        # Get the SQL query from the text field
        sql_query = self.SQLField.toPlainText()

        # Call the writequery function with the SQL query
        result = writequery(sql_query)
        
        # Display the result in the output text area
        self.show_result(result)

    def show_result(self, result):
        if isinstance(result, pd.DataFrame):
            # Create a table view widget
            table_view = QTableView()
            
            # Create a standard item model
            model = QStandardItemModel()
            model.setColumnCount(len(result.columns))
            model.setRowCount(len(result.index))
            
            # Populate the model with DataFrame data
            for row in range(len(result.index)):
                for col in range(len(result.columns)):
                    item = QStandardItem(str(result.iloc[row, col]))
                    model.setItem(row, col, item)
            
            # Set the model to the table view
            table_view.setModel(model)
            
            # Set the table view as the widget in the scroll area
            self.OutSQLScrollArea.setWidget(table_view)
        else:
            # If result is not a DataFrame, display as text
            result_text = str(result)
            output_widget = QtWidgets.QTextEdit(result_text)
            self.OutSQLScrollArea.setWidget(output_widget)


def writequery(code):
    cursor = None
    conn = None
   
    try:
        conn = pyodbc.connect(
            "Driver={ODBC Driver 18 for SQL Server};"
            "Server=.;"
            "Database=Criminal Investigation System;"
            "Trusted_Connection=yes;"
            "Encrypt=no;"
        )
        query = code
        df = pd.read_sql_query(query, conn)       
              
       
    except pyodbc.Error as e:
        print("Error executing values into:", e)

    finally:    
        if cursor:
            cursor.close()  
        if conn:
            conn.close()
        
    return df


# if __name__ == "__main__":
#     import sys

#     app = QtWidgets.QApplication(sys.argv)
#     ui = DatabaseManagerSQL()
#     ui.show()
#     sys.exit(app.exec_())
