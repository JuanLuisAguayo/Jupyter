# Tablas Avanzadas de Teoría de la Información

## Introducción

Este apéndice reúne tablas de referencia rápida con definiciones, propiedades,
desigualdades fundamentales y relaciones estructurales entre medidas de la
teoría de la información.  
El objetivo es proporcionar un compendio operativo útil para investigación,
docencia y aplicaciones en ciencia de datos e ingeniería.

---

## B.1 Definiciones Fundamentales

| Medida | Definición Matemática | Interpretación |
|---|---|---|
| Entropía | $H(X)=-\sum_x P(x)\log P(x)$ | Incertidumbre promedio |
| Entropía conjunta | $H(X,Y)$ | Incertidumbre del sistema completo |
| Entropía condicional | $H(X\|Y)$ | Incertidumbre restante |
| Información mutua | $I(X;Y)$ | Dependencia estadística |
| MI condicional | $I(X;Y\|Z)$ | Dependencia condicionada |
| Divergencia KL | $D_{KL}(P\|\|Q)$ | Diferencia entre distribuciones |

---

## B.2 Relaciones Fundamentales

| Relación | Expresión |
|---|---|
| Regla de cadena | $H(X,Y)=H(X)+H(Y\|X)$ |
| MI por entropías | $I(X;Y)=H(X)+H(Y)-H(X,Y)$ |
| MI alternativa | $I(X;Y)=H(X)-H(X\|Y)$ |
| MI condicional | $I(X;Y\|Z)=H(X\|Z)-H(X\|Y,Z)$ |
| Cadena MI | $I(X;Y,Z)=I(X;Y)+I(X;Z\|Y)$ |

---

## B.3 Desigualdades Clásicas

| Desigualdad | Expresión |
|---|---|
| No negatividad KL | $D_{KL}(P\|\|Q)\ge0$ |
| No negatividad MI | $I(X;Y)\ge0$ |
| Subaditividad | $H(X,Y)\le H(X)+H(Y)$ |
| Monotonía | $H(X\|Y)\le H(X)$ |
| Procesamiento de datos | $I(X;Z)\le I(X;Y)$ |

---

## B.4 Propiedades Algebraicas

| Propiedad | Entropía | Información Mutua |
|---|---|---|
| Simetría | $H(X,Y)=H(Y,X)$ | $I(X;Y)=I(Y;X)$ |
| No negatividad | $H(X)\ge0$ | $I(X;Y)\ge0$ |
| Invariancia | Bajo permutaciones | Bajo permutaciones |
| Extensibilidad | Sí | Sí |

---

## B.5 Descomposición Multivariada

| Expansión | Expresión |
|---|---|
| Entropía triple | $H(X,Y,Z)=H(X)+H(Y\|X)+H(Z\|X,Y)$ |
| MI triple | $I(X;Y,Z)=I(X;Y)+I(X;Z\|Y)$ |
| MI cuádruple | $I(X;Y,Z,W)=I(X;Y)+I(X;Z\|Y)+I(X;W\|Y,Z)$ |

---

## B.6 Interpretaciones en Ciencia de Datos

| Medida | Uso típico |
|---|---|
| Entropía | Medición de complejidad |
| MI | Selección de características |
| MI condicional | Eliminación de redundancia |
| KL | Evaluación de modelos |
| Entropía conjunta | Modelado multivariado |

---

## B.7 Propiedades en Aprendizaje Automático

| Contexto | Uso de MI |
|---|---|
| Feature Selection | Ranking informacional |
| Clustering | Medida de similitud |
| Deep Learning | Bottleneck informacional |
| Representaciones latentes | Maximización MI |
| Regularización | Penalización KL |

---

## B.8 Propiedades de Independencia

| Condición | Consecuencia |
|---|---|
| Independencia | $I(X;Y)=0$ |
| Independencia condicional | $I(X;Y\|Z)=0$ |
| Cadena de Markov | Procesamiento de datos |
| Factorización | $P(x,y)=P(x)P(y)$ |

---

## B.9 Propiedades Diferenciales (Continuas)

| Medida | Forma Continua |
|---|---|
| Entropía diferencial | $h(X)=-\int p(x)\log p(x)\,dx$ |
| MI continua | Integral doble |
| KL continua | Integral sobre densidades |

---

## B.10 Complejidad Computacional (Estimación MI)

| Método | Complejidad Aproximada |
|---|---|
| Histogramas | $O(n)$ |
| KDE | $O(n^2)$ |
| kNN | $O(n\log n)$ |
| MINE | Dependiente del modelo |

---

## B.11 Resumen de Relaciones Clave

$$
\begin{aligned}
I(X;Y) &= H(X)-H(X|Y) \\
I(X;Y) &= D_{KL}(P(X,Y)||P(X)P(Y)) \\
H(X,Y) &= H(X)+H(Y|X) \\
I(X;Y|Z) &= H(X|Z)-H(X|Y,Z)
\end{aligned}
$$

---

## Conclusión del Apéndice

Las tablas anteriores sintetizan las relaciones estructurales más importantes
de la teoría de la información y constituyen una referencia rápida para:

- desarrollo teórico
- análisis estadístico
- modelamiento multivariado
- aplicaciones en ciencia de datos y aprendizaje automático
