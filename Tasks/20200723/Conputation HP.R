gdp<-read.csv('/Users/law/SASUniversityEdition/myfolders/Python/Tasks/20200723/gdp.csv')
library(mFilter)
gdp$Time<-ts(gdp$Time,start = 2000,end=2020,frequency = 4)
hp<-hpfilter(x = gdp$Time, freq = 4, type = "frequency", drift = TRUE)
write.csv(hp$cycle,file='hp.csv')