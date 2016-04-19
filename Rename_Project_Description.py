'''
When ArcMap exports data from Feature Classes to a shapefile,
the field names are conveniently cut off at 13 characters. 

Good riddance. Who needed full field names anyways?

When making a new Feautre Class using one of these exported shapefiles as a template,
the new FC will naturally also contain the truncated field names.

To address this issue, this script finds a desired Feature Class and then
updates each truncated filed name to its full specification. 
Aliases however, are not updated.
To update aliases, frist run this script, then run Alias_Project_Description.py
'''

import arcpy
# Set workspace environment to geodatabase
arcpy.env.workspace = r"C:\Users\jamatney\AppData\Roaming\Esri\Desktop10.2\ArcCatalog\rtca user connected to rtca_new database.sde"

# Loop through feature classes looking for a field named 'elev'
fcList = arcpy.ListFeatureClasses() # get a list of feature classes
for fc in fcList:  # loop through feature classes
    print fc
    if fc == "RTCA_new.RTCA.CORS_DESCRIPTION":
        print fc
        fieldList = arcpy.ListFields(fc)  # get a list of fields for each feature class
        for field in fieldList: # loop through each field
            if field.name == 'RTCA_Pro_1':
                arcpy.AlterField_management(fc, field.name, "RTCA_Project_Number", "RTCA Project Number")
            elif field.name == 'RTCA_Proje':
                arcpy.AlterField_management(fc, field.name, "RTCA_Project_Number", "RTCA_Project_Number")
            elif field.name == 'NPS_Progra':
                arcpy.AlterField_management(fc, field.name, "NPS_Program", "NPS Program")
            elif field.name == 'Project_Go':
                arcpy.AlterField_management(fc, field.name, "Project_Goal", "Project Goal")
            elif field.name == 'Portfoli':
                arcpy.AlterField_management(fc, field.name, "Portfolio", "Portfolio")
            elif field.name == 'Anticipate':
                arcpy.AlterField_management(fc, field.name, "Anticipated_Outcome", "Anticipated Outcome")
            elif field.name == 'Anticipa_1':
                arcpy.AlterField_management(fc, field.name, "Anticipated_Outcome", "Anticipated Outcome")
            elif field.name == 'ZIPCODE':
                arcpy.AlterField_management(fc, field.name, "Project_Zipcode", "Project Zipcodes")
            elif field.name == 'ZIPCODE':
                arcpy.AlterField_management(fc, field.name, "Project_Zipcode", "Project Zipcodes")
            elif field.name == 'Project_Zi':
                arcpy.AlterField_management(fc, field.name, "Project_Zipcode", "Project Zipcodes")
            elif field.name == 'PO_NAME':
                arcpy.AlterField_management(fc, field.name, "Project_City", "Project City")
            elif field.name == 'Project_Ci':
                arcpy.AlterField_management(fc, field.name, "Project_City", "Project City")
            elif field.name == 'State':
                arcpy.AlterField_management(fc, field.name, "Project_State", "Project State")
            elif field.name == 'Project_Na':
                arcpy.AlterField_management(fc, field.name, "Project_Name", "Project Name")
            elif field.name == 'FiscalYear':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year_Start", "Fiscal Year Start")
            elif field.name == 'Fiscal_Yea':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year_Start", "Fiscal Year Start")
            elif field.name == 'FiscalYe_1':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year_End", "Fiscal Year End")
            elif field.name == 'Fiscal_Y_1':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year_End", "Fiscal Year End")
            elif field.name == 'Project_St':
                arcpy.AlterField_management(fc, field.name, "Project_Status", "Project Status")
            elif field.name == 'Annual_Sta':
                arcpy.AlterField_management(fc, field.name, "Annual_Status", "Annual Status")
            elif field.name == 'Project_Ap':
                arcpy.AlterField_management(fc, field.name, "Project_Approver", "Project Approver")
            elif field.name == 'NPS_Projec':
                arcpy.AlterField_management(fc, field.name, "NPS_Project_Manager", "NPS Project Manager")
            elif field.name == 'NPS_Proj_1':
                arcpy.AlterField_management(fc, field.name, "NPS_Project_Manager_Email", "NPS Project Manager Email")
            elif field.name == 'RTCA_Lead_':
                arcpy.AlterField_management(fc, field.name, "RTCA_Lead_State", "RTCA Lead State")
            elif field.name == 'NPS_Co_Lea':
                arcpy.AlterField_management(fc, field.name, "NPS_Co_Lead", "NPS Co Lead")
            elif field.name == 'NPS_Unit_N':
                arcpy.AlterField_management(fc, field.name, "NPS_Unit_Name", "NPS Unit Name")
            elif field.name == 'NPS_Unit_C':
                arcpy.AlterField_management(fc, field.name, "NPS_Unit_Code", "NPS Unit Code")
            elif field.name == 'NPS_Region':
                arcpy.AlterField_management(fc, field.name, "NPS_Regional_Office", "NPS Regional Office")
            elif field.name == 'NPS_Role_C':
                arcpy.AlterField_management(fc, field.name, "NPS_Role_Category", "NPS Role Category")
            elif field.name == 'NPS_Role_N':
                arcpy.AlterField_management(fc, field.name, "NPS_Role_Narrative", "NPS Role Narrative")
            elif field.name == 'Milestone_':
                arcpy.AlterField_management(fc, field.name, "Milestone_Measure", "Milestone Measure")
            elif field.name == 'Milestone1':
                arcpy.AlterField_management(fc, field.name, "Milestone_Quantity", "Milestone Quantity")
            elif field.name == 'Strategic_':
                arcpy.AlterField_management(fc, field.name, "Strategic_Category", "Strategic Category")
            elif field.name == 'Strategic1':
                arcpy.AlterField_management(fc, field.name, "Strategic_Description", "Strategic Description")
            elif field.name == 'National_I':
                arcpy.AlterField_management(fc, field.name, "National_Initiative", "National Initiative")
            elif field.name == 'Public_Pri':
                arcpy.AlterField_management(fc, field.name, "Public_Private_Record", "Public Private Record")
            elif field.name == 'Project_Su':
                arcpy.AlterField_management(fc, field.name, "Project_Success_Story", "Project Success Story")
            elif field.name == 'Leveraging':
                arcpy.AlterField_management(fc, field.name, "Leveraging_Partner", "Leveraging Partner")
            elif field.name == 'Leveragi_1':
                arcpy.AlterField_management(fc, field.name, "Leveraging_PartnerDD", "Leveraging Partner Direct Dollars")
            elif field.name == 'Leveragi_2':
                arcpy.AlterField_management(fc, field.name, "Leveraging_PartnerIKD", "Leveraging Partner In-Kind Dollars")
            elif field.name == 'Descriptio':
                arcpy.AlterField_management(fc, field.name, "Description_of_IKService", "Description of In-Kind Service")
            elif field.name == 'NPS_Direct':
                arcpy.AlterField_management(fc, field.name, "NPS_Direct_Dollars", "NPS Direct Dollars")
            elif field.name == 'NPS_Staff_':
                arcpy.AlterField_management(fc, field.name, "NPS_Staff_Time_Dollars", "NPS Staff Time Dollars")
            elif field.name == 'PrimaryPar':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerOrganization", "Primary Partner Organization")
            elif field.name == 'PrimaryP_1':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerContactName", "Primary Partner Contact Name")
            elif field.name == 'PrimaryP_2':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerPhone", "Primary Partner Phone")
            elif field.name == 'PrimaryP_3':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerEmail", "Primary Partner Email")
            elif field.name == 'PrimaryP_4':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerAddress", "Primary Partner Address")
            elif field.name == 'PrimaryP_5':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerCity", "Primary Partner City")
            elif field.name == 'PrimaryP_6':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerState", "Primary Partner State")
            elif field.name == 'PrimaryP_7':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerZip", "Primary Partner Zip")
            elif field.name == 'PrimaryP_8':
                arcpy.AlterField_management(fc, field.name, "PrimaryPartnerWebsite", "Primary Partner Website")
            elif field.name == 'SecondaryP':
                arcpy.AlterField_management(fc, field.name, "SecondaryPartnerOrganization", "Secondary Partner Organization")
            elif field.name == 'Secondar_1':
                arcpy.AlterField_management(fc, field.name, "SecondaryPartnerContactName", "Secondary Partner Contact Name")
            elif field.name == 'Secondar_2':
                arcpy.AlterField_management(fc, field.name, "SecondaryPartnerEmail", "Secondary Partner Email")
            elif field.name == 'NationalCo':
                arcpy.AlterField_management(fc, field.name, "NationalCopName", "National Cooperator Name")
            elif field.name == 'National_1':
                arcpy.AlterField_management(fc, field.name, "NationalCopContactName", "National Cooperator Contact Name")
            elif field.name == 'National_2':
                arcpy.AlterField_management(fc, field.name, "NationalCopEmail", "National Cooperator Email")
            elif field.name == 'RTCA_Lead':
                arcpy.AlterField_management(fc, field.name, "RTCA_Lead", "RTCA Lead")
            elif field.name == 'RTCA_Co_Le':
                arcpy.AlterField_management(fc, field.name, "RTCA_Co_Lead", "RTCA Co Lead")
            elif field.name == 'RTCA_Lead1':
                arcpy.AlterField_management(fc, field.name, "RTCA_Lead_State", "RTCA Lead State")
            elif field.name == 'Attachment':
                arcpy.AlterField_management(fc, field.name, "Attachment_Name", "Attachment Name")
            elif field.name == 'Attachme_1':
                arcpy.AlterField_management(fc, field.name, "Attachment_Description", "Attachment Description")
            elif field.name == 'Project_Lo':
                arcpy.AlterField_management(fc, field.name, "Project_Location_City_Town", "Project Location - City/Town")
            elif field.name == 'Project__1':
                arcpy.AlterField_management(fc, field.name, "Project_Location_State", "Project Location - State")
            elif field.name == 'Project__2':
                arcpy.AlterField_management(fc, field.name, "Project_Location_Zipcodes", "Project Location - Zipcodes")
            elif field.name == 'Project__3':
                arcpy.AlterField_management(fc, field.name, "Project_Location_Description", "Project Location Description")
            elif field.name == 'Project_We':
                arcpy.AlterField_management(fc, field.name, "Project_Website", "Project Website")
            elif field.name == 'ProjectSuc':
                arcpy.AlterField_management(fc, field.name, "Project_Success_Story_Attach", "Project Success Story Attachments")
            elif field.name == 'Project_Ag':
                arcpy.AlterField_management(fc, field.name, "Project_Agreement_Attachments", "Project Agreement Attachments")
            elif field.name == 'Photo_Atta':
                arcpy.AlterField_management(fc, field.name, "Photo_Attachments", "Photo Attachments")
            elif field.name == 'Other_Atta':
                arcpy.AlterField_management(fc, field.name, "Other_Attachments", "Other Attachments")
            elif field.name == 'SHAPE':
                arcpy.AlterField_management(fc, field.name, "SHAPE", "SHAPE")

            else:
                pass
            print "Name: ", field.name
            print "Alias: ", field.aliasName
    else:
        print "No such Geodatabase Object"
