import numpy as np
from math import log2


def entropy(probabilities):
    """
    Calcula la entropía de Shannon H(X) en bits.
    Ignora probabilidades nulas.
    """
    return -sum(p * log2(p) for p in probabilities if p > 0)


def mutual_information(data):
    """
    Calcula entropías marginales, conjuntas e información mutua
    entre dos variables binarias.

    Variables:
    - Columna 0: Vejez (X)
    - Columna 1: Hipertensión (Y)

    data : array Nx2
    """
    N = len(data)

    # Probabilidades marginales
    px = np.array([np.sum(data[:, 0] == x) / N for x in (0, 1)])
    py = np.array([np.sum(data[:, 1] == y) / N for y in (0, 1)])

    # Probabilidades conjuntas
    pxy = np.zeros((2, 2))
    for x in (0, 1):
        for y in (0, 1):
            pxy[x, y] = np.sum(
                (data[:, 0] == x) & (data[:, 1] == y)
            ) / N

    # Entropías
    Hx = entropy(px)
    Hy = entropy(py)
    Hxy = entropy(pxy.flatten())

    # Información mutua
    Ixy = Hx + Hy - Hxy

    return Hx, Hy, Hxy, Ixy


if __name__ == "__main__":
    # Datos observacionales
    # [vejez, hipertensión]
    data = np.array([
        [0, 0],
        [1, 0],
        [1, 1],
        [1, 1],
        [1, 0],
        [1, 1],
        [1, 0]
    ])

    Hx, Hy, Hxy, Ixy = mutual_information(data)

    print("Resultados (en bits):")
    print(f"H(X)   = {Hx:.4f}")
    print(f"H(Y)   = {Hy:.4f}")
    print(f"H(X,Y) = {Hxy:.4f}")
    print(f"I(X;Y) = {Ixy:.4f}")
