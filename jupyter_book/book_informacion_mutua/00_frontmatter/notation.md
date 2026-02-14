# Notación y Convenciones Matemáticas

Este capítulo establece las convenciones matemáticas, probabilísticas e informacionales utilizadas a lo largo del libro. La notación ha sido diseñada para mantener coherencia con la literatura científica moderna en teoría de la información, estadística matemática y ciencia de datos.

---

## 1. Conjuntos y Espacios

- $\mathbb{R}$ : conjunto de los números reales.
- $\mathbb{R}^n$ : espacio euclidiano de dimensión $n$.
- $\mathcal{X}, \mathcal{Y}, \mathcal{Z}$ : espacios de valores de variables aleatorias.
- $\Omega$ : espacio muestral.
- $\mathcal{F}$ : $\sigma$-álgebra asociada al espacio de probabilidad.
- $(\Omega, \mathcal{F}, \mathbb{P})$ : espacio de probabilidad.

---

## 2. Variables Aleatorias y Distribuciones

- $X, Y, Z$ : variables aleatorias.
- $\mathbf{X}$ : vector aleatorio multivariado.
- $x, y, z$ : realizaciones específicas de variables aleatorias.
- $p(x)$ : función de masa de probabilidad.
- $f(x)$ : función de densidad de probabilidad.
- $p(x,y)$ : distribución conjunta.
- $p(x|y)$ : distribución condicional.

Distribuciones marginales:

$$
p(x) = \sum_y p(x,y)
$$

o en el caso continuo,

$$
f(x) = \int f(x,y)\,dy.
$$

---

## 3. Operadores Probabilísticos

- $\mathbb{P}(A)$ : probabilidad de un evento $A$.
- $\mathbb{E}[X]$ : esperanza matemática.
- $\mathrm{Var}(X)$ : varianza.
- $\mathrm{Cov}(X,Y)$ : covarianza.

Esperanza condicional:

$$
\mathbb{E}[X|Y].
$$

---

## 4. Entropía e Información

Entropía de Shannon:

$$
H(X) = -\sum_x p(x)\log p(x).
$$

Entropía conjunta:

$$
H(X,Y).
$$

Entropía condicional:

$$
H(X|Y).
$$

Información mutua:

$$
I(X;Y).
$$

Información mutua condicional:

$$
I(X;Y|Z).
$$

Divergencia de Kullback–Leibler:

$$
D_{KL}(P\|Q).
$$

---

## 5. Vectores y Matrices Informacionales

- $\mathbf{X} = (X_1,\dots,X_n)$ : vector aleatorio.
- $\Sigma$ : matriz de covarianza.
- $\mathbf{M}$ : matriz de información mutua.
- $M_{ij}$ : información mutua entre $X_i$ y $X_j$.

---

## 6. Convenciones Tipográficas

- Variables aleatorias: letras mayúsculas ($X, Y, Z$).
- Observaciones: letras minúsculas ($x, y, z$).
- Vectores: negrita ($\mathbf{X}$).
- Conjuntos: caligráfico ($\mathcal{X}$).
- Operadores matemáticos: roman upright (ej. $\mathrm{Var}$).

---

## 7. Notación para Aprendizaje Automático

- $\mathbf{X}$ : matriz de datos.
- $\mathbf{z}$ : representación latente.
- $\theta$ : parámetros de modelos.
- $\mathcal{L}(\theta)$ : función de pérdida.
- $\hat{\theta}$ : estimador.

---

## 8. Convenciones Logarítmicas

A menos que se indique lo contrario:

- $\log$ denota logaritmo base 2.
- Las unidades de información se expresan en bits.

---

## 9. Comentarios Finales

Las definiciones matemáticas detalladas y demostraciones formales se presentan en capítulos posteriores. La notación aquí introducida se utilizará consistentemente a lo largo del texto para garantizar precisión conceptual y coherencia estructural.
