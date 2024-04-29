import pyodbc
from globalFunc import *

class Affects:
    def __init__(self, CaseID, VictimID):
        self.CaseID = CaseID
        self.VictimID = VictimID

    def insert_into_database(self):
        try:
            values = (self.CaseID, self.VictimID)
            insert_into_table("Affects", [values])
            print("Affects inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Affects:", e)
    def get_all():
        return get_all_ids("Affects","*")
    def get_columns(columns_name):
        return get_all_ids("Affects",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("Affects", primary_key, values)

        except pyodbc.Error as e:
            print("Error deleting Affects:", e)
