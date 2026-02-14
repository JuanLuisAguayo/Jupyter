# Entropía de Shannon

La entropía es una de las nociones centrales de la teoría de la información. Introducida por Claude Shannon en 1948, cuantifica la incertidumbre promedio asociada a una variable aleatoria y constituye la base matemática para el análisis de sistemas de comunicación, aprendizaje automático y modelos probabilísticos.

---

## 1. Motivación Conceptual

Considérese una variable aleatoria discreta $X$ con distribución de probabilidad $p(x)$. Si los resultados son altamente predecibles, la incertidumbre es baja; si son impredecibles, la incertidumbre es alta.

La entropía mide formalmente esta incertidumbre promedio.

Ejemplos intuitivos:

- Un dado cargado tiene menor entropía que un dado justo.
- Una variable determinista tiene entropía cero.
- Una distribución uniforme maximiza la entropía.

---

## 2. Definición Formal (Caso Discreto)

Sea $X$ una variable aleatoria discreta con función de masa $p(x)$. La entropía de Shannon se define como:

$$
H(X) = -\sum_{x \in \mathcal{X}} p(x)\log p(x).
$$

donde:

- $\log$ es el logaritmo base 2.
- La unidad es el bit.

---

## 3. Interpretación Informacional

La cantidad:

$$
-\log p(x)
$$

representa la información asociada al evento $x$. Por tanto, la entropía es el valor esperado de la información:

$$
H(X) = \mathbb{E}[-\log p(X)].
$$

Interpretación:

- Alta entropía → mayor incertidumbre promedio.
- Baja entropía → mayor previsibilidad.

---

## 4. Caso Continuo

Para variables aleatorias continuas con densidad $f(x)$:

$$
h(X) = -\int f(x)\log f(x)\,dx.
$$

Esta cantidad se denomina entropía diferencial.

Advertencias:

- Puede ser negativa.
- No es invariante ante transformaciones lineales.

---

## 5. Propiedades Fundamentales

### 5.1 No negatividad

$$
H(X) \ge 0.
$$

### 5.2 Máximo para distribuciones uniformes

Si $|\mathcal{X}| = n$:

$$
H(X) \le \log n.
$$

### 5.3 Invarianza ante permutaciones

La entropía depende únicamente de la distribución, no del etiquetado de los estados.

### 5.4 Aditividad para variables independientes

Si $X$ y $Y$ son independientes:

$$
H(X,Y) = H(X) + H(Y).
$$

---

## 6. Ejemplo Computacional

Sea una variable binaria:

$$
P(X=0)=0.5,\quad P(X=1)=0.5.
$$

Entonces:

$$
H(X)= -0.5\log 0.5 -0.5\log 0.5 = 1\ \text{bit}.
$$

Caso sesgado:

$$
P(X=1)=0.9,\quad P(X=0)=0.1.
$$

$$
H(X) \approx 0.469\ \text{bits}.
$$

Interpretación:

- Mayor sesgo → menor entropía.
- Mayor equilibrio → mayor incertidumbre.

---

## 7. Interpretación Geométrica

La entropía puede interpretarse como una medida de dispersión probabilística sobre el simplex de probabilidades.

- Distribuciones concentradas → cercanas a vértices.
- Distribuciones uniformes → centro del simplex.

Esta perspectiva es útil en:

- optimización
- aprendizaje profundo
- teoría de códigos

---

## 8. Rol en Ciencia de Datos

Aplicaciones modernas incluyen:

- selección de características
- árboles de decisión
- regularización probabilística
- aprendizaje no supervisado
- modelos generativos

En aprendizaje automático:

$$
\text{Ganancia de información} = H(Y) - H(Y|X).
$$

---

## 9. Conexión con Capítulos Posteriores

La entropía sirve como base para:

- entropía condicional
- información mutua
- divergencia KL
- matrices de información
- modelos multivariados

Estos conceptos serán desarrollados en los capítulos siguientes.

---

## 10. Comentarios Finales

La entropía establece el marco cuantitativo fundamental para medir incertidumbre e información. Su formulación probabilística permite conectar estadística, teoría de la comunicación y aprendizaje automático dentro de una estructura matemática unificada.

{cite}`shannon1948`, {cite}`mackay2003information`, {cite}`cover2006elements`