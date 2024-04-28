select Officer.OfficerID, Arrest.CriminalID, Officer.FirstName+' '+Officer.LastName as OfficerName,  
Criminal.FirstName+' '+Criminal.LastName as CriminalName, Arrest.ArrestDate From Officer join Arrest on Officer.OfficerID=Arrest.OfficerID 
join Criminal on Criminal.CriminalID = Arrest.CriminalID;