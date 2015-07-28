BULK INSERT RTCA_new.rtca.APPLICANT_PARTNER
FROM 'C:\Users\jamatney\Documents\RTCA_Tables\RTCA_APPLICANT_PARTNER.csv'
WITH
(
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',  --CSV field delimiter
    ROWTERMINATOR = '\n',   --Use to shift the control to next row
    TABLOCK
)
