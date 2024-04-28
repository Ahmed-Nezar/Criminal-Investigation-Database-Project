Select Victim.VictimID,FirstName+' '+LastName as Name,Victim_Phone_Number.PhoneNumber from Victim join Victim_Phone_Number
on Victim.VictimID=Victim_Phone_Number.Victim_ID;