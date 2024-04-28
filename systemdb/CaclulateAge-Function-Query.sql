CREATE FUNCTION CalculateAge (@dob DATE)
RETURNS INT
AS
BEGIN
    DECLARE @age INT;
    SET @age = DATEDIFF(YEAR, @dob, GETDATE());
    RETURN @age;
END;