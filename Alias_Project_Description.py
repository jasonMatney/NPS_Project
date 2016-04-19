import arcpy
# Set workspace environment to geodatabase
arcpy.env.workspace = r"C:\Users\jamatney\AppData\Roaming\Esri\Desktop10.2\ArcCatalog\rtca user connected to rtca_new database.sde"

# Loop through feature classes looking for a field named 'elev'
fcList = arcpy.ListFeatureClasses() # get a list of feature classes
for fc in fcList:  # loop through feature classes
    print fc
    if fc == "RTCA_new.RTCA.CORS_DESCRIPTION_APRIL":
        print fc
        fieldList = arcpy.ListFields(fc)  # get a list of fields for each feature class
        for field in fieldList: # loop through each field
            if field.name == 'RTCA_Project_Number':
                arcpy.AlterField_management(fc, field.name, "RTCA_Project_Number", "RTCA Project Number")
            elif field.name == 'NPS_Program':
                arcpy.AlterField_management(fc, field.name, "NPS_Program", "NPS Program")
            elif field.name == 'Portfolio':
                arcpy.AlterField_management(fc, field.name, "Portfolio", "Portfolio")
            elif field.name == 'Project_Goal':
                arcpy.AlterField_management(fc, field.name, "Project_Goal", "Project Goal")
            elif field.name == 'Anticipated_Outcome':
                arcpy.AlterField_management(fc, field.name, "Anticipated_Outcome", "Anticipated Outcome")
            elif field.name == 'Project_Zipcode':
                arcpy.AlterField_management(fc, field.name, "Project_Zipcode", "Project Zipcodes")
            elif field.name == 'Project_City':
                arcpy.AlterField_management(fc, field.name, "Project_City", "Project City")
            elif field.name == 'Project_State':
                arcpy.AlterField_management(fc, field.name, "Project_State", "Project State")
            elif field.name == 'Project_Name':
                arcpy.AlterField_management(fc, field.name, "Project_Name", "Project Name")
            elif field.name == 'Fiscal_Year_Start':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year_Start", "Fiscal Year Start")
            elif field.name == 'Fiscal_Year_End':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year_End", "Fiscal Year End")
            elif field.name == 'Project_Status':
                arcpy.AlterField_management(fc, field.name, "Project_Status", "Project Status")
            elif field.name == 'Annual_Status':
                arcpy.AlterField_management(fc, field.name, "Annual_Status", "Annual Status")
            elif field.name == 'Project_Approver':
                arcpy.AlterField_management(fc, field.name, "Project_Approver", "Project Approver")
            elif field.name == 'NPS_Project_Manager':
                arcpy.AlterField_management(fc, field.name, "NPS_Project_Manager", "NPS Project Manager")
            elif field.name == 'NPS_Project_Manager_Email':
                arcpy.AlterField_management(fc, field.name, "NPS_Project_Manager_Email", "NPS Project Manager Email")
            elif field.name == 'RTCA_Lead_State':
                arcpy.AlterField_management(fc, field.name, "RTCA_Lead_State", "RTCA Lead State")
            elif field.name == 'NPS_Co_Lead':
                arcpy.AlterField_management(fc, field.name, "NPS_Co_Lead", "NPS Co Lead")
            elif field.name == 'NPS_Unit_Name':
                arcpy.AlterField_management(fc, field.name, "NPS_Unit_Name", "NPS Unit Name")
            elif field.name == 'NPS_Unit_Code':
                arcpy.AlterField_management(fc, field.name, "NPS_Unit_Code", "NPS Unit Code")
            elif field.name == 'NPS_Regional_Office':
                arcpy.AlterField_management(fc, field.name, "NPS_Regional_Office", "NPS Regional Office")
            elif field.name == 'NPS_Role_Category':
                arcpy.AlterField_management(fc, field.name, "NPS_Role_Category", "NPS Role Category")
            elif field.name == 'NPS_Role_Narrative':
                arcpy.AlterField_management(fc, field.name, "NPS_Role_Narrative", "NPS Role Narrative")
            elif field.name == 'Milestone_Measure':
                arcpy.AlterField_management(fc, field.name, "Milestone_Measure", "Milestone Measure")
            elif field.name == 'Milestone_Quantity':
                arcpy.AlterField_management(fc, field.name, "Milestone_Quantity", "Milestone Quantity")
            elif field.name == 'Strategic_Category':
                arcpy.AlterField_management(fc, field.name, "Strategic_Category", "Strategic Category")
            elif field.name == 'Strategic_Description':
                arcpy.AlterField_management(fc, field.name, "Strategic_Description", "Strategic Description")
            elif field.name == 'National_Initiative':
                arcpy.AlterField_management(fc, field.name, "National_Initiative", "National Initiative")
            elif field.name == 'Public_Private_Record':
                arcpy.AlterField_management(fc, field.name, "Public_Private_Record", "Public Private Record")
            elif field.name == 'Project_Success_Story':
                arcpy.AlterField_management(fc, field.name, "Project_Success_Story", "Project Success Story")
            elif field.name == 'Leveraging_Partner':
                arcpy.AlterField_management(fc, field.name, "Leveraging_Partner", "Leveraging Partner")
            elif field.name == 'Leveraging_PartnerDD':
                arcpy.AlterField_management(fc, field.name, "Leveraging_PartnerDD", "Leveraging Partner Direct Dollars")
            elif field.name == 'Leveraging_PartnerIKD':
                arcpy.AlterField_management(fc, field.name, "Leveraging_PartnerIKD", "Leveraging Partner In-Kind Dollars")
            elif field.name == 'Description_of_IKService':
                arcpy.AlterField_management(fc, field.name, "Description_of_IKService", "Description of In-Kind Service")
            elif field.name == 'NPS_Direct_Dollars':
                arcpy.AlterField_management(fc, field.name, "NPS_Direct_Dollars", "NPS Direct Dollars")
            elif field.name == 'NPS_Staff_Time_Dollars':
                arcpy.AlterField_management(fc, field.name, "NPS_Staff_Time_Dollars", "NPS Staff Time Dollars")
            elif field.name == 'PrimaryPartnerOrganization':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerOrganization", "Primary Partner Organization")
            elif field.name == 'PrimaryPartnerContactName':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerContactName", "Primary Partner Contact Name")
            elif field.name == 'PrimaryPartnerPhone':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerPhone", "Primary Partner Phone")
            elif field.name == 'PrimaryPartnerEmail':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerEmail", "Primary Partner Email")
            elif field.name == 'PrimaryPartnerAddress':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerAddress", "Primary Partner Address")
            elif field.name == 'PrimaryPartnerCity':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerCity", "Primary Partner City")
            elif field.name == 'PrimaryPartnerState':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerState", "Primary Partner State")
            elif field.name == 'PrimaryPartnerZip':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerZip", "Primary Partner Zip")
            elif field.name == 'PrimaryPartnerWebsite':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerWebsite", "Primary Partner Website")
            elif field.name == 'SecondaryPartnerOrganization':
                arcpy.AlterField_management(fc, field.name, "SecondaryPartnerOrganization", "Secondary Partner Organization")
            elif field.name == 'SecondaryPartnerContactName':
                arcpy.AlterField_management(fc, field.name, "SecondaryPartnerContactName", "Secondary Partner Contact Name")
            elif field.name == 'SecondaryPartnerEmail':
                arcpy.AlterField_management(fc, field.name, "SecondaryPartnerEmail", "Secondary Partner Email")
            elif field.name == 'NationalCopName':
                arcpy.AlterField_management(fc, field.name, "NationalCopName", "National Cooperator Name")
            elif field.name == 'NationalCopContactName':
                arcpy.AlterField_management(fc, field.name, "NationalCopContactName", "National Cooperator Contact Name")
            elif field.name == 'NationalCopEmail':
                arcpy.AlterField_management(fc, field.name, "NationalCopEmail", "National Cooperator Email")
            elif field.name == 'RTCA_Lead':
                arcpy.AlterField_management(fc, field.name, "RTCA_Lead", "RTCA Lead")
            elif field.name == 'RTCA_Co_Lead':
                arcpy.AlterField_management(fc, field.name, "RTCA_Co_Lead", "RTCA Co Lead")
            elif field.name == 'RTCA_Lead_State':
                arcpy.AlterField_management(fc, field.name, "RTCA_Lead_State", "RTCA Lead State")
            elif field.name == 'Attachment_Name':
                arcpy.AlterField_management(fc, field.name, "Attachment_Name", "Attachment Name")
            elif field.name == 'Attachment_Description':
                arcpy.AlterField_management(fc, field.name, "Attachment_Description", "Attachment Description")
            elif field.name == 'Project_Location_City_Town':
                arcpy.AlterField_management(fc, field.name, "Project_Location_City_Town", "Project Location - City/Town")
            elif field.name == 'Project_Location_State':
                arcpy.AlterField_management(fc, field.name, "Project_Location_State", "Project Location - State")
            elif field.name == 'Project_Location_Zipcodes':
                arcpy.AlterField_management(fc, field.name, "Project_Location_Zipcodes", "Project Location - Zipcodes")
            elif field.name == 'Project_Location_Description':
                arcpy.AlterField_management(fc, field.name, "Project_Location_Description", "Project Location Description")
            elif field.name == 'Project_Website':
                arcpy.AlterField_management(fc, field.name, "Project_Website", "Project Website")
            elif field.name == 'Project_Success_Story_Attach':
                arcpy.AlterField_management(fc, field.name, "Project_Success_Story_Attach", "Project Success Story Attachments")
            elif field.name == 'Project_Agreement_Attachments':
                arcpy.AlterField_management(fc, field.name, "Project_Agreement_Attachments", "Project Agreement Attachments")
            elif field.name == 'Photo_Attachments':
                arcpy.AlterField_management(fc, field.name, "Photo_Attachments", "Photo Attachments")
            elif field.name == 'Other_Attachments':
                arcpy.AlterField_management(fc, field.name, "Other_Attachments", "Other Attachments")
            else:
                pass
            print "Name: ", field.name
            print "Alias: ", field.aliasName
    else:
        print "No such Geodatabase Object"
