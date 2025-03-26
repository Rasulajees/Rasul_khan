import pandas as pd

d1=pd.read_csv('AI & DATA SCIENCE/DATA SETS/brain_tumor_dataset.csv')
d2=pd.read_csv('AI & DATA SCIENCE/DATA SETS/expenses.csv')
print(d1,'\n',d2,'\n')

datas=pd.concat([d1,d2])
datas.rename(columns={'sex':'Gender'},inplace=True)
print(datas,'\n')
"""print(datas.head(50))
print(datas.tail(50))"""

y=datas.isnull().sum()
print(y,'\n')
print(datas.fillna(0))

print(datas.loc[1411])
