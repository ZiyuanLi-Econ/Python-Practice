import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import seaborn as sns
from scipy.optimize import minimize
from scipy.stats import norm


##Q3
#Q3.1
# Q3.1: Cournot duopoly equilibrium price

# inverse demand:
# p_i = 100 - q_i
# q_i = q_i1 + q_i2

# marginal costs:
# mc_i1 = exp(theta1 + theta2*x1_i + sigma*eps1_i)
# mc_i2 = exp(theta1 + theta2*x2_i + sigma*eps2_i)

# firm 1 profit:
# pi_i1 = (p_i - mc_i1) * q_i1
#       = (100 - q_i1 - q_i2 - mc_i1) * q_i1

# firm 2 profit:
# pi_i2 = (p_i - mc_i2) * q_i2
#       = (100 - q_i1 - q_i2 - mc_i2) * q_i2

# FOC firm 1:
# d pi_i1 / d q_i1 = 100 - 2*q_i1 - q_i2 - mc_i1 = 0

# FOC firm 2:
# d pi_i2 / d q_i2 = 100 - q_i1 - 2*q_i2 - mc_i2 = 0

# solving the two FOCs gives:
# q_i1 = (100 - 2*mc_i1 + mc_i2) / 3
# q_i2 = (100 - 2*mc_i2 + mc_i1) / 3

# equilibrium price:
# p_i = 100 - q_i1 - q_i2

# substitute q_i1 and q_i2:
# p_i = 100 - [(100 - 2*mc_i1 + mc_i2) / 3
#              + (100 - 2*mc_i2 + mc_i1) / 3]

# simplify:
# p_i = (100 + mc_i1 + mc_i2) / 3

# substitute marginal costs:
# p_i = (100
#        + exp(theta1 + theta2*x1_i + sigma*eps1_i)
#        + exp(theta1 + theta2*x2_i + sigma*eps2_i)) / 3


#Q3.2
# load data
df = pd.read_csv(r'C:\Users\17964\Desktop\Python\EIO\PS1\data3.dat', sep=',', header=None)
draws = pd.read_csv(r'C:\Users\17964\Desktop\Python\EIO\PS1\drawsml.dat', sep=r'\s+', header=None).values

# variables
p = df[0].values
x1 = df[1].values
x2 = df[2].values

n = len(p)
S = draws.shape[1]

# negative simulated log-likelihood
def neg_sml(params):
    theta1, theta2, kappa = params[0], params[1], params[2]
    sigma = np.exp(kappa)
    loglike = 0

    for i in range(n):

        eps2_draws = draws[i, :]
        mc2 = np.exp(theta1 + theta2 * x2[i] + sigma * eps2_draws)

        # price equation:
        # p = (100 + mc1 + mc2) / 3
        # solve for mc1:
        mc1_implied = 3 * p[i] - 100 - mc2

        # if mc1 <= 0, log(mc1) invalid
        valid = mc1_implied > 0

        if np.sum(valid) == 0:
            loglike += np.log(0.0001)
            continue

        mc1_valid = mc1_implied[valid]

        # invert eps1 from mc1
        eps1_implied = (np.log(mc1_valid) - theta1 - theta2 * x1[i]) / sigma

        # Jacobian term: |d eps1 / d p|
        jacobian = 3 / (sigma * mc1_valid)
        # density contribution
        density = norm.pdf(eps1_implied) * jacobian
        # integrate out eps2 by simulation average
        sim_density = np.mean(density)
        # avoid log of zero or negative
        sim_density = max(sim_density, 0.0001)
        loglike += np.log(sim_density)

    return -loglike


# starting values
start = np.array([0, 1, 0])

# derivative-free optimization
result = minimize(neg_sml, [0, 1, 0], method="Nelder-Mead")

theta1_hat = result.x[0]
theta2_hat = result.x[1]
kappa_hat  = result.x[2]

sigma_hat = np.exp(kappa_hat)
print("theta1 =", theta1_hat)
print("theta2 =", theta2_hat)
print("sigma  =", sigma_hat)
print("negative log-likelihood =", result.fun)


#Q3.3
# No, because the pricing equation contains two unobserved shocks but only one observed outcome pi. 
# Therefore, the model is not invertible: for a given observed price, 
# there are infinitely many combinations of (ε1i,ε2i) consistent with the data.
# As a result, the individual unobservables cannot be recovered from the observed data, 
# and moments based directly on ε1i or ε2i cannot be constructed.


#Q3.4
# variables
p = df.iloc[:, 0].values
x1 = df.iloc[:, 1].values
x2 = df.iloc[:, 2].values

n = len(p)
S = 20
# first 20 columns: eps1 draws
eps1_draws = draws[:, :20]
# second 20 columns: eps2 draws
eps2_draws = draws[:, 20:40]

# simulate E[p|x,theta] and E[p^2|x,theta]
def simulate_price_moments(params):
    theta1, theta2, kappa = params[0], params[1], params[2]
    sigma = np.exp(kappa)
    mc1 = np.exp(theta1 + theta2 * x1[:, None] + sigma * eps1_draws)
    mc2 = np.exp(theta1 + theta2 * x2[:, None] + sigma * eps2_draws)
    p_sim = (100 + mc1 + mc2) / 3
    Ep = np.mean(p_sim, axis=1)
    Ep2 = np.mean(p_sim ** 2, axis=1)
    return Ep, Ep2


# sample moments
def moments_q3(params):
    Ep, Ep2 = simulate_price_moments(params)
    resid_p = p - Ep
    resid_p2 = p ** 2 - Ep2

    m1 = np.mean(resid_p)
    m2 = np.mean(x1 * resid_p)
    m3 = np.mean(x2 * resid_p)
    m4 = np.mean(resid_p2)

    g = np.array([m1, m2, m3, m4])
    return g


# ---------- Stage 1 ----------
W1 = np.eye(4)
def objective_stage1(params):
    g = moments_q3(params)
    return g.T @ W1 @ g

result_stage1 = minimize(objective_stage1, [0, 1, 0], method="Nelder-Mead")

theta_init = result_stage1.x
print("Stage 1 estimates:")
print("theta1_init =", theta_init[0])
print("theta2_init =", theta_init[1])
print("sigma_init  =", np.exp(theta_init[2]))
print("objective   =", result_stage1.fun)

# ---------- Stage 2 ----------
Ep_init, Ep2_init = simulate_price_moments(theta_init)
resid_p_init = p - Ep_init
resid_p2_init = p ** 2 - Ep2_init

# individual moments, n x 4
g_i = np.column_stack((resid_p_init, x1 * resid_p_init, x2 * resid_p_init, resid_p2_init))
S_hat = (g_i.T @ g_i) / n
W2 = np.linalg.inv(S_hat)


def objective_stage2(params):
    g = moments_q3(params)
    return g.T @ W2 @ g

result_stage2 = minimize(objective_stage2, theta_init, method="Nelder-Mead")

theta_gmm = result_stage2.x
print("\nStage 2 estimates:")
print("theta1 =", theta_gmm[0])
print("theta2 =", theta_gmm[1])
print("sigma  =", np.exp(theta_gmm[2]))
print("objective =", result_stage2.fun)



#Q3.5
# Q3.5
# The additional moment: E[p_i^2 - E(p_i^2 | x1_i, x2_i, theta)] = 0 is important for identifying sigma.
# The first three moments mainly match the conditional mean: E[p_i | x1_i, x2_i], which mostly identifies theta1 and theta2.

# However, sigma controls the variance of the unobserved cost shocks: eps_1i and eps_2i.
# Different values of sigma can generate similar average prices,
# but they imply different levels of price dispersion.

# Therefore, the additional second-moment condition using p_i^2
# helps match the variance of prices in the data.

# This provides information about the dispersion of unobserved costs
# and helps identify sigma.