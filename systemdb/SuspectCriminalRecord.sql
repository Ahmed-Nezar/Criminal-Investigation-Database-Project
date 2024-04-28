select Suspect.SuspectID,FirstName+ ' '+LastName as Name,Criminal_Record,CaseID from Suspect join CriminalRecord on
Suspect.SuspectID=CriminalRecord.SuspectID
join Involved on Suspect.SuspectID=Involved.SuspectID;