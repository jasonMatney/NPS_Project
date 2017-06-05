import arcpy
# Set workspace environment to geodatabase
arcpy.env.workspace = r"C:\Users\jamatney\AppData\Roaming\ESRI\Desktop10.5\ArcCatalog\Connection to rtca-db.cnr.ncsu.edu.sde"

# Loop through feature classes looking for a field named 'elev'
fcList = arcpy.ListFeatureClasses() # get a list of feature classes
for fc in fcList:  # loop through feature classes
    print fc
    if fc == "RTCADB.JAMATNEY.Full_Project_Description":
        print fc
        fieldList = arcpy.ListFields(fc)  # get a list of fields for each feature class
        for field in fieldList: # loop through each field
            if field.name == 'RTCA_Project_Number':
                arcpy.AlterField_management(fc, field.name, new_field_alias="RTCA Project Number")
            elif field.name == 'Project_Name':
                arcpy.AlterField_management(fc, field.name, new_field_alias="Project Name")
            elif field.name == 'NPS_Program':
                arcpy.AlterField_management(fc, field.name, new_field_alias="NPS Program")
            elif field.name == 'Strategic_Goal':
                arcpy.AlterField_management(fc, field.name, new_field_alias="Strategic Goal")
            elif field.name == 'Strategic_Goal_IfOtherExplain':
                arcpy.AlterField_management(fc, field.name, "Strategic_Goal_IfOtherExplain", "Strategic Goal - If Other Explain")
            elif field.name == 'Anticipated_Outcome':
                arcpy.AlterField_management(fc, field.name, "Anticipated_Outcome", "Anticipated Outcome")
            elif field.name == 'Anticipated_IfOtherExplain':
                arcpy.AlterField_management(fc, field.name, "Anticipated_IfOtherExplain", "Anticipated Outcome - If Other Explain")
            elif field.name == 'Project_Goal':
                arcpy.AlterField_management(fc, field.name, "Project_Goal", "Project Goal")
            elif field.name == 'NPS_Role_Category':
                arcpy.AlterField_management(fc, field.name, "NPS_Role_Category", "NPS Role Category")
            elif field.name == 'NPSRoleCat_IfOtherExplain':
                arcpy.AlterField_management(fc, field.name, "NPSRoleCat_IfOtherExplain", "NPS Role Category - If Other Explain")
            elif field.name == 'NPS_Role_Narrative':
                arcpy.AlterField_management(fc, field.name, "NPS_Role_Narrative", "NPS Role Narrative")
            elif field.name == 'Project_Status':
                arcpy.AlterField_management(fc, field.name, "Project_Status", "Project Status")
            elif field.name == 'Fiscal_Year_Start':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year_Start", "Fiscal Year Start")
            elif field.name == 'Fiscal_Year_End':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year_End", "Fiscal Year End")
            elif field.name == 'NPS_Regional_Office':
                arcpy.AlterField_management(fc, field.name, "NPS_Regional_Office", "NPS Regional Office")
            elif field.name == 'NPS_Project_Manager':
                arcpy.AlterField_management(fc, field.name, "NPS_Project_Manager", "NPS Project Manager")
            elif field.name == 'NPS_Project_Manager_Email':
                arcpy.AlterField_management(fc, field.name, "NPS_Project_Manager_Email", "NPS Project Manager Email")
            elif field.name == 'NPS_Project_Team_Members':
                arcpy.AlterField_management(fc, field.name, "NPS_Project_Team_Members", "NPS Project Team Members")
            elif field.name == 'Project_Location_City_Town':
                arcpy.AlterField_management(fc, field.name, "Project_Location_City_Town", "Project Location - City or Town")
            elif field.name == 'Project_Location_State':
                arcpy.AlterField_management(fc, field.name, "Project_Location_State", "Project Location - State")
            elif field.name == 'Project_Location_Zipcodes':
                arcpy.AlterField_management(fc, field.name, "Project_Location_Zipcodes", "Project Location - Zipcodes")
            elif field.name == 'Project_Location_Description':
                arcpy.AlterField_management(fc, field.name, "Project_Location_Description", "Project Location - Description")
            elif field.name == 'ApplicantOrganization':
                arcpy.AlterField_management(fc, field.name, "ApplicantOrganization", "Applicant - Name of Organization")
            elif field.name == 'ApplicantContactName':
                arcpy.AlterField_management(fc, field.name, "ApplicantContactName", "Applicant - Contact Name")
            elif field.name == 'ApplicantTelephoneNumber':
                arcpy.AlterField_management(fc, field.name, "ApplicantTelephoneNumber", "Applicant - Telephone Number")
            elif field.name == 'ApplicantEmail':
                arcpy.AlterField_management(fc, field.name, "ApplicantEmail","Applicant - Email")
            elif field.name == 'ApplicantMailingAddress':
                arcpy.AlterField_management(fc, field.name, "ApplicantMailingAddress", "Applicant - Mailing Address")
            elif field.name == 'ApplicantCity':
                arcpy.AlterField_management(fc, field.name, "ApplicantCity", "Applicant - City")
            elif field.name == 'ApplicantState':
                arcpy.AlterField_management(fc, field.name, "ApplicantState", "Applicant - State")
            elif field.name == 'ApplicantZip':
                arcpy.AlterField_management(fc, field.name, "ApplicantZip", "Applicant - Zipcode")
            elif field.name == 'ApplicantWebsite':
                arcpy.AlterField_management(fc, field.name, "ApplicantWebsite", "Applicant - Website")
            elif field.name == 'AssociatedPartnersOrganization':
                arcpy.AlterField_management(fc, field.name, "AssociatedPartnersOrganization", "Associated Partners - Name of Organization")
            elif field.name == 'AssociatedPartnersContactName':
                arcpy.AlterField_management(fc, field.name, "AssociatedPartnersContactName", "Associated Partners - Contact Name")
            elif field.name == 'AssociatedPartnersEmail':
                arcpy.AlterField_management(fc, field.name, "AssociatedPartnersEmail", "Associated Partners - Email")
            elif field.name == 'NationalCopName':
                arcpy.AlterField_management(fc, field.name, "NationalCopName", "National Cooperator - Name of Organization")
            elif field.name == 'NatCooperatorOrg_IfOtherExplain':
                arcpy.AlterField_management(fc, field.name, "NatCooperatorOrg_IfOtherExplain", "National Cooperator - If Other Explain")
            elif field.name == 'NationalCopContactName':
                arcpy.AlterField_management(fc, field.name, "NationalCopContactName", "National Cooperator - Contact Name")
            elif field.name == 'NationalCopEmail':
                arcpy.AlterField_management(fc, field.name, "NationalCopEmail", "National Cooperator - Email")
            elif field.name == 'NPS_Unit_Name':
                arcpy.AlterField_management(fc, field.name, "NPS_Unit_Name", "NPS Unit Name")
            elif field.name == 'Project_Website':
                arcpy.AlterField_management(fc, field.name, "Project_Website", "Project Website")
            elif field.name == 'ProjectApplicationAttachment':
                arcpy.AlterField_management(fc, field.name, "ProjectApplicationAttachment", "Project Application - Attachment")
            elif field.name == 'Project_Agreement_Attachment':
                arcpy.AlterField_management(fc, field.name, "Project_Agreement_Attachment", "Project Agreement - Attachment")
            elif field.name == 'ProjectWorkPlanAttachment':
                arcpy.AlterField_management(fc, field.name, "ProjectWorkPlanAttachment", "Project Work Plan - Attachment")
            elif field.name == 'Photo_Attachment':
                arcpy.AlterField_management(fc, field.name, "Photo_Attachment", "Photo - Attachment")
            elif field.name == 'PhotoCaptionCreditAttachment':
                arcpy.AlterField_management(fc, field.name, "PhotoCaptionCreditAttachment", "Photo Caption Credit - Attachment")
            elif field.name == 'SuccessStory_Attachment':
                arcpy.AlterField_management(fc, field.name, "SuccessStory_Attachment", "Success Story - Attachment")
            elif field.name == 'Other_Attachment':
                arcpy.AlterField_management(fc, field.name, "Other_Attachment", "Other - Attachment")
            elif field.name == 'created_user':
                arcpy.AlterField_management(fc, field.name, "created_user", "created user")
            elif field.name == 'created_date':
                arcpy.AlterField_management(fc, field.name, "created_date", "created date")
            elif field.name == 'last_edited_user':
                arcpy.AlterField_management(fc, field.name, "last_edited_user", "last edited user")
            elif field.name == 'last_edited_date':
                arcpy.AlterField_management(fc, field.name, "last_edited_date", "last edited date")


            else:
                pass
            print "Name: ", field.name
            print "Alias: ", field.aliasName
    else:
        print "No such Geodatabase Object"
