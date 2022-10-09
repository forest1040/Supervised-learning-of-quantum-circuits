import pandas as pd
import numpy as np

df = pd.read_csv('qdata/output_N11_P100.dat')
#df.iloc[1] = np.nan
#print(df)

u = df['value'].unique()
print(len(u))

# u = df.nunique(dropna=False)
# print(u)
