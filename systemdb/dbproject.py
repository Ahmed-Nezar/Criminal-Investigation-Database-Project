import pyodbc
#Criminal Investigation System
def insert_into_table(table_name, values):
    cursor = None
    conn = None
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                               'Server=.;'
                               'Database=Criminal Investigation System;'
                               'Trusted_Connection=yes;')
        cursor = conn.cursor()

        # Construct the SQL query dynamically
        placeholders = ','.join(['?' for _ in range(len(values[0]))])
        query = f'INSERT INTO {table_name} VALUES ({placeholders})'
        
        cursor.executemany(query, values)
        conn.commit()
        print("Values inserted into", table_name, "successfully.")

    except pyodbc.Error as e:
        print("Error inserting values into", table_name + ":", e)

    finally:
        if cursor:
            cursor.close()  
        if conn:
            conn.close()

def writequery(code):
    cursor = None
    conn = None
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                               'Server=.;'
                               'Database=Criminal Investigation System;'
                               'Trusted_Connection=yes;')
        cursor = conn.cursor()

        # Construct the SQL query dynamically
        query = code
        
        cursor.execute(query)
        conn.commit()
        print("The code is run successfully.")

    except pyodbc.Error as e:
        print("Error inserting values into:", e)

    finally:
        if cursor:
            cursor.close()  
        if conn:
            conn.close()

def get_all_ids(table_name, primary_keys):
    ids = []
    cursor = None
    conn = None
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                               'Server=.;'
                               'Database=quiz;'
                               'Trusted_Connection=yes;')
        cursor = conn.cursor()

        column_names = ", ".join(primary_keys)
        cursor.execute(f'SELECT {column_names} FROM {table_name}')
        rows = cursor.fetchall()
        if primary_keys=='*':
            ids=rows
        else:
            for row in rows:
                if len(primary_keys) == 1:
                    ids.append(row[0])
                else:
                    ids.append(row)

    except pyodbc.Error as e:
        print("Error fetching IDs:", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return ids



class Suspect:
    def __init__(self, SuspectID, FirstName, LastName, Gender, DateOfBirth, PhoneRecord, AddressStreet, AddressGovernment, AddressZIP):
        self.SuspectID = SuspectID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Gender = Gender
        self.DateOfBirth = DateOfBirth
        self.PhoneRecord = PhoneRecord
        self.AddressStreet = AddressStreet
        self.AddressGovernment = AddressGovernment
        self.AddressZIP = AddressZIP

    def insert_into_database(self):
        try:
            values = (self.SuspectID, self.FirstName, self.LastName, self.Gender, self.DateOfBirth, self.PhoneRecord, self.AddressStreet, self.AddressGovernment, self.AddressZIP)
            insert_into_table("Suspect", [values])
            print("Suspect inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Suspect:", e)
    def get_all():
        return get_all_ids("Suspect","*")
    def get_columns(columns_name):
        return get_all_ids("Suspect",columns_name)
    
class Criminal:
    def __init__(self, CriminalID, FirstName, LastName, Status, Description):
        self.CriminalID = CriminalID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Status = Status
        self.Description = Description

    def insert_into_database(self):
        try:
            values = (self.CriminalID, self.FirstName, self.LastName, self.Status, self.Description)
            insert_into_table("Criminal", [values])
            print("Criminal inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Criminal:", e)
        def get_all():
            return get_all_ids("Criminal","*")
        def get_columns(columns_name):
            return get_all_ids("Criminal",columns_name)

class CriminalRecord:
    
    def __init__(self, SuspectID, CriminalID, CrimeRecord):
        self.SuspectID = SuspectID
        self.CriminalID = CriminalID
        self.CrimeRecord = CrimeRecord
    def insert_into_database(self):
        try:
            values = (self.SuspectID, self.CriminalID, self.CrimeRecord)
            insert_into_table("CriminalRecord", [values])
            print("CriminalRecord inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting CriminalRecord:", e)
    def get_all():
        return get_all_ids("CriminalRecord","*")
    def get_columns(columns_name):
        return get_all_ids("CriminalRecord",columns_name)

class Case:
    def __init__(self, CaseID, StartDate, EndDate, Description, Status, OfficerID):
        self.CaseID = CaseID
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.Description = Description
        self.Status = Status
        self.OfficerID = OfficerID

    def insert_into_database(self):
        try:
            values = (self.CaseID, self.StartDate, self.EndDate, self.Description, self.Status, self.OfficerID)
            insert_into_table("Case", [values])
            print("Case inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Case:", e)
    def get_all():
        return get_all_ids("Case","*")
    def get_columns(columns_name):
        return get_all_ids("Case",columns_name)



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
class Evidence:
    def __init__(self, CaseID, Type, Description):
        self.CaseID = CaseID
        self.Type = Type
        self.Description = Description

    def insert_into_database(self):
        try:
            values = (self.CaseID, self.Type, self.Description)
            insert_into_table("Evidence", [values])
            print("Evidence inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Evidence:", e)
    def get_all():
        return get_all_ids("Evidence","*")
    def get_columns(columns_name):
        return get_all_ids("Evidence",columns_name)

class Witness:
    def __init__(self, WitnessID, FirstName, LastName, DateOfBirth, Gender, Age, Address, PhoneNumber, Email):
        self.WitnessID = WitnessID
        self.FirstName = FirstName
        self.LastName = LastName
        self.DateOfBirth = DateOfBirth
        self.Gender = Gender
        self.Age = Age
        self.Address = Address
        self.PhoneNumber = PhoneNumber
        self.Email = Email

    def insert_into_database(self):
        try:
            values = (self.WitnessID, self.FirstName, self.LastName, self.DateOfBirth, self.Gender, self.Age, self.Address, self.PhoneNumber, self.Email)
            insert_into_table("Witness1", [values])
            print("Witness inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Witness:", e)
    def get_all():
        return get_all_ids("Witness1","*")
    def get_columns(columns_name):
        return get_all_ids("Witness1",columns_name)

class Victim:
    def __init__(self, VictimID, FirstName, LastName, DateOfBirth, Age, Gender, Address, PhoneNumber, Injuries):
        self.VictimID = VictimID
        self.FirstName = FirstName
        self.LastName = LastName
        self.DateOfBirth = DateOfBirth
        self.Age = Age
        self.Gender = Gender
        self.Address = Address
        self.PhoneNumber = PhoneNumber
        self.Injuries = Injuries

    def insert_into_database(self):
        try:
            values = (self.VictimID, self.FirstName, self.LastName, self.DateOfBirth, self.Age, self.Gender, self.Address, self.PhoneNumber, self.Injuries)
            insert_into_table("Victim", [values])
            print("Victim inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Victim:", e)
    def get_all():
        return get_all_ids("Victim","*")
    def get_columns(columns_name):
        return get_all_ids("Victim",columns_name)

class Officer:
    def __init__(self, OfficerID, FirstName, LastName, DateOfBirth, Gender, BadgeNumber, Rank, SupervisorID, Email, PhoneNumber):
        self.OfficerID = OfficerID
        self.FirstName = FirstName
        self.LastName = LastName
        self.DateOfBirth = DateOfBirth
        self.Gender = Gender
        self.BadgeNumber = BadgeNumber
        self.Rank = Rank
        self.SupervisorID = SupervisorID
        self.Email = Email
        self.PhoneNumber = PhoneNumber

    def insert_into_database(self):
        try:
            values = (self.OfficerID, self.FirstName, self.LastName, self.DateOfBirth, self.Gender, self.BadgeNumber, self.Rank, self.SupervisorID, self.Email, self.PhoneNumber)
            insert_into_table("Officer", [values])
            print("Officer inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Officer:", e)
    def get_all():
        return get_all_ids("Officer","*")
    def get_columns(columns_name):
        return get_all_ids("Officer",columns_name)
    
class PoliceStation:
    def __init__(self, StationID, Name, Location, Telephone, StationChief):
        self.StationID = StationID
        self.Name = Name
        self.Location = Location
        self.Telephone = Telephone
        self.StationChief = StationChief

    def insert_into_database(self):
        try:
            values = (self.StationID, self.Name, self.Location, self.Telephone, self.StationChief)
            insert_into_table("PoliceStation", [values])
            print("PoliceStation inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting PoliceStation:", e)
    def get_all():
        return get_all_ids("PoliceStation","*")
    def get_columns(columns_name):
        return get_all_ids("PoliceStation",columns_name)

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

class Interrogates:
    def __init__(self, OfficerID, SuspectID):
        self.OfficerID = OfficerID
        self.SuspectID = SuspectID

    def insert_into_database(self):
        try:
            values = (self.OfficerID, self.SuspectID)
            insert_into_table("Interrogates", [values])
            print("Interrogates inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Interrogates:", e)
    def get_all():
        return get_all_ids("Interrogates","*")
    def get_columns(columns_name):
        return get_all_ids("Interrogates",columns_name)

class Affects:
    def __init__(self, CaseID, VictimID):
        self.CaseID = CaseID
        self.VictimID = VictimID

    def insert_into_database(self):
        try:
            values = (self.CaseID, self.VictimID)
            insert_into_table("Affects", [values])
            print("Affects inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Affects:", e)
    def get_all():
        return get_all_ids("Affects","*")
    def get_columns(columns_name):
        return get_all_ids("Affects",columns_name)

class Witnessed:
    def __init__(self, CaseID, WitnessID):
        self.CaseID = CaseID
        self.WitnessID = WitnessID

    def insert_into_database(self):
        try:
            values = (self.CaseID, self.WitnessID)
            insert_into_table("Witnessed", [values])
            print("Witnessed inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Witnessed:", e)

    def get_all():
        return get_all_ids("Witnessed","*")
    def get_columns(columns_name):
        return get_all_ids("Witnessed",columns_name)

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


