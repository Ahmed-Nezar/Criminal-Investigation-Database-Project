import pyodbc
from .globalFunc import *

class Arrest:
    def __init__(self, OfficerID, CaseID, ArrestDate):
        self.OfficerID = OfficerID
        self.CaseID = CaseID
        self.ArrestDate = ArrestDate

    def insert_into_database(self):
        try:
            values = (self.OfficerID, self.CaseID, self.ArrestDate)
            insert_into_table("Arrest", [values])
            print("Arrest inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Arrest:", e)
    def get_all():
        return get_all_ids("Arrest","*")
    def get_columns(columns_name):
        return get_all_ids("Arrest",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("Arrest", primary_key, values)
            print("Arrest deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Arrest:", e)