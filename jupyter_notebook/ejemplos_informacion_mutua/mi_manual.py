import numpy as np

def entropy(p):
    """Entropía de Shannon"""
    p = p[p > 0]
    return -np.sum(p * np.log2(p))

def mutual_information(x, y):
    """MI discreta desde la definición"""
    joint_xy = np.histogram2d(x, y, bins=10)[0]
    joint_xy /= joint_xy.sum()

    px = joint_xy.sum(axis=1)
    py = joint_xy.sum(axis=0)

    Hx = entropy(px)
    Hy = entropy(py)
    Hxy = entropy(joint_xy.flatten())

    return Hx + Hy - Hxy

# Ejemplo numérico
np.random.seed(1)
x = np.random.randint(0, 5, 1000)
y = x + np.random.randint(0, 2, 1000)  # correlación fuerte

print("Información mutua (manual):", mutual_information(x, y))
