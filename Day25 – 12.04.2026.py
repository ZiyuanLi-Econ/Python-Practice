import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,10)
y = np.random.randn(10)

#function 单图
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regression')
plt.show()

#function 多图 
plt.subplot(1,2,1)
plt.plot(x,y)
plt.xlabel('A')
plt.subplot(1,2,2)
plt.plot(y,x)


#画布法：单图 
fig = plt.figure(figsize=(10,2), dpi=200)
ax = fig.add_axes([0,0,1,1])
ax.plot(x, x+1, label='L1')
ax.plot(x, x+2, label='L2') #多条线
ax.legend(loc=0) #label位置
ax.legend(loc=(0.1,0.1))


#画布法：多图
fig,axes = plt.subplots(1,2)
axes[0].plot(x,y)
axes[1].plot(y,x)
ax.set_xlabel('A')
plt.tight_layout() #避免重叠

#储存
fig.savefig('picture.png',dpi=200)


##color
fig=plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='b',linewidth = 2, linestyle ='--' , alpha =0.8, marker='o',markersize=10, markerfacecolor='b',markeredgewidth=3,markeredgecolor='b') #RGB Hex code
ax.set_xlim([0,1])
plt.show()

from random import sample #直方图
data = sample(range(1,1000),100)
plt.hist(data)
plt.show()

import seaborn as sns
tips = sns.load_dataset('tips')
tips.head()
