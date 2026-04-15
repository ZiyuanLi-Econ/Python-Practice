import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset('iris')
iris.head()
iris['species'].unique()
sns.pairplot(iris)
#grids
g=sns.PairGrid(iris)
g.map_diag(sns.histplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)
plt.show()

tips=sns.load_dataset('tips')
tips.head()
g = sns.FacetGrid(data=tips,col='time',row='smoker')
g.map(sns.histplot,'total_bill')
plt.show()
#color*style
sns.set_style('ticks')
sns.set_context('poster')
sns.countplot(x='sex',data=tips)
sns.despine()
plt.show()
