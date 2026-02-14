import math

# Definición de la distribución conjunta P(X,Y)
# Formato: P[(X, Y)] = probabilidad
P_xy = {
    ("Soleado", "No"): 0.50,
    ("Soleado", "Sí"): 0.10,
    ("Lluvioso", "No"): 0.10,
    ("Lluvioso", "Sí"): 0.30
}

# Paso 1: calcular la distribución marginal P(Y)
P_y = {}
for (x, y), p in P_xy.items():
    P_y[y] = P_y.get(y, 0) + p

# Paso 2: calcular la entropía condicional H(X|Y)
H_X_given_Y = 0.0

for (x, y), p_xy in P_xy.items():
    p_y = P_y[y]
    p_x_given_y = p_xy / p_y

    # Evitar log(0)
    if p_x_given_y > 0:
        H_X_given_Y -= p_xy * math.log2(p_x_given_y)

# Mostrar resultados
print("Distribución marginal P(Y):")
for y, p in P_y.items():
    print(f"P(Y={y}) = {p:.2f}")

print(f"\nEntropía condicional H(X|Y) = {H_X_given_Y:.4f} bits")