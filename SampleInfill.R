rm(list=ls())
setwd("C:\\Users\\jamatney\\Documents\\RTCA\\data\\RTCA_Tables_Raw")
list.files()
temp <- list.files(path = getwd()) 

tbl_Con_Nps_Areas <- read.csv("tbl_Con_Nps_Areas.csv")
tbl_ConAllStates <- read.csv("tbl_ConAllStates.csv")
tbl_CongDistricts <- read.csv("tbl_CongDistricts.csv")            
tbl_ConNCoop <- read.csv("tbl_ConNCoop.csv")
tbl_ConOffice <- read.csv("tbl_ConOffice.csv")

tbl_ConSucReport <- read.csv("tbl_ConSucReport.csv")
tbl_Consultation <- read.csv("tbl_Consultation.csv")
tbl_Consultation_Fiscal_Years <- read.csv("tbl_Consultation_Fiscal_Years.csv")
tbl_CustomizedDumpTable <- read.csv("tbl_CustomizedDumpTable.csv")      
tbl_DumpTable <- read.csv("tbl_DumpTable.csv")

tbl_Member <- read.csv("tbl_Member.csv")    
tbl_Member_Office <- read.csv("tbl_Member_Office.csv")         
tbl_Member_State <- read.csv("tbl_Member_State.csv")
tbl_Nps_Areas <- read.csv("tbl_Nps_Areas.csv")
tbl_Office <- read.csv("tbl_Office.csv")                   
tbl_Prj_Nps_Areas <- read.csv("tbl_Prj_Nps_Areas.csv")

tbl_PrjApplicant <- read.csv("tbl_PrjApplicant.csv")
tbl_PrjApplicantWebsite <- read.csv("tbl_PrjApplicantWebsite.csv")      
tbl_PrjCloseOutInfo <- read.csv("tbl_PrjCloseOutInfo.csv")
tbl_PrjCongDistricts_Test <- read.csv("tbl_PrjCongDistricts_Test.csv")    

tbl_PrjCooperator <- read.csv("tbl_PrjCooperator.csv")
tbl_PrjDetailDocument <- read.csv("tbl_PrjDetailDocument.csv")
tbl_PrjDetailInfo <- read.csv("tbl_PrjDetailInfo.csv")            
tbl_PrjDetailPartnerWebsite <- read.csv("tbl_PrjDetailPartnerWebsite.csv")

tbl_PrjDetailPhoto <- read.csv("tbl_PrjDetailPhoto.csv")
tbl_PrjNationalCooperator <- read.csv("tbl_PrjNationalCooperator.csv")    
tbl_PrjNCoop <- read.csv("tbl_PrjNCoop.csv")
tbl_PrjOffice <- read.csv("tbl_PrjOffice.csv")

tbl_prjPhase <- read.csv("tbl_prjPhase.csv")                 
tbl_prjStates <- read.csv("tbl_prjStates.csv")
tbl_PrjSucReport <- read.csv("tbl_PrjSucReport.csv")
tbl_Project_Fiscal_Years <- read.csv("tbl_Project_Fiscal_Years.csv")     

tbl_ProjectTracking <- read.csv("tbl_ProjectTracking.csv")
tbl_State <- read.csv("tbl_State.csv")                    
tbl_Sys_Config <- read.csv("tbl_Sys_Config.csv")    

list.of.data.frames <- list(tbl_Con_Nps_Areas, 
                            tbl_ConAllStates, 
                            tbl_CongDistricts, 
                            tbl_ConNCoop, 
                            tbl_ConOffice, 
                            tbl_ConSucReport,
                            tbl_Consultation,
                            tbl_Consultation_Fiscal_Years,
                            tbl_CustomizedDumpTable,
                            tbl_DumpTable,
                            tbl_Member,
                            tbl_Member_Office,
                            tbl_Member_State,
                            tbl_Nps_Areas,
                            tbl_Office,
                            tbl_Prj_Nps_Areas,
                            tbl_PrjApplicant,
                            tbl_PrjApplicantWebsite,
                            tbl_PrjCloseOutInfo,
                            tbl_PrjCongDistricts_Test,
                            tbl_PrjCooperator,
                            tbl_PrjDetailDocument,
                            tbl_PrjDetailInfo,
                            tbl_PrjDetailPartnerWebsite,
                            tbl_PrjDetailPhoto,
                            tbl_PrjNationalCooperator,
                            tbl_PrjNCoop,
                            tbl_PrjOffice,
                            tbl_prjPhase,
                            tbl_prjStates,
                            tbl_PrjSucReport,
                            tbl_Project_Fiscal_Years,
                            tbl_ProjectTracking,
                            tbl_State,
                            tbl_Sys_Config)

merged.data.frame = Reduce(function(...) merge(..., all=T), list.of.data.frames)

dat <- read.csv("ApplicantPartnerOut.csv", header=TRUE, sep=",")
ser <- read.csv("RTCA_FINANCIAL.csv")
head(ser)
head(dat)
listr <- c("Healthy Communities", "Large Landscapes", "Outdoor Recreation", "Rivers and Watersheds", "Transportation", "Urban", "Youth Engagement")

length(ser$OBJECTID)
length(ser$Project_ID)
dat <- cbind(ser$Project_ID, dat)
dat <- cbind(ser$OBJECTID, dat)
drops <- c("OBJECTID","Project_ID")
dat <- dat[,!(names(dat) %in% drops)]
head(dat)
colnames(dat)[1] <- "OBJECTID"
colnames(dat)[2] <- "Project_ID"
head(dat)
write.csv(dat, row.names = FALSE, "data.csv")
start <- read.csv("data.csv")
toy.df <- start[,2:11]
toy.df[1:20,]
complete = na.omit(toy.df)

toy.df[is.na(toy.df$Partner_Organization), c("Partner_Organization","Partner_Website","Contact_Name","Contact_Phone_Number","Contact_Email","Mailing_Address","City","State","Zip_Code")] =
  complete[sample(1:nrow(complete), size = sum(is.na(toy.df$Partner_Organization)), replace = TRUE),
           c("Partner_Organization","Partner_Website","Contact_Name","Contact_Phone_Number","Contact_Email","Mailing_Address","City","State","Zip_Code")]
toy.df
full <- cbind(start[,1],toy.df)
colnames(full)[1] <- "OBJECTID"
str(full)
write.csv(full, row.names=FALSE, "RTCA_APPLICANT_PARTNER.csv")

head(start)
listr <- c("National Park Foundation", "National Forest Foundation", 
           "Sonoran Institute", "Publilc Lands Partnership", 
           "Association of Partners for Public Lands", "Partners in Parks", 
           "Community and Ecosystem Stewardship","University of Michigan Collaboration",
           "Sustainable Communities Network","International Mountain Bicycling Association")
listw <- c("http://www.nationalparks.org/","http://www.nationalforests.org/",
           "http://www.sonoraninstitute.org/","http://publiclandspartnership.org/",
           "http://www.appl.org/i4a/pages/index.cfm?pageid=1","http://www.partnersinparks.org/",
           "http://ocs.fortlewis.edu/Stewardship/default.htm","http://www.snre.umich.edu/ecomgt//collaboration.htm",
           "http://www.sustainable.org/","https://www.imba.com/")

sample(listr,100, replace=TRUE)
require(plyr)
combined <- cbind(dat[c("OBJECTID","Project_ID")], as.data.frame(listr))
length(dat$Unit_Name)
dat$Category <- sample(listr, length(dat$Category), replace=TRUE)

listr <- c("Assist with Efforts", "Develop a master plan", "Facilitate Meetings", "Assist with engagement", "Identify management strategies", "Provide support", "Provide guidance")

dat$Definition  <- sample(listr, length(dat$Definition), replace=TRUE)
head(dat)


dat$Unit_Name  <- sample(listr, length(dat$Unit_Name), replace=TRUE)
dat$Fiscal_Year <- sample(1995:2015, length(dat$Fiscal_Year), replace=TRUE)
head(dat)
n=length(100:30000)
dat$Dollar_Amount <- sample(100:10000, length(dat$Dollar_Amount), replace=TRUE)

write.csv(dat, row.names=FALSE, "RTCA_SERVICE.csv")


