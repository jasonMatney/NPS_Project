USE RTCA_new
GO

CREATE VIEW view_Add_Members AS
SELECT [RTCA_ProjectNumber]
      ,[Project_Name]
      ,[Fiscal_Year_Start]
      ,[Fiscal_Year_Stop]
      ,[Project_Location]
      ,[Project_Status]
      ,[Member_ID]
      ,NPS.[CopID]
      ,[NPSContactPointInfo]
      ,[AnticipatedOutcome]
      ,[PublicInvolvement]
      ,[Goal]
      ,[Rationale]
      ,[EstProjPayPeriod]
      ,[WorkToDate]
      ,[IntendCloseOut]
      ,[NPCost]
      ,[ApprovStatus]
      ,[LogLast]
      ,[IsCurrent]
      ,[ReadyForReview]
      ,[NationalCopID]
      ,[NationalCopName]
      ,[NationalCopContactPerson]
      ,[NationalCopPhone]
      ,[NationalCopEmail]
      ,[NationalCopAddress]
      ,[NationalCopWebsiteList]
	  ,[CopName] AS LocalCopName
      ,[CopContactPerson] AS LocalCopContactPerson
      ,[CopPhone1] AS LocalCopPhone1
      ,[CopPhone2] AS LocalCopPhone2
      ,[CopPhone3] AS LocalCopPhone3
      ,[CopPhoneExt] AS LocalCopPhoneExt
      ,[CopAddress] AS LocalCopAddress
      ,[CopAddress2] AS LocalCopAddress2
      ,[CopCity] AS LocalCopCity
      ,[CopEmail] AS LocalCopEmail
      ,[Zip] AS LocalCopZip
      ,PC.[StateID] AS LocalCopStateID
      ,PC.[WebsiteList] AS LocalCopWebsiteList
	  FROM rtca.US_National_Park_Service AS NPS
	  LEFT JOIN 
	  rtca.tbl_PrjCooperator AS PC
	  ON NPS.CopID = PC.CopID
