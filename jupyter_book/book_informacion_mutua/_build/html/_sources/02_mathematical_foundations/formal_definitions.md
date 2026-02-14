# Definiciones Formales

## Introducción

En los capítulos anteriores se presentaron las definiciones clásicas
de entropía e información mutua para variables discretas. Sin embargo,
para desarrollar resultados rigurosos y extensiones multivariadas es
necesario establecer un marco formal basado en teoría de la medida
y probabilidad moderna.

Este capítulo introduce:

- espacios de probabilidad
- variables aleatorias medibles
- distribuciones conjuntas y marginales
- definiciones generales de entropía
- información mutua en espacios generales

---

## Espacio de Probabilidad

Un espacio de probabilidad se define como la terna

$$
(\Omega,\mathcal{F},P)
$$

donde:

- $\Omega$ es el espacio muestral
- $\mathcal{F}$ es una $\sigma$-álgebra de eventos
- $P:\mathcal{F}\to[0,1]$ es una medida de probabilidad

cumpliendo:

1. $P(\Omega)=1$
2. $P(A)\ge0$
3. aditividad numerable

$$
P\left(\bigcup_i A_i\right)=\sum_i P(A_i)
$$

para eventos disjuntos.

---

## Variables Aleatorias

Una variable aleatoria es una función medible

$$
X:\Omega\rightarrow \mathbb{R}
$$

tal que

$$
X^{-1}(B)\in \mathcal{F}
$$

para todo conjunto boreliano $B$.

Tipos relevantes:

- discretas
- continuas
- mixtas
- vectoriales
- procesos estocásticos

---

## Distribuciones de Probabilidad

Sea $(X,Y)$ un vector aleatorio.

### Distribución Conjunta

$$
P_{X,Y}(A\times B)=P(X\in A, Y\in B).
$$

### Distribuciones Marginales

$$
P_X(A)=P(X\in A)
$$

$$
P_Y(B)=P(Y\in B)
$$

### Independencia

Las variables son independientes si

$$
P_{X,Y}=P_X\otimes P_Y.
$$

---

## Entropía General

### Caso Discreto

$$
H(X)=-\sum_x P(x)\log P(x).
$$

### Caso Continuo (Entropía Diferencial)

Si $X$ tiene densidad $f(x)$:

$$
h(X)=-\int f(x)\log f(x)\,dx.
$$

Observaciones:

- puede ser negativa
- depende de la escala
- no es invariante ante transformaciones generales

---

## Entropía Condicional

### Forma General

$$
H(X|Y)=\mathbb{E}_{Y}[H(X|Y=y)].
$$

Caso discreto:

$$
H(X|Y)=-\sum_{x,y}P(x,y)\log P(x|y).
$$

---

## Entropía Conjunta

$$
H(X,Y)=-\sum_{x,y}P(x,y)\log P(x,y).
$$

Regla de la cadena:

$$
H(X,Y)=H(X)+H(Y|X).
$$

---

## Información Mutua General

La definición más general se formula mediante divergencia KL:

$$
I(X;Y)=D_{KL}(P_{X,Y}\,\|\,P_X\otimes P_Y).
$$

Caso discreto:

$$
I(X;Y)=\sum_{x,y}P(x,y)
\log\frac{P(x,y)}{P(x)P(y)}.
$$

Caso continuo:

$$
I(X;Y)=\int\int p(x,y)\log
\frac{p(x,y)}{p(x)p(y)}dxdy.
$$

---

## Información Mutua Condicional

Definición general:

$$
I(X;Y|Z)=
\mathbb{E}_Z
\left[
D_{KL}(P_{X,Y|Z}\,\|\,P_{X|Z}P_{Y|Z})
\right].
$$

Forma entrópica:

$$
I(X;Y|Z)=H(X|Z)-H(X|Y,Z).
$$

---

## Información Mutua Multivariada

Para un vector aleatorio

$$
\mathbf{X}=(X_1,\dots,X_n)
$$

la información total se define como

$$
TC(\mathbf{X})=
D_{KL}(P_{\mathbf{X}}\,
\|\,\prod_i P_{X_i}).
$$

Interpretación:

- mide dependencia global
- base para modelos multivariados
- fundamento de matrices de información mutua

---

## Variables Aleatorias Vectoriales

Sea

$$
\mathbf{X}\in \mathbb{R}^d.
$$

La entropía diferencial multivariada:

$$
h(\mathbf{X})=-\int f(\mathbf{x})
\log f(\mathbf{x})\,d\mathbf{x}.
$$

Información mutua vectorial:

$$
I(\mathbf{X};\mathbf{Y})
=D_{KL}(P_{\mathbf{X},\mathbf{Y}}
\|P_{\mathbf{X}}P_{\mathbf{Y}}).
$$

---

## Independencia Condicional

Las variables $X$ e $Y$ son independientes dado $Z$ si

$$
P_{X,Y|Z}=P_{X|Z}P_{Y|Z}.
$$

Equivalente a

$$
I(X;Y|Z)=0.
$$

---

## Notación Funcional

Se utilizarán las siguientes convenciones:

- letras mayúsculas: variables aleatorias
- minúsculas: realizaciones
- negrita: vectores aleatorios
- $\mathbb{E}$: esperanza
- $D_{KL}$: divergencia de Kullback–Leibler

---

## Ejemplo Formal Discreto

Sea:

$$
X,Y\in\{0,1\}.
$$

Distribución conjunta:

$$
P(0,0)=0.4,\quad
P(0,1)=0.1,
$$

$$
P(1,0)=0.2,\quad
P(1,1)=0.3.
$$

Marginales:

$$
P_X(0)=0.5,\quad
P_X(1)=0.5
$$

$$
P_Y(0)=0.6,\quad
P_Y(1)=0.4.
$$

Información mutua:

$$
I(X;Y)=\sum_{x,y}P(x,y)
\log\frac{P(x,y)}{P(x)P(y)}.
$$

Este ejemplo se retomará en capítulos posteriores para:

- matrices de información mutua
- modelos multivariados
- clustering informacional

---

## Conclusión

Las definiciones formales introducidas permiten extender los conceptos
clásicos de entropía e información mutua hacia:

- espacios generales de probabilidad
- variables continuas y vectoriales
- modelos multivariados complejos
- ciencia de datos moderna

Este formalismo servirá como base para el desarrollo riguroso de
propiedades matemáticas y teoremas en el siguiente capítulo.

{cite}`csiszar2011information`, {cite}`cover2006elements`