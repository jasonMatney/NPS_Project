rm(list=ls())
require(devtools)
install_github('likert', 'jbryer')
require(likert) 
as.numeric.factor <- function(x) {as.numeric(levels(x))[x]}
ls("package:likert")

setwd("/Users/jason/Desktop/Data")
list.files()
rtca <- read.csv("Likert_NoResponse.csv", header=TRUE)
full_response <- read.csv("RTCA_September_25_2C_2017_08_22/RTCA_September_25_2017_08_22.csv")
numeric_likert <- read.csv("raw_likert_data.csv",header = TRUE)
# head(as.data.frame(full_response$Q3))
full_response.dat <- full_response[3:21,] # get just the responses
full_response.dat <- full_response.dat[-c(1, 10),] # remove test and non-response
full_response.dat <- full_response.dat[-c(13,14,15),]# remove non-response likert
full_response.dat[,"wilcox_grouping"] <- c(1,0,1,1,0,1,1,0,0,1,1,1,1,0) # make groups of 1's and 0's


numeric_likert_wilcox <- cbind(numeric_likert,full_response.dat[,c(41)]) # add grouping variable
colnames(numeric_likert_wilcox)[13] <- "wilcox_grouping"
wilcox.test(Q7_1 ~ wilcox_grouping, data=numeric_likert_wilcox)
            
## Multiple Wilcoxon rank sum tests for time, age, frail between genders.
likert_columns <- c("Q7_1","Q7_2","Q7_3","Q7_4","Q7_5","Q7_6","Q7_7","Q7_8","Q7_9","Q7_10","Q7_11","Q7_12")
lapply(numeric_likert_wilcox[,likert_columns], function(x) wilcox.test(x ~ wilcox_grouping, data = numeric_likert_wilcox))
group_1_likert <- numeric_likert_wilcox[numeric_likert_wilcox[,"wilcox_grouping"]==1,] # has used all apps
group_2_likert <- numeric_likert_wilcox[numeric_likert_wilcox[,"wilcox_grouping"]==0,] # has not used all apps

summary(numeric_likert_wilcox)
summary(group_1_likert)
summary(group_2_likert)
#group1_likert <- group1[,24:35] # get just the likert responses for group 1
#group2_likert <- group2[,24:35] # get just the likert responses for group 2
# 
# likert.levels <- c(7, 6, 5, 4, 3, 2, 1)
# 
# # Here we will recode each factor and explicitly set the levels
# for(i in seq_along(full_response.likert)) {
#   full_response.likert[,i] <- factor(full_response.likert[,i], levels=likert.levels)
# }

rtca
sapply(rtca, class) #Verify that all the columns are indeed factors
sapply(rtca, function(x) { length(levels(x)) } ) # The number of levels in each factor
rtcalevels <- c("Strongly disagree", "Somewhat disagree", "Disagree", "Neither agree nor disagree", "Somewhat agree", "Agree", "Strongly agree")

# Here we will recode each factor and explicitly set the levels
for(i in seq_along(rtca)) {
  rtca[,i] <- factor(rtca[,i], levels=rtcalevels)
}



rtca_lik <- likert(rtca)
summary(rtca_lik)

plot(rtca_lik,centered=FALSE, plot.percent.neutral=FALSE)
plot(rtca_lik,  centered=FALSE, group.order=(c("Q7_1","Q7_2","Q7_3","Q7_4","Q7_5","Q7_6","Q7_7","Q7_8","Q7_9","Q7_10","Q7_11", "Q7_12")), plot.percent.neutral=FALSE)

wilcox.test(mpg ~ am, data=mtcars) 

#------------------------
rtca_grouped <- rtca
rtca_grouped[,"wilcox_grouping"] <- c(1,0,1,1,0,1,1,0,0,1,1,1,1,0)

group_1 <- rtca_grouped[which(rtca_grouped$wilcox_grouping==1),]
group_2 <- rtca_grouped[which(rtca_grouped$wilcox_grouping==0),]

drops <- c("wilcox_grouping")
group_1_likert <- group_1
group_1_likert <- group_1_likert[ , !(names(group_1_likert) %in% drops)]
group_1_likert_Q5 <- group_1_likert$Q7_5
group_1_likert_Q11 <- group_1_likert$Q7_11 

group_2_likert <- group_2
group_2_likert <- group_2_likert[ , !(names(group_2_likert) %in% drops)]
group_2_likert_Q5 <- group_2_likert$Q7_5
group_2_likert_Q11 <- group_2_likert$Q7_11 

library(plyr)
Q5.1.df <- as.data.frame(group_1_likert_Q5)
Q5.2.df <- as.data.frame(group_2_likert_Q5)
Q5_combined <- rbind.fill(Q5.1.df, Q5.2.df)
plot(likert(Q5_combined), plot.percent.neutral=FALSE)

Q11.1.df <- as.data.frame(group_1_likert_Q11)
Q11.2.df <- as.data.frame(group_2_likert_Q11)
Q11_combined <- rbind.fill(Q11.1.df, Q11.2.df)
plot(likert(Q11_combined), plot.percent.neutral=FALSE)




