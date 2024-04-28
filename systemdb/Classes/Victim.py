import pyodbc
from .globalFunc import *

class Victim:
    def __init__(self, VictimID, FirstName, LastName, DateOfBirth, Gender, Address):
        self.VictimID = VictimID
        self.FirstName = FirstName
        self.LastName = LastName
        self.DateOfBirth = DateOfBirth
        self.Age = get_age_from_birthdate(DateOfBirth)
        self.Gender = Gender
        self.Address = Address

    def insert_into_database(self):
        try:
            values = (self.VictimID, self.FirstName, self.LastName, self.DateOfBirth, self.Age, self.Gender, self.Address)
            insert_into_table("Victim", [values])
            print("Victim inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Victim:", e)
    def get_all():
        return get_all_ids("Victim","*")
    def get_columns(columns_name):
        return get_all_ids("Victim",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("Victim", primary_key, values)
            print("Victim deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Victim:", e)
    def search(value):
        return search_by_primary_key('Victim','VictimID',value)
