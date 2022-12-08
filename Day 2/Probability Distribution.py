import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

import os
os.chdir(r"C:\akki_is_legend\Adv Analytics\Datasets")

car93=pd.read_csv("Cars93.csv")
print(car93.info())

car93['Type'].value_counts(normalize=True)

car93['AirBags'].value_counts(normalize=True)

pd.crosstab(car93['Type'],car93['AirBags'],normalize='index',
            margins=True)

pd.crosstab(car93['Type'],car93['AirBags'],normalize='all',

            margins=True)
