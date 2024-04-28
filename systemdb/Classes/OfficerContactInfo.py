import pyodbc
from .globalFunc import *

class OfficerContactInfo:
    
    def __init__(self, OfficerID, Email, PhoneNo):
        self.OfficerID = OfficerID
        self.Email = Email
        self.PhoneNo = PhoneNo
    def insert_into_database(self):
        try:
            values = (self.OfficerID, self.Email, self.PhoneNo)
            insert_into_table("OfficerContactInfo", [values])

        except pyodbc.Error as e:
            print("Error inserting OfficerContactInfo:", e)
    def get_all():
        return get_all_ids("OfficerContactInfo","*")
    def get_columns(columns_name):
        return get_all_ids("OfficerContactInfo",columns_name)
    def delete(primary_keys,values):
        try:
            delete_from_table("OfficerContactInfo", primary_keys, values)
            print("OfficerContactInfo deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting OfficerContactInfo:", e)
    
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
            query = """select Officer.OfficerID, FirstName+' '+LastName, Email,PhoneNumber from Officer 
                    Join OfficerContactInfo on Officer.OfficerID = OfficerContactInfo.OfficerID;"""
            
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