import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

import os
os.chdir(r"C:\akki_is_legend\Adv Analytics\Datasets")

house=pd.read_csv("Housing.csv")

#1)skew
from scipy.stats import skew
skew(house['price'])
house['price'].skew()

#kurtsis
from scipy.stats import kurtosis
kurtosis(house['price'],fisher=True)
house['price'].kurtosis() 

#Histogram
sb.histplot(data=house,x='price',bins=8)
plt.show()

#2)Scatter Plot
sb.scatterplot(data=house,x='lotsize',y='price',hue='airco')
plt.show()


#3)Box Plot : Lotsize by bedrooms
sb.boxplot(x='bedrooms',y='lotsize',data=house)
plt.show()

#Box Plot : Price by bathrooms
sb.boxplot(x='bathrms',y='price',data=house)
plt.show()

#4)subplots
plt.subplot(2,2,1)
sb.boxplot(data=house['price'])
plt.subplot(2,2,2)
sb.histplot(data=house,x='price',bins=15)
plt.subplot(2,2,3)
sb.scatterplot(data=house,x='lotsize',y='price',hue='bedrooms')
plt.subplot(2,2,4)
cts=house['bathrms'].value_counts()
cts.plot(kind='bar')
plt.tight_layout()
plt.show()

#5)Facet Grid
g=sb.FacetGrid(house,col="bathrms")
g=g.map(plt.scatter,"lotsize","price",color="Red")
plt.show()

#6)Joint Plot
sb.jointplot(data=house,x="lotsize",y="price",color=("Red"))
plt.title("Joint Plot")
plt.xlabel("Size of Lots")
plt.ylabel("Price")
plt.show() 
