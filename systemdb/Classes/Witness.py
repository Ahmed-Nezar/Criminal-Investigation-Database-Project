import pyodbc
from systemdb.globalFunc import *

class Witness:
    def __init__(self, WitnessID, FirstName, LastName, DateOfBirth, Gender, Address, PhoneNumber, Email):
        self.WitnessID = WitnessID
        self.FirstName = FirstName
        self.LastName = LastName
        self.DateOfBirth = DateOfBirth
        self.Gender = Gender
        self.Age = get_age_from_birthdate(DateOfBirth)
        self.Address = Address
        self.PhoneNumber = PhoneNumber
        self.Email = Email

    def insert_into_database(self):
        try:
            values = (self.WitnessID, self.FirstName, self.LastName, self.DateOfBirth, self.Gender, self.Age, self.Address, self.PhoneNumber, self.Email)
            insert_into_table("Witness1", [values])
            print("Witness inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Witness:", e)
    def get_all():
        return get_all_ids("Witness1","*")
    def get_columns(columns_name):
        return get_all_ids("Witness1",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("Witness1", primary_key, values)
            print("Witness deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Witness:", e)
