# Clustering basado en Información Mutua

## Introducción

La información mutua constituye una herramienta fundamental para medir la dependencia estadística entre variables aleatorias.  
En ciencia de datos, se utiliza ampliamente para:

- Evaluar calidad de agrupamientos
- Diseñar funciones objetivo
- Comparar particiones
- Detectar estructura latente en datos

A diferencia de métricas basadas en distancia euclidiana, la información mutua captura relaciones no lineales y dependencias complejas.

---

## Definición de Información Mutua para Clustering

Sean:

- $C$ : etiquetas reales
- $\hat{C}$ : etiquetas obtenidas por el algoritmo de clustering

La información mutua se define como:

$$
I(C;\hat{C}) = \sum_{c,\hat{c}} P(c,\hat{c})
\log \frac{P(c,\hat{c})}{P(c)P(\hat{c})}
$$

Interpretación:

- $I=0$ → independencia total
- $I$ grande → fuerte concordancia estructural

---

## Normalized Mutual Information (NMI)

Para comparar clustering con distinto número de grupos se utiliza:

$$
NMI = \frac{I(C;\hat{C})}{\sqrt{H(C)H(\hat{C})}}
$$

Propiedades:

- $0 \leq NMI \leq 1$
- Invariante ante permutaciones de etiquetas
- Robusta frente a clusters desbalanceados

---

## Ajuste por Azar: Adjusted Mutual Information (AMI)

Corrige el sesgo introducido por coincidencias aleatorias:

$$
AMI = \frac{I - E[I]}{\max(H(C),H(\hat{C})) - E[I]}
$$

Ventajas:

- Penaliza coincidencias fortuitas
- Mejora comparabilidad entre modelos

---

## Ejemplo Conceptual

Supongamos:

- Clases reales: 3
- Clusters obtenidos: 3

Matriz de contingencia:

| Real / Pred | A | B | C |
|-------------|---|---|---|
| 1 | 30 | 2 | 1 |
| 2 | 3 | 25 | 2 |
| 3 | 1 | 4 | 28 |

A partir de esta tabla:

1. Se calcula $P(c,\hat{c})$
2. Se obtienen marginales
3. Se evalúa la suma de información mutua

Resultado esperado:

- NMI alto
- Buen alineamiento estructural

---

## Información Mutua como Función Objetivo

Algunos algoritmos maximizan directamente:

$$
\max I(X;Z)
$$

donde:

- $X$ datos originales
- $Z$ representación latente

Ejemplos:

- Information Bottleneck Clustering
- Deep InfoMax Clustering
- Spectral Clustering basado en MI

---

## Ventajas frente a Distancias Clásicas

| Métrica | Dependencias no lineales | Invarianza | Robustez |
|--------|--------------------------|------------|----------|
| Euclidiana | No | Baja | Media |
| Coseno | Parcial | Media | Media |
| Información Mutua | Sí | Alta | Alta |

---

## Limitaciones

- Estimación de probabilidades en alta dimensión
- Sensibilidad a discretización
- Costo computacional

Soluciones modernas:

- Estimadores kNN
- KDE
- Redes neuronales estimadoras de MI

---

## Conclusiones

La información mutua permite:

- Evaluar clustering sin suposiciones geométricas
- Capturar relaciones complejas
- Diseñar algoritmos robustos

Es especialmente útil en:

- Datos no lineales
- Variables categóricas
- Representaciones profundas

{cite}`bishop2006pattern`, {cite}`murphy2012ml`.