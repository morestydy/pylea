import pandas as pd

df = pd.read_excel(r"l9/Lesson9.xlsx")


df.index = ["0a","1b","2c","3d","4e"]
print(df)
df1 = df
# drop()函数,axis = 1 表示删除列
# 传入列名删除列
print(df.drop(["名称","顶踩比例"],axis=1))
# 传入列号删除列
print(df.drop(df.columns[[0,3]],axis=1))
# axis = 0 表示删除行
# 传入行名删除行
print(df.drop(['0a','2c'],axis=0))
# 传入行号删除行
print(df.drop(df.index[[0,2]],axis=0))


# 查看某个值出现的次数
print("查看顶踩比例中的数值的出现次数分布：")
print(df['顶踩比例'].value_counts())

print("查看顶踩比例中的数值出现的百分比：")
print(df['顶踩比例'].value_counts(normalize=True))


# Section3 获取唯一值
# 获取某列的非重复值
# 先把那列复制一份，然后用unique来获取
print("获取顶踩比例列中唯一值：")
print(df['顶踩比例'].unique())


# Section4 数值查找
# 可以是针对某列的，也可以是针对整张表格
# 只要是包含列表中其中一个就返回true
print("查看观看次数列有没有480和235：")
print(df['观看次数'].isin([480,235]))

print("查看全表中是否有480和235：")
print(df.isin([480,235]))

