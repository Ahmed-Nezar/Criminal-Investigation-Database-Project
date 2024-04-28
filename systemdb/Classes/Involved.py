import pyodbc
from .globalFunc import *

class Involved:
    def __init__(self, SuspectID, CaseID):
        self.CaseID = CaseID
        self.SuspectID = SuspectID
    def insert_into_database(self):
        try:
            values = (self.SuspectID, self.CaseID)
            insert_into_table("Involved", [values])
            print("Involved inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Involved:", e)
    def get_all():
        return get_all_ids("Involved","*")
    def get_columns(columns_name):
        return get_all_ids("Involved",columns_name)
    def delete(values):
        try:
            delete_from_table("Involved",["SuspectID","CaseID"],values)
            print("Involved deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Involved:", e)

    def search(value):
        return search_by_primary_key('Involved',"CaseID",value)