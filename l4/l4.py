import pandas as pd

df = pd.read_excel(r"E:/learning/py/exercise/l4/Lesson4.xlsx")
print("1.excel的数据是","*"*15)
print(df,"\n")
df2 = pd.read_excel(r"E:/learning/py/exercise/l4/Lesson4.xlsx",index_col=0)
print("2.excel的数据是","*"*15)
print(df2,"\n")

df2 = pd.read_excel(r"E:/learning/py/exercise/l4/Lesson4.xlsx",usecols=[0,3])
print(df2)

print('*'*10,'读取csv','*'*10)
df3 = pd.read_csv(r'l4/Lesson4_csv.csv')
print(df3)
print('*'*10,'读取csv','*'*10)
df3 = pd.read_csv(r'l4/Lesson4_csv_blank.csv')
print(df3)
print('*'*10,'读取csv','*'*10)
df3 = pd.read_csv(r'l4/Lesson4_csv_blank.csv',sep=' ')
print(df3)
print('*'*10,'读取csv','*'*10)
df3 = pd.read_csv(r'l4/Lesson4_csv_blank.csv',sep=' ',nrows=2)
print(df3)

print('*'*10,'读取TXT','*'*10)
df4 = pd.read_table(r'l4/Lesson4_csv_blank.txt',sep=' ')
print(df4)

print(df4.head(3))
print("数据分布:")
print(df4.describe(),'\n')
print("-"*30 + "End Section 2 熟悉数据" + "-"*30)

