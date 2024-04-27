import pyodbc
from systemdb.globalFunc import *

class PoliceStation:
    def __init__(self, StationID, Name, Location, Telephone, StationChief):
        self.StationID = StationID
        self.Name = Name
        self.Location = Location
        self.Telephone = Telephone
        self.StationChief = StationChief

    def insert_into_database(self):
        try:
            values = (self.StationID, self.Name, self.Location, self.Telephone, self.StationChief)
            insert_into_table("PoliceStation", [values])
            print("PoliceStation inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting PoliceStation:", e)
    def get_all():
        return get_all_ids("PoliceStation","*")
    def get_columns(columns_name):
        return get_all_ids("PoliceStation",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("PoliceStation", primary_key, values)
            print("PoliceStation deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting PoliceStation:", e)