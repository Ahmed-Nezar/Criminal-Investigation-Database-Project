-- Inserting in Tables that don't contain Foreign Keys
-- Inserting data into the Suspect table
INSERT INTO Suspect (SuspectID, FirstName, LastName, Gender, DateOfBirth, PhoneRecord, AddressStreet, AddressGovernment, AddressZIP) 
VALUES 
(815,'Bob', 'Brown', 'Male', '1985-03-15', 'Record2024', '456 Elm St', 'Springfield', '98765'),
(820,'Alice', 'Smith', 'Female', '1990-07-20', 'Record2024', '789 Oak St', 'Springfield', '98765'),
(830, 'John', 'Doe', 'Male', '1978-12-10', 'Record2024', '123 Maple St', 'Springfield', '98765'),
(840, 'Emily', 'Johnson', 'Female', '1989-05-02', 'Record2024', '321 Pine St', 'Springfield', '98765'),
(850, 'Michael', 'Williams', 'Male', '1982-09-18', 'Record2024', '567 Birch St', 'Springfield', '98765'),
(860, 'Sarah', 'Garcia', 'Female', '1995-04-30', 'Record2024', '890 Cedar St', 'Springfield', '98765'),
(870, 'David', 'Martinez', 'Male', '1987-11-25', 'Record2024', '234 Walnut St', 'Springfield', '98765'),
(880, 'Jessica', 'Brown', 'Female', '1983-08-14', 'Record2024', '678 Sycamore St', 'Springfield', '98765'),
(890, 'Christopher', 'Wilson', 'Male', '1975-06-05', 'Record2024', '901 Pineapple St', 'Springfield', '98765'),
(810, 'Michelle', 'Lopez', 'Female', '1992-02-28', 'Record2024', '345 Mango St', 'Springfield', '98765'),
(811, 'Daniel', 'Gonzalez', 'Male', '1980-10-12', 'Record2024', '789 Coconut St', 'Springfield', '98765');

-- Inserting Data into Criminal Table
INSERT INTO Criminal (CriminalID, FirstName, LastName, Status, Description) 
VALUES 
(215, 'Bob', 'Brown', 'Apprehended', 'Involved in multiple robberies'),
(220, 'Alice', 'Smith', 'At Large', 'Suspected of embezzlement'),
(230, 'John', 'Doe', 'Apprehended', 'Drug trafficking'),
(240, 'Emily', 'Johnson', 'At Large', 'Forgery and identity theft'),
(250, 'Michael', 'Williams', 'At Large', 'Suspected of assault'),
(260, 'Sarah', 'Garcia', 'At Large', 'Hacking and cybercrimes'),
(270, 'David', 'Martinez', 'Apprehended', 'Illegal gambling'),
(280, 'Jessica', 'Brown', 'At Large', 'Counterfeiting'),
(290, 'Christopher', 'Wilson', 'At Large', 'Suspected of arson'),
(210, 'Michelle', 'Lopez', 'Apprehended', 'Human trafficking'),
(211, 'Daniel', 'Gonzalez', 'At Large', 'Money laundering');

--Inserting into Witness
INSERT INTO Witness (WitnessID, FirstName, LastName, DateOfBirth, Gender, Age, Address) 
VALUES 
(616, 'Charlie', 'Green', '1987-08-09', 'Male', 36, '789 Oak St'),
(620, 'Emma', 'Taylor', '1995-04-25', 'Female', 29, '123 Maple St'),
(630, 'William', 'Anderson', '1980-12-15', 'Male', 43, '321 Pine St'),
(640, 'Olivia', 'White', '1992-06-03', 'Female', 31, '567 Birch St'),
(650, 'James', 'Brown', '1978-09-20', 'Male', 45, '890 Cedar St'),
(660, 'Ava', 'Jones', '1983-11-28', 'Female', 40, '234 Walnut St'),
(670, 'Logan', 'Clark', '1990-07-14', 'Male', 33, '678 Sycamore St'),
(680, 'Sophia', 'Hall', '1986-03-10', 'Female', 38, '901 Pineapple St'),
(690, 'Jackson', 'King', '1972-05-18', 'Male', 51, '345 Mango St'),
(610, 'Isabella', 'Lee', '1988-02-02', 'Female', 36, '789 Coconut St'),
(611, 'Mason', 'Wright', '1997-09-12', 'Male', 26, '678 Walnut St');

--Inserting into Victim
INSERT INTO Victim (VictimID, FirstName, LastName, DateOfBirth, Age, Gender, Address) 
VALUES 
(181, 'Alice', 'Smith', '1990-05-20', 33, 'Female', '123 Maple St'),
(182, 'John', 'Doe', '1985-12-10', 38, 'Male', '456 Elm St'),
(183, 'Emily', 'Johnson', '1989-02-05', 33, 'Female', '789 Oak St'),
(184, 'Michael', 'Williams', '1982-06-18', 41, 'Male', '123 Maple St'),
(185, 'Sarah', 'Garcia', '1995-03-30', 29, 'Female', '321 Pine St'),
(186, 'David', 'Martinez', '1987-08-25', 36, 'Male', '567 Birch St'),
(187, 'Jessica', 'Brown', '1983-05-14', 38, 'Female', '890 Cedar St'),
(188, 'Christopher', 'Wilson', '1975-11-05', 48, 'Male', '234 Walnut St'),
(189, 'Michelle', 'Lopez', '1992-08-28', 31, 'Female', '678 Sycamore St'),
(190, 'Daniel', 'Gonzalez', '1980-03-12', 44, 'Male', '901 Pineapple St'),
(191, 'Sophia', 'Hernandez', '1984-10-02', 39, 'Female', '345 Mango St');
-------------------------------------------------------------------------------------------
--Inserting data into columns having Forign Keys
-- Inserting data into the Officer table
INSERT INTO Officer (OfficerID, FirstName, LastName, DateOfBirth, Gender, BadgeNumber, Rank, SupervisorID, StationID) 
VALUES 
(1000, 'John', 'Doe', '1980-04-15', 'Male', '12345', 'Sergeant', NULL, NULL),
(1001, 'Alice', 'Smith', '1985-09-20', 'Female', '54321', 'Lieutenant', NULL, NULL),
(1002, 'Michael', 'Johnson', '1992-12-05', 'Male', '67890', 'Detective', NULL, NULL),
(1003, 'Emily', 'Brown', '1978-06-02', 'Female', '09876', 'Captain', NULL, NULL),
(1004, 'David', 'Martinez', '1987-11-25', 'Male', '13579', 'Officer', NULL, NULL),
(1005, 'Jessica', 'Garcia', '1990-03-14', 'Female', '24680', 'Officer', NULL, NULL),
(1006, 'Matthew', 'Rodriguez', '1983-08-30', 'Male', '97531', 'Detective', NULL, NULL),
(1007, 'Emma', 'Hernandez', '1988-05-25', 'Female', '86420', 'Officer', NULL, NULL),
(1008, 'Christopher', 'Lopez', '1976-10-15', 'Male', '01234', 'Sergeant', NULL, NULL),
(1009, 'Sophia', 'Gonzalez', '1989-02-28', 'Female', '56789', 'Lieutenant', NULL, NULL),
(1010, 'James', 'Perez', '1981-07-12', 'Male', '54321', 'Officer', NULL, NULL);

INSERT INTO PoliceStation (StationID, Name, Location, Telephone, StationChief) 
VALUES 
(901, 'Station A', '123 Main St', '555-1234', 1001),
(902, 'Station B', '456 Elm St', '555-5678', 1004),
(903, 'Station C', '789 Oak St', '555-9012', 1006),
(904, 'Station D', '321 Maple St', '555-3456', 1008),
(905, 'Station E', '654 Pine St', '555-7890', 1010);

-- Setting Station ID For Each Officer
UPDATE Officer
SET StationID = 901
WHERE OfficerID < 1003;

UPDATE Officer
SET StationID = 902
WHERE OfficerID BETWEEN 1004 AND 1005;

UPDATE Officer
SET StationID = 903
WHERE OfficerID BETWEEN 1006 AND 1007;

UPDATE Officer
SET StationID = 904
WHERE OfficerID BETWEEN 1007 AND 1008;

UPDATE Officer
SET StationID = 905
WHERE OfficerID BETWEEN 1009 AND 1010;

-- Setting Superviser ID For Each Officer
UPDATE Officer
SET SupervisorID = 1000
WHERE OfficerID BETWEEN 1000 AND 1003;

UPDATE Officer
SET SupervisorID = 1004
WHERE OfficerID BETWEEN 1004 AND 1005;

UPDATE Officer
SET SupervisorID = 1006
WHERE OfficerID BETWEEN 1006 AND 1007;

UPDATE Officer
SET SupervisorID = 1008
WHERE OfficerID BETWEEN 1007 AND 1008;

UPDATE Officer
SET SupervisorID = 1010
WHERE OfficerID BETWEEN 1009 AND 1010;



--Inserting Into Crime Record
INSERT INTO CrimeRecord (CriminalID, CrimeRecord) 
VALUES
(215, 'Perpetrated a series of sophisticated cyber attacks targeting financial institutions, resulting in significant financial losses and data breaches.'),
(220, 'Convicted of multiple counts of grand theft auto and evasion of law enforcement after orchestrating a large-scale car theft ring across state borders.'),
(230, 'Involved in a high-profile corporate espionage case, stealing trade secrets and proprietary information from a leading technology company for a competitor.'),
(240, 'Committed armed robbery at several convenience stores, threatening clerks with a firearm and stealing cash and merchandise.'),
(250, 'Convicted of drug trafficking, operating a large-scale narcotics distribution network distributing illegal substances across multiple states.'),
(260, 'Responsible for orchestrating a Ponzi scheme that defrauded investors of millions of dollars through false promises of high returns on investment.'),
(270, 'Found guilty of orchestrating a complex money laundering operation to conceal the illicit proceeds of various criminal activities, including drug trafficking and fraud.'),
(280, 'Convicted of multiple counts of aggravated assault and battery after engaging in violent altercations resulting in severe injuries to victims.'),
(290, 'Involved in a string of sophisticated identity thefts, stealing personal information to commit financial fraud and identity-related crimes.'),
(210, 'Convicted of arson for setting fire to multiple residential buildings, endangering the lives of occupants and causing extensive property damage.'),
(211, 'Found guilty of homicide in the first degree, having committed premeditated murder with malice aforethought, resulting in the loss of an innocent life.');

--Inserting Into Case
INSERT INTO _Case_ (CaseID, StartDate, EndDate, Description, Status, OfficerID) 
VALUES
(401, '2024-04-01', '2024-04-15', 'Financial fraud investigation involving a Ponzi scheme', 'Open', 1000),
(402, '2024-03-20', '2024-04-10', 'Drug trafficking and distribution network dismantlement', 'Closed', 1001),
(403, '2024-03-15', '2024-04-05', 'Corporate espionage case involving theft of intellectual property', 'Open', 1002),
(404, '2024-04-05', '2024-04-25', 'Armed robbery spree targeting convenience stores', 'Open', 1003),
(405, '2024-03-25', '2024-04-20', 'Identity theft and financial fraud investigation', 'Closed', 1004),
(406, '2024-04-10', '2024-04-30', 'Homicide investigation involving premeditated murder', 'Open', 1005),
(407, '2024-04-03', '2024-04-18', 'Money laundering operation dismantlement', 'Open', 1006),
(408, '2024-03-30', '2024-04-15', 'Series of cyber attacks on financial institutions', 'Open', 1007),
(409, '2024-03-22', '2024-04-12', 'Grand theft auto ring bust', 'Closed', 1008),
(410, '2024-04-08', '2024-04-28', 'Arson investigation involving multiple incidents', 'Open', 1009);

--Inserting Into CrimeScene
INSERT INTO CrimeScene(CaseID, Time, Location)
VALUES
(401, '2024-04-01 10:00:00', '123 Main Street, Anytown'),
(402, '2024-03-20 15:30:00', '456 Elm Street, Newtown'),
(403, '2024-03-15 08:45:00', '789 Oak Street, Springfield'),
(404, '2024-04-05 22:10:00', '321 Pine Street, Rivertown'),
(405, '2024-03-25 13:20:00', '654 Maple Street, Hilltown'),
(406, '2024-04-10 09:15:00', '987 Birch Street, Lakeside'),
(407, '2024-04-03 18:00:00', '741 Cedar Street, Seaview'),
(408, '2024-03-30 11:40:00', '852 Walnut Street, Mountainville'),
(409, '2024-03-22 07:55:00', '369 Cherry Street, Riverside'),
(410, '2024-04-08 14:25:00', '159 Sycamore Street, Lakeshore');

--Inserting Into Evidence
INSERT INTO Evidence(CaseID, Type, Description)
VALUES
(401, 'Document', 'Financial records linking suspects to fraudulent activities'),
(402, 'Weapon', 'Firearm used in the commission of the crime'),
(403, 'Electronic Device', 'Stolen laptop containing proprietary information'),
(404, 'Clothing', 'Apparel worn by suspect during armed robbery'),
(405, 'Identification', 'Forged IDs used in identity theft scheme'),
(406, 'Forensic Sample', 'DNA evidence collected at the crime scene'),
(407, 'Surveillance Footage', 'Video footage capturing suspects movements'),
(408, 'Drug Paraphernalia', 'Evidence of drug manufacturing found at location'),
(409, 'Tool', 'Crowbar used to break into vehicles'),
(410, 'Accelerant', 'Substance used to ignite fires at multiple locations');

--Inserting Into Criminal Record

INSERT INTO CriminalRecord(SuspectID, Criminal_Record)
VALUES
(815, 'Previously convicted for grand theft auto and evasion of law enforcement.'),
(820, 'Known to be involved in drug trafficking and distribution networks across state lines.'),
(830, 'Suspected of orchestrating a series of cyber attacks targeting government institutions.'),
(840, 'Previously arrested for armed robbery and assault with a deadly weapon.'),
(850, 'Suspected of involvement in organized crime and racketeering activities.'),
(860, 'Previously convicted for white-collar crimes including fraud and embezzlement.'),
(870, 'Known to be associated with a notorious street gang involved in various criminal activities.'),
(880, 'Previously arrested for arson and vandalism.'),
(810, 'Suspected of involvement in a homicide case currently under investigation.'),
(811, 'Previously convicted of identity theft and financial fraud offenses.');

--Inserting Into Involved
INSERT INTO Involved(SuspectID, CaseID)
VALUES
(815, 401),
(820, 402), 
(830, 403), 
(840, 404), 
(850, 405), 
(860, 406), 
(870, 407), 
(880, 408), 
(810, 409), 
(811, 410); 

--Inserting Into Witness Contact Info
INSERT INTO Witness_Contact(WitnessID, PhoneNumber, Email)
VALUES
(616, '555-123-4567', 'witness616@example.com'),
(620, '555-234-5678', 'witness620@example.com'),
(630, '555-345-6789', 'witness630@example.com'),
(640, '555-456-7890', 'witness640@example.com'),
(650, '555-567-8901', 'witness650@example.com'),
(660, '555-678-9012', 'witness660@example.com'),
(670, '555-789-0123', 'witness670@example.com'),
(680, '555-890-1234', 'witness680@example.com'),
(690, '555-901-2345', 'witness690@example.com'),
(610, '555-012-3456', 'witness610@example.com'),
(611, '555-111-2222', 'witness611@example.com');

--Inserting Into Witnessed
INSERT INTO Witnessed(CaseID, WitnessID)
VALUES
(401, 616), 
(402, 620),
(403, 630), 
(404, 640), 
(405, 650), 
(406, 660), 
(407, 670), 
(408, 680), 
(409, 690), 
(410, 610), 
(401, 611); 

--Inserting Into Victim Phone Number
INSERT INTO Victim_Phone_Number(Victim_ID, PhoneNumber)
VALUES
(181, '555-111-1111'),
(182, '555-222-2222'),
(183, '555-333-3333'),
(184, '555-444-4444'),
(185, '555-555-5555'),
(186, '555-666-6666'),
(187, '555-777-7777'),
(188, '555-888-8888'),
(189, '555-999-9999'),
(190, '555-101-0101'),
(191, '555-121-2121');

--Inserting into Affects
INSERT INTO Affects(CaseID, VictimID)
VALUES
(401, 181), 
(402, 182), 
(403, 183), 
(404, 184), 
(405, 185), 
(406, 186), 
(407, 187), 
(408, 188), 
(409, 189), 
(410, 190), 
(401, 191); 

--Inserting Into Injuries
INSERT INTO Injuries(Victim_ID, Injury)
VALUES
(181, 'trauma'),
(182, 'Broken leg'),
(183, 'Bruises'),
(184, 'Wound '),
(185, 'Concussion'),
(186, 'Fractured ribs'),
(187, 'Severe burns'),
(188, 'wounds'),
(189, 'Sprained ankle'),
(190, 'Whiplash injuries'),
(191, 'Broken nose');

--Inserting Into Investigate
INSERT INTO Investigates(OfficerID, CaseID, LeadInvestigatiorID)
VALUES
(1000, 401, 1010),
(1001, 402, 1009),
(1002, 403, 1008), 
(1003, 404, 1007), 
(1004, 405, 1006), 
(1005, 406, 1005), 
(1006, 407, 1004), 
(1007, 408, 1003),
(1008, 409, 1002), 
(1009, 410, 1001), 
(1010, 401, 1000); 

--Inserting Into Arrest
INSERT INTO Arrest(OfficerID, CaseID, ArrestDate)
VALUES
(1000, 401, '2024-04-10'), 
(1001, 402, '2024-03-25'), 
(1002, 403, '2024-03-20'), 
(1003, 404, '2024-04-05'), 
(1004, 405, '2024-03-30'), 
(1005, 406, '2024-04-15'), 
(1006, 407, '2024-04-03'), 
(1007, 408, '2024-03-28'), 
(1008, 409, '2024-04-12'),
(1009, 410, '2024-04-20'), 
(1010, 401, '2024-04-10'); 

--Inserting Into O.Contact Info
INSERT INTO OfficerContactInfo(OfficerID, Email, PhoneNumber)
VALUES
(1000, 'officer1000@example.com', '555-100-1000'),
(1001, 'officer1001@example.com', '555-100-1001'),
(1002, 'officer1002@example.com', '555-100-1002'),
(1003, 'officer1003@example.com', '555-100-1003'),
(1004, 'officer1004@example.com', '555-100-1004'),
(1005, 'officer1005@example.com', '555-100-1005'),
(1006, 'officer1006@example.com', '555-100-1006'),
(1007, 'officer1007@example.com', '555-100-1007'),
(1008, 'officer1008@example.com', '555-100-1008'),
(1009, 'officer1009@example.com', '555-100-1009'),
(1010, 'officer1010@example.com', '555-100-1010');

--Inserting into interrogate
INSERT INTO Interrogates(OfficerID, SuspectID)
VALUES
(1000, 815),
(1001, 820),
(1002, 830),
(1003, 840),
(1004, 850),
(1005, 860),
(1006, 870),
(1007, 880),
(1008, 810),
(1009, 811);


























