import pandas as pd
from pandas.core.indexes.base import Index

# S1 = pd.Series(['a','b','c','d'],index=[0,1,2,3])
# print(S1)

# # 传入字典，key为索引，value为数据
# print("传入字典：")
# S3 = pd.Series({1:'a',2:'b',3:'c',4:'d'})
# print(S3)

# print(S1.index)
# print(S3.index)
# print(S1.values)
# print(S3.values)


df1 = pd.DataFrame(['a','b','c','d'])
print(df1)

print("传入一个嵌套列表：")
df2 = pd.DataFrame([['a','A'],['b','B'],['c','C'],['d','D']])
print(df2)

print("传入一个嵌套列表，里面是元组：")
df2 = pd.DataFrame([('a','A'),('b','B'),('c','C'),('d','D')])
print(df2)
df4 = pd.DataFrame([('a','A'),('b','B'),('c','C'),('d','D')],columns=['小写','大写'],index=['1','2','3','4'])
print(df4)
df5 = pd.DataFrame({"小写":['a','b','c','d'],'大写':['A','B','C','D']},index=['1','2','3','4'])
print(df5)

print(df5.index)
print(df5.columns)