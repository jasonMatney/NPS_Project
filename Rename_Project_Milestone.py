import arcpy
# Set workspace environment to geodatabase
arcpy.env.workspace = r"C:\Users\jamatney\AppData\Roaming\Esri\Desktop10.2\ArcCatalog\rtca user connected to rtca_new database.sde"

# Loop through feature classes looking for a field named 'elev'
fcList = arcpy.ListFeatureClasses() # get a list of feature classes
for fc in fcList:  # loop through feature classes
    print fc
    if fc == "RTCA_new.RTCA.CORS_MILESTONE":
        print fc
        fieldList = arcpy.ListFields(fc)  # get a list of fields for each feature class
        for field in fieldList: # loop through each field
            if field.name == 'Project_Na':
                arcpy.AlterField_management(fc, field.name, "Project_Name", "Project Name")
            elif field.name == 'Fiscal_Yea':
                arcpy.AlterField_management(fc, field.name, "Fiscal_Year", "Fiscal Year")
            elif field.name == 'NPS_Role_C':
                arcpy.AlterField_management(fc, field.name, "NPS_Role_Category", "NPS Role Category")
            elif field.name == 'NPS_Role_N':
                arcpy.AlterField_management(fc, field.name, "NPS_Role_Narrative", "NPS Role Narrative")
            elif field.name == 'Milestone_':
                arcpy.AlterField_management(fc, field.name, "Milestone_Measure", "Milestone Measure")
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
            elif field.name == 'TotalLever':
                arcpy.AlterField_management(fc, field.name, "Total_Leveraging_Partner_Invest", "Total Leveraging Partner Investment")
            elif field.name == 'NPSPayPeri':
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
                arcpy.AlterField_management(fc, field.name, "End_Product_Attachments", "End Product Attachments")
            elif field.name == 'Other_Atta':
                arcpy.AlterField_management(fc, field.name, "Other_Attachments", "Other Attachments")
            else:
                pass
            print "Name: ", field.name
            print "Alias: ", field.aliasName
    else:
        print "No such Geodatabase Object"
