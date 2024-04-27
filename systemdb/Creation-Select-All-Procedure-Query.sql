CREATE PROCEDURE GetAllRecords(
    @TableName NVARCHAR(MAX),
    @Keys NVARCHAR(MAX)
)
AS
BEGIN
    DECLARE @SQLQuery NVARCHAR(MAX)
    SET @SQLQuery = 'SELECT ' + @Keys + ' FROM ' + @TableName
    EXEC sp_executesql @SQLQuery
END

EXEC GetAllRecords @TableName = Officer, @Keys = OfficerID;
