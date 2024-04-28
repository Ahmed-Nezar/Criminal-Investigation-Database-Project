import pyodbc
from .globalFunc import *

class CrimeRecord:
    
    def __init__(self, CrimeID, CrimeRecord):
        self.CrimeID = CrimeID
        self.CrimeRecord = CrimeRecord
    def insert_into_database(self):
        try:
            values = (self.CrimeID, self.CrimeRecord)
            insert_into_table("CrimeRecord", [values])
            print("CrimeRecord inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting CrimeRecord:", e)
    def get_all():
        return get_all_ids("CrimeRecord","*")
    def get_columns(columns_name):
        return get_all_ids("CrimeRecord",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("CrimeRecord", primary_key, values)

        except pyodbc.Error as e:
            print("Error deleting CrimeRecord:", e)
    
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
            query = """select Criminal.CriminalID,FirstName+ ' '+LastName as Name,CrimeRecord from Criminal join CrimeRecord on
                        Criminal.CriminalID = CrimeRecord.CriminalID;"""
            
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