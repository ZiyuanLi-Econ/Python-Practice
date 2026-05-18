import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import seaborn as sns
from scipy.optimize import minimize
from scipy.stats import norm


##Q2
#Q2.1
# load data
df = pd.read_csv(r'C:\Users\17964\Desktop\Python\EIO\PS1\data2.dat', sep=r'\s+', header=None)

# variables
y = df[0].values
x = df[1].values

def neg_loglikeli(params):
    theta1, theta2, kappa = params[0], params[1], params[2]
    sigma = np.exp(kappa)
    mu = theta1 + theta2 ** x
    logy = np.log(y)
    logpdf = norm.logpdf(logy, loc=mu, scale=sigma)
    return -np.mean(logpdf)

starts = [1,1,0]
result = minimize(neg_loglikeli, starts)
result

# estimates
theta1_hat = result.x[0]
theta2_hat = result.x[1]
kappa_hat  = result.x[2]

sigma_hat = np.exp(kappa_hat)

print("theta1 =", theta1_hat)
print("theta2 =", theta2_hat)
print("sigma  =", sigma_hat)


#Q2.2
# ---------- Stage 1 ----------
# variables
y = df[0].values
x = df[1].values
logy = np.log(y)

n = len(y)

# instruments
Z = np.column_stack((np.ones(n), x))

# stage 1 weight matrix
W1 = np.linalg.inv((Z.T @ Z) / n)

# moment function
def moments_q2(theta):
    theta1, theta2 = theta[0], theta[1]
    power_term = np.power(x, theta2)
    eps = logy - power_term - theta1
    g = (Z.T @ eps) / n
    return g

# stage 1 GMM objective
def gmm_stage1_objective(theta):
    g = moments_q2(theta)
    return g.T @ W1 @ g

startss=[0,0]
result_stage1 = minimize(gmm_stage1_objective, startss, method="Nelder-Mead")

# stage 1 estimates
theta_init = result_stage1.x

print("Stage 1 estimates:")
print("theta1_init =", theta_init[0])
print("theta2_init =", theta_init[1])
print("objective   =", result_stage1.fun)


# ---------- Stage 2 ----------
# residuals using stage 1 estimates
theta1_init = theta_init[0]
theta2_init = theta_init[1]

eps_init = logy - theta1_init - np.power(x, theta2_init)

# individual moments: each row is z_i * eps_i
g_i = Z * eps_init[: , None]

# optimal weight matrix
W2 = np.linalg.inv((g_i.T @ g_i)/n)

# stage 2 GMM objective
def gmm_stage2_objective(theta):
    g = moments_q2(theta)
    return g.T @ W2 @ g

# optimization
result_stage2 = minimize(gmm_stage2_objective, theta_init, method="Nelder-Mead")

# stage 2 estimates
theta_gmm = result_stage2.x

print("Stage 2 estimates:")
print("theta1 =", theta_gmm[0])
print("theta2 =", theta_gmm[1])
print("objective =", result_stage2.fun)



