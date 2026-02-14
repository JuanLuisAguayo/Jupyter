# Información Mutua

## Introducción

La información mutua es una medida fundamental de dependencia estadística
entre variables aleatorias. Cuantifica la reducción promedio de incertidumbre
de una variable cuando se conoce otra.

A diferencia de la correlación lineal, la información mutua captura
dependencias no lineales y relaciones complejas entre variables,
constituyendo una herramienta central en teoría de la información,
aprendizaje automático, estadística multivariada y ciencia de datos.

---

## Definición Formal

Sean $X$ e $Y$ variables aleatorias discretas con distribución conjunta
$P(X,Y)$ y marginales $P(X)$ y $P(Y)$. La información mutua se define como

$$
I(X;Y)=\sum_{x,y} P(x,y)\log\frac{P(x,y)}{P(x)P(y)}.
$$

---

## Interpretaciones Equivalentes

La información mutua puede escribirse en términos de entropías como:

### Forma Entrópica Principal

$$
I(X;Y)=H(X)+H(Y)-H(X,Y).
$$

### Reducción de Incertidumbre

$$
I(X;Y)=H(X)-H(X|Y).
$$

$$
I(X;Y)=H(Y)-H(Y|X).
$$

Estas expresiones muestran que la información mutua mide la disminución
de incertidumbre al conocer la otra variable.

---

## Interpretación como Divergencia KL

La información mutua también puede expresarse como una divergencia
de Kullback–Leibler:

$$
I(X;Y)=D_{KL}\big(P(X,Y)\,\|\,P(X)P(Y)\big).
$$

Interpretación:

- Mide qué tan distinta es la distribución conjunta respecto a la
  distribución que existiría bajo independencia.
- Si las variables son independientes, la divergencia es cero.

---

## Propiedades Fundamentales

### 1. No negatividad

$$
I(X;Y)\ge 0.
$$

### 2. Simetría

$$
I(X;Y)=I(Y;X).
$$

### 3. Independencia

Si $X$ e $Y$ son independientes:

$$
I(X;Y)=0.
$$

### 4. Cota Superior

$$
I(X;Y)\le \mín{(H(X),H(Y))}.
$$

### 5. Invarianza ante transformaciones biyectivas

La información mutua no cambia bajo transformaciones determinísticas
invertibles de las variables.

---

## Ejemplo Resuelto: Clima y Congestión Vehicular

Considere la distribución:

|Clima $X$|Congestión $Y$|P(X,Y)|
|---|---|---|
|Soleado|No|0.50|
|Soleado|Sí|0.10|
|Lluvioso|No|0.15|
|Lluvioso|Sí|0.25|

Marginales:

$$
P(X=Soleado)=0.60,\quad P(X=Lluvioso)=0.40
$$

$$
P(Y=No)=0.65,\quad P(Y=Sí)=0.35
$$

Entropías previamente obtenidas:

$$
H(X)=0.97 \text{ bits}
$$

$$
H(X|Y)=0.81 \text{ bits}
$$

Información mutua:

$$
I(X;Y)=H(X)-H(X|Y)
$$

$$
I(X;Y)=0.97-0.81=0.16 \text{ bits}.
$$

Interpretación:

- Existe dependencia moderada entre clima y congestión.
- Conocer la congestión reduce ligeramente la incertidumbre del clima.

---

## Información Mutua Normalizada

Para comparar dependencias entre distintos sistemas se utilizan versiones
normalizadas, por ejemplo:

$$
NMI=\frac{I(X;Y)}{\sqrt{H(X)H(Y)}}.
$$

Aplicaciones:

- clustering
- evaluación de modelos
- análisis de dependencia relativa

---

## Extensión a Variables Continuas

Para variables continuas con densidad conjunta $p(x,y)$:

$$
I(X;Y)=\int\int p(x,y)\log\frac{p(x,y)}{p(x)p(y)}dx\,dy.
$$

Observación:

- se usa entropía diferencial
- pueden aparecer valores negativos en entropía diferencial, pero
  la información mutua permanece no negativa

---

## Interpretación Geométrica Informacional

Conceptualmente:

- $H(X)$ es la incertidumbre total de $X$
- $H(X|Y)$ es la parte no explicada por $Y$
- la intersección corresponde a $I(X;Y)$

Esta interpretación se usa frecuentemente en diagramas tipo Venn
informacionales.

---

## Aplicaciones

### Aprendizaje Automático

- selección de características
- reducción de dimensionalidad
- aprendizaje profundo
- representación latente

### Ciencia de Datos

- análisis de dependencia no lineal
- clustering basado en información
- análisis exploratorio

### Comunicaciones

- capacidad de canal
- codificación óptima
- análisis de ruido

### Estadística Multivariada

- matrices de información mutua
- análisis de redes probabilísticas
- modelos gráficos

---

## Relación con Capítulos Posteriores

Este concepto será extendido en:

- Matriz de Información Mutua
- Información Mutua Condicional
- Modelos Multivariados de Alta Dimensión
- Divergencia de Kullback–Leibler

---

## Conclusión

La información mutua proporciona una medida universal de dependencia
estadística que trasciende relaciones lineales y permite caracterizar
estructuras informacionales complejas. Su formulación basada en entropía
y divergencia KL la convierte en una herramienta central para el análisis
teórico y aplicado en sistemas multivariados modernos.

{cite}`shannon1948`, {cite}`cover2006elements`