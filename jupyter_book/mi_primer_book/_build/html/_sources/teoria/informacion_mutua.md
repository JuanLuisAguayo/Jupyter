# Información Mutua

## 1. Introducción

La información mutua mide la cantidad de información compartida entre dos variables aleatorias.
Formalmente cuantifica la reducción de incertidumbre de una variable al observar otra.

---

## 2. Definiciones fundamentales

```{prf:definition} Entropía
:label: def-entropia

Sea $X$ una variable aleatoria discreta con función de probabilidad $p(x)$.
La entropía de Shannon se define como

$$
\Entropy(X) = -\sum_{x} p(x)\log p(x).
$$
```

```{prf:definition} Información mutua
:label: def-info-mutua

Sean $X$ e $Y$ variables aleatorias con distribución conjunta $p(x,y)$.
La información mutua se define como

$$
\MI(X;Y)=\sum_{x,y} p(x,y)\log \frac{p(x,y)}{p(x)p(y)}.
$$
```

---

## 3. Interpretaciones equivalentes

```{prf:proposition}
:label: prop-formas-mi

La información mutua puede escribirse como

```{math}
\MI(X;Y)=\Entropy(X)-\Entropy(X|Y).
```
```

```{prf:proof}

Partimos de la definición de entropía condicional:

```{math}
\Entropy(X|Y)=\Entropy(X,Y)-\Entropy(Y).
```

Sustituyendo en la identidad de entropía conjunta:

```{math}
\MI(X;Y)=\Entropy(X)+\Entropy(Y)-\Entropy(X,Y).
```
```

---

## 4. Ejemplo resuelto

```{prf:example}
Considere las variables:

- $X \in \{\text{Soleado},\text{Lluvioso}\}$
- $Y \in \{\text{Sí},\text{No}\}$

con distribución conjunta dada.
```

### Desarrollo

```{math}
\Entropy(X)=-\sum p(x)\log p(x)
```

### Interpretación

La información mutua positiva indica dependencia estadística
entre clima y congestión.

---

## 5. Propiedades importantes

```{prf:theorem}
:label: thm-no-negatividad

$$
\MI(X;Y)\ge 0.
$$
```

```{prf:proof}
Se demuestra usando la divergencia KL:

```{math}
\MI(X;Y)=\KL(p(x,y)\|p(x)p(y)).
```
```

---

## 6. Ejercicios propuestos

1. Demuestre que $\MI(X;Y)=0$ si $X$ e $Y$ son independientes.
2. Calcule la información mutua para una distribución equiprobable.
3. Demuestre la simetría $\MI(X;Y)=\MI(Y;X)$.

---

## 7. Comentarios finales

La información mutua es una medida fundamental en:

- aprendizaje automático
- selección de variables
- codificación de fuentes
- análisis de dependencia no lineal
```
