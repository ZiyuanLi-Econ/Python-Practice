import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as sc
from scipy.optimize import minimize

from scipy.stats import norm
from scipy.stats import t

# Simulate distribution
data = norm.rvs(loc=10, scale=5, size=1000)

def neg_loglikeli(theta, data):
    mu, sigma = theta
    
    if sigma <= 0:
        return 1e10
    
    return -np.sum(norm.logpdf(data, loc=mu, scale=sigma))

res = minimize(neg_loglikeli, [3, 3], args=[data,], method='BFGS')
print(res.x)


# Monte Carlo simulation
ols_store = []
mle_store = []

for r in range(1000):

    x = np.random.randn(200)
    true_beta0, true_beta1, true_sigma = [15, 30, 1]
    y = true_beta0 + true_beta1 * x + np.random.randn(200) * true_sigma


    # OLS: minimize SSE
    def sse(theta):
        beta0, beta1 = theta
        y_hat = beta0 + beta1 * x
        return np.mean((y - y_hat) ** 2)

    res = minimize(sse, 
        [0, 0], 
        method="BFGS"
    )
    ols_store.append(res.x)


    # Likelihood: assume y | x follows normal distribution
    def neg_loglikelihood(theta, x, y):
        beta0, beta1, sigma = theta
        mu = beta0 + beta1 * x
        return -np.sum(norm.logpdf(y, loc=mu, scale=sigma))

    tes = minimize(
        neg_loglikelihood,
        [0, 0, 1],
        args=(x, y),
        bounds=[(None, None), (None, None), (1e-6, None)]
    )
    mle_store.append(tes.x)


ols_store = np.array(ols_store)
mle_store = np.array(mle_store)

# Compare beta0, beta1
true_beta = np.array([true_beta0, true_beta1])

print("===== OLS =====")
print("Mean:", ols_store.mean(axis=0))
print("Bias:", ols_store.mean(axis=0) - true_beta)
print("Std:", ols_store.std(axis=0))
print("RMSE:", np.sqrt(np.mean((ols_store - true_beta) ** 2, axis=0)))

print("\n===== MLE =====")
print("Mean:", mle_store[:, :2].mean(axis=0))
print("Bias:", mle_store[:, :2].mean(axis=0) - true_beta)
print("Std:", mle_store[:, :2].std(axis=0))
print("RMSE:", np.sqrt(np.mean((mle_store[:, :2] - true_beta) ** 2, axis=0)))

print("\n===== Sigma =====")
print("True sigma:", true_sigma)
print("MLE sigma mean:", mle_store[:, 2].mean())
print("MLE sigma bias:", mle_store[:, 2].mean() - true_sigma)
print("MLE sigma std:", mle_store[:, 2].std())
