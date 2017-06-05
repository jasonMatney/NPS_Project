import arcpy
# This is possible in python using FeatureClasstoFeatureClass with Fieldmappings. You can also rename fields at the same time.
#So if you have a Featureclass with FIELD3,FIELD2,FIELD1 and you want the result to be FIELD1,FIELD2,FIELD3 then the following code should accomplish this.
arcpy.env.workspace = r"C:\Users\jamatney\AppData\Roaming\ESRI\Desktop10.5\ArcCatalog\Connection to rtca-db.cnr.ncsu.edu.sde"
arcpy.env.overwriteOutput = True

input_fpath = "RTCADB.JAMATNEY.Full_Project_Description"

output_dpath = arcpy.env.workspace
output_fname = "Full_Project_Description_Mapped"

fms = arcpy.FieldMappings()

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"RTCA_Project_Number")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Project_Name")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NPS_Program")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Strategic_Goal")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Secondary_Strategic_Goal")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Strategic_Goal_IfOtherExplain")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Anticipated_Outcome")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Secondary_Anticipated_Outcome")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Anticipated_IfOtherExplain")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Project_Goal")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NPS_Role_Category")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Secondary_NPS_Role_Category")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NPSRoleCat_IfOtherExplain")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NPS_Role_Narrative")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Project_Status")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Fiscal_Year_Start")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Fiscal_Year_End")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NPS_Regional_Office")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NPS_Project_Manager")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NPS_Project_Manager_Email")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NPS_Project_Team_Members")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Project_Location_City_Town")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Project_Location_State")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Project_Location_Zipcodes")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Project_Location_Description")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"ApplicantOrganization")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"ApplicantContactName")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"ApplicantTelephoneNumber")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"ApplicantEmail")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"ApplicantMailingAddress")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"ApplicantCity")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"ApplicantState")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"ApplicantZip")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"ApplicantWebsite")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"AssociatedPartnersOrganization")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"AssociatedPartnersContactName")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"AssociatedPartnersEmail")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NationalCopName")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Secondary_National_Cooperator")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NatCooperatorOrg_IfOtherExplain")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NationalCopContactName")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NationalCopEmail")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"NPS_Unit_Name")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Secondary_NPS_Unit")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Project_Website")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"ProjectApplicationAttachment")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Project_Agreement_Attachment")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"ProjectWorkPlanAttachment")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Photo_Attachment")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"PhotoCaptionCreditAttachment")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"SuccessStory_Attachment")
fms.addFieldMap(fm)

fm = arcpy.FieldMap()
fm.addInputField(input_fpath,"Other_Attachments")
fms.addFieldMap(fm)


arcpy.conversion.FeatureClassToFeatureClass(input_fpath,output_dpath,output_fname,"",fms)
