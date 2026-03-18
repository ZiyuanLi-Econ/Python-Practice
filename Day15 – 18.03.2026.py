#review
import numpy as np
my_list=[1,2,3,4]
np.array(my_list)
np.array([[1,2,3,4],[5,6,7,8]])
np.arange(1,7).reshape(2,3)
np.zeros(10)
np.ones(25).reshape(5,5)
np.eye(4)
np.arange(0,10,2)
np.linspace(0,5,11)
np.random.rand(10)*10
np.random.randn(100)
np.arange(20).reshape(4,5).shape
arr = np.arange(10)
arr
arr.max()
arr.argmax()
arr+100
np.sqrt(arr)
np.sum(arr)
arr**1/2
mat = np.arange(12).reshape(3,4)
np.sum(mat, axis=0)
np.sum(mat,axis=1,keepdims=1)
mat=np.arange(25).reshape(5,5)
mat
mat[1:2]
mat[0:1,3:6]=100
mat=np.arange(25).reshape(5,5)
mat[mat>5]
mat>5
mat[mat%2==0]

#panda p23
import pandas as pd
labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
arr
d={'a':10,'b':20,'c':30}
pd.Series(data = my_data)
pd.Series(my_data)
pd.Series(my_data,index = labels)
pd.Series(my_data,labels)
pd.Series(arr)
pd.Series(d)
pd.Series(data=labels,index = labels)
pd.Series(data=[sum,print,len])
ser1 = pd.Series([1,2,3,4],['usa','ussr','japan','germany'])
ser1
ser2=pd.Series([1,2,5,4],['usa','germany','italy','japan'])
ser2
ser1['usa']
ser3 = pd.Series(data = labels)
ser3
ser3[0]
ser1 + ser2

#panda p24
from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','S','X','Z'])
df
df[['W','Z']]
type(df['W'])
df['new1']= df['W']+ df['X']
df['new1']**1/2
df.drop('new1',axis=1)
df.drop('new1',axis=1,inplace=True)
df
df.drop('E')
df.shape
df.loc['A']
df.iloc[2]
df.loc['B','W']
df.loc[['A','B'],['W','S']]


########Conclusions:
# Series: 1D data + index (labels)
ser = pd.Series(data=my_data, index=labels)
ser1 = pd.Series([1,2,3,4], ['A','B','C','D'])

ser1['A']          # access by label
ser1.iloc[1]       # access by position
ser1[ser1 == 1]    # boolean indexing (filter by value)

ser1 + ser2        # automatic alignment by index

# DataFrame
np.random.seed(555)
df = pd.DataFrame(randn(4,4), ['A','B','C','D'], ['Q','W','E','R'])

df['Q']                          # single column → Series
df[['Q','W']]                    # multiple columns → DataFrame

df.loc['A']                      # select row by label
df.loc['A','W']                  # single value (row + column label)
df.loc[['A','C'], ['Q','E']]     # subset of rows and columns

df.iloc[1]                       # select row by position

df['T'] = df['Q'] + df['W']      # create new column
df.drop('T', axis=1, inplace=True)  # drop column