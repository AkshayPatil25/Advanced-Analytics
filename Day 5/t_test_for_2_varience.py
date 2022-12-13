import pandas as pd
from scipy.stats import ttest_1samp
from scipy.stats import ttest_rel
from scipy.stats import bartlett,ttest_ind


co=pd.read_csv("CO2.csv")
chill=co[co['Treatment']=="chilled"]
nonchill=co[co['Treatment']=="nonchilled"]

bartlett(chill['uptake'],nonchill['uptake'])

ttest_ind(chill['uptake'],nonchill['uptake'],equal_var=True)

#########################################################################
# Puromycin
pm=pd.read_csv("Puromycin.csv")

treated=pm[pm['state']=="treated"]

untreated=pm[pm['state']=="untreated"]

bartlett(treated['rate'],untreated['rate'])

ttest_ind(treated['rate'],untreated['rate'],equal_var=True)

########################################################################
#  Soporific

p=pd.read_csv("Soporific.csv")

sopl1=p[p['Drug A']=="sopl1"]

sopl2=p[p['Drug B']=="sopl2"]

bartlett(p['Drug A'],p['Drug B'])

ttest_ind(p['Drug A'],p['Drug B'],equal_var=True)

########################################################################
# Housing 

housing=pd.read_csv("Housing.csv")

prefered = housing[housing['prefarea']=='yes']

no_prefered = housing[housing['prefarea']=='no']

bartlett(prefered['price'],no_prefered['price'])

ttest_ind(prefered['price'],no_prefered['price'],
          alternative='greater',equal_var=True)

housing.groupby('prefarea')['price'].mean()

#----------------------------------------------------------------------
# Airco
housing=pd.read_csv("Housing.csv")
prefered = housing[housing['airco']=='yes']

no_prefered = housing[housing['airco']=='no']

bartlett(prefered['price'],no_prefered['price'])

ttest_ind(prefered['price'],no_prefered['price'],
          alternative='greater',equal_var=True)


housing.groupby('airco')['price'].mean()

########################################################################

# Gas
housing=pd.read_csv("Housing.csv")
gas = housing[housing['gashw']=='yes']

no_gas = housing[housing['gashw']=='no']

bartlett(gas['price'],no_gas['price'])

ttest_ind(gas['price'],no_gas['price'],
          alternative='greater',equal_var=True)


housing.groupby('gashw')['price'].mean()


#######################################################################
# Car93  
# Origin
car=pd.read_csv("Cars93.csv")

usa=car[car['Origin']=='USA']
non_usa=car[car['Origin']=='non-USA']

bartlett(usa['Price'],non_usa['Price'])

ttest_ind(usa['Price'],non_usa['Price'],
          alternative='greater',equal_var=True)

car.groupby('Origin')['Price'].mean()

# Note : Mean of prices  

########################################################################
# Transmission 
cars=pd.read_csv("Cars93.csv")

manual=cars[cars['Man.trans.avail']=='Yes']
no_manual=cars[cars['Man.trans.avail']=='No']

bartlett(manual['Price'],no_manual['Price'])

ttest_ind(manual['Price'],no_manual['Price'],equal_var=True)

cars.groupby('Man.trans.avail')['Price'].mean()
#######################################################################
