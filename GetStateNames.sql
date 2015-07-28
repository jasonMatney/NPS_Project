USE RTCA

GO

WITH Data AS 
( SELECT    A.PrjNumber, 
        S.StateID,
        N.StateName
FROM dbo.tbl_PrjApplicant as A
    LEFT JOIN dbo.tbl_PrjStates as S
        ON A.PrjNumber = S.PrjNumber
    LEFT JOIN dbo.tbl_State as N
        ON S.StateID = N.StateID
)
SELECT PrjNumber, StateName
FROM Data
ORDER BY PrjNumber
