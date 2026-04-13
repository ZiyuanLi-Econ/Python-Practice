import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
x,y=1,1
#
plt.plot(x,y)
plt.subplots(1,2,1)
#
fig = plt.figure(figsize=(),dpi=1)
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x+1,label='')
ax.legend(loc=0)
#
fig,ax = plt.subplots(1,2)
ax[0].plot(color='',linewidth=2,linestyle='',alpha=1,marker='o')
ax[0].set_xlabel('')
ax[0].set_xlmi([0,1])
plt.tight_layout()
fig.savefig('name',dpi=200)

##seaborn data part
x = np.random.randn(100)
z = np.random.randn(100)
y = x+1
kla = [1 if xi>0 else 0 for xi in x]
df = pd.DataFrame({'x':x,'y':y,'z':z,'kla':kla})


# dirstribution plot
sns.kdeplot(x) #
sns.histplot(x,kde=True,bins=30) #
sns.jointplot(x=x,y=y,kind='reg')
sns.pairplot(df,hue='',palette='') #hue类别数据
sns.rugplot(x)

#categorial plots
sns.catplot(x='kla',y='x',data=df,kind='bar')
sns.barplot(x='kla',y='x',data=df,estimator=np.std)
sns.countplot(x=kla,data=df)
sns.boxplot(x=kla,y=x,data=df,hue='')
sns.violinplot(x=kla,y=x,data=df,hue='',split=True)
sns.stripplot(x=kla,y=x,data=df,jitter=True)
sns.swarmplot(x=kla,y=x,data=df)
plt.show()
