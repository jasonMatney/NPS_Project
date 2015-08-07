import arcpy
import os

def listFcsInGDB():
    ''' set your arcpy.env.workspace to a gdb before calling '''
    for fds in arcpy.ListDatasets('','feature') + ['']:
        for fc in arcpy.ListFeatureClasses('','',fds):
            yield os.path.join(arcpy.env.workspace, fds, fc)

#Set workspace environment to geodatabase
arcpy.env.workspace = r"C:\Users\jamatney\AppData\Roaming\Esri\Desktop10.2\ArcCatalog\rtca user connected to rtca_new database.sde"

#call ListFeatureClass function
fcList = arcpy.ListFeatureClasses()

# Print the name of the current fc:
for fc in fcList:
    if fc == "RTCA_new.RTCA.NPS_CORS_RTCA":
        fieldList = [f.name for f in arcpy.ListFields(fc)]
        for field in fieldList:
            if field == 'RTCA_PrjNu':
                arcpy.AlterField_management(fc, field, "RTCA_Project_Number")
            elif field == 'RTCA_Proje':
                arcpy.AlterField_management(fc, field, "RTCA_Project_Number1")
            elif field == 'PO_NAME':
                arcpy.AlterField_management(fc, field, "Post_Office_Name")
            elif field == 'ZIPCODE_TY':
                arcpy.AlterField_management(fc, field, "Zipcode_Type")
            elif field == 'Project_Na':
                arcpy.AlterField_management(fc, field, "Project_Name")
            elif field == 'Fiscal_Yea':
                arcpy.AlterField_management(fc, field, "Fiscal_Year_Start")
            elif field == 'Fiscal_Y_1':
                arcpy.AlterField_management(fc, field, "Fiscal_Year_Stop")
            elif field == 'Project_Lo':
                arcpy.AlterField_management(fc, field, "Project_Location")
            elif field == 'NPSContact':
                arcpy.AlterField_management(fc, field, "NPSContactPointInfo")
            elif field == 'Anticipate':
                arcpy.AlterField_management(fc, field, "AnticipateOutcome")
            elif field == 'PublicInvo':
                arcpy.AlterField_management(fc, field, "PublicInvolvement")
            elif field == 'EstProjPay':
                arcpy.AlterField_management(fc, field, "EstProjPayPeriod")
            elif field == 'IntendClos':
                arcpy.AlterField_management(fc, field, "IntendCloseOut")
            elif field == 'ApprovStat':
                arcpy.AlterField_management(fc, field, "ApprovStatus")
            elif field == 'ReadyForRe':
                arcpy.AlterField_management(fc, field, "ReadyForReview")
            elif field == 'Project_De':
                arcpy.AlterField_management(fc, field, "Project_Description")
            elif field == 'NPS_Projec':
                arcpy.AlterField_management(fc, field, "NPS_Project_Type")
            elif field == 'Annual_Sta':
                arcpy.AlterField_management(fc, field, "Annual_Status")
            elif field == 'NPS_Unit_N':
                arcpy.AlterField_management(fc, field, "NPS_Unit_Name")
            elif field == 'NPS_Unit_C':
                arcpy.AlterField_management(fc, field, "NPS_Unit_Code")
            elif field == 'NPS_Office':
                arcpy.AlterField_management(fc, field, "NPS_Office_Name")
            elif field == 'Project_Ap':
                arcpy.AlterField_management(fc, field, "Project_Approver")
            elif field == 'Milestone_':
                arcpy.AlterField_management(fc, field, "Milestone_Category")
            elif field == 'Milestone1':
                arcpy.AlterField_management(fc, field, "Milestone_Definition")
            elif field == 'Service_Ca':
                arcpy.AlterField_management(fc, field, "Strategic_Category")
            elif field == 'Service_De':
                arcpy.AlterField_management(fc, field, "Strategic_Description")
            elif field == 'Financial_':
                arcpy.AlterField_management(fc, field, "Financial_Unit_Name")
            elif field == 'National_I':
                arcpy.AlterField_management(fc, field, "National_Initiative")
            elif field == 'Public_Pri':
                arcpy.AlterField_management(fc, field, "Public_Private_Record")
            elif field == 'Project_Su':
                arcpy.AlterField_management(fc, field, "Project_Success_Report")
            elif field == 'Leveraging':
                arcpy.AlterField_management(fc, field, "Leveraging_Outcome")
            elif field == 'Leveragi_1':
                arcpy.AlterField_management(fc, field, "Leveraging_Participants")
            elif field == 'Leveragi_2':
                arcpy.AlterField_management(fc, field, "Leveraging_Completion_Date")
            elif field == 'Leveragi_3':
                arcpy.AlterField_management(fc, field, "Leveraging_Partner")
            elif field == 'Leveragi_4':
                arcpy.AlterField_management(fc, field, "Leveraging_Partner_Match")
            elif field == 'Leveragi_5':
                arcpy.AlterField_management(fc, field, "Leveraging_Challenge_Cost_Share")
            elif field == 'Leveragi_6':
                arcpy.AlterField_management(fc, field, "Leveraging_National_Initiative")
            elif field == 'NationalCo':
                arcpy.AlterField_management(fc, field, "NationalCopID")
            elif field == 'National_1':
                arcpy.AlterField_management(fc, field, "NationalCopName")
            elif field == 'National_2':
                arcpy.AlterField_management(fc, field, "NationalCopContactPerson")
            elif field == 'National_3':
                arcpy.AlterField_management(fc, field, "NationalCopPhone")
            elif field == 'National_4':
                arcpy.AlterField_management(fc, field, "NationalCopEmail")
            elif field == 'National_5':
                arcpy.AlterField_management(fc, field, "NationalCopAddress")
            elif field == 'National_6':
                arcpy.AlterField_management(fc, field, "NationalCopWebsiteList")
            elif field == 'LocalCopNa':
                arcpy.AlterField_management(fc, field, "LocalCopName")
            elif field == 'LocalCopCo':
                arcpy.AlterField_management(fc, field, "LocalCopContactPerson")
            elif field == 'LocalCopPh':
                arcpy.AlterField_management(fc, field, "LocalCopPhone")
            elif field == 'LocalCopEm':
                arcpy.AlterField_management(fc, field, "LocalCopEmail")
            elif field == 'LocalCopAd':
                arcpy.AlterField_management(fc, field, "LocalCopAddress")
            elif field == 'LocalCopCi':
                arcpy.AlterField_management(fc, field, "LocalCopCity")
            elif field == 'LocalCopSt':
                arcpy.AlterField_management(fc, field, "LocalCopStateName")
            elif field == 'LocalCopZi':
                arcpy.AlterField_management(fc, field, "LocalCopZip")
            elif field == 'LocalCopWe':
                arcpy.AlterField_management(fc, field, "LocalCopWebsiteList")
            elif field == 'RTCAFieldS':
                arcpy.AlterField_management(fc, field, "RTCAFieldStaff_AccessLevel")
            elif field == 'RTCAFiel_1':
                arcpy.AlterField_management(fc, field, "RTCAFieldStaff_OfficeID")
            elif field == 'RTCAFiel_2':
                arcpy.AlterField_management(fc, field, "RTCAFieldStaff_Name")
            elif field == 'RTCAFiel_3':
                arcpy.AlterField_management(fc, field, "RTCAFieldStaff_Email")
            elif field == 'RTCAFiel_4':
                arcpy.AlterField_management(fc, field, "RTCAFieldStaff_MailingAddress")
            elif field == 'RTCAFiel_5':
                arcpy.AlterField_management(fc, field, "RTCAFieldStaff_City")
            elif field == 'RTCAFiel_6':
                arcpy.AlterField_management(fc, field, "RTCAFieldStaff_State")
            elif field == 'RTCAFiel_7':
                arcpy.AlterField_management(fc, field, "RTCAFieldStaff_Zip")
            elif field == 'RTCAFiel_8':
                arcpy.AlterField_management(fc, field, "RTCAFieldStaff_Phone")
            elif field == 'RTCAFiel_9':
                arcpy.AlterField_management(fc, field, "RTCAFieldStaff_Fax")
            elif field == 'RTCAFiel_10':
                arcpy.AlterField_management(fc, field, "RTCAFieldStaff_Cell")
            elif field == 'Annual_Sta':
                arcpy.AlterField_management(fc, field, "Annual_Status")
            elif field == 'Annual_Yea':
                arcpy.AlterField_management(fc, field, "Annual_Year")
            elif field == 'Dropped_Ex':
                arcpy.AlterField_management(fc, field, "Dropped_Explanation")
            elif field == 'ApplicantN':
                arcpy.AlterField_management(fc, field, "Applicant_NPS_Contact")
            elif field == 'Project_Le':
                arcpy.AlterField_management(fc, field, "Applicant_NPS_Contact")
            elif field == 'Project_Co':
                arcpy.AlterField_management(fc, field, "Applicant_Project_CoLead")
            elif field == 'Public_Pri':
                arcpy.AlterField_management(fc, field, "Public_Private_Partnership")
            elif field == 'StateName':
                arcpy.AlterField_management(fc, field, "State_Name")
            elif field == 'Unit_Name':
                arcpy.AlterField_management(fc, field, "NPS_Unit_Name")
            elif field == 'Unit_Code':
                arcpy.AlterField_management(fc, field, "NPS_Unit_Code")
            elif field == 'Contact_In':
                arcpy.AlterField_management(fc, field, "NPS_Contact_Information")
            elif field == 'OfficeName':
                arcpy.AlterField_management(fc, field, "NPS_Office_Name")
            elif field == 'PrjApprove':
                arcpy.AlterField_management(fc, field, "Project_Approver")
            elif field == 'PrjAppro_1':
                arcpy.AlterField_management(fc, field, "Project_Approver_Email")
            elif field == 'National_C':
                arcpy.AlterField_management(fc, field, "National_Cooperator_Agency")
            elif field == 'National_1':
                arcpy.AlterField_management(fc, field, "National_Cooperator_Bureau")
            elif field == 'Cooperator':
                arcpy.AlterField_management(fc, field, "Cooperator_Contact_Information")
            elif field == 'Attachment':
                arcpy.AlterField_management(fc, field, "AttachmentID")
            elif field == 'Attachme_1':
                arcpy.AlterField_management(fc, field, "Attachment_Name")
            elif field == 'Attachme_2':
                arcpy.AlterField_management(fc, field, "Attachment_Description")
            elif field == 'Website_Na':
                arcpy.AlterField_management(fc, field, "Website_Name")
            elif field == 'Website_UR':
                arcpy.AlterField_management(fc, field, "Website_URL")
            elif field == 'Milestone_':
                arcpy.AlterField_management(fc, field, "Milestone_Category")
            elif field == 'Milestone1':
                arcpy.AlterField_management(fc, field, "Milestone_Description")
            elif field == 'Service_Ca':
                arcpy.AlterField_management(fc, field, "Service_Category")
            elif field == 'Service_De':
                arcpy.AlterField_management(fc, field, "Service_Description")
            elif field == 'RTCA_Finan':
                arcpy.AlterField_management(fc, field, "RTCA_Financial_Unit_Name")
            elif field == 'RTCA_Fin_1':
                arcpy.AlterField_management(fc, field, "RTCA_Financial_Fiscal_Year")
            elif field == 'RTCA_Fin_2':
                arcpy.AlterField_management(fc, field, "RTCA_Financial_Dollar_Amount")
            elif field == 'RTCA_Fin_3':
                arcpy.AlterField_management(fc, field, "RTCA_Financial_Total_Investment")
            elif field == 'Applicant_':
                arcpy.AlterField_management(fc, field, "Applicant_Partner_Organization")
            elif field == 'Applicant1':
                arcpy.AlterField_management(fc, field, "Applicant_Partner_Website")
            elif field == 'Applican_1':
                arcpy.AlterField_management(fc, field, "Applicant_Contact_Name")
            elif field == 'Applican_2':
                arcpy.AlterField_management(fc, field, "Applicant_Contact_Phone_Number")
            elif field == 'Applican_3':
                arcpy.AlterField_management(fc, field, "Applicant_Contact_Email")
            elif field == 'Applican_4':
                arcpy.AlterField_management(fc, field, "Applicant_Contact_Address")
            elif field == 'Applican_5':
                arcpy.AlterField_management(fc, field, "Applicant_City")
            elif field == 'Applican_6':
                arcpy.AlterField_management(fc, field, "Applicant_State")
            elif field == 'Applican_7':
                arcpy.AlterField_management(fc, field, "Applicant_Zipcode")
            elif field == 'LoginName':
                arcpy.AlterField_management(fc, field, "Member_Login_Name")
            elif field == 'Password':
                arcpy.AlterField_management(fc, field, "Member_Password")
            elif field == 'AccessLeve':
                arcpy.AlterField_management(fc, field, "Member_Access_Level")
            elif field == 'MemberRegi':
                arcpy.AlterField_management(fc, field, "Member_Region_ID")
            elif field == 'MemberOffi':
                arcpy.AlterField_management(fc, field, "Member_Office_ID")
            elif field == 'MemberStat':
                arcpy.AlterField_management(fc, field, "Member_State_ID")
            elif field == 'MemberTitl':
                arcpy.AlterField_management(fc, field, "Member_Title")
            elif field == 'MemberFNam':
                arcpy.AlterField_management(fc, field, "Member_First_Name")
            elif field == 'MemberLNam':
                arcpy.AlterField_management(fc, field, "Member_Last_Name")
            elif field == 'MemberEmai':
                arcpy.AlterField_management(fc, field, "Member_Email")
            elif field == 'MemberMail':
                arcpy.AlterField_management(fc, field, "Member_Mailing_Address")
            elif field == 'MemberMa_1':
                arcpy.AlterField_management(fc, field, "Member_Mailing_Address_2")
            elif field == 'MemberCity':
                arcpy.AlterField_management(fc, field, "Member_City")
            elif field == 'MemberZip':
                arcpy.AlterField_management(fc, field, "Member_Zip")
            elif field == 'MemberPhon':
                arcpy.AlterField_management(fc, field, "Member_Phone_1")
            elif field == 'MemberPh_1':
                arcpy.AlterField_management(fc, field, "Member_Phone_2")
            elif field == 'MemberPh_2':
                arcpy.AlterField_management(fc, field, "Member_Phone_3")
            elif field == 'MemberPh_3':
                arcpy.AlterField_management(fc, field, "Member_Phone_Ext")
            elif field == 'MemberFax1':
                arcpy.AlterField_management(fc, field, "Member_Fax_1")
            elif field == 'MemberFax2':
                arcpy.AlterField_management(fc, field, "Member_Fax_2")
            elif field == 'MemberFax3':
                arcpy.AlterField_management(fc, field, "Member_Fax_3")
            elif field == 'MemberCell':
                arcpy.AlterField_management(fc, field, "Member_Cell_1")
            elif field == 'MemberCe_1':
                arcpy.AlterField_management(fc, field, "Member_Cell_2")
            elif field == 'MemberCe_2':
                arcpy.AlterField_management(fc, field, "Member_Cell_3")
            elif field == 'CopName':
                arcpy.AlterField_management(fc, field, "Cooperator_Name")
            elif field == 'CopContact':
                arcpy.AlterField_management(fc, field, "Cooperator_Contact")
            elif field == 'CopPhone1':
                arcpy.AlterField_management(fc, field, "Cooperator_Phone_1")
            elif field == 'CopPhone2':
                arcpy.AlterField_management(fc, field, "Cooperator_Phone_2")
            elif field == 'CopPhone3':
                arcpy.AlterField_management(fc, field, "Cooperator_Phone_3")
            elif field == 'CopPhoneEx':
                arcpy.AlterField_management(fc, field, "Cooperator_Phone_Ext")
            elif field == 'CopAddress':
                arcpy.AlterField_management(fc, field, "Cooperator_Address_1")
            elif field == 'CopAddre_1':
                arcpy.AlterField_management(fc, field, "Cooperator_Address_2")
            elif field == 'CopCity':
                arcpy.AlterField_management(fc, field, "Cooperator_City")
            elif field == 'CopEmail':
                arcpy.AlterField_management(fc, field, "Cooperator_Email")
            elif field == 'CopZip':
                arcpy.AlterField_management(fc, field, "Cooperator_Zip")
            elif field == 'CopStateID':
                arcpy.AlterField_management(fc, field, "Cooperator_StateID")
            elif field == 'WebsiteLis':
                arcpy.AlterField_management(fc, field, "Website_List")
            elif field == 'POINT_X_1':
                arcpy.AlterField_management(fc, field, "X_Coordinate")
            elif field == 'POINT_Y_1':
                arcpy.AlterField_management(fc, field, "Y_Coordinate")
            else:
                pass
            print field
    else:
        pass
