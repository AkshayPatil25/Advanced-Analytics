import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

pizza=pd.read_csv("pizza.csv")

lr=LinearRegression()

x=pizza[['Promote']]
y=pizza['Sales']

lr.fit(x,y)
print(lr.intercept_)
print(lr.coef_)

#Yi^
y_pred=lr.predict(x)
y_pred

##############################
#This=
num=np.sum((y-y_pred)**2)
den=np.sum((y-y.mean())**2)
1-(num/den)
#Or
#This=
print(r2_score(y,y_pred))
##############################
##Insure Auto
#y=operating cost x=home find r^2

insure=pd.read_csv("Insure_auto.csv")

x=insure[['Home']]
y=insure['Operating_Cost']
lr.fit(x,y)
y_pred=lr.predict(x)
print(r2_score(y,y_pred))

#y=operating cost x=automobile find r^2

insure=pd.read_csv("Insure_auto.csv")

x=insure[['Automobile']]
y=insure['Operating_Cost']
lr.fit(x,y)
y_pred=lr.predict(x)
print(r2_score(y,y_pred))

#Combined r^2
x=insure[['Home','Automobile']]
y=insure['Operating_Cost']
lr.fit(x,y)
print(lr.intercept_)
print(lr.coef_)
y_pred=lr.predict(x)
print(r2_score(y,y_pred))

#########################################
###Boston

boston=pd.read_csv("Boston.csv")
 
x=boston.drop('medv',axis=1) #OR x=boston.iloc[:,:-1] 
y=boston['medv']
lr.fit(x, y)
print(lr.intercept_)
print(lr.coef_)
y_pred=lr.predict(x)
print(r2_score(y,y_pred))
