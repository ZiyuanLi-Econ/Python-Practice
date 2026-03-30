import numpy as np
import pandas as pd
np.array([[1,2,3],[4,5,6]])
np.arange(0,10,2)
np.linspace(0,10,6)
np.eye(10)
np.ones((10,10)).reshape()
np.random.randn()
arr=np.random.rand(10)
arr.argmax()
np.sqrt(arr)
np.sum(arr)
arr[1:2,3:4]=100
arr=arr[arr>5]
arr
arr>5
arr[arr>0.5]
ser=pd.Series([1,2,3],['A','B','C'])
ser
ser['A']
ser[ser==1]
ser.iloc[0]
df=pd.DataFrame(np.random.randn(5,5),[1,2,3,4,5],[6,7,8,9,10])
df=pd.DataFrame(np.eye(5),[1,2,3,4,5],[6,7,8,9,10])
df
df[6]
df[[6,7]]
df.loc[1,6]
df.loc[[1,3],[7,9]]
df[11]=df[6]+df[7]
df.drop(11,axis=1,inplace=True)
df[df>0.5]
df[df[10]>=1]
df[(df[6]>0)&(df[7]>0)]
df[(df[6]>0)|(df[7]>0)]
df.loc[df[6]>0,[6,7,8]]
df.reset_index()
np.random.seed(5)
np.random.seed(101)
#conditional selection
booldf = df >0
booldf
df[booldf]
df[df>0]
df[df[6]>0]
df.loc[df[6]>0]
df[6]>0
df[df[6]>0]
df=pd.DataFrame(np.random.randn(5,5),[1,2,3,4,5],[6,7,8,9,10])
df.loc[[1,2],[6,7]]
df.loc[df[7]>0]
df.loc[(df[7]>0)&(df[8]>0),[6,10]]
df.reset_index()
df = pd.DataFrame({
    6:  [1, -2, 3, -4, 5],
    7:  [0,  2, -1,  3, -2],
    8:  [4, -3, 2,  -1,  0],
    9:  [1,  1, 1,   1,  1],
    10: [-1, 2, -3,  4, -5]
}, index=[1,2,3,4,5])
df.loc[(df[7]>0)&((df[8]>0)|(df[10]>0)),[6,10]]
newind ='1 7 2 3 4'.split()
newind

#!!!!!!!!!!!!!!!!!!!!!!
df['states']=newind
df.loc[6]=[1,1,1,1,1,1]
#!!!!!!!!!!!!!!!!!!!!!!

