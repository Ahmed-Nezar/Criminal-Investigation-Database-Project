import pyodbc
from .globalFunc import *

class Arrest:
    def __init__(self, OfficerID, CaseID, ArrestDate):
        self.OfficerID = OfficerID
        self.CaseID = CaseID
        self.ArrestDate = ArrestDate

    def insert_into_database(self):
        try:
            values = (self.OfficerID, self.CaseID, self.ArrestDate)
            insert_into_table("Arrest", [values])
            print("Arrest inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Arrest:", e)
    def get_all():
        return get_all_ids("Arrest","*")
    def get_columns(columns_name):
        return get_all_ids("Arrest",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("Arrest", primary_key, values)
            print("Arrest deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Arrest:", e)
    
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
            query = """select Officer.OfficerID, Arrest.CriminalID, Officer.FirstName+' '+Officer.LastName as OfficerName,  
                    Criminal.FirstName+' '+Criminal.LastName as CriminalName, Arrest.ArrestDate From Officer join Arrest on Officer.OfficerID=Arrest.OfficerID 
                    join Criminal on Criminal.CriminalID = Arrest.CriminalID;"""
            
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