import arcpy
# Set workspace environment to geodatabase
arcpy.env.workspace = r"C:\Users\jamatney\AppData\Roaming\Esri\Desktop10.2\ArcCatalog\rtca user connected to rtca_new database.sde"

# Loop through feature classes looking for a field named 'elev'
fcList = arcpy.ListTables() # get a list of feature classes
for fc in fcList:  # loop through feature classes
    print fc
    if fc == "RTCA_new.RTCA.CORS_Milestone_Table":
        print fc
        fieldList = arcpy.ListFields(fc)  # get a list of fields for each feature class
        for field in fieldList: # loop through each field
            if field.name == 'Project_Na':
                arcpy.AlterField_management(fc, field.name, "Project_Name", "Project Name")
            elif field.name == 'FiscalYear':
                arcpy.AlterField_management(fc, field.name, "FiscalYearStart", "Fiscal Year Start")
            elif field.name == 'FiscalYe_1':
                arcpy.AlterField_management(fc, field.name, "FiscalYearStop", "Fiscal Year Stop")
            elif field.name == 'Milestone':
                arcpy.AlterField_management(fc, field.name, "Milestone", "Milestone")
            elif field.name == 'MilestoneI':
                arcpy.AlterField_management(fc, field.name, "MilestoneIfOtherExplain", "Milestone - If Other, Explain")
            elif field.name == 'Milestone_':
                arcpy.AlterField_management(fc, field.name, "Milestone_Measure", "Milestone Measure")
            elif field.name == 'MilestoneM':
                arcpy.AlterField_management(fc, field.name, "MilestoneMeasureIfOtherExplain", "Milestone Measure - If Other, Explain")
            elif field.name == 'Milestone1':
                arcpy.AlterField_management(fc, field.name, "Milestone_Quantity", "Milestone Quantity")
            elif field.name == 'Mileston_1':
                arcpy.AlterField_management(fc, field.name, "Milestone_Status", "Milestone Status")
            elif field.name == 'Leveraging':
                arcpy.AlterField_management(fc, field.name, "Leveraging_Partner_Name", "Leveraging Partner Name")
            elif field.name == 'Leveragi_1':
                arcpy.AlterField_management(fc, field.name, "Leveraging_PartnerDD", "Leveraging Partner Direct Dollars")
            elif field.name == 'Leveragi_2':
                arcpy.AlterField_management(fc, field.name, "Leveraging_PartnerIKD", "Leveraging Partner In-Kind Dollars")
            elif field.name == 'Descriptio':
                arcpy.AlterField_management(fc, field.name, "Description_of_IKService", "Description of In-Kind Service")
            elif field.name == 'Total_Leve':
                arcpy.AlterField_management(fc, field.name, "Total_Leveraging_Partner_Invest", "Total Leveraging Partner Investment")
            elif field.name == 'NPS_Pay_Pe':
                arcpy.AlterField_management(fc, field.name, "NPS_Pay_Periods_Invested", "NPS Pay Periods Invested")
            elif field.name == 'NPS_Staff_':
                arcpy.AlterField_management(fc, field.name, "NPS_Staff_Time_Dollars", "NPS Staff Time Dollars")
            elif field.name == 'NPS_NonSal':
                arcpy.AlterField_management(fc, field.name, "NPS_NonSalary_Dollars", "NPS Non-Salary Dollars")
            elif field.name == 'Total_NPS_':
                arcpy.AlterField_management(fc, field.name, "Total_NPS_Investment", "Total NPS Investment")
            elif field.name == 'Total_Proj':
                arcpy.AlterField_management(fc, field.name, "Total_Project_Investment", "Total Project Investment")
            elif field.name == 'End_Produc':
                arcpy.AlterField_management(fc, field.name, "End_Product_Attachment", "End Product - Attachment")
            elif field.name == 'Other_Atta':
                arcpy.AlterField_management(fc, field.name, "Other_Attachments", "Other - Attachment")
            elif field.name == 'PhotoAttac':
                arcpy.AlterField_management(fc, field.name, "PhotoAttachment", "Photo - Attachment")
            elif field.name == 'ProjectSuc':
                arcpy.AlterField_management(fc, field.name, "ProjectSuccessStoryAttachment", "Project Success Story - Attachment")
            elif field.name == 'PhotoCredi':
                arcpy.AlterField_management(fc, field.name, "PhotoCredit", "Photo Credit")
            elif field.name == 'PhotoCapti':
                arcpy.AlterField_management(fc, field.name, "PhotoCaptionCreditAttachment", "Photo Caption Credit - Attachment")
            elif field.name == 'RTCA_Proje':
                arcpy.AlterField_management(fc, field.name, "RTCA_Project_Number", "RTCA Project Number")
            else:
                pass
            print "Name: ", field.name
            print "Alias: ", field.aliasName
    else:
        print "No such Geodatabase Object"
