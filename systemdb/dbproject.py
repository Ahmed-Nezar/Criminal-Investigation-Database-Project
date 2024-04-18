import pyodbc


def get_all_ids(table_name, primary_keys):
    ids = []
    cursor = None
    conn = None
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                               'Server=.;'
                               'Database=Criminal Investigation System;'
                               'Trusted_Connection=yes;')
        cursor = conn.cursor()

        column_names = ", ".join(primary_keys)
        cursor.execute(f'SELECT {column_names} FROM {table_name}')
        rows = cursor.fetchall()
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
        cursor = None 
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=.;'
                                   'Database=Criminal Investigation System;'
                                   'Trusted_Connection=yes;')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Suspect (SuspectID, FirstName, LastName, Gender, DateOfBirth, PhoneRecord, AddressStreet, AddressGovernment, AddressZIP)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (self.SuspectID, self.FirstName, self.LastName, self.Gender, self.DateOfBirth, self.PhoneRecord, self.AddressStreet, self.AddressGovernment, self.AddressZIP))

            conn.commit()
            print("Suspect inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Suspect:", e)

        finally:
            if cursor:
                cursor.close()  # Close cursor
            if conn:
                conn.close()  # Close connection
    
    
class Criminal:
    def __init__(self, CriminalID, FirstName, LastName, Status, Description):
        self.CriminalID = CriminalID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Status = Status
        self.Description = Description

    def insert_into_database(self):
        cursor = None 
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=.;'
                                   'Database=Criminal Investigation System;'
                                   'Trusted_Connection=yes;')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Criminal (CriminalID, FirstName, LastName, Status, Description)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.CriminalID, self.FirstName, self.LastName, self.Status, self.Description))

            conn.commit()
            print("Criminal inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Criminal:", e)

        finally:
            if cursor:
                cursor.close()  # Close cursor
            if conn:
                conn.close()  # Close connection
class CriminalRecord:
    
    def __init__(self, SuspectID, CriminalID, CrimeRecord):
        self.SuspectID = SuspectID
        self.CriminalID = CriminalID
        self.CrimeRecord = CrimeRecord

    def insert_into_database(self):
        cursor = None 

        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=.;'
                                   'Database=Criminal Investigation System;'
                                   'Trusted_Connection=yes;')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO CriminalRecord (SuspectID, CriminalID, CrimeRecord)
                VALUES (?, ?, ?)
            ''', (self.SuspectID, self.CriminalID, self.CrimeRecord))

            conn.commit()
            print("CriminalRecord inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting CriminalRecord:", e)

        finally:
            if cursor:
                cursor.close()  # Close cursor
            if conn:
                conn.close()  # Close connection

class Case:
    def __init__(self, CaseID, StartDate, EndDate, Description, Status, OfficerID):
        self.CaseID = CaseID
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.Description = Description
        self.Status = Status
        self.OfficerID = OfficerID

    def insert_into_database(self):
        cursor = None 
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=.;'
                                   'Database=Criminal Investigation System;'
                                   'Trusted_Connection=yes;')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Case1 (CaseID, StartDate, EndDate, Description, Status, OfficerID)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (self.CaseID, self.StartDate, self.EndDate, self.Description, self.Status, self.OfficerID))

            conn.commit()
            print("Case inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Case:", e)

        finally:
            if cursor:
                cursor.close()  # Close cursor
            if conn:
                conn.close()  # Close connection



class CrimeScene:
    def __init__(self, CaseID, Time, Location):
        self.CaseID = CaseID
        self.Time = Time
        self.Location = Location

    def insert_into_database(self):
        cursor = None 
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=.;'
                                   'Database=Criminal Investigation System;'
                                   'Trusted_Connection=yes;')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO CrimeScene (CaseID, Time, Location)
                VALUES (?, ?, ?)
            ''', (self.CaseID, self.Time, self.Location))

            conn.commit()
            print("CrimeScene inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting CrimeScene:", e)

        finally:
            if cursor:
                cursor.close()  # Close cursor
            if conn:
                conn.close()  # Close connection

class Evidence:
    def __init__(self, CaseID, Type, Description):
        self.CaseID = CaseID
        self.Type = Type
        self.Description = Description

    def insert_into_database(self):
        cursor = None 
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=.;'
                                   'Database=Criminal Investigation System;'
                                   'Trusted_Connection=yes;')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Evidence (CaseID, Type, Description)
                VALUES (?, ?, ?)
            ''', (self.CaseID, self.Type, self.Description))

            conn.commit()
            print("Evidence inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Evidence:", e)

        finally:
            if cursor:
                cursor.close()  # Close cursor
            if conn:
                conn.close()  # Close connection

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
        cursor = None 
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=.;'
                                   'Database=Criminal Investigation System;'
                                   'Trusted_Connection=yes;')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Witness1 (WitnessID, FirstName, LastName, DateOfBirth, Gender, Age, Address, PhoneNumber, Email)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (self.WitnessID, self.FirstName, self.LastName, self.DateOfBirth, self.Gender, self.Age, self.Address, self.PhoneNumber, self.Email))

            conn.commit()
            print("Witness inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Witness:", e)

        finally:
            if cursor:
                cursor.close()  # Close cursor
            if conn:
                conn.close()  # Close connection

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
        cursor = None 
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=.;'
                                   'Database=Criminal Investigation System;'
                                   'Trusted_Connection=yes;')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Victim (VictimID, FirstName, LastName, DateOfBirth, Age, Gender, Address, PhoneNumber, Injuries)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (self.VictimID, self.FirstName, self.LastName, self.DateOfBirth, self.Age, self.Gender, self.Address, self.PhoneNumber, self.Injuries))

            conn.commit()
            print("Victim inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Victim:", e)

        finally:
            if cursor:
                cursor.close()  # Close cursor
            if conn:
                conn.close()  # Close connection

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
        cursor = None 
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=.;'
                                   'Database=Criminal Investigation System;'
                                   'Trusted_Connection=yes;')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Officer (OfficerID, FirstName, LastName, DateOfBirth, Gender, BadgeNumber, Rank, SupervisorID, Email, PhoneNumber)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (self.OfficerID, self.FirstName, self.LastName, self.DateOfBirth, self.Gender, self.BadgeNumber, self.Rank, self.SupervisorID, self.Email, self.PhoneNumber))

            conn.commit()
            print("Officer inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Officer:", e)

        finally:
            if cursor:
                cursor.close()  # Close cursor
            if conn:
                conn.close()  # Close connection

class PoliceStation:
    def __init__(self, StationID, Name, Location, Telephone, StationChief):
        self.StationID = StationID
        self.Name = Name
        self.Location = Location
        self.Telephone = Telephone
        self.StationChief = StationChief

    def insert_into_database(self):
        cursor = None 
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=.;'
                                   'Database=Criminal Investigation System;'
                                   'Trusted_Connection=yes;')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO PoliceStation (StationID, Name, Location, Telephone, StationChief)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.StationID, self.Name, self.Location, self.Telephone, self.StationChief))

            conn.commit()
            print("PoliceStation inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting PoliceStation:", e)

        finally:
            if cursor:
                cursor.close()  # Close cursor
            if conn:
                conn.close()  # Close connection

class Arrest:
    def __init__(self, OfficerID, CaseID, ArrestDate):
        self.OfficerID = OfficerID
        self.CaseID = CaseID
        self.ArrestDate = ArrestDate

    def insert_into_database(self):
        cursor = None 
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=.;'
                                   'Database=Criminal Investigation System;'
                                   'Trusted_Connection=yes;')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Arrest (OfficerID, CaseID, ArrestDate)
                VALUES (?, ?, ?)
            ''', (self.OfficerID, self.CaseID, self.ArrestDate))

            conn.commit()
            print("Arrest inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Arrest:", e)

        finally:
            if cursor:
                cursor.close()  # Close cursor
            if conn:
                conn.close()  # Close connection

class Interrogates:
    def __init__(self, OfficerID, SuspectID):
        self.OfficerID = OfficerID
        self.SuspectID = SuspectID

    def insert_into_database(self):
        cursor = None 
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=.;'
                                   'Database=Criminal Investigation System;'
                                   'Trusted_Connection=yes;')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Interrogates (OfficerID, SuspectID)
                VALUES (?, ?)
            ''', (self.OfficerID, self.SuspectID))

            conn.commit()
            print("Interrogates inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Interrogates:", e)

        finally:
            if cursor:
                cursor.close()  # Close cursor
            if conn:
                conn.close()  # Close connection

class Affects:
    def __init__(self, CaseID, VictimID):
        self.CaseID = CaseID
        self.VictimID = VictimID

    def insert_into_database(self):
        cursor = None 
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=.;'
                                   'Database=Criminal Investigation System;'
                                   'Trusted_Connection=yes;')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Affects (CaseID, VictimID)
                VALUES (?, ?)
            ''', (self.CaseID, self.VictimID))

            conn.commit()
            print("Affects inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Affects:", e)

        finally:
            if cursor:
                cursor.close()  # Close cursor
            if conn:
                conn.close()  # Close connection

class Witnessed:
    def __init__(self, CaseID, WitnessID):
        self.CaseID = CaseID
        self.WitnessID = WitnessID

    def insert_into_database(self):
        cursor = None 
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=.;'
                                   'Database=Criminal Investigation System;'
                                   'Trusted_Connection=yes;')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Witnessed (CaseID, WitnessID)
                VALUES (?, ?)
            ''', (self.CaseID, self.WitnessID))

            conn.commit()
            print("Witnessed inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Witnessed:", e)

        finally:
            if cursor:
                cursor.close()  # Close cursor
            if conn:
                conn.close()  # Close connection

class Investigates:
    def __init__(self, OfficerID, CaseID, LeadInvestigatorID):
        self.OfficerID = OfficerID
        self.CaseID = CaseID
        self.LeadInvestigatorID = LeadInvestigatorID

    def insert_into_database(self):
        cursor = None 
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=.;'
                                   'Database=Criminal Investigation System;'
                                   'Trusted_Connection=yes;')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Investigates (OfficerID, CaseID, LeadInvestigatorID)
                VALUES (?, ?, ?)
            ''', (self.OfficerID, self.CaseID, self.LeadInvestigatorID))

            conn.commit()
            print("Investigates inserted successfully.")

        except pyodbc.Error as e:
            print("Error inserting Investigates:", e)

        finally:
            if cursor:
                cursor.close()  # Close cursor
            if conn:
                conn.close()  # Close connection


