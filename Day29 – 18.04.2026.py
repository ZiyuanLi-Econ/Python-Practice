#Q1: Build Regression 
import pandas as pd
import statsmodels.api as sm
df = pd.read_csv(r'C:\Users\17964\Desktop\Python\EIO\PS1\\data1.dat',sep=r'\s+',header=None)
x = sm.add_constant(df[1])
y=df[0]
model = sm.OLS(y,x).fit()
model.summary()


##Q1.1
theta1_hat = model.params['const']
theta2_hat = model.params[1]
se_theta1 = model.bse['const']
se_theta2 = model.bse[1]
print(theta1_hat, theta2_hat, se_theta1, se_theta2)


##Simulation
import numpy as np
import matplotlib.pyplot as plt
beta1=[]
for i in range(1000):
    x = df[1] + np.random.randn(len(df[1]))
    y = df[0] + np.random.randn(len(df[0]))

    X = sm.add_constant(x)

    model = sm.OLS(y,X)
    results = model.fit()

    beta1.append(results.params[1])

np.mean(beta1)
np.std(beta1)
beta1[:50]

plt.hist(beta1, 30)
plt.show()