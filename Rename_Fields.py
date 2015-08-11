import arcpy
# Set workspace environment to geodatabase
arcpy.env.workspace = r"C:\Users\jamatney\AppData\Roaming\Esri\Desktop10.2\ArcCatalog\rtca user connected to rtca_new database.sde"

# Loop through feature classes looking for a field named 'elev'
fcList = arcpy.ListFeatureClasses() # get a list of feature classes
for fc in fcList:  # loop through feature classes
    if fc == "RTCA_new.RTCA.CORS":
        print fc
        fieldList = arcpy.ListFields(fc)  # get a list of fields for each feature class
        for field in fieldList: # loop through each field
            if field.name == 'RTCA_PrjNu':
                arcpy.AlterField_management(fc, field.name, "RTCA_Project_Number", "RTCA Project Number")
            elif field.name == 'RTCA_Proje':
                arcpy.AlterField_management(fc, field.name, "RTCA_Project_Number1", "RTCA Project Number 1")
            elif field.name == 'PO_NAME':
                arcpy.AlterField_management(fc, field.name, "Post_Office_Name", "Post Office Name")
            elif field.name == 'ZIPCODE_TY':
                arcpy.AlterField_management(fc, field.name, "Zipcode_Type", "Zipcode Type")
            elif field.name == 'Project_Na':
                arcpy.AlterField_management(fc, field.name, "Project_Name", "Project Name")
            elif field.name == 'Project_St':
                arcpy.AlterField_management(fc, field.name, "Project_Status", "Project Status")
            elif field.name == 'Fiscal_Yea':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year_Start", "Fiscal Year Start")
            elif field.name == 'Fiscal_Y_1':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year_Stop", "Fiscal Year Stop")
            elif field.name == 'Project_Lo':
                arcpy.AlterField_management(fc, field.name, "Project_Location", "Project Location")
            elif field.name == 'NPSContact':
                arcpy.AlterField_management(fc, field.name, "NPSContactPointInfo", "NPS Contact Point Info")
            elif field.name == 'Anticipate':
                arcpy.AlterField_management(fc, field.name, "AnticipateOutcome", "Anticipate Outcome")
            elif field.name == 'PublicInvo':
                arcpy.AlterField_management(fc, field.name, "PublicInvolvement", "Public Involvement")
            elif field.name == 'EstProjPay':
                arcpy.AlterField_management(fc, field.name, "EstProjPayPeriod", "Est Proj Pay Period")
            elif field.name == 'IntendClos':
                arcpy.AlterField_management(fc, field.name, "IntendCloseOut", "Intend Close Out")
            elif field.name == 'ApprovStat':
                arcpy.AlterField_management(fc, field.name, "ApprovStatus", "Approval Status")
            elif field.name == 'ReadyForRe':
                arcpy.AlterField_management(fc, field.name, "ReadyForReview", "Ready For Review")
            elif field.name == 'Project_De':
                arcpy.AlterField_management(fc, field.name, "Project_Description", "Project Description")
            elif field.name == 'NPS_Projec':
                arcpy.AlterField_management(fc, field.name, "NPS_Project_Type", "NPS Project Type")
            elif field.name == 'Annual_Sta':
                arcpy.AlterField_management(fc, field.name, "Annual_Status", "Annual Status")
            elif field.name == 'NPS_Unit_N':
                arcpy.AlterField_management(fc, field.name, "NPS_Unit_Name", "NPS Unit Name")
            elif field.name == 'NPS_Unit_C':
                arcpy.AlterField_management(fc, field.name, "NPS_Unit_Code", "NPS Unit Code")
            elif field.name == 'NPS_Office':
                arcpy.AlterField_management(fc, field.name, "NPS_Office_Name", "NPS Office Name")
            elif field.name == 'Project_Ap':
                arcpy.AlterField_management(fc, field.name, "Project_Approver", "Project Approver")
            elif field.name == 'Milestone_':
                arcpy.AlterField_management(fc, field.name, "Milestone_Category", "Milestone Category")
            elif field.name == 'Milestone1':
                arcpy.AlterField_management(fc, field.name, "Milestone_Definition", "Milestone Definition")
            elif field.name == 'Service_Ca':
                arcpy.AlterField_management(fc, field.name, "Strategic_Category", "Strategic Category")
            elif field.name == 'Service_De':
                arcpy.AlterField_management(fc, field.name, "Strategic_Description", "Strategic Description")
            elif field.name == 'Financial_':
                arcpy.AlterField_management(fc, field.name, "Financial_Unit_Name", "Financial Unit Name")
            elif field.name == 'National_I':
                arcpy.AlterField_management(fc, field.name, "National_Initiative", "National Initiative")
            elif field.name == 'Public_Pri':
                arcpy.AlterField_management(fc, field.name, "Public_Private_Record", "Public Private Record")
            elif field.name == 'Project_Su':
                arcpy.AlterField_management(fc, field.name, "Project_Success_Report", "Project Success Report")
            elif field.name == 'Leveraging':
                arcpy.AlterField_management(fc, field.name, "Leveraging_Outcome", "Leveraging Outcome")
            elif field.name == 'Leveragi_1':
                arcpy.AlterField_management(fc, field.name, "Leveraging_Participants", "Leveraging Participants")
            elif field.name == 'Leveragi_2':
                arcpy.AlterField_management(fc, field.name, "Leveraging_Completion_Date", "Leveraging Completion Date")
            elif field.name == 'Leveragi_3':
                arcpy.AlterField_management(fc, field.name, "Leveraging_Partner", "Leveraging Partner")
            elif field.name == 'Leveragi_4':
                arcpy.AlterField_management(fc, field.name, "Leveraging_Partner_Match", "Leveraging Partner Match")
            elif field.name == 'Leveragi_5':
                arcpy.AlterField_management(fc, field.name, "Leveraging_Challenge_Cost_Share", "Leveraging Challenge Cost Share")
            elif field.name == 'Leveragi_6':
                arcpy.AlterField_management(fc, field.name, "Leveraging_National_Initiative", "Leveraging National Initiative")
            elif field.name == 'NationalCo':
                arcpy.AlterField_management(fc, field.name, "NationalCopName", "National Cooperator Name")
            elif field.name == 'National_1':
                arcpy.AlterField_management(fc, field.name, "NationalCopContactPerson", "National Cooperator Contact Person")
            elif field.name == 'National_2':
                arcpy.AlterField_management(fc, field.name, "NationalCopPhone", "National Cooperator Phone")
            elif field.name == 'National_3':
                arcpy.AlterField_management(fc, field.name, "NationalCopEmail", "National Cooperator Email")
            elif field.name == 'National_4':
                arcpy.AlterField_management(fc, field.name, "NationalCopAddress", "National Cooperator Address")
            elif field.name == 'National_5':
                arcpy.AlterField_management(fc, field.name, "NationalCopWebsiteList", "National Cooperator Website List")
            elif field.name == 'LocalCopNa':
                arcpy.AlterField_management(fc, field.name, "LocalCopName", "Local Cooperator Name")
            elif field.name == 'LocalCopCo':
                arcpy.AlterField_management(fc, field.name, "LocalCopContactPerson", "Local Cooperator Contact Person")
            elif field.name == 'LocalCopPh':
                arcpy.AlterField_management(fc, field.name, "LocalCopPhone", "Local Cooperator Phone")
            elif field.name == 'LocalCopEm':
                arcpy.AlterField_management(fc, field.name, "LocalCopEmail", "Local Cooperator Email")
            elif field.name == 'LocalCopAd':
                arcpy.AlterField_management(fc, field.name, "LocalCopAddress", "Local Cooperator Address")
            elif field.name == 'LocalCopCi':
                arcpy.AlterField_management(fc, field.name, "LocalCopCity", "Local Cooperator City")
            elif field.name == 'LocalCopSt':
                arcpy.AlterField_management(fc, field.name, "LocalCopStateName", "Local Cooperator State Name")
            elif field.name == 'LocalCopZi':
                arcpy.AlterField_management(fc, field.name, "LocalCopZip", "Local Cooperator Zip")
            elif field.name == 'LocalCopWe':
                arcpy.AlterField_management(fc, field.name, "LocalCopWebsiteList", "Local Cooperator Website List")
            elif field.name == 'RTCAFieldS':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_Name", "RTCA Field Staff Name")
            elif field.name == 'RTCAFiel_1':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_Email", "RTCA Field Staff Email")
            elif field.name == 'RTCAFiel_2':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_MailingAddress", "RTCA Field Staff mailing Address")
            elif field.name == 'RTCAFiel_3':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_City", "RTCA Field Staff City")
            elif field.name == 'RTCAFiel_4':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_State", "RTCA Field Staff State")
            elif field.name == 'RTCAFiel_5':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_Zip", "RTCA Field Staff Zip")
            elif field.name == 'RTCAFiel_6':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_Phone", "RTCA Field Staff Phone")
            elif field.name == 'RTCAFiel_7':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_Fax", "RTCA Field Staff Fax")
            elif field.name == 'RTCAFiel_8':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_Cell", "RTCA Field Staff Cell")
            elif field.name == 'Project_Co':
                arcpy.AlterField_management(fc, field.name, "Project_Co_Lead", "Project Co Lead")
            elif field.name == 'Project_We':
                arcpy.AlterField_management(fc, field.name, "Project_Website", "Project Website")
            elif field.name == 'Attachment':
                arcpy.AlterField_management(fc, field.name, "Attachment_Name", "Attachment Name")
            elif field.name == 'Attachme_1':
                arcpy.AlterField_management(fc, field.name, "Attachment_Description", "Attachment Description")
            else:
                pass
            print "Name: ", field.name
            print "Alias: ", field.aliasName
