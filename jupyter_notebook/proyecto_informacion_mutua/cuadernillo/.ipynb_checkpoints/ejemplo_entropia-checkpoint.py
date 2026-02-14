import math

def entropia_shannon(probabilidades):
    """
    Calcula la entropía de Shannon en bits.
    
    Parámetros:
    probabilidades (dict): diccionario con eventos como claves y probabilidades como valores
    
    Retorna:
    float: entropía en bits
    """
    H = 0.0
    for evento, p in probabilidades.items():
        if p > 0:
            H -= p * math.log2(p)
    return H


# Probabilidades del sistema de alertas
alertas = {
    "Verde": 0.65,
    "Amarillo": 0.25,
    "Naranja": 0.08,
    "Rojo": 0.02
}

# Cálculo de la entropía
H = entropia_shannon(alertas)

print(f"Entropía del sistema de alertas: H(X) = {H:.4f} bits")
