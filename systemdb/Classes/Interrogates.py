import pyodbc
from systemdb.globalFunc import *

class Interrogates:
    def __init__(self, OfficerID, SuspectID):
        self.OfficerID = OfficerID
        self.SuspectID = SuspectID

    def insert_into_database(self):
        try:
            values = (self.OfficerID, self.SuspectID)
            insert_into_table("Interrogates", [values])
            print("Interrogates inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Interrogates:", e)
    def get_all():
        return get_all_ids("Interrogates","*")
    def get_columns(columns_name):
        return get_all_ids("Interrogates",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("Interrogates", primary_key, values)
            print("Interrogates deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Interrogates:", e)