import numpy as np
from scipy.optimize import minimize

n = 500
u = np.random.randn(n)
z = np.random.randn(n)

x  = 0.8*u + z + np.random.randn(n)*0.1
y = 2 + 3*x + u 

def moment(beta, x, y, z):
    u_hat = y - beta*x
    return np.mean(z*u_hat)

def gmm_obj(beta, x, y, z):
    g = moment(beta, x, y, z)
    return g**2

res = minimize(gmm_obj, 1, args=(x, y, z))
print(res.x)