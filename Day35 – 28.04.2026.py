import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as sc
from scipy.optimize import minimize

from scipy.stats import norm
from scipy.stats import t

norm.pdf([1,3,5],loc=100, scale=5)
norm.logpdf([1,10], loc=10, scale=1)
norm.rvs(loc=5, scale=2, size=100)

t.logpdf(10,df=5)
t.rvs(df=10000,size=100)

####


# 1️⃣ Generate data (pretend we don't know the true parameters)
data = norm.rvs(loc=15, scale=7, size=100)

# 2️⃣ Scoring function (negative log-likelihood)
def neg_loglik(theta, data):
    mu, sigma = theta
    return -np.sum(norm.logpdf(data, loc=mu, scale=sigma))
    # logpdf → how "likely" each point is under (mu, sigma)
    # sum → total score (log-likelihood)
    # negative → because minimize() only minimizes

# 3️⃣ Optimization (MLE)
res = minimize(
    neg_loglik,
    x0=[0, 1],                      # starting guess (NOT the answer)
    args=(data,),                   # pass data into function
    bounds=[(None, None), (1e-6, None)]  # enforce sigma > 0
)

print(res.x)  # estimated [mu, sigma]
