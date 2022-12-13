#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency


# In[3]:


car= pd.read_csv("C:/akki_is_legend/Adv Analytics/Datasets/Cars93.csv")
car


# In[5]:


# Question 1 Is price influanced by type ? 
# Using Anova

car_ols=ols('Price ~ Type', data=car).fit()


# In[7]:


table = anova_lm(car_ols,typ=2)
print(table)

# P_value is less than Alpha


# In[8]:


# Question 2 Is price influanced by AirBags ?
# Using Anova

car_ols=ols('Price ~ AirBags', data=car).fit()
table = anova_lm(car_ols,typ=2)
print(table)

# P_value is less than Alpha


# In[9]:


# Question 3 Is price influanced by DriveTrain ?
# Using Anova

car_ols=ols('Price ~ DriveTrain', data=car).fit()
table = anova_lm(car_ols,typ=2)
print(table)


# P_value is less than Alpha


# In[19]:


# Question 4 Are Type and Airbags related ?
# Chi-Square Test

ctab=pd.crosstab(car['Type'],car['AirBags'])

test_statistics,p_value,df,expected_frequencies=chi2_contingency(ctab)
print(p_value)


# In[20]:


# Question 5 Are Type and DriveTrain related ?
# Chi-Square Test

ctab=pd.crosstab(car['Type'],car['DriveTrain'])

test_statistics,p_value,df,expected_frequencies=chi2_contingency(ctab)
print(p_value)


# In[21]:


# Question 6 Are Type and Origin related ?
# Chi-Square Test

ctab=pd.crosstab(car['Type'],car['Origin'])

test_statistics,p_value,df,expected_frequencies=chi2_contingency(ctab)
print(p_value)

