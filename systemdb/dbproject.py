from globalFunc import *
from Classes.Suspect import Suspect
from Classes.Criminal import Criminal
from Classes.CriminalRecord import CriminalRecord
from Classes.Victim import Victim
from Classes.Case import Case
from Classes.Affects import Affects
from Classes.Witness import Witness

#Criminal Investigation System


# CREATE PROCEDURE GetAllRecordsWithKeys
#     @TableName NVARCHAR(50),
#     @Keys NVARCHAR(MAX)
# AS
# BEGIN
#     DECLARE @SQLQuery NVARCHAR(MAX)
#     SET @SQLQuery = 'SELECT ' + @Keys + ' FROM ' + @TableName
#     EXEC sp_executesql @SQLQuery
# END

# CREATE FUNCTION CalculateAge (@dob DATE)
# RETURNS INT
# AS
# BEGIN
#     DECLARE @age INT;
#     SET @age = DATEDIFF(YEAR, @dob, GETDATE());
#     RETURN @age;
# END;


print(Witness.get_all())
