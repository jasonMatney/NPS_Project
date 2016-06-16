import arcpy
# Set workspace environment to geodatabase
arcpy.env.workspace = r"C:\Users\jamatney\AppData\Roaming\Esri\Desktop10.2\ArcCatalog\rtca user connected to rtca_new database.sde"

# Loop through feature classes looking for a field named 'elev'
fcList = arcpy.ListFeatureClasses() # get a list of feature classes
for fc in fcList:  # loop through feature classes
    print fc
    if fc == "RTCA_new.RTCA.FULL_Project_Description":
        print fc
        fieldList = arcpy.ListFields(fc)  # get a list of fields for each feature class
        for field in fieldList: # loop through each field
            if field.name == 'RTCA_new_R':
                arcpy.AlterField_management(fc, field.name, "Project_Name", "Project_Name")
            elif field.name == 'RTCA_new_1':
                arcpy.AlterField_management(fc, field.name, "NPS_Program", "NPS_Program")
            elif field.name == 'RTCA_new_2':
                arcpy.AlterField_management(fc, field.name, "Portfolio", "Portfolio")
            elif field.name == 'RTCA_new_3':
                arcpy.AlterField_management(fc, field.name, "Portfolio_IfOtherExplain", "Portfolio_IfOtherExplain")
            elif field.name == 'RTCA_new_4':
                arcpy.AlterField_management(fc, field.name, "Anticipated_Outcome", "Anticipated_Outcome")
            elif field.name == 'RTCA_new_5':
                arcpy.AlterField_management(fc, field.name, "Anticipated_IfOtherExplain", "Anticipated_IfOtherExplain")
            elif field.name == 'RTCA_new_6':
                arcpy.AlterField_management(fc, field.name, "Project_Goal", "Project Zipcodes")
            elif field.name == 'RTCA_new_7':
                arcpy.AlterField_management(fc, field.name, "RTCA_Project_Number", "RTCA_Project_Number")
            elif field.name == 'RTCA_new_8':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year_Start", "Fiscal_Year_Start")
            elif field.name == 'RTCA_new_9':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year_End", "Fiscal_Year_End")
            elif field.name == 'RTCA_ne_10':
                arcpy.AlterField_management(fc, field.name, "Project_Status", "Project_Status")
            elif field.name == 'RTCA_ne_11':
                arcpy.AlterField_management(fc, field.name, "NPS_Regional_Office", "NPS_Regional_Office")
            elif field.name == 'RTCA_ne_12':
                arcpy.AlterField_management(fc, field.name, "NPS_Project_Manager", "NPS_Project_Manager")
            elif field.name == 'RTCA_ne_13':
                arcpy.AlterField_management(fc, field.name, "NPS_Project_Manager_Email", "NPS_Project_Manager_Email")
            elif field.name == 'RTCA_ne_14':
                arcpy.AlterField_management(fc, field.name, "NPS_Role_Category", "NPS_Role_Category")
            elif field.name == 'RTCA_ne_15':
                arcpy.AlterField_management(fc, field.name, "NPSRoleCat_IfOtherExplain", "NPSRoleCat_IfOtherExplain")
            elif field.name == 'RTCA_ne_16':
                arcpy.AlterField_management(fc, field.name, "NPS_Role_Narrative", "NPS_Role_Narrative")
            elif field.name == 'RTCA_ne_17':
                arcpy.AlterField_management(fc, field.name, "NPS_Project_Team_Members", "NPS_Project_Team_Members")
            elif field.name == 'RTCA_ne_18':
                arcpy.AlterField_management(fc, field.name, "Project_Location_City_Town", "Project_Location_City_Town")
            elif field.name == 'RTCA_ne_19':
                arcpy.AlterField_management(fc, field.name, "Project_Location_State", "Project_Location_State")
            elif field.name == 'RTCA_ne_20':
                arcpy.AlterField_management(fc, field.name, "Project_Location_Zipcodes", "Project_Location_Zipcodes")
            elif field.name == 'RTCA_ne_21':
                arcpy.AlterField_management(fc, field.name, "Project_Location_Description", "Project_Location_Description")
            elif field.name == 'RTCA_ne_22':
                arcpy.AlterField_management(fc, field.name, "General_Project_Type", "General_Project_Type")
            elif field.name == 'RTCA_ne_23':
                arcpy.AlterField_management(fc, field.name, "ApplicantOrganization", "ApplicantOrganization")
            elif field.name == 'RTCA_ne_24':
                arcpy.AlterField_management(fc, field.name, "ApplicantContactName", "ApplicantContactName")
            elif field.name == 'RTCA_ne_25':
                arcpy.AlterField_management(fc, field.name, "ApplicantTelephoneNumber", "ApplicantTelephoneNumber")
            elif field.name == 'RTCA_ne_26':
                arcpy.AlterField_management(fc, field.name, "ApplicantEmail", "ApplicantEmail")
            elif field.name == 'RTCA_ne_27':
                arcpy.AlterField_management(fc, field.name, "ApplicantMailingAddress", "ApplicantMailingAddress")
            elif field.name == 'RTCA_ne_28':
                arcpy.AlterField_management(fc, field.name, "ApplicantCity", "ApplicantCity")
            elif field.name == 'RTCA_ne_29':
                arcpy.AlterField_management(fc, field.name, "ApplicantState", "ApplicantState")
            elif field.name == 'RTCA_ne_30':
                arcpy.AlterField_management(fc, field.name, "ApplicantZip", "ApplicantZip")
            elif field.name == 'RTCA_ne_31':
                arcpy.AlterField_management(fc, field.name, "ApplicantWebsite", "ApplicantWebsite")
            elif field.name == 'RTCA_ne_32':
                arcpy.AlterField_management(fc, field.name, "AssociatedPartnersOrganization", "AssociatedPartnersOrganization")
            elif field.name == 'RTCA_ne_33':
                arcpy.AlterField_management(fc, field.name, "AssociatedPartnersContactName", "AssociatedPartnersContactName")
            elif field.name == 'RTCA_ne_34':
                arcpy.AlterField_management(fc, field.name, "AssociatedPartnersEmail", "AssociatedPartnersEmail")
            elif field.name == 'RTCA_ne_35':
                arcpy.AlterField_management(fc, field.name, "NationalCopName", "NationalCopName")
            elif field.name == 'RTCA_ne_36':
                arcpy.AlterField_management(fc, field.name, "NatCooperatorOrg_IfOtherExplain", "NatCooperatorOrg_IfOtherExplain")
            elif field.name == 'RTCA_ne_37':
                arcpy.AlterField_management(fc, field.name, "NationalCopContactName", "NationalCopContactName")
            elif field.name == 'RTCA_ne_38':
                arcpy.AlterField_management(fc, field.name, "NationalCopEmail", "NationalCopEmail")
            elif field.name == 'RTCA_ne_39':
                arcpy.AlterField_management(fc, field.name, "NPS_Unit_Name", "NPS_Unit_Name")
            elif field.name == 'RTCA_ne_40':
                arcpy.AlterField_management(fc, field.name, "Project_Website", "Project_Website")
            elif field.name == 'RTCA_ne_41':
                arcpy.AlterField_management(fc, field.name, "Project_Agreement_Attachment", "Project_Agreement_Attachment")
            elif field.name == 'RTCA_ne_42':
                arcpy.AlterField_management(fc, field.name, "Photo_Attachment", "Photo_Attachment")
            elif field.name == 'RTCA_ne_43':
                arcpy.AlterField_management(fc, field.name, "Other_Attachment", "Other_Attachment")
            elif field.name == 'RTCA_ne_44':
                arcpy.AlterField_management(fc, field.name, "ProjectApplicationAttachment", "ProjectApplicationAttachment")
            elif field.name == 'RTCA_ne_45':
                arcpy.AlterField_management(fc, field.name, "ProjectWorkPlanAttachment", "ProjectWorkPlanAttachment")
            elif field.name == 'RTCA_ne_46':
                arcpy.AlterField_management(fc, field.name, "PhotoCredit", "PhotoCredit")
            elif field.name == 'RTCA_ne_47':
                arcpy.AlterField_management(fc, field.name, "PhotoCaptionCreditAttachment", "PhotoCaptionCreditAttachment")
            else:
                pass
            print "Name: ", field.name
            print "Alias: ", field.aliasName
    else:
        print "No such Geodatabase Object"
