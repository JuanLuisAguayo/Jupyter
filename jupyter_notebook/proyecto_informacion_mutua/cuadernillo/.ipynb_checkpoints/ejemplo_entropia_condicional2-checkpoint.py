import math

# Definición de la distribución conjunta P(X,Y)
# Formato: P[(X, Y)] = probabilidad
P_xy = {
    ("Soleado", "No"): 0.50,
    ("Soleado", "Sí"): 0.10,
    ("Lluvioso", "No"): 0.10,
    ("Lluvioso", "Sí"): 0.30
}

# Paso 1: calcular la distribución marginal P(X)
P_x = {}
for (x, y), p in P_xy.items():
    P_x[x] = P_x.get(x, 0) + p

# Paso 2: calcular la entropía condicional H(Y|X)
H_Y_given_X = 0.0

for (x, y), p_xy in P_xy.items():
    p_x = P_x[x]
    p_y_given_x = p_xy / p_x

    # Evitar log(0)
    if p_y_given_x > 0:
        H_Y_given_X -= p_xy * math.log2(p_y_given_x)

# Mostrar resultados
print("Distribución marginal P(X):")
for x, p in P_x.items():
    print(f"P(X={x}) = {p:.2f}")

print(f"\nEntropía condicional H(Y|X) = {H_Y_given_X:.4f} bits")
