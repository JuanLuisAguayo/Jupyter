# Propiedades y Teoremas Fundamentales

## Introducción

En este capítulo se presentan las propiedades matemáticas esenciales
de la entropía, la entropía condicional y la información mutua.
Estos resultados constituyen la base teórica para:

- modelos multivariados
- aprendizaje automático basado en información
- selección de características
- análisis de dependencia estadística

Se incluyen demostraciones formales y resultados clásicos de la
teoría de la información.

---

## No Negatividad de la Entropía

### Teorema

Para toda variable aleatoria discreta:

$$
H(X)\ge 0.
$$

### Demostración

Dado que $0\le P(x)\le 1$ se tiene:

$$
\log P(x)\le 0.
$$

Entonces:

$$
- P(x)\log P(x)\ge 0.
$$

Sumando sobre todos los valores:

$$
H(X)\ge 0.
$$

---

## Entropía Máxima

### Teorema

Entre todas las distribuciones discretas con soporte finito de tamaño $n$,
la entropía es máxima para la distribución uniforme:

$$
P(x)=\frac{1}{n}.
$$

### Resultado

$$
H(X)\le \log n.
$$

La igualdad ocurre solo en el caso equiprobable.

---

## Regla de la Cadena

### Teorema

$$
H(X,Y)=H(X)+H(Y|X).
$$

### Demostración

Partimos de:

$$
P(x,y)=P(x)P(y|x).
$$

Luego:

$$
\log P(x,y)=\log P(x)+\log P(y|x).
$$

Sustituyendo en la definición de entropía conjunta:

$$
H(X,Y)=-\sum P(x,y)\log P(x,y).
$$

Se obtiene:

$$
H(X,Y)=H(X)+H(Y|X).
$$

---

## Subaditividad

### Teorema

$$
H(X,Y)\le H(X)+H(Y).
$$

### Demostración

Usando:

$$
H(Y|X)\le H(Y).
$$

y la regla de la cadena:

$$
H(X,Y)=H(X)+H(Y|X).
$$

se concluye la desigualdad.

---

## Desigualdad de Gibbs

### Teorema

Para distribuciones $P$ y $Q$:

$$
D_{KL}(P\|Q)\ge 0.
$$

### Demostración (Jensen)

La función $-\log x$ es convexa.
Aplicando desigualdad de Jensen:

$$
\mathbb{E}\left[\log\frac{Q}{P}\right]
\le
\log\mathbb{E}\left[\frac{Q}{P}\right].
$$

Se concluye:

$$
D_{KL}(P\|Q)\ge 0.
$$

---

## No Negatividad de la Información Mutua

### Teorema

$$
I(X;Y)\ge 0.
$$

### Demostración

Usando:

$$
I(X;Y)=D_{KL}(P_{X,Y}\|P_XP_Y)
$$

y la desigualdad de Gibbs.

---

## Simetría

### Propiedad

$$
I(X;Y)=I(Y;X).
$$

Esto se deduce directamente de:

$$
H(X)+H(Y)-H(X,Y).
$$

---

## Información Mutua Nula

### Teorema

$$
I(X;Y)=0 \iff X\perp Y.
$$

### Interpretación

La información mutua mide dependencia estadística.

---

## Regla de la Cadena para Información Mutua

### Teorema

$$
I(X;Y,Z)=I(X;Y)+I(X;Z|Y).
$$

### Extensión

Para múltiples variables:

$$
I(X;Y_1,\dots,Y_n)=
\sum_{i=1}^{n}
I(X;Y_i|Y_1,\dots,Y_{i-1}).
$$

---

## Desigualdad de Procesamiento de Datos

### Teorema

Si:

$$
X\rightarrow Y\rightarrow Z
$$

es una cadena de Markov, entonces:

$$
I(X;Z)\le I(X;Y).
$$

### Interpretación

Ninguna transformación puede aumentar la información.

Aplicaciones:

- redes neuronales profundas
- compresión de datos
- modelos generativos

---

## Monotonicidad Condicional

### Teorema

$$
H(X|Y,Z)\le H(X|Y).
$$

Más información nunca aumenta la incertidumbre.

---

## Descomposición de Información Mutua

### Identidad

$$
I(X;Y)=H(X)-H(X|Y).
$$

También:

$$
I(X;Y)=H(Y)-H(Y|X).
$$

---

## Submodularidad

### Teorema

La entropía es una función submodular:

$$
H(A)+H(B)\ge H(A\cup B)+H(A\cap B).
$$

Importancia:

- selección de variables
- optimización combinatoria
- aprendizaje estructural

---

## Convexidad y Concavidad

- La entropía es función cóncava de la distribución
- La divergencia KL es convexa

Consecuencias:

- estabilidad numérica
- existencia de soluciones óptimas
- optimización convexa

---

## Información Total (Dependencia Multivariada)

### Definición

$$
TC(X_1,\dots,X_n)=
D_{KL}(P\|\prod_i P_i).
$$

Propiedades:

- siempre no negativa
- cero solo si independencia total
- generalización multivariada de información mutua

---

## Desigualdades Multivariadas

Para variables múltiples:

$$
I(X;Y,Z)\ge I(X;Y).
$$

$$
H(X,Y,Z)\le H(X)+H(Y)+H(Z).
$$

---

## Ejemplo Numérico

Sea:

$$
P(0,0)=0.4,\;
P(0,1)=0.1,\;
P(1,0)=0.2,\;
P(1,1)=0.3.
$$

Entonces:

$$
I(X;Y)\ge 0
$$

y

$$
H(X,Y)\le H(X)+H(Y).
$$

Este ejemplo se utilizará posteriormente en:

- matrices de información mutua
- clustering informacional
- selección de variables

---

## Conclusión

Las propiedades presentadas establecen la base teórica necesaria
para desarrollar:

- modelos multivariados de dependencia
- matrices de información mutua
- aprendizaje profundo informacional
- algoritmos de ciencia de datos basados en teoría de la información

El siguiente capítulo introducirá formalmente la divergencia de
Kullback–Leibler como herramienta central para medir diferencias
entre distribuciones.

{cite}`csiszar2011information`, {cite}`cover2006elements`