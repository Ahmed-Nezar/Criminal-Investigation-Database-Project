select Criminal.CriminalID,FirstName+ ' '+LastName as Name,CrimeRecord from Criminal join CrimeRecord on
Criminal.CriminalID = CrimeRecord.CriminalID;