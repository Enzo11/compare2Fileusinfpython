import pandas as pd

import numpy as np

dfmay = pd.read_excel('files/1.xlsx'
)

dfjune = pd.read_excel('files/2.xlsx'
)

#print(dfmay.equals(dfjune))

comparevalues = dfmay.values == dfjune.values

print(comparevalues)

rows,cols = np.where(comparevalues==False)

for item in zip(rows,cols):
    dfmay.iloc[item[0],item[1]] = ' {} --> {} '.format(dfmay.iloc[item[0], item[1]], dfjune.iloc[item[0],item[1]])


dfmay.to_excel('files/output.xlsx', index=False,header=True)
