# Divergencia de Kullback–Leibler

## Introducción

La divergencia de Kullback–Leibler (KL) es una medida fundamental
de la diferencia entre dos distribuciones de probabilidad.

En teoría de la información, cuantifica la cantidad de información
perdida al aproximar una distribución verdadera mediante otra.

En ciencia de datos y aprendizaje automático aparece en:

- aprendizaje profundo
- modelos generativos
- inferencia variacional
- selección de modelos
- regularización informacional

---

## Definición Formal (Variables Discretas)

Sean $P$ y $Q$ dos distribuciones sobre el mismo espacio.

La divergencia KL se define como:

$$
D_{KL}(P\|Q)=
\sum_x P(x)\log\frac{P(x)}{Q(x)}.
$$

Interpretación:

- mide discrepancia probabilística
- no es una distancia métrica
- es una medida direccional

---

## Definición Continua

Para variables continuas:

$$
D_{KL}(P\|Q)=
\int p(x)\log\frac{p(x)}{q(x)}dx.
$$

---

## Interpretación Informacional

Reescribiendo:

$$
D_{KL}(P\|Q)
=
-\sum P(x)\log Q(x)
-
H(P).
$$

Interpretación:

- diferencia entre entropía cruzada y entropía real
- exceso de longitud de código
- pérdida de eficiencia de compresión

---

## Propiedades Fundamentales

### No Negatividad

$$
D_{KL}(P\|Q)\ge 0.
$$

Igualdad solo si:

$$
P=Q.
$$

---

### No Simetría

$$
D_{KL}(P\|Q)\neq D_{KL}(Q\|P).
$$

Consecuencia:

no es una métrica.

---

### No Cumple Desigualdad Triangular

No define distancia geométrica clásica.

---

### Convexidad

La divergencia KL es convexa respecto a $Q$.

Importancia:

- optimización convexa
- aprendizaje probabilístico
- estabilidad numérica

---

## Relación con Entropía Cruzada

Definición:

$$
H(P,Q)=
-\sum P(x)\log Q(x).
$$

Entonces:

$$
D_{KL}(P\|Q)=H(P,Q)-H(P).
$$

---

## Relación con Información Mutua

Recordemos:

$$
I(X;Y)=
D_{KL}(P_{X,Y}\|P_XP_Y).
$$

Interpretación:

la información mutua mide desviación respecto a independencia.

---

## Ejemplo Discreto

Sea:

$$
P=(0.6,0.4),
\quad
Q=(0.5,0.5).
$$

Entonces:

$$
D_{KL}(P\|Q)
=
0.6\log\frac{0.6}{0.5}
+
0.4\log\frac{0.4}{0.5}.
$$

Calculando:

$$
=0.6\log(1.2)+0.4\log(0.8).
$$

Resultado positivo ⇒ distribuciones diferentes.

---

## Ejemplo Interpretativo (Modelo Mal Especificado)

Supongamos:

- distribución real: $P$
- modelo estimado: $Q$

La divergencia KL mide:

- error informacional del modelo
- pérdida de eficiencia predictiva

Aplicaciones:

- modelos bayesianos
- machine learning
- selección de arquitectura

---

## Divergencia KL Condicional

Para variables:

$$
D_{KL}(P(X|Y)\|Q(X|Y)).
$$

Definición promedio:

$$
\mathbb{E}_Y
\left[
D_{KL}(P(X|Y)\|Q(X|Y))
\right].
$$

Uso:

- modelos jerárquicos
- inferencia variacional
- redes probabilísticas

---

## Descomposición de KL

Para variables conjuntas:

$$
D_{KL}(P(X,Y)\|Q(X,Y))
=
D_{KL}(P(X)\|Q(X))
+
D_{KL}(P(Y|X)\|Q(Y|X)).
$$

Importancia:

- modelos estructurados
- factorización probabilística
- aprendizaje profundo

---

## KL en Aprendizaje Automático

### Función de Pérdida

Muchos modelos minimizan:

$$
D_{KL}(P_{datos}\|P_{modelo}).
$$

Ejemplos:

- modelos generativos
- VAE
- language models

---

### Regularización

KL controla:

- complejidad del modelo
- sobreajuste
- divergencia respecto a prior

---

## Inferencia Variacional

Objetivo:

aproximar posterior:

$$
p(z|x)
$$

mediante:

$$
q(z).
$$

Minimizando:

$$
D_{KL}(q(z)\|p(z|x)).
$$

Base matemática de:

- autoencoders variacionales
- modelos bayesianos modernos

---

## Relación con Otras Medidas

- Jensen–Shannon divergence
- Total variation
- Wasserstein distance

KL destaca por:

- tractabilidad analítica
- diferenciabilidad
- conexión directa con entropía

---

## Ejemplo Multivariado

Sea:

$$
P(X,Y)
$$

y modelo independiente:

$$
Q=P_XP_Y.
$$

Entonces:

$$
D_{KL}(P\|Q)=I(X;Y).
$$

Interpretación:

la información mutua es KL contra independencia.

---

## Conclusión

La divergencia de Kullback–Leibler constituye el núcleo matemático
de la teoría moderna de la información y el aprendizaje automático.

Proporciona:

- medida fundamental de discrepancia
- base para información mutua
- herramienta central en deep learning
- fundamento de inferencia probabilística

En los siguientes capítulos se utilizará extensivamente para:

- matrices de información mutua
- modelos multivariados
- selección de características
- análisis informacional en ciencia de datos

{cite}`kullback1951`, {cite}`bishop2006pattern`