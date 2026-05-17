import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import seaborn as sns
from scipy.optimize import minimize
from scipy.stats import norm

#Q1
##Q1.1

# load data
df = pd.read_csv(r'C:\Users\17964\Desktop\Python\EIO\PS1\\data1.dat', sep = r'\s+', header=None)

# define y and X
x = sm.add_constant(df[1])
y = df[0]

#OLS
model = sm.OLS(y,x).fit()
y_pred = model.predict(x)

# Inferences
print(model.params)
print(model.bse)



##Q1.2
# define variables
y = df[0].values
x = df[1].values

# negative log-likelihood
def neg_loglikeli(params):
    theta1, theta2, kappa = params[0],params[1],params[2]
    mu = theta1 + theta2 * x
    sigma = np.exp(kappa)
    logpdf = norm.logpdf(y, loc=mu, scale=sigma)
    return -np.sum(logpdf)

result = minimize(neg_loglikeli, [0,0,0])


# estimates
theta1_hat = result.x[0]
theta2_hat = result.x[1]
kappa_hat  = result.x[2]
sigma_hat = np.exp(kappa_hat)

print("theta1 =", theta1_hat)
print("theta2 =", theta2_hat)
print("sigma  =", sigma_hat)


#SE
n = len(y)

# score matrix
scores = np.zeros((n, 3))

# step size for numerical derivative
h = 0.0001

for i in range(n):
    yi = y[i]
    xi = x[i]

    # individual log-likelihood
    def loglike_i(params):
        theta1, theta2, kappa = params[0],params[1],params[2]
        sigma = np.exp(kappa)
        mu = theta1 + theta2 * xi
        return norm.logpdf(yi, loc=mu, scale=sigma)
    theta_hat = np.array([theta1_hat, theta2_hat, kappa_hat])

    # numerical derivatives
    for j in range(3):
        theta_up = theta_hat.copy()
        theta_up[j] += h
        derivative = (loglike_i(theta_up) - loglike_i(theta_hat)) / h
        scores[i, j] = derivative

# information matrix
info_matrix = scores.T @ scores
# covariance matrix
cov_matrix = np.linalg.inv(info_matrix)
# standard errors
se = np.sqrt(np.diag(cov_matrix))

print("\nStandard Errors:")
print("SE(theta1) =", se[0])
print("SE(theta2) =", se[1])
print("SE(kappa)  =", se[2])



##Q1.3
# variables
y = df[0].values
x = df[1].values
n = len(y)

Z = np.column_stack((np.ones(n), x))
# weight matrix
W = np.linalg.inv((Z.T @ Z) / n)

# moment function
def moments(theta):
    theta1, theta2 = theta[0], theta[1]
    u = y - theta1 - theta2 * x
    g = (Z.T @ u) / n
    return g

# GMM objective
def objective(theta):
    g = moments(theta)
    return g.T @ W @ g

# optimization
result = minimize(objective, [0,0])
# estimates
theta_hat = result.x

print("theta1 =", theta_hat[0])
print("theta2 =", theta_hat[1])