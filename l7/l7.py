import pandas as pd

df = pd.read_excel('l7/Lesson7.xlsx')
print(df)
df.index = ["一","二","三","四","五"]
print("读入的表格内容为：")
print(df,'\n')
# 只选择名称列
print("只选择了名称列：")
print(df["名称"],'\n')
print(df[['名称','观看次数']])

print("通过第几列来选择：")
print(df.iloc[:,[0,2]])
print(df.iloc[0:3,])

print(df.loc['一'])
print(df.iloc[1])


print(df[(df['观看次数']>300) & (df['评论数']>20)])

print(df.loc[['一','三'],['名称','观看次数']])

print(df.iloc[[0,1],[1,2]])

print(df[(df['观看次数']>300)&(df['评论数']>20)][['评论数','观看次数']])