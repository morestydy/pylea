import pandas as pd

df = pd.read_excel(r'l8/Lesson8.xlsx')
df1 = df
print(df)

df['顶踩比例'] = df['顶踩比例'].replace(2.000,1.000)
print(df)

df = df.replace(1.000,2.000)
print(df)

df=df1

df = df.replace([480,342],1214)
print(df)

df = df1
df = df.replace({480:400,342:300})
print(df)

print("*"*15,'-'*5,"*"*15)
print(df.sort_values(by='观看次数',ascending=False))
print(df.sort_values(by='观看次数',ascending=True))
df=df1
df.loc[[1], ['发布时间']] = None
print(df)

print(df.sort_values(by='发布时间',ascending=False,na_position='first'))

print(df.sort_values(by=['顶踩比例','观看次数'],ascending=[False,True]))

# 用rank(ascending,method)函数进行排名
# ascending表明是升序还是降序，method有average、first、min、max 这4种取值
# 按照顶踩比例，降序排列
df = df1
print(df['顶踩比例'].sort_values(ascending=False))


print(df['顶踩比例'].rank())
print(df['顶踩比例'].rank(method="average",ascending=False))
print(df['顶踩比例'].rank(method="max",ascending=False))

