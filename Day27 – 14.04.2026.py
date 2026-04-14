import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)

n = 300

df = pd.DataFrame({
    'income': np.random.normal(50000, 15000, n),      # 收入
    'age': np.random.normal(35, 10, n),              # 年龄
    'education_years': np.random.randint(10, 20, n), # 教育年限
    'gender': np.random.choice(['Male', 'Female'], n),
    'region': np.random.choice(['EU', 'Asia', 'US'], n),
})

# 
df['consumption'] = (
    0.6 * df['income']
    + 2000 * df['education_years']
    - 300 * df['age']
    + np.random.normal(0, 5000, n)
)

df.head()

sns.barplot(df['income'])
sns.histplot(df['education_years'], bins=10)
sns.jointplot(x=df['age'], y=df['consumption'], data=df,kind ='reg')
sns.pairplot(df,hue='gender')
sns.catplot(x='region',y='education_years',hue='gender',data=df,kind='box')
sns.catplot(x='region', data=df,kind='count')
fig, axes=plt.subplots(1,2,figsize=(12,5))
axes[0].plot(df['income'], df['consumption'])
#####Preferences: Open User Settings (JSON)

#matirx plot
sns.heatmap(df[['income','education_years','age']].corr(),annot=True,cmap='coolwarm',linecolor='white',linewidths=3) 
pdd=df.pivot_table(index='education_years',columns='age',values='income')
sns.clustermap(df[['income','education_years','age']])

#regression
sns.lmplot(x='age',y='income',data=df,col='region',hue='gender',markers=['o','v'])
plt.show()