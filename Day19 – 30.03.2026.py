import pandas as pd
import numpy as np
outside=['g1','g1','g1','g2','g2','g2']
inside=[1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df=pd.DataFrame(np.random.randn(6,2),hier_index,['A','B'])
df
df.loc['g1']
df.index.names = ['groups','number']
df.loc['g2'].loc[2]['B']
df.loc['g1'].loc[3]['A']
df.loc['g1']
df.xs(1,level = 'number')
df.xs('g2',level = 'groups')
df.xs('g2')

d={'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df=pd.DataFrame(d)
df.dropna()
df.dropna(axis=1)
df.dropna(thresh=1)
df.dropna(thresh=2)
df.fillna(value=1)
df['A'].fillna(value=df['A'].mean())


#添加列 df['states']=[1,2,3,4]
#添加行 df.loc['hang'] = [1,2,3,4]
#两层结构 
outside=['g1','g1','g1','g2','g2','g2']
inside=[1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df=pd.DataFrame(np.random.randn(6,2),hier_index,['A','B'])
#两层命名 df.index.names = ['groups','numbers']
#两层引用 df.loc['g2'].loc[1]['A'] or df.loc[('g2', 1), 'A']
df.xs(1,level = 'number')
df.xs('g2')
#处理nan
df.dropna(axis=1)
df.dropna(thresh=1)
df.fillna(value=1)
