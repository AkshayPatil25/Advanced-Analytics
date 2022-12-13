import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
#############################################################################
# Yield.csv
#Anova

agr= pd.read_csv("Yield.csv")

agr_ols=ols('Yield ~ Treatments', data=agr).fit()

table = anova_lm(agr_ols,typ=2)
print(table)


############################################################################
# Post Hoc Tukey HSD
compare = pairwise_tukeyhsd(agr['Yield'],agr['Treatments'],alpha=0.05)

dd = pd.DataFrame(compare._results_table.data)
dd

agr.groupby('Treatments')['Yield'].mean()

############################################################################
# PlantGrowth

agr= pd.read_csv("PlantGrowth.csv")

agr_ols=ols('weight ~ group', data=agr).fit()

table = anova_lm(agr_ols,typ=2)
print(table)
#-------------------------------------------------------------
# Post Hoc Tukey HSD
compare = pairwise_tukeyhsd(agr['weight'],agr['group'],alpha=0.05)

dd = pd.DataFrame(compare._results_table.data)
dd

agr.groupby('group')['weight'].mean()

#############################################################################

# Train

agr=pd.read_csv("train.csv")

agr['Item_Type'].unique()

agr_ols=ols('Item_Outlet_Sales ~ Item_Type', data=agr).fit()

table = anova_lm(agr_ols,typ=2)
print(table)
