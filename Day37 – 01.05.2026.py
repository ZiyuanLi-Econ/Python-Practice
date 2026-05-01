import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.optimize as sc
from scipy.optimize import minimize

from scipy.stats import norm
from scipy.stats import t

data = norm.rvs(loc=3, scale=1, size=200)
def neg_loglike(theta, data):
    miu, sigma = theta
    return - np.mean(norm.logpdf(data, loc=miu, scale=sigma))

res = minimize(neg_loglike, [0,0.1], args=[data,], method='BFGS')
print(res.x)

x = np.random.randn(100)
true_beta0, true_beta1, true_sigma = [5,10,1]
y = true_beta0 + true_beta1*x + np.random.randn(100)*true_sigma

def sse(theta):
    beta0, beta1 = theta
    y_hat = beta0 + beta1*x 
    return np.mean((y-y_hat)**2)

ress = minimize(sse, [0,0])
print(ress.x)

def neg_loglikelihood(theta1, x, y):
    beta0, beta1, sigma =theta1
    miu = beta0 + beta1*x
    return -np.mean(norm.logpdf(y, loc=miu, scale=sigma))

res = minimize(neg_loglikelihood, [0,0,0.1], args=(x,y))
res.x

############ DiD
n = 200

treat = np.random.binomial(1, 0.5, n)
post = np.random.binomial(1, 0.5, n)

beta0 = 1
beta1 = 2   # treat
beta2 = 3   # post
delta = 5   # DID effect

y = (beta0 
     + beta1 * treat 
     + beta2 * post 
     + delta * treat * post
     + np.random.randn(n))

df = pd.DataFrame({"y": y, "treat": treat, "post": post})

model = smf.ols("y ~ treat * post", data=df).fit()
print(model.params)


###########
def neg_loglik(theta, x, y):
    b0, b1, sigma = theta
    mu = b0 + b1 * x
    return -np.sum(norm.logpdf(y, loc=mu, scale=sigma))

def run_simulation(DGP_func, B=500, n=200):
    beta_hat = []
    
    for _ in range(B):
        x, y = DGP_func(n)
        
        res = minimize(
            neg_loglik,
            x0=[0, 0, 1],
            args=(x, y),
            bounds=[(None,None),(None,None),(1e-6,None)]
        )
        
        beta_hat.append(res.x[1])  # β1
    
    beta_hat = np.array(beta_hat)
    return beta_hat

def evaluate(beta_hat, true_beta):
    mean = np.mean(beta_hat)
    std = np.std(beta_hat)
    bias = mean - true_beta
    mse = np.mean((beta_hat - true_beta)**2)
    rmse = np.sqrt(mse)
    
    print(f"mean: {mean:.3f}")
    print(f"std: {std:.3f}")
    print(f"bias: {bias:.3f}")
    print(f"RMSE: {rmse:.3f}")