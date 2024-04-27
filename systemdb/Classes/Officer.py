import pyodbc
from .globalFunc import *

class Officer:
    def __init__(self, OfficerID, FirstName, LastName, DateOfBirth, Gender, BadgeNumber, Rank, SupervisorID, Email, PhoneNumber):
        self.OfficerID = OfficerID
        self.FirstName = FirstName
        self.LastName = LastName
        self.DateOfBirth = DateOfBirth
        self.Gender = Gender
        self.BadgeNumber = BadgeNumber
        self.Rank = Rank
        self.SupervisorID = SupervisorID
        self.Email = Email
        self.PhoneNumber = PhoneNumber

    def insert_into_database(self):
        try:
            values = (self.OfficerID, self.FirstName, self.LastName, self.DateOfBirth, self.Gender, self.BadgeNumber, self.Rank, self.SupervisorID, self.Email, self.PhoneNumber)
            insert_into_table("Officer", [values])
            print("Officer inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Officer:", e)
    def get_all():
        return get_all_ids("Officer","*")
    def get_columns(columns_name):
        return get_all_ids("Officer",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("Officer", primary_key, values)
            print("Officer deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Officer:", e)
