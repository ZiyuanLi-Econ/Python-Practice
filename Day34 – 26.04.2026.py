import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as sc




################## ONE-TIME
beta0_true = 2
beta1_true = 5
beta2_true = -3

x = np.random.normal(size=(200, 2))
e = np.random.randn(200)

y = beta0_true + beta1_true * x[:, 0] + beta2_true * x[:, 1] + e

X = sm.add_constant(x)     # X = np.column_stack([np.ones(200), x])

# statsmodels
model = sm.OLS(y, X).fit()
print("statsmodels:", model.params)


# optimization
def sse(theta):
    y_hat = X @ theta
    return np.sum((y - y_hat) ** 2)

theta0 = [1, 1, 1]

res = sc.minimize(sse, theta0, method='BFGS')

print("optimization:", res.x)
print("success:", res.success)
print("message:", res.message)
print("SSE:", res.fun)


##
labels = ['beta0', 'beta1', 'beta2']
plt.plot(labels, [beta0_true, beta1_true,beta2_true], label='true')
plt.plot(labels, model.params, label='statsmodels')
plt.plot(labels, res.x, label='optimization')

plt.legend()
plt.title('Comparison')
plt.show()


#################SIMULATION
beta0_true = 2
beta1_true = 5
beta2_true = -3
true_beta = [beta0_true, beta1_true, beta2_true]

statsmodels_res = []
optimization_res = []

def sse(theta, X, y):
    y_hat = X @ theta
    return np.sum((y - y_hat) ** 2)

for i in range(1000):
    x = np.random.normal(size=(200, 2))
    e = np.random.randn(200)

    y = beta0_true + beta1_true * x[:, 0] + beta2_true * x[:, 1] + e
    X = sm.add_constant(x)

    # statsmodels
    model = sm.OLS(y, X).fit()
    statsmodels_res.append(model.params)

    # optimization
    theta0 = [1, 1, 1]
    res = sc.minimize(sse, theta0, args=(X, y), method='BFGS')
    optimization_res.append(res.x)

statsmodels_res = np.array(statsmodels_res)
optimization_res = np.array(optimization_res)

#mean
print("true:", [2,5,-3])
print("statsmodels mean:", statsmodels_res.mean(axis=0))
print("optimization mean:", optimization_res.mean(axis=0))

#SD
print("statsmodels std:", statsmodels_res.std(axis=0))
print("optimization std:", optimization_res.std(axis=0))

#rmse
rmse_sm = np.sqrt(np.mean((statsmodels_res - true_beta)**2, axis=0))
rmse_opt = np.sqrt(np.mean((optimization_res - true_beta)**2, axis=0))
print("RMSE statsmodels:", rmse_sm)
print("RMSE optimization:", rmse_opt)

