import pyodbc
from .globalFunc import *

class VictimPhoneNumber:
    def __init__(self, VictimID, PhoneNumber):
        self.VictimID = VictimID
        self.PhoneNumber = PhoneNumber

    def insert_into_database(self):
        try:
            values = (self.VictimID, self.PhoneNumber)
            insert_into_table("Victim_Phone_Number", [values])

        except pyodbc.Error as e:
            print("Error inserting Victim Phone Number:", e)

    
    def get_all():
        return get_all_ids("Victim_Phone_Number", "*")

    
    def get_columns(columns_name):
        return get_all_ids("Victim_Phone_Number", columns_name)

    
    def delete(primary_key, values):
        try:
            delete_from_table("Victim_Phone_Number", primary_key, values)
            print("Victim Phone Number deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Victim Phone Number:", e)

    def search(value):
        return search_by_primary_key('Victim_Phone_Number', 'Victim_ID', value)

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
            query = """Select Victim.VictimID,FirstName+' '+LastName as Name,Victim_Phone_Number.PhoneNumber from Victim join Victim_Phone_Number
                    on Victim.VictimID=Victim_Phone_Number.Victim_ID;"""
            
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