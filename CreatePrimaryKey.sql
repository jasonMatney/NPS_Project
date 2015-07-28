/* To prevent any potential data loss issues, you should review this script in detail before running it outside the context of the database designer.*/
BEGIN TRANSACTION
SET QUOTED_IDENTIFIER ON
SET ARITHABORT ON
SET NUMERIC_ROUNDABORT OFF
SET CONCAT_NULL_YIELDS_NULL ON
SET ANSI_NULLS ON
SET ANSI_PADDING ON
SET ANSI_WARNINGS ON
COMMIT
BEGIN TRANSACTION
GO
CREATE TABLE dbo.Tmp_RTCA_Project
    (
    Project_ID int NOT NULL,
    Project_Name varchar(MAX) NULL,
    Fiscal_Year_Start varchar(50) NULL,
    Fiscal_Year_Stop varchar(50) NULL,
    Project_Scoping varchar(MAX) NULL,
    Annual_Status varchar(50) NULL,
    Annual_Year datetime NULL,
    NPS_Role varchar(MAX) NULL,
    Dropped_Explanation varchar(MAX) NULL,
    Project_Lead varchar(MAX) NULL,
    Project_Co_Lead varchar(MAX) NULL,
    Public_Private_Record varchar(MAX) NULL,
    MemberID int NULL,
    CopID int NULL,
    Zip varchar(50) NULL
    )  ON [PRIMARY]
     TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE dbo.Tmp_RTCA_Project SET (LOCK_ESCALATION = TABLE)
GO
IF EXISTS(SELECT * FROM dbo.RTCA_Project)
     EXEC('INSERT INTO dbo.Tmp_RTCA_Project (Project_ID, Project_Name, Fiscal_Year_Start, Fiscal_Year_Stop, Project_Scoping, Annual_Status, Annual_Year, NPS_Role, Dropped_Explanation, Project_Lead, Project_Co_Lead, Public_Private_Record, MemberID, CopID, Zip)
        SELECT Project_ID, Project_Name, Fiscal_Year_Start, Fiscal_Year_Stop, Project_Scoping, Annual_Status, Annual_Year, NPS_Role, Dropped_Explanation, Project_Lead, Project_Co_Lead, Public_Private_Record, MemberID, CopID, Zip FROM dbo.RTCA_Project WITH (HOLDLOCK TABLOCKX)')
GO
DROP TABLE dbo.RTCA_Project
GO
EXECUTE sp_rename N'dbo.Tmp_RTCA_Project', N'RTCA_Project', 'OBJECT' 
GO
ALTER TABLE dbo.RTCA_Project ADD CONSTRAINT
    PK_RTCA_Project PRIMARY KEY CLUSTERED 
    (
    Project_ID
    ) WITH( STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

GO
COMMIT
