BULK INSERT RTCA_new.rtca.US_National_Park_Service
FROM 'C:\Users\jamatney\RTCA_Tables\view_Applicant_Detail.csv'
WITH
(
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',  --CSV field delimiter
    ROWTERMINATOR = '\n',   --Use to shift the control to next row
    TABLOCK
)
