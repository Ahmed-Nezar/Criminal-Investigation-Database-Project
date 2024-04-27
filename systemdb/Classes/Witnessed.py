import pyodbc
from systemdb.globalFunc import *

class Witnessed:
    def __init__(self, CaseID, WitnessID):
        self.CaseID = CaseID
        self.WitnessID = WitnessID

    def insert_into_database(self):
        try:
            values = (self.CaseID, self.WitnessID)
            insert_into_table("Witnessed", [values])
            print("Witnessed inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Witnessed:", e)

    def get_all():
        return get_all_ids("Witnessed","*")
    def get_columns(columns_name):
        return get_all_ids("Witnessed",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("Witnessed", primary_key, values)
            print("Witnessed deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Witnessed:", e)
