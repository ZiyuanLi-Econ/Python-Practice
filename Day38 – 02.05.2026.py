import numpy as np
import statsmodels.api as sm
from scipy.optimize import minimize
from scipy.stats import norm
import matplotlib.pyplot as plt



###DGP
def DGP1(n):
    x = np.random.randn(n)
    y = 2 + 3*x + np.random.randn(n)
    return x,y

# Hetero
def DGP2(n):
    x = np.random.randn(n)
    noise = np.random.randn(n)*(1 + x**2)
    y = 2 + 3*x + noise
    return x,y

# endo
def DGP3(n):
    u = np.random.randn(n)
    x = 0.8*u + np.random.randn(n)
    y = 2 + 3*x + u
    return x,y


####
def neg_loglikelihood(theta,x,y):
    b0, b1, sigma = theta
    miu = b0 + b1*x
    return -np.mean(norm.logpdf(y, loc=miu, scale=sigma))

def estimate_mle(x,y):
    res = minimize(neg_loglikelihood, [0,0,1], args=(x,y), bounds=[(None,None),(None,None),(1e-6,None)])
    return res.x[1]

def estimate_ols(x,y):
    X = sm.add_constant(x)
    model = sm.OLS(y,X).fit()
    return model.params[1]


###
def run_simulation(DGP, B=500, n=200):
    mle_beta1 = [] 
    ols_beta1 = []

    for i in range(B):
        x, y = DGP(n)

        mle_beta1.append(estimate_mle(x,y))
        ols_beta1.append(estimate_ols(x,y))

    return np.array(mle_beta1), np.array(ols_beta1)


### evaluate
def evaluate(beta_hat, true_beta=3, name=''):
    mean = np.mean(beta_hat)
    std = np.std(beta_hat, ddof=1)
    bias = mean - true_beta
    mse = np.mean((beta_hat - true_beta)**2)
    rmse = np.sqrt(mse)

    print(f"\n{name}")
    print('mean:', mean)
    print('std:', std)
    print('bias:', bias)
    print('mse:', mse)
    print('rmse:', rmse)

###
mle1, ols1 = run_simulation(DGP1)
evaluate(mle1, name="MLE - DGP1")
evaluate(ols1, name="OLS - DGP1")

mle2, ols2 = run_simulation(DGP2)
evaluate(mle2, name="MLE - DGP2 Heteroskedastic")
evaluate(ols2, name="OLS - DGP2 Heteroskedastic")

mle3, ols3 = run_simulation(DGP3)
evaluate(mle3, name="MLE - DGP3 Endogeneity")
evaluate(ols3, name="OLS - DGP3 Endogeneity")