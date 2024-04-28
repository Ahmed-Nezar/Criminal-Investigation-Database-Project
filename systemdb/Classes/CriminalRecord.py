import pyodbc
from .globalFunc import *

class CriminalRecord:
    
    def __init__(self, SuspectID, CrimeRecord):
        self.SuspectID = SuspectID
        self.CrimeRecord = CrimeRecord
    def insert_into_database(self):
        try:
            values = (self.SuspectID, self.CrimeRecord)
            insert_into_table("CriminalRecord", [values])
            print("CriminalRecord inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting CriminalRecord:", e)
    def get_all():
        return get_all_ids("CriminalRecord","*")
    def get_columns(columns_name):
        return get_all_ids("CriminalRecord",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("CriminalRecord", primary_key, values)
            print("CriminalRecord deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting CriminalRecord:", e)
    
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
            query = """select Suspect.SuspectID,FirstName+ ' '+LastName as Name,Criminal_Record,CaseID from Suspect join CriminalRecord on
                        Suspect.SuspectID=CriminalRecord.SuspectID
                        join Involved on Suspect.SuspectID=Involved.SuspectID;"""
            
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