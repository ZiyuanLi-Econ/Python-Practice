import numpy as np
import pandas as pd

np.random.seed(42)

df = pd.DataFrame(
    np.random.randn(5,4),
    index=['A','B','C','D','E'],
    columns=['Q','W','E','R']
)

ser1 = pd.Series([1,2,3,4], ['A','B','C','D'])
ser2 = pd.Series([10,20,30,40], ['B','C','D','E'])

df
ser1
ser2

#
ser1['C']
ser1.iloc[3]
ser1[ser1>2]
ser1[ser1==2]
ser1+ser2
df['Q']
df[['Q','W']]
df.loc['B']
df.loc[['A','B']]
df.iloc[2]
df.loc['C','E']
df.loc[['A','B'],['Q','W']]
df['T']=df['Q']+df['W']
df.drop('T',axis=1,inplace=True)
df
df['Z']=df['Q']*2
df.loc['Z']=df.loc['C']+df.loc['B']
df>0
(df>0).sum(axis=1).sum()
df[df>0]
df.loc[df['W']>0,['Q','E']]
df[(df['W']>0)&(df['E']>0)]
df.set_index('Q')
df = df.drop('E')
df.drop('E',inplace=True)
outside = ['g1','g1','g1','g2','g2','g2']
inside = [1,2,3,1,2,3]
x = pd.MultiIndex.from_tuples(list(zip(outside,inside)))
mmnn = pd.DataFrame(np.random.randn(6,2),x,['A','B'])
mmnn = pd.DataFrame(np.random.randn(6,2),index = x, columns = ['A','B'])
mmnn.index.names=['groups','numbers']
mmnn.loc['g2']
mmnn.loc['g2','A']
mmnn.xs(1,level='numbers')
mmnn.xs('g2',level='groups')['A']
mmnn.xs('g2',level='groups').loc[2]
mmnn.loc(1,level='numbers')
mnn = mmnn[mmnn>0]
mnn
mnn.dropna(thresh=1)
mnn.dropna(axis=1)
mnn.fillna(value=mnn.xs(1,level='numbers').sum())

#groupby
data = {
    'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
    'Sales': [200, 120, 340, 124, 243, 350]
}
data
data = pd.DataFrame(data)
data.index.names=['Nr']
df = data.groupby('Company').sum()
df = data.groupby('Company')
data.groupby('Company')['Sales'].mean()
data.groupby('Company').mean(numeric_only=True)
df.mean(numeric_only=True)
df.std(numeric_only=True).loc[['FB','GOOG']]
df.count()
df.min()
df.describe()
df.describe().transpose()

#merging,joining,concatenating
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
}, index=[0, 1, 2, 3])

df2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7']
}, index=[4, 5, 6, 7])

df3 = pd.DataFrame({
    'A': ['A8', 'A9', 'A10', 'A11'],
    'B': ['B8', 'B9', 'B10', 'B11'],
    'C': ['C8', 'C9', 'C10', 'C11'],
    'D': ['D8', 'D9', 'D10', 'D11']
}, index=[8, 9, 10, 11])

df1
df2
df3
pd.concat([df1,df2,df3])
pd.concat([df1,df2,df3],axis=1).fillna(value=1)

#merge
left = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

right = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

left
right
pd.merge(right,left,how='left',on='key')


left = pd.DataFrame({
    'key1': ['A','A','B'],
    'key2': ['X','Y','X'],
    'value1': [1,2,3]
})

right = pd.DataFrame({
    'key1': ['A','A','B'],
    'key2': ['X','X','X'],
    'value2': [10,20,30]
})
left
right
pd.merge(left,right,how='outer',on=['key1','key2'])
left.join(right)
left.set_index('key').join(right.set_index('key'))
#merge = 按“column行”对齐. join = 按“index”列对齐

left = pd.DataFrame({
    'key': ['K0','K1','K2'],
    'A': ['A0','A1','A2']
})

right = pd.DataFrame({
    'key': ['K0','K1','K3'],
    'B': ['B0','B1','B3']
})
left
right
pd.merge(left, right, on='key', how='left')
left.set_index('key').join(right.set_index('key'))
