import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import seaborn as sns
from linearmodels.iv import IV2SLS


# Baseline
beta1 = []
beta_ovb1 = []
true_beta1 = 5

for i in range(1000):
    x = np.random.randn(100)
    y = 2 + true_beta1*x + np.random.randn(100)
    X = sm.add_constant(x)
    model = sm.OLS(y,X).fit()
    beta1.append(model.params[1])

beta1 = np.array(beta1)

# OVB
for i in range(1000):
    x1 = np.random.randn(100)
    u = np.random.randn(100)
    e = 0.8 * x1 + u    
    y1 = 2 + true_beta1*x1 + e
    X1 = sm.add_constant(x1)
    model1 = sm.OLS(y1,X1).fit()
    beta_ovb1.append(model1.params[1])

beta_ovb1 = np.array(beta_ovb1)   

print("Baseline mean:", beta1.mean())
print("OVB mean:", beta_ovb1.mean())

#  IV
beta_iv = []
for i in range(1000):
    z = np.random.randn(100)
    u = np.random.randn(100)
    v = np.random.randn(100)
    x = 0.8*z + 0.8*u + v
    y = 2 + 5*x + u
    model_iv = IV2SLS(dependent=y, exog=np.ones(100), endog=x, instruments=z).fit()
    beta_iv.append(model_iv.params["endog"]) 

    #first_stage = sm.OLS(x,sm.add_constant(z)).fit()
    #x_hat = first_stage.fittedvalues
    #second_stage = sm.OLS(y,sm.add_constant(x_hat)).fit()
    #beta_iv.append(second_stage.params[1])

beta_iv = np.array(beta_iv)

print('iv_mean:', np.mean(beta_iv))
print('iv_std:', np.std(beta_iv))

######################
# Common settings
N_sim = 1000
n = 100
true_beta1 = 5

# =========================
# 1. Baseline: clean OLS
# =========================

beta_baseline = []

for i in range(N_sim):
    x = np.random.randn(n)
    u = np.random.randn(n)
    
    y = 2 + true_beta1 * x + u
    
    X = sm.add_constant(x)
    model = sm.OLS(y, X).fit()
    
    beta_baseline.append(model.params[1])

beta_baseline = np.array(beta_baseline)


# =========================
# 2. Endogenous OLS
# =========================

beta_endo_ols = []

for i in range(N_sim):
    x = np.random.randn(n)
    u = np.random.randn(n)
    
    e = 0.8 * x + u
    y = 2 + true_beta1 * x + e
    
    X = sm.add_constant(x)
    model = sm.OLS(y, X).fit()
    
    beta_endo_ols.append(model.params[1])

beta_endo_ols = np.array(beta_endo_ols)


# =========================
# 3. IV / 2SLS
# =========================

beta_iv = []

for i in range(N_sim):
    z = np.random.randn(n)      # instrument
    u = np.random.randn(n)      # structural error
    v = np.random.randn(n)      # extra noise in x
    
    x = 0.8 * z + 0.8 * u + v   # endogenous x
    y = 2 + true_beta1 * x + u
    
    model_iv = IV2SLS(
        dependent=y,
        exog=np.ones(n),
        endog=x,
        instruments=z
    ).fit()
    
    beta_iv.append(model_iv.params["endog"])

beta_iv = np.array(beta_iv)

##
print("Baseline OLS mean:", beta_baseline.mean())
print("Endogenous OLS mean:", beta_endo_ols.mean())
print("IV mean:", beta_iv.mean())

print("Baseline OLS bias:", beta_baseline.mean() - true_beta1)
print("Endogenous OLS bias:", beta_endo_ols.mean() - true_beta1)
print("IV bias:", beta_iv.mean() - true_beta1)

# =========================
# Evaluation function
# =========================

def evaluate(beta_hat, true_beta):
    bias = beta_hat.mean() - true_beta
    variance = beta_hat.var()
    mse = ((beta_hat - true_beta) ** 2).mean()
    rmse = np.sqrt(mse)
    mcse = beta_hat.std() / np.sqrt(len(beta_hat))
    
    return {
        "mean": beta_hat.mean(),
        "bias": bias,
        "variance": variance,
        "mse": mse,
        "rmse": rmse,
        "mcse": mcse
    }


# =========================
# Evaluate three estimators
# =========================

eval_baseline = evaluate(beta_baseline, true_beta1)
eval_endo_ols = evaluate(beta_endo_ols, true_beta1)
eval_iv = evaluate(beta_iv, true_beta1)

print("Baseline OLS:", eval_baseline)
print("Endogenous OLS:", eval_endo_ols)
print("IV:", eval_iv)


results = pd.DataFrame({
    "Baseline OLS": eval_baseline,
    "Endogenous OLS": eval_endo_ols,
    "IV": eval_iv
}).T

results