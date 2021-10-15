import pandas as pd
from pandas.core.frame import DataFrame

df = pd.read_excel(r'l6/Lesson6.xlsx')
df1 = df
print(df)
print(df['名称'].dtype)
print('*'*30)
print(df.dtypes)
print(df['观看次数'].astype('float'))
print(df['观看次数'].dtype)
print('*'*15,'索引设置','*'*15)
df.index=[1,2,3,4,5]
# df.columns=[1,2,3,4,5]
print(df)
df = df1
df = df.set_index("观看次数")
print(df)
df = df1
df = df.rename(columns={'发布时间':'新发布时间'})
print(df)
df = df1
df = df.rename(index={1:'一',2:'二',3:'三'})
print(df)