import numpy as np
import scipy.optimize as sc
import matplotlib.pyplot as plt

def objective(theta):
    return (theta[0]-3)**2 + (theta[1]-2)**2

theta0 = np.array([0,0])
bounds = [(None,None),(0,3)]
res = sc.minimize(objective,theta0, method='L-BFGS-B', bounds=bounds)

print(res.x, res.success, res.message)


#
np.random.seed(555)

n=100
x=np.random.uniform(1,5,size=n)
beta0_true=1
beta1_true=2
beta2_true=0.5
error = np.random.normal(0, 0.5, size=n)

y = beta0_true + beta1_true*x **beta2_true + error
#plt.scatter(x,y)
#plt.show()

def sse(theta):
    beta0, beta1, beta2 = theta
    y_hat = beta0 + beta1*x**beta2
    return np.sum((y - y_hat)**2)

theta0 = [0,1,1]
bounds = [(None,None),(0,10),(0,5)]
res = sc.minimize(sse,theta0,method='L-BFGS-B',bounds=bounds)
print(res.x, res.success, res.message, res.fun)