# Entropía Conjunta y Entropía Condicional

## Introducción

En teoría de la información, la **entropía conjunta** y la **entropía condicional**
permiten cuantificar la incertidumbre total de sistemas multivariables y la
incertidumbre residual de una variable cuando otra es conocida.

Estas cantidades constituyen la base formal para definir medidas más avanzadas
como la información mutua, la información mutua condicional y diversas medidas
de dependencia estadística en modelos multivariados.

---

## Entropía Conjunta

### Definición

Sean $X$ y $Y$ variables aleatorias discretas con distribución conjunta
$P(X,Y)$. La entropía conjunta se define como

$$
H(X,Y) = - \sum_{x} \sum_{y} P(x,y)\,\log P(x,y).
$$

---

### Interpretación

La entropía conjunta mide:

- La incertidumbre total del sistema formado por $(X,Y)$.
- La cantidad promedio de información necesaria para describir simultáneamente
  ambas variables.

---

### Propiedades

1. **Simetría**

$$
H(X,Y)=H(Y,X)
$$

2. **No negatividad**

$$
H(X,Y)\ge 0
$$

3. **Independencia**

Si $X$ e $Y$ son independientes:

$$
H(X,Y)=H(X)+H(Y)
$$

---

### Ejemplo Resuelto

Considere la distribución:

|X|Y|P(X,Y)|
|---|---|---|
|0|0|0.25|
|0|1|0.25|
|1|0|0.25|
|1|1|0.25|

Entonces

$$
H(X,Y) = -4(0.25\log 0.25)
$$

$$
= -\log 0.25
$$

$$
= 2 \text{ bits}.
$$

Interpretación: el sistema posee incertidumbre máxima para dos variables binarias
equiprobables e independientes.

---

## Entropía Condicional

### Definición

La entropía condicional de $X$ dado $Y$ es

$$
H(X|Y) = - \sum_{x,y} P(x,y)\log P(x|y).
$$

Equivalentemente

$$
H(X|Y) = \sum_y P(y)\,H(X|Y=y).
$$

---

### Interpretación

Mide:

- La incertidumbre restante de $X$ después de conocer $Y$.
- El promedio de incertidumbre de $X$ dentro de cada subconjunto definido por
  valores de $Y$.

---

### Casos Extremos

1. **Dependencia Determinística**

Si $X=f(Y)$

$$
H(X|Y)=0
$$

2. **Independencia**

Si $X$ e $Y$ son independientes

$$
H(X|Y)=H(X)
$$

---

### Ejemplo Resuelto

Suponga la distribución:

|Clima $X$|Congestión $Y$|P(X,Y)|
|---|---|---|
|Soleado|No|0.50|
|Soleado|Sí|0.10|
|Lluvioso|No|0.15|
|Lluvioso|Sí|0.25|

Marginal de $Y$:

$$
P(Y=No)=0.65,\quad P(Y=Sí)=0.35.
$$

Probabilidades condicionales:

$$
P(Soleado|No)=0.769,\quad P(Lluvioso|No)=0.231
$$

$$
P(Soleado|Sí)=0.286,\quad P(Lluvioso|Sí)=0.714
$$

Entropías condicionadas:

$$
H(X|No)=0.78 \text{ bits}
$$

$$
H(X|Sí)=0.86 \text{ bits}
$$

Entropía condicional total:

$$
H(X|Y)=0.65(0.78)+0.35(0.86)=0.81 \text{ bits}.
$$

Interpretación: conocer la congestión reduce parcialmente la incertidumbre del
clima, pero no completamente.

---

## Relación Fundamental (Regla de la Cadena)

La relación central entre estas cantidades es

$$
H(X,Y)=H(Y)+H(X|Y)
$$

y también

$$
H(X,Y)=H(X)+H(Y|X).
$$

---

### Demostración Esquemática

Partiendo de

$$
P(x,y)=P(x|y)P(y)
$$

entonces

$$
H(X,Y) = -\sum_{x,y} P(x,y)\log[P(x|y)P(y)].
$$

Separando logaritmos

$$
H(X,Y)=H(Y)+H(X|Y).
$$

---

## Interpretación Geométrica

En términos conceptuales:

- $H(X)$ representa la incertidumbre total de $X$.
- $H(X|Y)$ es la porción no explicada por $Y$.
- La diferencia $H(X)-H(X|Y)$ corresponde a información compartida
  (información mutua).

---

## Aplicaciones

- Modelado de dependencia estadística
- Selección de características
- Sistemas de comunicación
- Aprendizaje profundo
- Modelos probabilísticos multivariados

---

## Conclusión

La entropía conjunta y la entropía condicional constituyen herramientas
fundamentales para descomponer la incertidumbre en sistemas multivariados.
Estas cantidades permiten comprender la estructura informacional entre
variables y preparan el camino para la formulación formal de la información
mutua, estudiada en el siguiente capítulo.

{cite}`mackay2003information`, {cite}`cover2006elements`