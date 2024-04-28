import pyodbc
from .globalFunc import *

class WitnessContactInfo:
    def __init__(self, WitnessID, PhoneNumber, Email):
        self.WitnessID = WitnessID
        self.PhoneNumber = PhoneNumber
        self.Email = Email

    def insert_into_database(self):
        try:
            values = (self.WitnessID, self.PhoneNumber, self.Email)
            insert_into_table("Witness_Contact", [values])

        except pyodbc.Error as e:
            print("Error inserting Witness Contact:", e)

    def get_all():
        return get_all_ids("Witness_Contact", "*")

    def get_columns(columns_name):
        return get_all_ids("Witness_Contact", columns_name)

    def delete(primary_key, values):
        try:
            delete_from_table("Witness_Contact", primary_key, values)
            print("Witness Contact deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Witness Contact:", e)

    def search(value):
        return search_by_primary_key('Witness_Contact', 'WitnessID', value)

    def return_view():
        cursor = None
        conn = None
        try:
            conn = pyodbc.connect(
                "Driver={ODBC Driver 18 for SQL Server};"
                "Server=.;"
                "Database=Criminal Investigation System;"
                "Trusted_Connection=yes;"
                "Encrypt=no;"
            )
            cursor = conn.cursor()

            # Construct the SQL query dynamically
            query = """Select Witness.WitnessID,FirstName+' '+LastName as Name,Witness_Contact.PhoneNumber,Witness_Contact.Email from Witness join Witness_Contact
                    on Witness.WitnessID=Witness_Contact.WitnessID;"""
            
            cursor.execute(query)
            print("The code is run successfully.")
            ids = []
            
            for row in cursor:
                ids.append(row)

        except pyodbc.Error as e:
            print("Error excuting values into:", e)

        finally:
            
            if cursor:
                cursor.close()  
            if conn:
                conn.close()
        
        return ids