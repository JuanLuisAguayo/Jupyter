import numpy as np
from sklearn.neighbors import KernelDensity

def kde_entropy(samples, bandwidth=0.3):
    kde = KernelDensity(kernel="gaussian", bandwidth=bandwidth)
    kde.fit(samples)
    log_probs = kde.score_samples(samples)
    return -np.mean(log_probs)

def mi_kde(x, y, bandwidth=0.3):
    xy = np.vstack([x, y]).T
    Hx = kde_entropy(x.reshape(-1, 1), bandwidth)
    Hy = kde_entropy(y.reshape(-1, 1), bandwidth)
    Hxy = kde_entropy(xy, bandwidth)
    return Hx + Hy - Hxy

np.random.seed(2)
x = np.random.randn(300)
y = x + 0.2 * np.random.randn(300)

print("MI (KDE):", mi_kde(x, y))
