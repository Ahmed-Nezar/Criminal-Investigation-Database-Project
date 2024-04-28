Select Witness.WitnessID,FirstName+' '+LastName as Name,Witness_Contact.PhoneNumber,Witness_Contact.Email from Witness join Witness_Contact
on Witness.WitnessID=Witness_Contact.WitnessID;