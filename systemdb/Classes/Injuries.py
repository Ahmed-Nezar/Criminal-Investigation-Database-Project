import pyodbc
from .globalFunc import *

class Injuries:
    def __init__(self, VictimID, Injury):
        self.VictimID = VictimID
        self.Injury = Injury

    def insert_into_database(self):
        try:
            values = (self.VictimID, self.Injury)
            insert_into_table("Injuries", [values])
            print("Injury inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Injury:", e)

    def get_all():
        return get_all_ids("Injuries", "*")

    def get_columns(columns_name):
        return get_all_ids("Injuries", columns_name)

    def delete(primary_key, values):
        try:
            delete_from_table("Injuries", primary_key, values)
            print("Injury deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Injury:", e)

    def search(value):
        return search_by_primary_key('Injuries', 'Victim_ID', value)
