'''
When ArcMap exports data from Feature Classes to a shapefile,
the field names are conveniently cut off at 13 characters. 

When making a new Feautre Class using one of these exported shapefiles as a template,
the new FC will naturally also contain the truncated field names.

Good riddance. Who needed full field names anyways?

The answer is of course, everybody.

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
    if fc == "RTCA_new.RTCA.CORS_Description":
        print fc
        fieldList = arcpy.ListFields(fc)  # get a list of fields for each feature class
        for field in fieldList: # loop through each field
            if field.name == 'Project_Na':
                arcpy.AlterField_management(fc, field.name, "Project_Name", "Project_Name")
            elif field.name == 'NPS_Progra':
                arcpy.AlterField_management(fc, field.name, "NPS_Program", "NPS_Program")
            elif field.name == 'Portfolio':
                arcpy.AlterField_management(fc, field.name, "Portfolio", "Portfolio")
            elif field.name == 'Portfolio_':
                arcpy.AlterField_management(fc, field.name, "Portfolio_IfOtherExplain", "Portfolio_IfOtherExplain")
            elif field.name == 'Anticipate':
                arcpy.AlterField_management(fc, field.name, "Anticipated_Outcome", "Anticipated_Outcome")
            elif field.name == 'Anticipa_1':
                arcpy.AlterField_management(fc, field.name, "Anticipated_IfOtherExplain", "Anticipated_IfOtherExplain")
            elif field.name == 'Project_Go':
                arcpy.AlterField_management(fc, field.name, "Project_Goal", "Project Zipcodes")
            elif field.name == 'RTCA_Proje':
                arcpy.AlterField_management(fc, field.name, "RTCA_Project_Number", "RTCA_Project_Number")
            elif field.name == 'Fiscal_Yea':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year_Start", "Fiscal_Year_Start")
            elif field.name == 'Fiscal_Y_1':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year_End", "Fiscal_Year_End")
            elif field.name == 'Project_St':
                arcpy.AlterField_management(fc, field.name, "Project_Status", "Project_Status")
            elif field.name == 'NPS_Region':
                arcpy.AlterField_management(fc, field.name, "NPS_Regional_Office", "NPS_Regional_Office")
            elif field.name == 'NPS_Projec':
                arcpy.AlterField_management(fc, field.name, "NPS_Project_Manager", "NPS_Project_Manager")
            elif field.name == 'NPS_Proj_1':
                arcpy.AlterField_management(fc, field.name, "NPS_Project_Manager_Email", "NPS_Project_Manager_Email")
            elif field.name == 'NPS_Role_C':
                arcpy.AlterField_management(fc, field.name, "NPS_Role_Category", "NPS_Role_Category")
            elif field.name == 'NPSRoleCat':
                arcpy.AlterField_management(fc, field.name, "NPSRoleCat_IfOtherExplain", "NPSRoleCat_IfOtherExplain")
            elif field.name == 'NPS_Role_N':
                arcpy.AlterField_management(fc, field.name, "NPS_Role_Narrative", "NPS_Role_Narrative")
            elif field.name == 'NPS_Proj_2':
                arcpy.AlterField_management(fc, field.name, "NPS_Project_Team_Members", "NPS_Project_Team_Members")
            elif field.name == 'Project_Lo':
                arcpy.AlterField_management(fc, field.name, "Project_Location_City_Town", "Project_Location_City_Town")
            elif field.name == 'Project__1':
                arcpy.AlterField_management(fc, field.name, "Project_Location_State", "Project_Location_State")
            elif field.name == 'Project__2':
                arcpy.AlterField_management(fc, field.name, "Project_Location_Zipcodes", "Project_Location_Zipcodes")
            elif field.name == 'Project__3':
                arcpy.AlterField_management(fc, field.name, "Project_Location_Description", "Project_Location_Description")
            elif field.name == 'ApplicantO':
                arcpy.AlterField_management(fc, field.name, "ApplicantOrganization", "ApplicantOrganization")
            elif field.name == 'ApplicantC':
                arcpy.AlterField_management(fc, field.name, "ApplicantContactName", "ApplicantContactName")
            elif field.name == 'ApplicantT':
                arcpy.AlterField_management(fc, field.name, "ApplicantTelephoneNumber", "ApplicantTelephoneNumber")
            elif field.name == 'ApplicantE':
                arcpy.AlterField_management(fc, field.name, "ApplicantEmail", "ApplicantEmail")
            elif field.name == 'ApplicantM':
                arcpy.AlterField_management(fc, field.name, "ApplicantMailingAddress", "ApplicantMailingAddress")
            elif field.name == 'Applican_1':
                arcpy.AlterField_management(fc, field.name, "ApplicantCity", "ApplicantCity")
            elif field.name == 'ApplicantS':
                arcpy.AlterField_management(fc, field.name, "ApplicantState", "ApplicantState")
            elif field.name == 'ApplicantZ':
                arcpy.AlterField_management(fc, field.name, "ApplicantZip", "ApplicantZip")
            elif field.name == 'ApplicantW':
                arcpy.AlterField_management(fc, field.name, "ApplicantWebsite", "ApplicantWebsite")
            elif field.name == 'Associated':
                arcpy.AlterField_management(fc, field.name, "AssociatedPartnersOrganization", "AssociatedPartnersOrganization")
            elif field.name == 'Associat_1':
                arcpy.AlterField_management(fc, field.name, "AssociatedPartnersContactName", "AssociatedPartnersContactName")
            elif field.name == 'Associat_2':
                arcpy.AlterField_management(fc, field.name, "AssociatedPartnersEmail", "AssociatedPartnersEmail")
            elif field.name == 'NationalCo':
                arcpy.AlterField_management(fc, field.name, "NationalCopName", "NationalCopName")
            elif field.name == 'NatCoopera':
                arcpy.AlterField_management(fc, field.name, "NatCooperatorOrg_IfOtherExplain", "NatCooperatorOrg_IfOtherExplain")
            elif field.name == 'National_1':
                arcpy.AlterField_management(fc, field.name, "NationalCopContactName", "NationalCopContactName")
            elif field.name == 'National_2':
                arcpy.AlterField_management(fc, field.name, "NationalCopEmail", "NationalCopEmail")
            elif field.name == 'NPS_Unit_N':
                arcpy.AlterField_management(fc, field.name, "NPS_Unit_Name", "NPS_Unit_Name")
            elif field.name == 'Project_We':
                arcpy.AlterField_management(fc, field.name, "Project_Website", "Project_Website")
            elif field.name == 'Project_Ag':
                arcpy.AlterField_management(fc, field.name, "Project_Agreement_Attachment", "Project_Agreement_Attachment")
            elif field.name == 'Photo_Atta':
                arcpy.AlterField_management(fc, field.name, "Photo_Attachment", "Photo_Attachment")
            elif field.name == 'Other_Atta':
                arcpy.AlterField_management(fc, field.name, "Other_Attachment", "Other_Attachment")
            elif field.name == 'ProjectApp':
                arcpy.AlterField_management(fc, field.name, "ProjectApplicationAttachment", "ProjectApplicationAttachment")
            elif field.name == 'ProjectWor':
                arcpy.AlterField_management(fc, field.name, "ProjectWorkPlanAttachment", "ProjectWorkPlanAttachment")
            elif field.name == 'PhotoCredi':
                arcpy.AlterField_management(fc, field.name, "PhotoCredit", "PhotoCredit")
            elif field.name == 'PhotoCapti':
                arcpy.AlterField_management(fc, field.name, "PhotoCaptionCreditAttachment", "PhotoCaptionCreditAttachment")

            else:
                pass
            print "Name: ", field.name
            print "Alias: ", field.aliasName
    else:
        print "No such Geodatabase Object"
