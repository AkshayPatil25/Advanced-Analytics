import pandas as pd
from scipy.stats import ttest_1samp
from scipy.stats import ttest_rel
from scipy.stats import bartlett,ttest_ind


pg=pd.read_csv("PlantGrowth.csv")

ttest_1samp(pg['weight'],popmean=6,alternative="two-sided")

ttest_1samp(pg['weight'],popmean=6,alternative="greater")

ttest_1samp(pg['weight'],popmean=6,alternative="less")

#################################################################

###CO2

co=pd.read_csv("CO2.csv")

ttest_1samp(co['uptake'],popmean=30,alternative="two-sided")


ttest_1samp(co['uptake'],popmean=30,alternative="greater")

##This is correct
ttest_1samp(co['uptake'],popmean=30,alternative="less")

#################################################################

###Indometh

im=pd.read_csv("Indometh.csv")

ttest_1samp(im['conc'],popmean=0.30,alternative="two-sided")

##this is correct               
ttest_1samp(im['conc'],popmean=0.30,alternative="greater")

ttest_1samp(im['conc'],popmean=0.30,alternative="less")

###############################################################
an=pd.read_csv("anorexia.csv")

cont=an[an['Treat']=='Cont']
ttest_rel(cont['Prewt'],cont['Postwt'], alternative="less")

ttest_rel(cont['Prewt'],cont['Postwt'], alternative="greater")

ttest_rel(cont['Prewt'],cont['Postwt'], alternative="two-sided")
###############################################################

###Plaque

pl=pd.read_csv("Plaque.csv")
pl_pivot=pd.pivot_table(pl,index=['Id','product'],columns='trt',values='score')

pl_pivot=pl_pivot.reset_index()

P1=pl_pivot[pl_pivot['product']=="P1"]
ttest_rel(P1['Before'],P1['After'],alternative="greater")

#########################################################
chill=co[co['Treatment']=="chilled"]
nonchill=co[co['Treatment']=="nonchilled"]

bartlett(chill['uptake'],nonchill['uptake'])
