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
            if field.name == 'RTCA_Project_Number':
                arcpy.AlterField_management(fc, field.name, "RTCA_Project_Number", "RTCA Project Number")
            elif field.name == 'RTCA_Project_Number1':
                arcpy.AlterField_management(fc, field.name, "RTCA_Project_Number1", "RTCA Project Number 1")
            elif field.name == 'Post_Office_Name':
                arcpy.AlterField_management(fc, field.name, "Post_Office_Name", "Post Office Name")
            elif field.name == 'STATE':
                arcpy.AlterField_management(fc, field.name, "State", "State")
            elif field.name == 'ZIPCODE':
                arcpy.AlterField_management(fc, field.name, "ZIPCODE", "Zipcode")
            elif field.name == 'NPS_Role':
                arcpy.AlterField_management(fc, field.name, "NPS_Role", "NPS Role")
            elif field.name == 'Zipcode_Type':
                arcpy.AlterField_management(fc, field.name, "Zipcode_Type", "Zipcode Type")
            elif field.name == 'Project_Name':
                arcpy.AlterField_management(fc, field.name, "Project_Name", "Project Name")
            elif field.name == 'Project_Status':
                arcpy.AlterField_management(fc, field.name, "Project_Status", "Project Status")
            elif field.name == 'Fiscal_Year_Start':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year_Start", "Fiscal Year Start")
            elif field.name == 'Fiscal_Year_Stop':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year_Stop", "Fiscal Year Stop")
            elif field.name == 'Project_Location':
                arcpy.AlterField_management(fc, field.name, "Project_Location", "Project Location")
            elif field.name == 'NPSContactPointInfo':
                arcpy.AlterField_management(fc, field.name, "NPSContactPointInfo", "NPS Contact Point Info")
            elif field.name == 'AnticipateOutcome':
                arcpy.AlterField_management(fc, field.name, "AnticipateOutcome", "Anticipate Outcome")
            elif field.name == 'PublicInvolvement':
                arcpy.AlterField_management(fc, field.name, "PublicInvolvement", "Public Involvement")
            elif field.name == 'EstProjPayPeriod':
                arcpy.AlterField_management(fc, field.name, "EstProjPayPeriod", "Est Proj Pay Period")
            elif field.name == 'IntendCloseOut':
                arcpy.AlterField_management(fc, field.name, "IntendCloseOut", "Intend Close Out")
            elif field.name == 'ApprovStatus':
                arcpy.AlterField_management(fc, field.name, "ApprovStatus", "Approval Status")
            elif field.name == 'ReadyForReview':
                arcpy.AlterField_management(fc, field.name, "ReadyForReview", "Ready For Review")
            elif field.name == 'Project_Description':
                arcpy.AlterField_management(fc, field.name, "Project_Description", "Project Description")
            elif field.name == 'NPS_Project_Type':
                arcpy.AlterField_management(fc, field.name, "NPS_Project_Type", "NPS Project Type")
            elif field.name == 'Annual_Status':
                arcpy.AlterField_management(fc, field.name, "Annual_Status", "Annual Status")
            elif field.name == 'NPS_Role':
                arcpy.AlterField_management(fc, field.name, "NPS_Role", "NPS Role")
            elif field.name == 'NPS_Unit_Name':
                arcpy.AlterField_management(fc, field.name, "NPS_Unit_Name", "NPS Unit Name")
            elif field.name == 'NPS_Unit_Code':
                arcpy.AlterField_management(fc, field.name, "NPS_Unit_Code", "NPS Unit Code")
            elif field.name == 'NPS_Office_Name':
                arcpy.AlterField_management(fc, field.name, "NPS_Office_Name", "NPS Office Name")
            elif field.name == 'Project_Approver':
                arcpy.AlterField_management(fc, field.name, "Project_Approver", "Project Approver")
            elif field.name == 'Milestone_Category':
                arcpy.AlterField_management(fc, field.name, "Milestone_Category", "Milestone Category")
            elif field.name == 'Milestone_Definition':
                arcpy.AlterField_management(fc, field.name, "Milestone_Definition", "Milestone Definition")
            elif field.name == 'Strategic_Category':
                arcpy.AlterField_management(fc, field.name, "Strategic_Category", "Strategic Category")
            elif field.name == 'Strategic_Description':
                arcpy.AlterField_management(fc, field.name, "Strategic_Description", "Strategic Description")
            elif field.name == 'Financial_Unit_Name':
                arcpy.AlterField_management(fc, field.name, "Financial_Unit_Name", "Financial Unit Name")
            elif field.name == 'National_Initiative':
                arcpy.AlterField_management(fc, field.name, "National_Initiative", "National Initiative")
            elif field.name == 'Public_Private_Record':
                arcpy.AlterField_management(fc, field.name, "Public_Private_Record", "Public Private Record")
            elif field.name == 'Project_Success_Report':
                arcpy.AlterField_management(fc, field.name, "Project_Success_Report", "Project Success Report")
            elif field.name == 'Leveraging_Outcome':
                arcpy.AlterField_management(fc, field.name, "Leveraging_Outcome", "Leveraging Outcome")
            elif field.name == 'Leveraging_Participants':
                arcpy.AlterField_management(fc, field.name, "Leveraging_Participants", "Leveraging Participants")
            elif field.name == 'Leveraging_Completion_Date':
                arcpy.AlterField_management(fc, field.name, "Leveraging_Completion_Date", "Leveraging Completion Date")
            elif field.name == 'Leveraging_Partner':
                arcpy.AlterField_management(fc, field.name, "Leveraging_Partner", "Leveraging Partner")
            elif field.name == 'Leveraging_Partner_Match':
                arcpy.AlterField_management(fc, field.name, "Leveraging_Partner_Match", "Leveraging Partner Match")
            elif field.name == 'Leveraging_Challenge_Cost_Share':
                arcpy.AlterField_management(fc, field.name, "Leveraging_Challenge_Cost_Share", "Leveraging Challenge Cost Share")
            elif field.name == 'Leveraging_National_Initiative':
                arcpy.AlterField_management(fc, field.name, "Leveraging_National_Initiative", "Leveraging National Initiative")
            elif field.name == 'NationalCopName':
                arcpy.AlterField_management(fc, field.name, "NationalCopName", "National Cooperator Name")
            elif field.name == 'NationalCopContactPerson':
                arcpy.AlterField_management(fc, field.name, "NationalCopContactPerson", "National Cooperator Contact Person")
            elif field.name == 'NationalCopPhone':
                arcpy.AlterField_management(fc, field.name, "NationalCopPhone", "National Cooperator Phone")
            elif field.name == 'NationalCopEmail':
                arcpy.AlterField_management(fc, field.name, "NationalCopEmail", "National Cooperator Email")
            elif field.name == 'NationalCopAddress':
                arcpy.AlterField_management(fc, field.name, "NationalCopAddress", "National Cooperator Address")
            elif field.name == 'NationalCopWebsiteList':
                arcpy.AlterField_management(fc, field.name, "NationalCopWebsiteList", "National Cooperator Website List")
            elif field.name == 'LocalCopName':
                arcpy.AlterField_management(fc, field.name, "LocalCopName", "Local Cooperator Name")
            elif field.name == 'LocalCopContactPerson':
                arcpy.AlterField_management(fc, field.name, "LocalCopContactPerson", "Local Cooperator Contact Person")
            elif field.name == 'LocalCopPhone':
                arcpy.AlterField_management(fc, field.name, "LocalCopPhone", "Local Cooperator Phone")
            elif field.name == 'LocalCopEmail':
                arcpy.AlterField_management(fc, field.name, "LocalCopEmail", "Local Cooperator Email")
            elif field.name == 'LocalCopAddress':
                arcpy.AlterField_management(fc, field.name, "LocalCopAddress", "Local Cooperator Address")
            elif field.name == 'LocalCopCity':
                arcpy.AlterField_management(fc, field.name, "LocalCopCity", "Local Cooperator City")
            elif field.name == 'LocalCopStateName':
                arcpy.AlterField_management(fc, field.name, "LocalCopStateName", "Local Cooperator State Name")
            elif field.name == 'LocalCopZip':
                arcpy.AlterField_management(fc, field.name, "LocalCopZip", "Local Cooperator Zip")
            elif field.name == 'LocalCopWebsiteList':
                arcpy.AlterField_management(fc, field.name, "LocalCopWebsiteList", "Local Cooperator Website List")
            elif field.name == 'RTCAFieldStaff_Name':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_Name", "RTCA Field Staff Name")
            elif field.name == 'RTCAFieldStaff_Email':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_Email", "RTCA Field Staff Email")
            elif field.name == 'RTCAFieldStaff_MailingAddress':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_MailingAddress", "RTCA Field Staff mailing Address")
            elif field.name == 'RTCAFieldStaff_City':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_City", "RTCA Field Staff City")
            elif field.name == 'RTCAFieldStaff_State':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_State", "RTCA Field Staff State")
            elif field.name == 'RTCAFieldStaff_Zip':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_Zip", "RTCA Field Staff Zip")
            elif field.name == 'RTCAFieldStaff_Phone':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_Phone", "RTCA Field Staff Phone")
            elif field.name == 'RTCAFieldStaff_Fax':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_Fax", "RTCA Field Staff Fax")
            elif field.name == 'RTCAFieldStaff_Cell':
                arcpy.AlterField_management(fc, field.name, "RTCAFieldStaff_Cell", "RTCA Field Staff Cell")
            elif field.name == 'Project_Co_Lead':
                arcpy.AlterField_management(fc, field.name, "Project_Co_Lead", "Project Co Lead")
            elif field.name == 'Project_Website':
                arcpy.AlterField_management(fc, field.name, "Project_Website", "Project Website")
            elif field.name == 'Attachment_Name':
                arcpy.AlterField_management(fc, field.name, "Attachment_Name", "Attachment Name")
            elif field.name == 'Attachment_Description':
                arcpy.AlterField_management(fc, field.name, "Attachment_Description", "Attachment Description")
            else:
                pass
            print "Name: ", field.name
            print "Alias: ", field.aliasName

#
#
#
# # Print the name of the current fc:
# for fc in fcList:
#     if fc == "RTCA_new.RTCA.CORS":
#         fieldList = arcpy.ListFields(fc)
#         for field in fieldList:
#             if field.name.upper() == 'RTCA_PROJECT_NUMBER':
#                 print "fc was: ", fc
#                 print "field was: ", field.name
#                 print "alias was: ", field.aliasName
#                 arcpy.AlterField_management(in_table=fc, \
#                 field=field, new_field_name="RTCA_Project_Number", new_field_alias="RTCA Project Number")
#                 print "fc is now: ", fc
#                 print "field is now: ", field.name
#                 print "alias is now: ", field.aliasName
