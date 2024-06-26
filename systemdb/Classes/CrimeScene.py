import pyodbc
from .globalFunc import *

class CrimeScene:
    def __init__(self, CaseID, Time, Location):
        self.CaseID = CaseID
        self.Time = Time
        self.Location = Location

    def insert_into_database(self):
        try:
            values = (self.CaseID, self.Time, self.Location)
            insert_into_table("CrimeScene", [values])
            print("CrimeScene inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting CrimeScene:", e)
    def get_all():
        return get_all_ids("CrimeScene","*")
    def get_columns(columns_name):
        return get_all_ids("CrimeScene",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("CrimeScene", primary_key, values)
            print("CrimeScene deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting CrimeScene:", e)
    
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
            query = """select CrimeScene.CaseID, Time, Location, Evidence.Type, Description from CrimeScene 
                        Join Evidence on CrimeScene.CaseID = Evidence.CaseID;"""
            
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
