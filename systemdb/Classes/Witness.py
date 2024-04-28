import pyodbc
from .globalFunc import *

class Witness:
    def __init__(self, WitnessID, FirstName, LastName, DateOfBirth, Gender, Address):
        self.WitnessID = WitnessID
        self.FirstName = FirstName
        self.LastName = LastName
        self.DateOfBirth = DateOfBirth
        self.Gender = Gender
        self.Age = get_age_from_birthdate(DateOfBirth)
        self.Address = Address

    def insert_into_database(self):
        try:
            values = (self.WitnessID, self.FirstName, self.LastName, self.DateOfBirth, self.Gender, self.Age, self.Address)
            insert_into_table("Witness", [values])
            print("Witness inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Witness:", e)
    def get_all():
        return get_all_ids("Witness","*")
    def get_columns(columns_name):
        return get_all_ids("Witness",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("Witnessed", primary_key, values)
            delete_from_table("Witness_Contact", primary_key, values)
            delete_from_table("Witness", primary_key, values)
            print("Witness deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Witness:", e)
    def search(value):
        return search_by_primary_key('Witness','WitnessID',value)