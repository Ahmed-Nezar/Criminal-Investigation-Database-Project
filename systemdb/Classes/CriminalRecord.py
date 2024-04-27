import pyodbc
from systemdb.globalFunc import *

class CriminalRecord:
    
    def __init__(self, SuspectID, CriminalID, CrimeRecord):
        self.SuspectID = SuspectID
        self.CriminalID = CriminalID
        self.CrimeRecord = CrimeRecord
    def insert_into_database(self):
        try:
            values = (self.SuspectID, self.CriminalID, self.CrimeRecord)
            insert_into_table("CriminalRecord", [values])
            print("CriminalRecord inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting CriminalRecord:", e)
    def get_all():
        return get_all_ids("CriminalRecord","*")
    def get_columns(columns_name):
        return get_all_ids("CriminalRecord",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("CriminalRecord", primary_key, values)
            print("CriminalRecord deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting CriminalRecord:", e)