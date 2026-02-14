import numpy as np
from sklearn.feature_selection import mutual_info_classif, mutual_info_regression

np.random.seed(0)

X = np.random.rand(1000, 1)
y = X[:, 0] * 3 + np.random.normal(0, 0.1, 1000)  # relación casi lineal

mi = mutual_info_regression(X, y, discrete_features=False)
print("Información mutua con sklearn:", mi[0])
