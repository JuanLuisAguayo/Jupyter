# Demostraciones Matemáticas Avanzadas

## Introducción

Este apéndice presenta demostraciones formales de resultados fundamentales de la teoría de la información utilizados a lo largo del libro.  
El enfoque combina rigor matemático con interpretaciones informacionales relevantes para ciencia de datos e ingeniería.

---

## A.1 No Negatividad de la Información Mutua

### Teorema

Para variables aleatorias discretas $X$ e $Y$:

$$
I(X;Y) \ge 0
$$

con igualdad si y sólo si $X$ e $Y$ son independientes.

---

### Demostración

Por definición:

$$
I(X;Y)=
\sum_{x,y} P(x,y)
\log \frac{P(x,y)}{P(x)P(y)}
$$

Esto corresponde exactamente a la divergencia KL:

$$
I(X;Y)=
D_{KL}\big(P(X,Y)\parallel P(X)P(Y)\big)
$$

Sabemos que:

$$
D_{KL}(P||Q)\ge 0
$$

por la desigualdad de Gibbs.

Por lo tanto:

$$
I(X;Y)\ge0
$$

La igualdad ocurre únicamente cuando:

$$
P(x,y)=P(x)P(y)
$$

lo que implica independencia estadística.

---

## A.2 Regla de la Cadena para la Entropía

### Teorema

$$
H(X,Y)=H(X)+H(Y|X)
$$

---

### Demostración

Definición de entropía conjunta:

$$
H(X,Y)=-\sum_{x,y}P(x,y)\log P(x,y)
$$

Usamos:

$$
P(x,y)=P(x)P(y|x)
$$

entonces:

$$
\log P(x,y)=\log P(x)+\log P(y|x)
$$

Sustituyendo:

$$
H(X,Y)=
-\sum P(x,y)\log P(x)
-\sum P(x,y)\log P(y|x)
$$

Primer término:

$$
-\sum_x P(x)\log P(x)=H(X)
$$

Segundo término:

$$
-\sum P(x,y)\log P(y|x)=H(Y|X)
$$

Concluimos:

$$
H(X,Y)=H(X)+H(Y|X)
$$

---

## A.3 Simetría de la Información Mutua

### Teorema

$$
I(X;Y)=I(Y;X)
$$

---

### Demostración

Usando la identidad:

$$
I(X;Y)=H(X)+H(Y)-H(X,Y)
$$

y observando que:

$$
H(X,Y)=H(Y,X)
$$

la expresión es simétrica en $X$ e $Y$.

Por lo tanto:

$$
I(X;Y)=I(Y;X)
$$

---

## A.4 Desigualdad de Gibbs

### Teorema

Para distribuciones $P$ y $Q$:

$$
D_{KL}(P||Q)\ge0
$$

---

### Demostración

Consideremos:

$$
\log x \le x-1
$$

para todo $x>0$.

Sea:

$$
x=\frac{Q(x)}{P(x)}
$$

entonces:

$$
-\log\frac{Q(x)}{P(x)}\ge1-\frac{Q(x)}{P(x)}
$$

Multiplicando por $P(x)$ y sumando:

$$
\sum P(x)\log\frac{P(x)}{Q(x)}\ge0
$$

lo que demuestra la no negatividad de la divergencia KL.

---

## A.5 Regla de la Cadena para Información Mutua

### Teorema

$$
I(X;Y,Z)=I(X;Y)+I(X;Z|Y)
$$

---

### Demostración

Partimos de:

$$
I(X;Y,Z)=H(X)-H(X|Y,Z)
$$

Usamos:

$$
H(X|Y,Z)=H(X|Y)-I(X;Z|Y)
$$

entonces:

$$
I(X;Y,Z)=
H(X)-H(X|Y)+I(X;Z|Y)
$$

pero:

$$
H(X)-H(X|Y)=I(X;Y)
$$

por lo que:

$$
I(X;Y,Z)=I(X;Y)+I(X;Z|Y)
$$

---

## A.6 Desigualdad de Procesamiento de Datos

### Teorema

Si:

$$
X \rightarrow Y \rightarrow Z
$$

forma una cadena de Markov, entonces:

$$
I(X;Z)\le I(X;Y)
$$

---

### Demostración (Esquema Formal)

Propiedad de Markov:

$$
P(z|x,y)=P(z|y)
$$

Se demuestra que:

$$
I(X;Z)=I(X;Y)-I(X;Y|Z)+I(X;Z|Y)
$$

pero:

$$
I(X;Z|Y)=0
$$

bajo la condición de Markov.

Dado que:

$$
I(X;Y|Z)\ge0
$$

se obtiene:

$$
I(X;Z)\le I(X;Y)
$$

---

## A.7 Descomposición de Información Mutua Multivariada

### Teorema

$$
I(X;Y,Z,W)
=I(X;Y)+I(X;Z|Y)+I(X;W|Y,Z)
$$

---

### Demostración

Aplicamos repetidamente la regla de la cadena:

$$
I(X;Y,Z,W)=I(X;Y)+I(X;Z,W|Y)
$$

Luego:

$$
I(X;Z,W|Y)=I(X;Z|Y)+I(X;W|Y,Z)
$$

Combinando:

$$
I(X;Y,Z,W)=I(X;Y)+I(X;Z|Y)+I(X;W|Y,Z)
$$

---

## Conclusión del Apéndice

Las demostraciones anteriores establecen los fundamentos formales para:

- teoría de la información clásica
- modelos multivariados
- aprendizaje profundo informacional
- análisis estadístico de dependencias

Sirven como base matemática rigurosa para los capítulos teóricos y aplicaciones presentados en el libro.
