import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

import os
os.chdir(r"C:\akki_is_legend\Adv Analytics\Datasets")

car93=pd.read_csv("Cars93.csv")
print(car93.info())

###Bar Plot
cts=car93['Type'].value_counts() #.value_counts() will give you frequency count
cts.plot(kind='bar')
plt.show()


cts=car93['Type'].value_counts() 
cts.plot(kind='bar')
plt.show()

#OR
#Matplotlib
plt.bar(cts.index,cts)
plt.show()

#Seaborn
cts1=cts.reset_index()
cts1.columns = ['Type', 'Count']
sb.barplot(data=cts1, x='Type', y='Count')
plt.show()

###Histogram
car93['Price'].plot(kind='hist',bins=8)
plt.show()

#Matplotlib
plt.hist(car93['Price'],bins=8)
plt.show()

#seaborn
sb.histplot(data=car93,x='Price',bins=8)
plt.show()

###Density plot / Distribution plot
car93['Price'].plot(kind='kde')
plt.show()

#Seaborn
sb.kdeplot(data=car93, x='Price')
plt.show()

###Scatter plot
car93.plot(kind='scatter',x='EngineSize',y='MPG.highway',color="airco")
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel("MPG.highway")
plt.show()

#Matplotlib
plt.scatter(car93['EngineSize'],car93['MPG.highway'])
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel("MPG.highway")
plt.show()


no_bags=car93[car93['AirBags']=="None"]
plt.scatter(no_bags['EngineSize'],no_bags['MPG.highway'],label="None")
driver=car93[car93['AirBags']=="Driver only"]
plt.scatter(driver['EngineSize'],driver['MPG.highway'],label="Driver only")
d_p=car93[car93['AirBags']=="Driver & Passenger"]
plt.scatter(d_p['EngineSize'],d_p['MPG.highway'],label="Driver & Passenger")
plt.legend(loc="best")
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel("MPG.highway")
plt.show()

#Seaborn
sb.scatterplot(data=car93,x="EngineSize",y="MPG.highway")
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel("MPG.highway")
plt.show()

sb.scatterplot(data=car93,x="EngineSize",y="MPG.highway",hue="AirBags")
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel("MPG.highway")
plt.show()


###Box Plot
car93['Price'].plot(kind='box')
plt.title("Box Plot")
plt.show()

#Matplotlib
plt.boxplot(car93["Price"])
plt.title("Box Plot")
plt.show()

#Seaborn
sb.boxplot(y="Price",data=car93)
plt.show()

sb.boxplot(x="AirBags",y="Price",data=car93)
plt.show()


###Facet Grid
g=sb.FacetGrid(car93,col="AirBags")
g=g.map(plt.scatter,"EngineSize","MPG.highway",color="Red")
plt.show()

g=sb.FacetGrid(car93,row="AirBags")
g=g.map(plt.scatter,"EngineSize","MPG.highway",color="Red")
plt.show()

###Sub Plot
plt.subplot(2,2,1)
sb.boxplot(data=car93['Price'])
plt.title("Box Plot")
plt.subplot(2,2,2)
sb.histplot(data=car93,x='Price',bins=8)
plt.title("Histogram")
plt.subplot(2,2,3)
sb.barplot(data=car93,x='AirBags',y='Price')
plt.title("Bar Plot")
plt.subplot(2,2,4)
sb.scatterplot(data=car93,x='EngineSize',y='MPG.highway')
plt.title("Scatter Plot")
plt.tight_layout()
plt.show()

###Joint Plot
sb.jointplot(data=car93,x="EngineSize",y="MPG.highway")
plt.xlabel("Engine Size")
plt.ylabel("MPG.highway")
plt.show()   

##Group By Aggregate
car93['Price'].mean()

no_bags=car93[car93['AirBags']=="None"]
driver=car93[car93['AirBags']=="Driver only"]
d_p=car93[car93['AirBags']=="Driver & Passenger"]
print(no_bags['Price'].mean())
print(driver['Price'].mean())
print(d_p['Price'].mean())

car93.groupby('AirBags')['Price'].mean()

#Bar Plot of Group By Aggregate
cts=car93.groupby('AirBags')['Price'].mean()
cts1=cts.reset_index()
sb.barplot(data=cts1,x='AirBags',y='Price')
plt.ylabel("Mean Price")
plt.show()







