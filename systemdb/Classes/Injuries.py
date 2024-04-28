import pyodbc
from .globalFunc import *

class Injuries:
    def __init__(self, VictimID, Injury):
        self.VictimID = VictimID
        self.Injury = Injury

    def insert_into_database(self):
        try:
            values = (self.VictimID, self.Injury)
            insert_into_table("Injuries", [values])
            print("Injury inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Injury:", e)

    def get_all():
        return get_all_ids("Injuries", "*")

    def get_columns(columns_name):
        return get_all_ids("Injuries", columns_name)

    def delete(primary_key, values):
        try:
            delete_from_table("Injuries", primary_key, values)
            print("Injury deleted successfully.")

        except pyodbc.Error as e:
            print("Error deleting Injury:", e)

    def search(value):
        return search_by_primary_key('Injuries', 'Victim_ID', value)
    
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
            query = """Select Victim.VictimID,FirstName+' '+LastName as Name,Injuries.Injury from Victim join Injuries
                    on Victim.VictimID=Injuries.Victim_ID;"""
            
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