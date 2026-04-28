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
# =========================
# 1️⃣ 生成数据（真实世界）
# =========================
data = norm.rvs(loc=15, scale=7, size=100)
# 从 N(15, 7^2) 抽100个样本
# 👉 真实参数：μ=15, σ=7


# =========================
# 2️⃣ 定义目标函数（负对数似然）
# =========================
def neg_loglik(theta, data):
    mu, sigma = theta  # theta = [μ, σ]

    # ❗ 如果 sigma 非法（<=0），直接返回很大值，避免优化器跑飞
    if sigma <= 0:
        return 1e10

    # logpdf：每个点的对数密度（“合理程度”）
    # sum：所有点加起来 = 总体评分（log-likelihood）
    # 加负号：因为 minimize 只能做“最小化”
    return -np.sum(norm.logpdf(data, loc=mu, scale=sigma))


# =========================
# 3️⃣ 调用优化器（MLE核心）
# =========================
res = minimize(
    neg_loglik,
    x0=[0, 1],                 # 初始猜测：μ=0, σ=1
    args=(data,),              # 把 data 传入函数
    bounds=[(None, None), (1e-6, None)]  # 限制 σ > 0
)
