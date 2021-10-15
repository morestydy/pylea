import pandas as pd
import datetime

df = pd.read_excel(r'l5/Lesson5.xlsx')
print(df)
print(df.info(),'\n')
print(df.isnull(),'\n')
print(df.dropna(),'\n')
# print(df.dropna(how='all'),'\n')
print(df.fillna(0),'\n')
print(df.fillna(0),'\n')
dataTime_p = datetime.datetime.strptime('2020/7/20 00/00/00',r'%Y/%m/%d %H/%M/%S')
print(df.fillna({'顶踩比例':0,'发布时间':dataTime_p}))

print('*'*15,'重复值删除处理','*'*15)
df1 = pd.read_excel(r'l5/Lesson5.xlsx',sheet_name='Sheet2')
print(df1)
print(df1.drop_duplicates(subset='名称',keep='first'))
print(df1.drop_duplicates(subset=['名称','观看次数']))

