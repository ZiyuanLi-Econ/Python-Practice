import numpy as np
import pandas as pd
np.array([[1,2,3],[4,5,6]])
np.arange(0,10)
np.arange(0,10,2)
np.linspace(0,10,2)
np.zeros(1).shape
np.ones(100).reshape(10,10)
np.eye(1)
np.random.rand(5,5)
np.random.randn(2,5,5)
arr = np.random.randint(2,100,4).reshape(2,2)
arr.argmax()
np.sum(arr,axis = 0,keepdims=True)
np.max(arr)
arr[0:2,0:2]
arr[0:2,0:2] = 100
ser=pd.Series(data=[1,2,3],index=['a','b','c'])
ser['a']
ser[ser==1]
ser.iloc[1]
np.random.seed(5555)
from numpy.random import randn
df=pd.DataFrame(randn(4,4),['A','B','C','D'],['Q','W','E','R'])
df
df['Q']
df[['Q','W']]
df['T']=df['Q']+df['W']
df.drop('T',axis = 1, inplace=True)
df.iloc[0]
df.loc['A','W']
df.loc[['A','C'],['Q','E']]
#
arr = np.linspace(10,30,3)
ser = pd.Series(data=arr,index=['a','b','c'])
ser.loc['b']
ser['b']
ser.iloc[1]
pd.Series(['a','b','c'])
df = pd.DataFrame(np.random.randn(4,4),['A','B','C','D'],['Q','W','E','R']) 

#pandas conditional selection
df >0
(df>0).values.sum()
(df>0).sum().sum()
booldf = df>0
df[booldf]
df[df>0]
(df['W']>0).sum()
df['W']>0
df[df['W']>0]
df[df['W']>0][['Q','E']]
df.loc[df['W']>0,['Q','E']]
#==df.loc[df['W']>0,['Q','E']]
boolster = df['W']>0
result = df[boolster]
result[['Q','E']]
df[(df['W']>0) & (df['E']>0)]
df[(df['W']>0) | (df['E']>0)]
df.reset_index()
newind = ' NY WY OR CO'.split()
newind
df['states']=newind
df.set_index('states')
