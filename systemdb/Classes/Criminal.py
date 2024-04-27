import pyodbc
from systemdb.globalFunc import *

class Criminal:
    def __init__(self, CriminalID, FirstName, LastName, Status, Description):
        self.CriminalID = CriminalID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Status = Status
        self.Description = Description

    def insert_into_database(self):
        try:
            values = (self.CriminalID, self.FirstName, self.LastName, self.Status, self.Description)
            insert_into_table("Criminal", [values])
            print("Criminal inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Criminal:", e)
    def get_all():
        return get_all_ids("Criminal","*")
    def get_columns(columns_name):
        return get_all_ids("Criminal",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("Criminal", primary_key, values)
            print("Criminal deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Criminal:", e)