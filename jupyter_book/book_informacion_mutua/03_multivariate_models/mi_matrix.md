# Matriz de Información Mutua

## Introducción

En sistemas multivariados resulta fundamental cuantificar
las dependencias entre múltiples variables aleatorias.

Mientras que la información mutua clásica mide la dependencia
entre dos variables, la matriz de información mutua permite
extender este concepto a conjuntos de variables.

Aplicaciones principales:

- análisis multivariado
- selección de características
- aprendizaje automático
- análisis de redes complejas
- modelamiento probabilístico de alta dimensión

---

## Definición del Sistema Multivariado

Sea un vector aleatorio:

$$
\mathbf{X} = (X_1,X_2,\dots,X_n).
$$

Cada variable tiene distribución marginal:

$$
P_{X_i}.
$$

La distribución conjunta es:

$$
P_{X_1,\dots,X_n}.
$$

---

## Definición de la Matriz de Información Mutua

La matriz de información mutua se define como:

$$
\mathbf{M} =
[I(X_i;X_j)]_{i,j=1}^n.
$$

Donde cada entrada es:

$$
M_{ij}=I(X_i;X_j).
$$

---

## Estructura de la Matriz

### Diagonal

$$
M_{ii}=H(X_i).
$$

Interpretación:

la información mutua de una variable consigo misma
equivale a su entropía.

---

### Simetría

$$
I(X_i;X_j)=I(X_j;X_i).
$$

Por lo tanto:

$$
\mathbf{M}
$$

es una matriz simétrica.

---

## Interpretación Informacional

Cada elemento mide:

- reducción de incertidumbre
- dependencia estadística
- redundancia informacional
- relación funcional potencial

Valores altos ⇒ fuerte dependencia.

Valores cercanos a cero ⇒ independencia.

---

## Relación con la Matriz de Covarianza

| Aspecto | Covarianza | Información Mutua |
|---|---|---|
| Tipo de dependencia | Lineal | General |
| Sensibilidad | Baja a no linealidad | Alta |
| Invarianza a transformaciones | Limitada | Más robusta |
| Aplicación | Estadística clásica | Ciencia de datos moderna |

La matriz de información mutua detecta:

- dependencias no lineales
- relaciones complejas
- interacciones ocultas

---

## Construcción Práctica

### Paso 1: Estimar distribuciones

- histogramas
- KDE
- estimadores k-NN
- modelos probabilísticos

### Paso 2: Calcular información mutua

$$
I(X_i;X_j)
=
H(X_i)+H(X_j)-H(X_i,X_j).
$$

### Paso 3: Construir la matriz

Para todo par:

$$
(i,j).
$$

---

## Ejemplo Conceptual

Sea:

$$
(X_1,X_2,X_3).
$$

La matriz es:

$$
\begin{pmatrix}
H(X_1) & I(X_1;X_2) & I(X_1;X_3) \\
I(X_2;X_1) & H(X_2) & I(X_2;X_3) \\
I(X_3;X_1) & I(X_3;X_2) & H(X_3)
\end{pmatrix}.
$$

---

## Propiedades Matemáticas

### No Negatividad

$$
M_{ij}\ge 0.
$$

---

### Simetría

$$
\mathbf{M}=\mathbf{M}^T.
$$

---

### Dependencia Funcional

Si:

$$
X_j=f(X_i)
$$

entonces:

$$
I(X_i;X_j)=H(X_j).
$$

---

## Interpretación Geométrica

La matriz define un grafo informacional:

- nodos = variables
- pesos = información mutua

Esto permite:

- análisis de redes
- clustering estructural
- inferencia causal preliminar

---

## Uso en Ciencia de Datos

### Selección de Variables

Identificar:

- redundancia
- variables irrelevantes
- grupos altamente dependientes

---

### Modelos Generativos

Detectar:

- estructuras probabilísticas
- correlaciones ocultas
- dependencias jerárquicas

---

### Deep Learning

- análisis de representaciones internas
- aprendizaje auto-supervisado
- regularización informacional

---

## Ejemplo Conceptual de Ciencia de Datos

Variables:

- Edad
- Presión arterial
- Índice de masa corporal
- Nivel de actividad

La matriz permite:

- detectar redundancia clínica
- analizar interacción fisiológica
- reducir dimensionalidad

---

## Limitaciones

- estimación difícil en alta dimensión
- sesgo en muestras pequeñas
- necesidad de estimadores robustos
- costo computacional elevado

---

## Extensiones

- matriz de información mutua condicional
- grafos de información
- redes bayesianas
- matrices normalizadas

---

## Conclusión

La matriz de información mutua generaliza el concepto
de dependencia informacional al contexto multivariado.

Proporciona una herramienta poderosa para:

- análisis estadístico avanzado
- aprendizaje automático
- ciencia de datos moderna
- modelamiento probabilístico de alta dimensión

En el siguiente capítulo se desarrollará la
información mutua condicional multivariada,
clave para analizar dependencias indirectas
y relaciones causales complejas.

{cite}`murphy2012ml`