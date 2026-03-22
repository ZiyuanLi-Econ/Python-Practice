import numpy as np
import pandas as pd
np.array([[1,2,3],[4,5,6]])
np.arange(1,7).reshape(2,3)
np.linspace(1,7,6)
np.zeros((10,10))
np.ones((5,5))
np.eye(10)
arr = np.random.rand(10) *10 - 5 
arr = arr.reshape(2,5)
arr>0
arr[arr>0]
sum(arr>0)
arr.shape
arr.argmax()
arr.argmax() - arr.argmin()
np.sum(arr,axis=0)
np.sum(arr,axis=1,keepdims=True)
arr[1]
arr[1,1]
arr[0:1,2:4]
arrcopy=arr.copy()

#####
ser = pd.Series([4,4,100],['USA','Japan','Germany'])
ser
ser['USA']
ser[ser == 100]
ser.iloc[2]
#
ett = pd.DataFrame(np.random.randn(3,4),['r0','r1','r2'],['c0','c1','c2','c3'])
ett
ett['c0']
ett[['c0','c1']]
ett.loc['r0']
ett.loc['r0','c0']
ett.loc[['r0','r2'],['c0','c1']]
ett['c4']=ett['c0']+ett['c1']
ett.drop('c4',axis=1,inplace=True)
ett*0,5 -1
ett
ett>0
(ett>0).sum().sum()
(ett>0).values.sum()
ett[ett>0]
ett.loc['r1',['c0','c1']]
ett['r1',['c0','c1']]
row=ett.loc['r1',['c0','c2']]
row[row>0]
row=ett.loc['r1',['c0','c2']].loc[lambda x: x>0]
ett[(ett['c0']>0) & (ett['c1']>0)]
newind = 'c0 c1 c2'.split()
ett['stats'] = newind
ett
ett = ett.set_index('stats')
