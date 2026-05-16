import numpy as np
from scipy.optimize import minimize
import statsmodels.api as sm

n = 1000
z = np.random.normal(size=n)
u = np.random.normal(size=n)
x = 0.8*z + 0.6*u + np.random.normal(size=n)

beta0 = 1
beta1 = 2
y = beta0 + beta1*x + u

X = sm.add_constant(x)
ols = sm.OLS(y,X).fit()
print("OLS:", ols.params)

Z = sm.add_constant(z)

def gmm_objective(beta):
    residual = y - X @ beta
    moments = Z.T @ residual / n
    return moments.T @ moments

res = minimize(gmm_objective, x0=np.array([0,0]))

print("GMM:", res.x)