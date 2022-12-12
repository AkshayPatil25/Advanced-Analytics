setwd("C:/akki_is_legend/Adv Analytics/Datasets")
pg=read.csv("PlantGrowth.csv")

t.test(pg$weight, mu=6 , alternative='t')

(mean(pg$weight)-6)/(sd(pg$weight)/sqrt(30))

t.test(pg$weight, mu=6 , alternative='g')

t.test(pg$weight, mu=6 , alternative='l')

co=read.csv("CO2.csv")
t.test(co$uptake, mu=30 , alternative='t')
t.test(co$uptake, mu=30, alternative='g')
t.test(co$uptake, mu=30 , alternative='l')

im=read.csv("Indometh.csv")
t.test(im$conc, mu=0.30 , alternative='t')
t.test(im$conc, mu=0.30 , alternative='g')
t.test(im$conc, mu=0.30 , alternative='l')

############################################################
library(tidyr)

eh=read.csv("Plaque.csv")

eh_pivot=pivot_wider(eh,id_cols=c("Id","product"),
                     names_from="trt",values_from="score")

P1=subset(eh_pivot,product=="P1")
t.test(P1$Before,P1$After,paired=T,alternative='g')

P2=subset(eh_pivot,product=="P2")
t.test(P2$Before,P2$After,paired=T,alternative='g')

P3<-subset(eh_pivot,product=="P3")
t.test(P3$Before,P3$After,paired=T,alternative='g')

#############################################################
co2<-read.csv("CO2.csv")
bartlett.test(co2$uptake ~ co2$Treatment)


