import numpy as np
import pandas as pd

df = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [444, 555, 666, 444],
    'col3': ['abc', 'def', 'ghi', 'xyz']
})

print(df.head())
df['col2'].unique()
df['col2'].nunique()
len(df['col2'].unique())
df['col2'].value_counts()
df[df['col1']>2]
df['col1']>2
(df['col1']>2).sum()
df[(df['col1']>2)&(df['col2']==444)]
def times2(x):
    return x*2
df['col1'].sum()
df['col1'].apply(times2) #逐个元素执行
df['col1'].apply(lambda x:x*2) #lambda临时函数
df.drop('col1',axis=1, inplace= True)
df.columns
df.index
df
df.sort_values(by = 'col2')
df.isnull()

data = {
    'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
    'B': ['one', 'one', 'two', 'two', 'one', 'one'],
    'C': ['x', 'y', 'x', 'y', 'x', 'y'],
    'D': [1, 3, 2, 5, 4, 1]
}

df = pd.DataFrame(data)

print(df)
df.pivot_table(values = 'D', index=['A','B'], columns=['C'])

####
import os
print(os.getcwd())
#1
pd.read_csv('example.csv')
df.to_csv('x',index=False) #把 DataFrame → 写成文件
#2
pd.read_excel('excel.xlsx',sheetname = 'sheet1')
df.to_excel('excel.xlsx',sheet_name='newsheet')
#3
data = pd.read_html('http://...')
data[0]
#4
from sqlalchemy import create_engine
engine = create_engine('sqlite:///')
df.to_sql('my_tanle',engine)
sqldf = pd.read_sql('my_table', con=engine)
