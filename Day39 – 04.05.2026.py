import numpy as np
import statsmodels.api as sm
from scipy.optimize import minimize
from scipy.stats import norm
import matplotlib.pyplot as plt

#
n = 200
beta_true = 2
sigma_u_true = 1
sigma_e_true = 1

x = np.random.randn(n)
u = np.random.randn(n)*sigma_u_true
eps = np.random.randn(n)*sigma_e_true

y = (beta_true + u)*x + eps

#
def neg_sml(theta, x, y):
    beta, sigma_u, sigma_e = theta
    if sigma_e_true <= 0 or sigma_u_true <= 0:
        return 1e10
    
    n = len(y)
    ll = 0
    for i in range(n):
        xi = x[i]
        yi = y[i]

        u_draws = np.random.randn(50)*sigma_u
        mu = (beta + u_draws)*xi
        densities = norm.pdf(yi, loc=mu, scale=sigma_e)

        avg_density = np.mean(densities)

        ll += np.log(avg_density + 1e-10)
    return -ll

#
res = minimize(neg_sml, [1,1,1], args=(x,y), bounds=[(None,None),(1e-6,None),(1e-6,None)])
print (res.x)

############################
# 1. Generate data
n = 300

beta_true = 2
sigma_alpha_true = 1
sigma_e_true = 1

x = np.random.randn(n)
alpha = np.random.randn(n) * sigma_alpha_true
eps = np.random.randn(n) * sigma_e_true

y = alpha + beta_true * x + eps


# 2. Simulated negative log-likelihood
def neg_sml(theta, x, y, R=100):
    beta, sigma_alpha, sigma_e = theta

    if sigma_alpha <= 0 or sigma_e <= 0:
        return 1e10

    n = len(y)
    ll = 0

    for i in range(n):
        xi = x[i]
        yi = y[i]

        alpha_draws = np.random.randn(R) * sigma_alpha

        mu = alpha_draws + beta * xi

        densities = norm.pdf(yi, loc=mu, scale=sigma_e)

        avg_density = np.mean(densities)

        ll += np.log(avg_density + 1e-10)

    return -ll


# 3. Estimate
res = minimize(
    neg_sml,
    x0=[1, 1, 1],
    args=(x, y),
    bounds=[(None, None), (1e-6, None), (1e-6, None)]
)

print("success:", res.success)
print("estimates:", res.x)
print("true:", [beta_true, sigma_alpha_true, sigma_e_true])