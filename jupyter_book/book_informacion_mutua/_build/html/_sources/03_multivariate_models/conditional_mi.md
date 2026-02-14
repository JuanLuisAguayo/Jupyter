# Información Mutua Condicional Multivariada

## Introducción

En sistemas multivariados complejos, las dependencias entre variables
no siempre son directas. Muchas relaciones observadas pueden deberse
a variables intermedias o factores latentes.

La información mutua condicional permite medir la dependencia entre
dos variables eliminando la influencia de una o más variables de control.

Este concepto es fundamental en:

- inferencia causal
- redes bayesianas
- selección de variables
- análisis de dependencia estructural
- aprendizaje automático moderno

---

## Definición General

Sean variables aleatorias:

$$
X,\ Y,\ Z.
$$

La información mutua condicional se define como:

$$
I(X;Y|Z)
=
H(X|Z)
-
H(X|Y,Z).
$$

También puede escribirse como:

$$
I(X;Y|Z)
=
H(X,Z)
+
H(Y,Z)
-
H(Z)
-
H(X,Y,Z).
$$

---

## Interpretación Informacional

La cantidad:

$$
I(X;Y|Z)
$$

mide la reducción de incertidumbre sobre $X$ al conocer $Y$,
una vez que ya conocemos $Z$.

Interpretación:

- dependencia directa residual
- información adicional
- asociación libre de confusores

---

## Caso Multivariado General

Sean vectores aleatorios:

$$
\mathbf{X},\ \mathbf{Y},\ \mathbf{Z}.
$$

La definición general es:

$$
I(\mathbf{X};\mathbf{Y}|\mathbf{Z})
=
H(\mathbf{X}|\mathbf{Z})
-
H(\mathbf{X}|\mathbf{Y},\mathbf{Z}).
$$

Equivalentemente:

$$
I(\mathbf{X};\mathbf{Y}|\mathbf{Z})
=
H(\mathbf{X},\mathbf{Z})
+
H(\mathbf{Y},\mathbf{Z})
-
H(\mathbf{Z})
-
H(\mathbf{X},\mathbf{Y},\mathbf{Z}).
$$

---

## Interpretación Geométrica

En términos de incertidumbre:

- $Z$ define el contexto informacional
- $Y$ aporta información adicional sobre $X$
- la dependencia medida es la parte irreducible
  una vez controlado $Z$

---

## Independencia Condicional

Si:

$$
X \perp Y \mid Z
$$

entonces:

$$
I(X;Y|Z)=0.
$$

Esto permite detectar:

- independencia estructural
- separación d-separation en grafos
- relaciones indirectas

---

## Propiedades Fundamentales

### No Negatividad

$$
I(X;Y|Z)\ge 0.
$$

---

### Simetría

$$
I(X;Y|Z)=I(Y;X|Z).
$$

---

### Regla de Cadena

$$
I(X;Y,Z)
=
I(X;Z)
+
I(X;Y|Z).
$$

---

### Expansión Multivariable

Para variables múltiples:

$$
I(X;Y_1,Y_2|Z)
=
I(X;Y_1|Z)
+
I(X;Y_2|Y_1,Z).
$$

---

## Relación con Grafos Probabilísticos

La información mutua condicional permite:

- aprender estructuras de redes bayesianas
- identificar aristas redundantes
- evaluar independencia estructural

Ejemplo:

$$
X \rightarrow Z \rightarrow Y
$$

puede implicar:

$$
I(X;Y)>0
$$

pero:

$$
I(X;Y|Z)=0.
$$

---

## Construcción de la Matriz de Información Mutua Condicional

Sea:

$$
\mathbf{X}=(X_1,\dots,X_n).
$$

Definimos la matriz condicionada a $Z$ como:

$$
M_{ij}^{(Z)}=I(X_i;X_j|Z).
$$

Aplicaciones:

- análisis estructural
- inferencia causal
- reducción de dimensionalidad

---

## Ejemplo Conceptual

Variables:

- Edad
- Presión arterial
- Índice de masa corporal
- Actividad física

Supongamos:

Edad → Presión
Edad → IMC
IMC → Presión

Entonces:

$$
I(IMC;Presión)>0
$$

pero posiblemente:

$$
I(IMC;Presión|Edad)
$$

disminuye significativamente.

---

## Aplicaciones en Ciencia de Datos

### Selección de Características

Detectar:

- redundancia indirecta
- variables irrelevantes
- efectos mediadores

---

### Aprendizaje Estructural

- redes bayesianas
- grafos probabilísticos
- modelos causales

---

### Deep Learning

- análisis de representaciones internas
- regularización informacional
- aprendizaje contrastivo

---

## Desafíos Computacionales

- estimación en alta dimensión
- sesgo en muestras pequeñas
- necesidad de estimadores robustos
- complejidad combinatoria

Métodos comunes:

- k-NN estimators
- métodos kernel
- modelos generativos
- normalizing flows

---

## Extensiones Avanzadas

- información mutua parcial
- información multivariada total
- sinergia e información redundante
- descomposición PID (Partial Information Decomposition)

---

## Conclusión

La información mutua condicional multivariada permite analizar
dependencias directas eliminando la influencia de variables de control.

Es una herramienta esencial para:

- inferencia causal
- modelamiento probabilístico
- análisis estructural
- aprendizaje automático moderno

En el siguiente capítulo se abordará el análisis de sistemas
de alta dimensión mediante herramientas computacionales
y notebooks experimentales.

{cite}`pearl2009causality`, {cite}`murphy2012ml`.