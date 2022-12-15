import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a=np.array([2,5,6,7,10])
b=np.array([30,24,20,17,7])
#Variance Covariance Matrix
np.cov(a,b)

pizza=pd.read_csv("pizza.csv")

pizza['Promote'].cov(pizza['Sales'])

#Variance Covariance Matrix
np.cov(pizza['Promote'],pizza['Sales'])
pizza.cov()

# Correlation
pizza['Promote'].corr(pizza['Sales'])

pizza['Promote'].corr(pizza['Promote'])

#Correlation matrix
pizza.corr()
np.corrcoef(pizza['Promote'],pizza['Sales'])

# Scatter Plot
sns.scatterplot(data=pizza,x='Promote',y='Sales')
plt.show()

###Insure Auto
insure=pd.read_csv("Insure_auto.csv")

#Correlation of Home and Automobile
np.corrcoef(insure['Home'],insure['Automobile'])
insure['Home'].corr(insure['Automobile'])

#Correlation of Home and Operating_Cost
np.corrcoef(insure['Home'],insure['Operating_Cost'])
insure['Home'].corr(insure['Operating_Cost'])

#Correlation of Operating_Cost and Automobile
np.corrcoef(insure['Operating_Cost'],insure['Automobile'])
insure['Operating_Cost'].corr(insure['Automobile'])

#Heatmap
sns.heatmap(
    insure.corr(),
    xticklabels=insure.corr().columns,
    yticklabels=insure.corr().columns,
    annot=True ##Write False to only see the colours
    )
plt.show()

#Pair plot
sns.pairplot(insure)
plt.show()

#Pair plot with density graph in diagonal (kde=density graph) 
sns.pairplot(insure,diag_kind='kde')
plt.show()

###Iris
iris=pd.read_csv("iris.csv")

sns.heatmap(
    iris.corr(),
    xticklabels=iris.corr().columns,
    yticklabels=iris.corr().columns,
    annot=True
    )
plt.show()

### Boston
boston=pd.read_csv("Boston.csv")

sns.heatmap(
    boston.corr(),
    xticklabels=boston.corr().columns,
    yticklabels=boston.corr().columns,
    annot=True
    )
plt.tight_layout()
plt.show()


