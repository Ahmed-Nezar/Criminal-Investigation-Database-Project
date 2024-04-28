Select Victim.VictimID,FirstName+' '+LastName as Name,Injuries.Injury from Victim join Injuries
on Victim.VictimID=Injuries.Victim_ID;