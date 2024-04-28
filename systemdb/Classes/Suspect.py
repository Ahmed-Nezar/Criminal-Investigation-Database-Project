import pyodbc
from .globalFunc import *

class Suspect:
    def __init__(self, SuspectID, FirstName, LastName, Gender, DateOfBirth, PhoneRecord, AddressStreet, AddressGovernment, AddressZIP,Criminal_Record):
        self.SuspectID = SuspectID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Gender = Gender
        self.DateOfBirth = DateOfBirth
        self.PhoneRecord = PhoneRecord
        self.AddressStreet = AddressStreet
        self.AddressGovernment = AddressGovernment
        self.AddressZIP = AddressZIP
        self.Criminal_Record=Criminal_Record

    def insert_into_database(self):
        try:
            values = (self.SuspectID, self.FirstName, self.LastName, self.Gender, self.DateOfBirth, self.PhoneRecord, self.AddressStreet, self.AddressGovernment, self.AddressZIP)
            insert_into_table("Suspect", [values])
            for x in self.Criminal_Record:
                 values = (self.SuspectID, x)
                 insert_into_table("CriminalRecord", values)
            print("Suspect inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Suspect:", e)
    def get_all():
        return get_all_ids("Suspect","*")
    def get_columns(columns_name):
        return get_all_ids("Suspect",columns_name)
    def delete(primarykey,values):
        try:
            delete_from_table("Suspect",primarykey,values)
            print("Suspect deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Suspect:", e)

    def search(value):
        return search_by_primary_key('Suspect','SuspectID',value)