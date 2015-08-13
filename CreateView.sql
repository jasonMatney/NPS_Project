USE RTCA_new
GO

CREATE VIEW view_2 AS SELECT
	   N.[OBJECTID]
      ,[RTCA_ProjectNumber]
      ,[Project_Name]
      ,[Fiscal_Year_Start]
      ,[Fiscal_Year_Stop]
      ,[Location_Description]
      ,[Project_Status]
      ,N.[MemberID]
	  ,P.[CopName] AS LocalCopName
      ,P.[CopContactPerson] AS LocalCopContactPerson
      ,P.[CopPhone1] AS LocalCopPhone1
      ,P.[CopPhone2] AS LocalCopPhone2
      ,P.[CopPhone3] AS LocalCopPhone3
      ,P.[CopPhoneExt] AS LocalCopPhoneExt
      ,P.[CopAddress] AS LocalCopAddress
      ,P.[CopAddress2] AS LocalCopAddress2
      ,P.[CopCity] AS LocalCopCity
      ,P.[CopEmail] AS LocalCopEmail
      ,P.[Zip] AS LocalCopZip
      ,P.[StateID] AS LocalCopStateID
      ,P.[WebsiteList] AS LocalCopWebsiteList
	  ,NP.[CopName]	AS NationalCopName
      ,NP.[CopContactPerson] AS NationalCopContactPerson
      ,NP.[CopPhone1] AS NationalCopPhone1
      ,NP.[CopPhone2] AS NationalCopPhone2
      ,NP.[CopPhone3] AS NationalCopPhone3
      ,NP.[CopPhoneExt]	AS NationalCopPhoneExt
      ,NP.[CopAddress] AS NationalCopAddress
      ,NP.[CopAddress2]	AS NationalCopAddress2
      ,NP.[CopCity]	AS NationalCopCity
      ,NP.[CopEmail] AS NationalCopEmail
      ,NP.[Zip]	AS NationalCopZip
      ,NP.[StateID]	AS NationalCopStateID
      ,NP.[WebsiteList]	AS NationalCopWebsiteList
      ,M.[Password] AS RTCAFieldStaff_Password
      ,M.[StateID]	AS RTCAFieldStaff_StateID
      ,M.[Email]	AS RTCAFieldStaff_Email
      ,M.[MailingAddress]	AS RTCAFieldStaff_MailingAddress
      ,M.[MailingAddress2]	AS RTCAFieldStaff_MailingAddress2
      ,M.[City]	AS RTCAFieldStaff_City
      ,M.[Zip] AS RTCAFieldStaff_Zip
      ,M.[Phone1] AS RTCAFieldStaff_Phone1
      ,M.[Phone2] AS RTCAFieldStaff_Phone2
      ,M.[Phone3] AS RTCAFieldStaff_Phone3
      ,M.[PhoneExt]	AS RTCAFieldStaff_PhoneExt
      ,M.[Fax1]	AS RTCAFieldStaff_Fax1
      ,M.[Fax2]	AS RTCAFieldStaff_Fax2
      ,M.[Fax3] AS RTCAFieldStaff_Fax3
      ,M.[Cell1] AS RTCAFieldStaff_Cell1
      ,M.[Cell2] AS RTCAFieldStaff_Cell2
      ,M.[Cell3] AS RTCAFieldStaff_Cell3
FROM rtca.US_National_Park_Service AS N
LEFT JOIN	  
rtca.tbl_PrjCooperator AS P
ON N.CopID = P.CopID
LEFT JOIN 
rtca.tbl_PrjNationalCooperator AS NP
ON N.CopID = NP.CopID
LEFT JOIN
rtca.tbl_Member AS M
ON N.MemberID = M.MemberID
