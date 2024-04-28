import pyodbc
from .globalFunc import *

class Investigates:
    def __init__(self, OfficerID, CaseID, LeadInvestigatorID):
        self.OfficerID = OfficerID
        self.CaseID = CaseID
        self.LeadInvestigatorID = LeadInvestigatorID

    def insert_into_database(self):
        try:
            values = (self.OfficerID, self.CaseID, self.LeadInvestigatorID)
            insert_into_table("Investigates", [values])
            print("Investigates inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Investigates:", e)
    def get_all():
        return get_all_ids("Investigates","*")
    def get_columns(columns_name):
        return get_all_ids("Investigates",columns_name)
    def delete(primary_key, values):
        try:
            delete_from_table("Investigates", primary_key, values)
            print("Investigates deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Investigates:", e)
    
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
            query = """Select * From Investigates;"""
            
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