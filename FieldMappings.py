import arcpy
# This is possible in python using FeatureClasstoFeatureClass with Fieldmappings. You can also rename fields at the same time.
#So if you have a Featureclass with FIELD3,FIELD2,FIELD1 and you want the result to be FIELD1,FIELD2,FIELD3 then the following code should accomplish this.
arcpy.env.workspace = r"C:\Users\jamatney\AppData\Roaming\Esri\Desktop10.2\ArcCatalog\rtca user connected to rtca_new database.sde"
arcpy.env.overwriteOutput = True

input_fpath = "RTCA_new.RTCA.CORS_MILESTONE_TEST"

output_dpath = arcpy.env.workspace
output_fname = "CORS_MILESTONE_TEST2"

fms = arcpy.FieldMappings()

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"RTCA_Project_Number")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Project_Name")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"FiscalYearStart")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"FiscalYearStop")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NPS_Role_Category")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NPSRoleNarrative")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Milestone")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Milestone_Measure")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Milestone_Quantity")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Milestone_Status")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Leveraging_Partner_Name")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Leveraging_PartnerDD")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Leveraging_PartnerIKD")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Description_of_IKService")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Total_Leveraging_Partner_Invest")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NPS_Pay_Periods_Invested")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NPS_Staff_Time_Dollars")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NPS_NonSalary_Dollars")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Total_NPS_Investment")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Total_Project_Investment")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"End_Product_Attachments")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Other_Attachments")
fms.addFieldMap(fm)


arcpy.conversion.FeatureClassToFeatureClass(input_fpath,output_dpath,output_fname,"",fms)
