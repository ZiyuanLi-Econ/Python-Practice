import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import seaborn as sns



# SE vs STD
beta1 = []
se = []

true_beta1 = 5

for i in range(1000):
    x = np.random.randn(100)
    y = 2 + true_beta1 * x + np.random.randn(100)
    
    X = sm.add_constant(x)
    model = sm.OLS(y, X).fit()
    
    beta1.append(model.params[1])   # β̂₁
    se.append(model.bse[1])         # SE(β̂₁)

beta1 = np.array(beta1)
se = np.array(se)

# Monte Carlo结果
beta1_std = np.std(beta1)   # 真正Std（跨样本）
se_mean = np.mean(se)       # 平均SE（理论估计）

print("Std(beta_hat):", beta1_std)
print("Mean SE:", se_mean)



#  t统计量、第一类错误、第二类错误与检验力
beta1 = []
se = []
t_value = []

true_beta1 = 5
beta0_null = 5

for i in range(1000):
    x = np.random.randn(100)
    X = sm.add_constant(x)

    ## 同方差
    # y = 2 + true_beta1 * x + np.random.randn(100)
    ## 异方差：variance 随 x 变化 （SE 错 → t 错 → 检验错）
    y = 2 + true_beta1 * x + np.random.randn(100) * (np.abs(x))

    ## 同方差
    #model = sm.OLS(y, X).fit()
    ## 异方差
    model = sm.OLS(y, X).fit(cov_type='HC1')

    beta_hat = model.params[1]
    se_hat = model.bse[1]

    t_stat = (beta_hat - beta0_null) / se_hat

    beta1.append(beta_hat)
    se.append(se_hat)
    t_value.append(t_stat)

beta1 = np.array(beta1)
se = np.array(se)
t_value = np.array(t_value)

# -----------------------------
# Std vs SE（核心检验）
# -----------------------------
beta1_std = np.std(beta1)
se_mean = np.mean(se)

print("Std(beta_hat) =", beta1_std)
print("Mean(SE)      =", se_mean)
print("Ratio Std/SE  =", beta1_std / se_mean)

# -----------------------------
# t统计量基本性质
# -----------------------------
t_mean = np.mean(t_value)
t_std = np.std(t_value)

print("Mean(t) =", t_mean)
print("Std(t)  =", t_std)

# -----------------------------
# t分布检查（hist + 正态对比）
# -----------------------------
sns.histplot(t_value, bins=30, stat="density", kde=True)

x = np.linspace(-4, 4, 100)
plt.plot(x, (1/np.sqrt(2*np.pi))*np.exp(-x**2/2), linewidth=2)

plt.show()

# -----------------------------
# 经验critical values
# -----------------------------
lower = np.percentile(t_value, 2.5)
upper = np.percentile(t_value, 97.5)
print("Empirical CV:", lower, upper)

# -----------------------------
# 第一类错误 / size（仅当 H0 为真）
# -----------------------------
reject = np.mean(np.abs(t_value) > 1.96)
print("Rejection rate (size):", reject)

# -----------------------------
# 第二类错误 / power（仅当 H0 为假，此处不适用）
# -----------------------------
beta_error = np.mean(np.abs(t_value) <= 1.96)
power = 1 - beta_error

print("Type II error:", beta_error)
print("Power:", power)

# -----------------------------
# Monte Carlo p-value
# -----------------------------
t_obs = 2.3
p_value = np.mean(np.abs(t_value) >= abs(t_obs))
print("Monte Carlo p-value:", p_value)