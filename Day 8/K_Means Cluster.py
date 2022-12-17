from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

milk=pd.read_csv("milk.csv",index_col=0)

scaler=StandardScaler()
milkscaled=scaler.fit_transform(milk)

#WSS=Within sums of squares
wss=[]
for i in np.arange(2,10):
    km=KMeans(n_clusters=i,random_state=2022)
    km.fit(milkscaled)
    wss.append(km.inertia_)    
    
plt.scatter(np.arange(2,10),wss)
plt.plot(np.arange(2,10),wss)
plt.title("Scree Plot")
plt.xlabel("Ks")
plt.ylabel("WSS")
plt.show()

#Best CLuster
km=KMeans(n_clusters=4,random_state=2022)
km.fit(milkscaled)
labels=km.predict(milkscaled)

milk["Cluster"]=labels
milk.sort_values('Cluster',inplace=True)

#Calculating the Centroids
milk.groupby('Cluster').mean()

#Finding the best cluster based on Silhouette
sil=[]
for i in np.arange(2,10):
    km=KMeans(n_clusters=i,random_state=2022)
    km.fit(milkscaled)
    labels=km.predict(milkscaled)
    sil.append(silhouette_score(milkscaled,labels))
    
ks=np.arange(2,10)
i_max=np.argmax(sil) #argmax will give you max values index
best_k=ks[i_max]
print("Best K =",best_k)

#Nutrient.csv
nutrient=pd.read_csv("nutrient.csv",index_col=0)

nutrientscaled=scaler.fit_transform(nutrient)

sil=[]
for i in np.arange(2,10):
    km=KMeans(n_clusters=i,random_state=2022)
    km.fit(nutrientscaled)
    labels=km.predict(nutrientscaled)
    sil.append(silhouette_score(nutrientscaled,labels))

ks=np.arange(2,10)
i_max=np.argmax(sil) 
best_k=ks[i_max]
print("Best K =",best_k)

###RFM
rfm=pd.read_csv(r"C:\akki_is_legend\Adv Analytics\Day 8\Recency Frequency Monetary\rfm_data_customer.csv",index_col=0)
rfm=rfm.drop(['most_recent_visit'],axis=1)
rfm.columns

rfmscaled=scaler.fit_transform(rfm)

sil=[]
for i in np.arange(2,10):
    km=KMeans(n_clusters=i,random_state=2022)
    km.fit(rfmscaled)
    labels=km.predict(rfmscaled)
    sil.append(silhouette_score(rfmscaled,labels))

ks=np.arange(2,10)
i_max=np.argmax(sil) 
best_k=ks[i_max]
print("Best K =",best_k)

km=KMeans(n_clusters=best_k,random_state=2022)
km.fit(rfmscaled)
labels=km.predict(rfmscaled)
    
rfm["Cluster"]=labels
rfm.sort_values('Cluster',inplace=True)

rfm.groupby('Cluster').mean()

### Boston ####
boston=pd.read_csv("Boston.csv",index_col=0)

bostonscaled=scaler.fit_transform(boston)

sil=[]
for i in np.arange(2,10):
    km=KMeans(n_clusters=i,random_state=2022)
    km.fit(bostonscaled)
    labels=km.predict(bostonscaled)
    sil.append(silhouette_score(bostonscaled,labels))

ks=np.arange(2,10)
i_max=np.argmax(sil) 
best_k=ks[i_max]
print("Best K =",best_k)

km=KMeans(n_clusters=best_k,random_state=2022)
km.fit(bostonscaled)
labels=km.predict(bostonscaled)
    
boston["Cluster"]=labels
boston.sort_values('Cluster',inplace=True)

boston.groupby('Cluster').mean()

##########################################################

