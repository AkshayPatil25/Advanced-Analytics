import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#To import without using python folder option
#Set directory 
import os
os.chdir(r"C:\akki_is_legend\Adv Analytics\Datasets")

car93=pd.read_csv("Cars93.csv")
print(car93.shape)
print(car93.columns)
print(car93.dtypes)
print(car93.info())

car93['Price'].mean()
car93['Price'].median()
car93['Price'].quantile(q=0.25)
car93['Price'].quantile(q=0.75)

car93['Price'].quantile(q=np.array([0.25,0.5,0.75]))

car93['Price'].plot(kind='box')
plt.show()

#Std deviation
car93['Price'].std()

#variance
car93['Price'].var()

#coefficient of variation
car93['Price'].std()/car93['Price'].mean()
 
#skewness
from scipy.stats import skew
skew(car93['Price'])
car93['Price'].skew()

#Kurtosis
#Fisher is scientist who made this formula
from scipy.stats import kurtosis
kurtosis(car93['Price'],fisher=True)
car93['Price'].kurtosis() 
#or you can use the formula car93['Price'].kurtosis()-3

































