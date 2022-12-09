from scipy.stats import poisson
import numpy as np

##Accidents

#a) exactly 5 accidents p[x=5]
poisson.pmf(5,12)

#b) at most 12 accidents p[x<=12]
poisson.cdf(12,12)

#c) at least 15 accidents p[x>14]
poisson.sf(14,12)

#d) between 10 and 15 accidentsp[10<=x<=15]
ks=np.arange(10,16)
s=0
for i in ks:
    s=s+poisson.pmf(i,12)
print(s)

#OR

#d) p[x<=15]-p[x<=9]
poisson.cdf(15,12)-poisson.cdf(9,12)

###################################################

#Q1) Calls /Customer Care
#a)p[x>70]
poisson.sf(70,56)

#b)p[x<20]
poisson.cdf(19,56)

###################################################

#Q2) Customer  Served
#a)p[x>5]
poisson.sf(5,4)

#b)p[x<3]
poisson.cdf(2,4)

