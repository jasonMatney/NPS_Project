CREATE TABLE TABLE1 (ID INT, VALUE INT)
GO
INSERT INTO TABLE1 VALUES (1 , 10), (2 , 20) , (3 , 30)
GO

CREATE FUNCTION dbo.udf_DefaultValue(@ID INT)
RETURNS INT
AS
BEGIN
    DECLARE @rtnValue INT;
    SELECT @rtnValue = VALUE *2 FROM TABLE1 WHERE ID = @ID
    RETURN @rtnValue;
END
GO

CREATE TABLE TABLE2 (ID INT
                  , VALUE INT
                  , ComputedColumn AS (VALUE * dbo.udf_DefaultValue(ID)) )
GO

INSERT INTO TABLE2 (ID , VALUE)
VALUES (1, 1)

SELECT * FROM TABLE2

/*****  Result Set  

ID  VALUE   ComputedColumn
1     1           20

*****/
