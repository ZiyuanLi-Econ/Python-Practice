import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import seaborn as sns

df = pd.read_csv(r'C:\Users\17964\Desktop\Python\EIO\PS1\\data1.dat', sep = r'\s+',header=None)
x = sm.add_constant(df[1])
y = df[0]
model = sm.OLS(y,x).fit()
y_pred = model.predict(x)

sns.regplot(x=df[1],y=y)
plt.xlabel('technology')
plt.ylabel('economy')
plt.show()

#simulation
beta1 = []
true_beta1 = 5
for i in range(1000):
    x = np.random.randn(100)
    y = 2 + true_beta1*x + np.random.randn(100)
    X = sm.add_constant(x)
    model = sm.OLS(y,X).fit()
    beta1.append(model.params[1])
beta1 = np.array(beta1)

print(f"Mean: {np.mean(beta1):.4f}") # f"文本 {变量}"
print(f"Std: {np.std(beta1):.4f}")
print(f"Bias: {np.mean(beta1) - true_beta1:.4f}")

plt.hist(beta1, bins=30)
plt.show()

#Simualation
beta_mean = []
beta_var = []
bias = []
true_beta1 = 5
z = np.linspace(100,10001,100)

for n in z:
    n = int(n)
    beta1 = []
    for i in range(1000):
        x = np.random.randn(n)
        y = 2 + true_beta1*x + np.random.randn(n)
        X = sm.add_constant(x)
        model = sm.OLS(y,X).fit()
        beta1.append(model.params[1])

    beta1 = np.array(beta1)
    beta_mean.append(np.mean(beta1))
    beta_var.append(np.var(beta1))
    bias.append(np.mean(beta1) - true_beta1)

beta_mean = np.array(beta_mean)
beta_var = np.array(beta_var)
bias = np.array(bias)

#graph
fig,axes = plt.subplots(1,3,figsize=(18, 5))
#mean
sns.regplot(x=z, y=beta_mean,ax=axes[0],color='blue')
axes[0].axhline(true_beta1, color='red', linestyle='--')
axes[0].set_title("Mean of beta_hat_1 vs sample size")
axes[0].set_xlabel("Sample size n")
axes[0].set_ylabel("Mean of beta_hat_1")
#bias
sns.regplot(x=z, y=bias,ax=axes[1])
axes[1].axhline(0,color='red', linestyle='--')
axes[1].set_title("Bias of beta_hat_1 vs sample size")
axes[1].set_xlabel("Sample size n")
axes[1].set_ylabel("Bias of beta_hat_1")
#var
sns.scatterplot(x=z, y=beta_var, ax=axes[2])
axes[2].axhline(0,color='red', linestyle='--')
axes[2].set_title("Variance of beta_hat_1 vs sample size")
axes[2].set_xlabel("Sample size n")
axes[2].set_ylabel("Variance of beta_hat_1")
#
plt.tight_layout()
plt.show()