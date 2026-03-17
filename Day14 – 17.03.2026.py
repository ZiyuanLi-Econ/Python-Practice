# review
arr = [1,2,3,4,5]
import numpy as np
np.arange(0,20,2)
np.zeros(10)
np.ones((5,5))
np.eye(3)
np.linspace(0,1,50)
np.random.rand(10)
np.random.randn(4,4)
np.random.randint(1,100,20)
np.random.randint(0,50,(5,5))
arr = np.arange(0,16)
arr.reshape(4,4)
arr = np.arange(0,20)
arr.reshape(5,4)
arr = np.arange(9)
arr.reshape(3,3)
arr = np.random.rand(100)*100
arr
arr.max()
arr.argmax()
# new courses Numpy 5 p17
arr = np.arange(0,9)
arr = arr.reshape(3,3)
arr[8]
arr[1:5]
arr[:2]
arr[:1]=100
arr = np.arange(0,11)
arr[:5]=10
arrcopy = arr.copy()
arr
arrcopy
arr = np.array([[0,1,2],[3,4,5]])
arr[1][1]
arr[1]
arr[1,1]
arr[:2,1:]#左闭右开
arr = np.arange(1,11)
arr
arr > 5
bool_arr = arr >5
arr[bool_arr]
arr[arr<5]
arr = np.random.randn(2,3,3)
arr[arr>0]
arr.sum()
arr=np.arange(50).reshape(5,10)
arr
arr[1:3,3:5] = 10
arr[arr == 10]

# new courses Numpy 6 p18
arr=np.arange(0,11)
arr*2
arr/arr
arr + 100
np.random.rand(10) + 100
arr1=np.arange(0,11)
arr2=np.zeros(11)
arr1/arr2
(arr2/arr2)+1
np.sqrt(arr1)
np.sin(arr)
arr**1/2

#p19/20
import numpy as np
np.zeros(10)
np.ones(10)*5
np.arange(10,51)
np.arange(10,51,2)
np.arange(0,9).reshape(3,3)
np.eye(3)
np.random.rand(1)
np.random.randn(25)
np.linspace(0.01,1,100)
x= np.random.rand(100)
x
k=[]
for y in x:
    print(f"{y:.2f}")
    k.append(y)
    print(k)
mat=np.arange(1,26).reshape(5,5)
mat
mat = mat[2:,1:]
mat[1,3]
mat=np.arange(1,26).reshape(5,5)
mat = mat[0:3,1:2]
mat
mat=np.arange(1,26).reshape(5,5)
mat
mat[4:5]
mat[3:5]
mat.sum()
np.std(mat)

#get the sum of all columns in mat
mat=np.arange(1,26).reshape(5,5)
mat
np.sum(mat,axis=1)
np.sum(mat,axis=0)

mat=np.arange(1,26).reshape(5,5)
zeroo = np.zeros(5)
for x in range(5):
    zeroo += mat[x]
zeroo

mat = np.arange(0,25).reshape(5,5)
np.sum(mat,axis=0,keepdims=True)
np.sum(mat,axis=1,keepdims=True)

