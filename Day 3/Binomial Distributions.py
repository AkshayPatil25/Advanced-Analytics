from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

binom.pmf(k=5,n=40,p=0.25)

##Customer
ks=np.arange(0,11)
s=0
for i in ks:
    s=s+binom.pmf(k=i,n=40,p=0.25)
print(s)

#OR

binom.cdf(k=10,n=40,p=0.25)

binom.sf(k=19,n=40,p=0.25)

binom.stats(n=40,p=0.25)

###Prob Plot

ks=np.arange(0,21)
probs=binom.pmf(ks,n=20,p=0.25)
plt.bar(ks,probs)
plt.xlabel("Ks")
plt.ylabel("PMF")
plt.show()

###########################################################

#Question 1) Disease
#a)p[x=5]
binom.pmf(k=5,n=20,p=0.15)
#b)p[x>12]
binom.sf(k=12,n=20,p=0.15)
#c)p[x<=10]
binom.cdf(k=10,n=20,p=0.15)
    
#Question 2) Worker
#a)p[x=0 i.e none]
binom.pmf(k=0,n=20,p=0.35)
#b)p[x=10]
binom.pmf(k=10,n=20,p=0.35)
#c)p[x<=10]
binom.cdf(k=10,n=20,p=0.35)
#d)p[x>13]
binom.sf(k=13,n=20,p=0.35)
