import pyodbc
from systemdb.globalFunc import *

class Evidence:
    def __init__(self, CaseID, Type, Description):
        self.CaseID = CaseID
        self.Type = Type
        self.Description = Description

    def insert_into_database(self):
        try:
            values = (self.CaseID, self.Type, self.Description)
            insert_into_table("Evidence", [values])
            print("Evidence inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Evidence:", e)
    def get_all():
        return get_all_ids("Evidence","*")
    def get_columns(columns_name):
        return get_all_ids("Evidence",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("Evidence", primary_key, values)
            print("Evidence deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Evidence:", e)