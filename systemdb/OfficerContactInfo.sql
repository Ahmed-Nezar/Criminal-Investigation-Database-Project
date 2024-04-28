select Officer.OfficerID, FirstName+' '+LastName, Email,PhoneNumber from Officer 
Join OfficerContactInfo on Officer.OfficerID = OfficerContactInfo.OfficerID;