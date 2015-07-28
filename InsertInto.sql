INSERT INTO Map.dbo.RTCA_Project(Project_ID,
                                 Project_Name,
                                 Fiscal_Year_Start,
                                 Fiscal_Year_Stop,
                                 Project_Scoping,
                                 Annual_Status,
                                 MemberID,
                                 CopID,
                                 Project_Lead,
                                 ZIP)
SELECT PrjNumber, PrjName, PrjFiscalYear, PrjLFiscalYear,
       PrjScoping, PrjStatus, MemberID, CopID, NPSContactPointInfos,
       zip
FROM RTCA.dbo.tbl_PrjApplicant
