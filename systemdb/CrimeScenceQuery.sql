select CrimeScene.CaseID, Time, Location, Evidence.Type, Description from CrimeScene 
Join Evidence on CrimeScene.CaseID = Evidence.CaseID;