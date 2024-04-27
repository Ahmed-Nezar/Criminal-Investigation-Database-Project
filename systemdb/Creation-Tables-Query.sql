CREATE DATABASE [Criminal Investigation System];
-- Suspect table
CREATE TABLE Suspect (
    SuspectID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender VARCHAR(10),
    DateOfBirth DATE,
    PhoneRecord VARCHAR(100), -- You may want to adjust the data type and size
    AddressStreet VARCHAR(100),
    AddressGovernment VARCHAR(100),
    AddressZIP VARCHAR(20)
);

-- Criminal table
CREATE TABLE Criminal (
    CriminalID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Status VARCHAR(50),
    Description TEXT
);

-- Criminal Record table
CREATE TABLE CriminalRecord (
    SuspectID INT,
    Criminal_Record VARCHAR(100),
    PRIMARY KEY (SuspectID, Criminal_Record),
	CONSTRAINT SID_FK FOREIGN KEY  (SuspectID) REFERENCES Suspect(SuspectID),
);

-- Case table
CREATE TABLE _Case_ (
    CaseID INT PRIMARY KEY,
    StartDate DATE,
    EndDate DATE,
    Description TEXT,
    Status VARCHAR(50),
	OfficerID INT, 
    
);

-- Crime Scene table
CREATE TABLE CrimeScene (
    CaseID INT, 
    Time DATETIME,
    Location VARCHAR(100),
    PRIMARY KEY (CaseID, Time),
    CONSTRAINT CaseID_CrimeScene_FK FOREIGN KEY (CaseID) REFERENCES _Case_(CaseID)
);

-- Evidence table
CREATE TABLE Evidence (
    CaseID INT,
    Type VARCHAR(50),
    Description TEXT,
    PRIMARY KEY (CaseID, Type),
    CONSTRAINT Case_ID_FK_Evidence FOREIGN KEY (CaseID) REFERENCES _Case_(CaseID)
);

-- Witness table
CREATE TABLE Witness (
    WitnessID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Gender VARCHAR(10),
    Age INT,
    Address VARCHAR(100),
);

CREATE TABLE Witness_Contact(
	WitnessID int,
	PhoneNumber varchar(20),
	Email varchar(50),
	PRIMARY KEY (WitnessID, Email, PhoneNumber),
	CONSTRAINT WitnessID_Contact_FK FOREIGN KEY (WitnessID) REFERENCES Witness(WitnessID),
);


-- Victim table
CREATE TABLE Victim (
    VictimID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Age INT,
    Gender VARCHAR(10),
    Address VARCHAR(100),
);

CREATE TABLE Victim_Phone_Number(
	Victim_ID INT,
	PhoneNumber VARCHAR(20),
	PRIMARY KEY(Victim_ID, PhoneNumber),
	CONSTRAINT Victim_ID_Victim_FK FOREIGN KEY (Victim_ID) REFERENCES Victim(VictimID),
);

CREATE TABLE Injuries(
	
	Victim_ID INT,
	Injury VARCHAR(20),
	PRIMARY KEY(Victim_ID, Injury),
	CONSTRAINT Victim_ID_INJURIES_FK FOREIGN KEY (Victim_ID) REFERENCES Victim(VictimID),
);



-- Officer table
CREATE TABLE Officer (
    OfficerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Gender VARCHAR(10),
    BadgeNumber VARCHAR(20),
    Rank VARCHAR(50),
    SupervisorID INT,
	StationID INT, 
    CONSTRAINT S_ID_FK_Officer FOREIGN KEY (SupervisorID) REFERENCES Officer(OfficerID)
);
ALTER TABLE _Case_
ADD CONSTRAINT FK_Case_Officer
FOREIGN KEY (OfficerID)
REFERENCES Officer(OfficerID);
-- Police Station table
CREATE TABLE PoliceStation (
    StationID INT PRIMARY KEY,
    Name VARCHAR(100),
    Location VARCHAR(100),
    Telephone VARCHAR(20),
    StationChief INT,
    CONSTRAINT StationChief_FK FOREIGN KEY (StationChief) REFERENCES Officer(OfficerID)
);

ALTER TABLE Officer
ADD CONSTRAINT FK_SationID_Officer FOREIGN KEY(StationID) REFERENCES PoliceStation(StationID);

-- Arrest table
CREATE TABLE Arrest (
    OfficerID INT,
    CaseID INT,
    ArrestDate DATE,
    PRIMARY KEY (OfficerID, CaseID, ArrestDate),
    FOREIGN KEY (OfficerID) REFERENCES Officer(OfficerID),
    FOREIGN KEY (CaseID) REFERENCES _Case_(CaseID)
);

-- Interrogates table
CREATE TABLE Interrogates (
    OfficerID INT,
    SuspectID INT,
    PRIMARY KEY (OfficerID, SuspectID),
    FOREIGN KEY (OfficerID) REFERENCES Officer(OfficerID),
    FOREIGN KEY (SuspectID) REFERENCES Suspect(SuspectID)
);

-- Affects table (Association between Case and Victim)
CREATE TABLE Affects (
    CaseID INT,
    VictimID INT,
    PRIMARY KEY (CaseID, VictimID),
    FOREIGN KEY (CaseID) REFERENCES _Case_(CaseID),
    FOREIGN KEY (VictimID) REFERENCES Victim(VictimID)
);

-- Witnessed table (Association between Case and Witness)
CREATE TABLE Witnessed (
    CaseID INT,
    WitnessID INT,
    PRIMARY KEY (CaseID, WitnessID),
    FOREIGN KEY (CaseID) REFERENCES _Case_(CaseID),
    FOREIGN KEY (WitnessID) REFERENCES Witness(WitnessID)
);

-- Investigates table (Association between Officer and Case)
CREATE TABLE Investigates (
    OfficerID INT,
    CaseID INT,
	LeadInvestigatiorID INT,
    PRIMARY KEY (OfficerID, CaseID),
    FOREIGN KEY (CaseID) REFERENCES _Case_(CaseID),
    FOREIGN KEY (OfficerID) REFERENCES Officer(OfficerID),
	FOREIGN KEY (LeadInvestigatiorID) REFERENCES Officer(OfficerID),
);


CREATE TABLE Involved (
	SuspectID int,
	CaseID int,
	PRIMARY KEY (SuspectID, CaseID),
	FOREIGN KEY (SuspectID) REFERENCES Suspect(SuspectID),
	FOREIGN KEY (CaseID) REFERENCES _Case_(CaseID),
);

CREATE TABLE OfficerContactInfo (
    OfficerID INT,
    Email VARCHAR(100),
    PhoneNumber VARCHAR(20),
    PRIMARY KEY (OfficerID, Email, PhoneNumber),
    FOREIGN KEY (OfficerID) REFERENCES Officer(OfficerID)
);

CREATE TABLE CrimeRecord (
    CriminalID INT,
    CrimeRecord VARCHAR(255),
    PRIMARY KEY (CriminalID, CrimeRecord),
    FOREIGN KEY (CriminalID) REFERENCES Criminal(CriminalID)
);


