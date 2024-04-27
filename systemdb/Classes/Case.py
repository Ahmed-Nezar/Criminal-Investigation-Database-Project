import pyodbc
from .globalFunc import *

class Case:
    def __init__(self, CaseID, StartDate, EndDate, Description, Status, OfficerID):
        self.CaseID = CaseID
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.Description = Description
        self.Status = Status
        self.OfficerID = OfficerID

    def insert_into_database(self):
        try:
            values = (self.CaseID, self.StartDate, self.EndDate, self.Description, self.Status, self.OfficerID)
            insert_into_table("Case", [values])
            print("Case inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Case:", e)
    def get_all():
        return get_all_ids("Case","*")
    def get_columns(columns_name):
        return get_all_ids("Case",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("Case", primary_key, values)
            print("Case deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Case:", e)