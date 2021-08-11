# Linear Algebra

**Algebra** is the study of mathematical **objects** and the **rules** to manipulate those objects.
- Mathematical objects called **algebraic structures** consist of an arbitrary **set** *(objects)* with certain operations *(rules)* defined on that set.
- A rule to manipulate algebraic structures is called an **operation** -- a way of combining any two members of the set to produce a unique third member of the set.

**Linear algebra** is the study of **vector spaces** -- an algebraic structure consisting of **vectors** and its **operations**.

## Vector Spaces

Definition of operations as a function on a set $V$.

```{admonition} Definition
An **addition on a set $V$** is a function that assigns an element $u+v \in V$
to each pair of elements $u$ and $v \in V$.

A **scalar multiplication on a set $V$** is a function that assigns an element $\lambda v \in V$ to each $\lambda \in F$ and each $v \in V$, where $F$ denotes a scalar <a href="https://en.wikipedia.org/wiki/Field_(mathematics)" target="_blank">field</a> .
```

Definition of vector space -- the primary mathematical structure studied in Linear Algebra{cite}`axler2014linear`.

```{admonition} Definition
A **vector space** is a set of vectors $V$ along with an **addition** on $V$ and a **scalar multiplication** on $V$ with a scalar field $F$ such that the following properties hold:

- commutativity
- associativity
- additive identity
- additive inverse
- multiplicative identity
- distributive properties
```

**To check if a mathematical stucture is a vector space, we need to prove that the properties hold.**

1. The set of Real Numbers $\mathbb{R}$ with addition operation $+$

Let $a, b \in \mathbb{R}$.
Then, commutativity holds since $a + b = b + a \in \mathbb{R}$ and associativity holds since $(a + b) + c =  a + (b + c) \in \mathbb{R}$. Additive identity is $0 \in \mathbb{R}$ since $a + 0 = a \in \mathbb{R}$. Additive inverse is $-a \in \mathbb{R}$ since $a + -a = 0 \in \mathbb{R}$

3. The set of n-tuples of real numbers denoted by $\mathbb{F}^{n}$ with element-wise addition operation $+$

### Finite-Dimensional Vector Spaces

The concepts of **linear combinations**, **span**, **independence**, **bases**, and **dimension** of a list of vector spaces provide additional structure.

```{admonition} Definition
A **linear combination** of a list of vectors with length *m*, $v_{1}, ... v_{m}$, is a vector in the form of $a_{1} v_{1}+...+a_{m} v_{m}$ where $a_{1},...,a_{m} \in F$
```

```{admonition} Definition
The **set** of all the linear combinations of a list of vectors is called the **span** of that list. Thus, the span of $v_{1}, ... v_{m}$ can be denoted as:

$$
span(v_{1}, ... v_{m}) = {a_{1} v_{1}+...+a_{m} v_{m} : a_{1},...,a_{m} \in F}
$$

```

```{admonition} Definition
A list of vectors with length $m$ is called **linearly independent** if the only choice of scalars that make the its linear combination equal to zero is if the scalars itself are zero. Otherwise the list of vectors are called **linearly dependent**.
```

From the definitions of **span**, **independence**, we define **basis**, and **dimension**.

```{admonition} Definition
A linearly independent list of vectors in $V$ that spans $V$ is called its **basis**. The length of this basis is called its **dimension**.
```


## Linear Maps

From the properties and structure of vector spaces, functions (mappings) from one vector space to another called **linear maps** or **linear transformations** can now be defined.

```{admonition} Definition
A **linear map** or **linear transformation** from a vector space $V$ to another vector space $W$ is a function $T$ with two properties:
1. Additivity - the linear map of a vector sum is a sum of linear maps
$$
T(u + v) = T(u) + T(v) \text{ for all } u,v \in V, T(u + v) = w \in W
$$

2. Homogeneity - the linear map of a scaled vector is the scaled linear map
$$
T(\lambda v) = \lambda T(v) \text{ for all } v \in V, \lambda \in F
$$
```
### General form of a Linear Map

$\text{Let } m, n > 0 \in \mathbb{Z} \text{ and }A_{j,k} \in F \text{ for } j = 1, \ldots ,m \text{ and } k = 1,...,n.$

$\text{A linear map } T \text{ from the set of all linear maps } \mathcal{L}(F^{n},F^{m}) \text{ has the general form: }$

```{math}
:label: linearmapgeneralform
T(x_{1},...,x_{n}) = (A_{1,1} x_{1}+ \cdots +A_{1,n} x_{n}, \ldots , A_{m,1} x_{1}+ \cdots +A_{m,n} x_{n})
```

**Take note of the comma, centered dots and lowered dots**

### Matrices
The properties in linear algebra can be expressed in terms of matrices to allow **explicit computation**.

```{admonition} Definition
An **m-by-n matrix** is a rectangular array of elements of the field $F$ with $m$ rows and $n$ columns:

```{math}
\begin{bmatrix} A_{1,1} & \ldots & A_{1,n} \\ \vdots &  & \vdots \\ A_{m,1} & \ldots & A_{m,n} \end{bmatrix}
```

### Matrix of a Linear Map

Matrices are used to **represent** linear maps

```{admonition} Definition
Given a linear map $T \in \mathcal{L} \left( V, W \right)$ where $v_{1},\ldots,v_{n}$ is a basis of $V$ and $w_{1}, \ldots ,v_{m}$ is a basis of $W$, then the **matrix of T** consists of the scalars $A_{1,k}, \ldots  ,A_{m,k}$ needed to write the $k$th basis of $V$ as a linear combination of the basis vectors in $W$.

```{math}
:label: matrixoflinearmap
Tv_{k} = A_{1,k}w_{1} + \ldots + A_{m,k}w_{m}
```

#### Example
Suppose $T \in \mathcal{L}(\mathbf{F^{2},F^{3}}) $ is defined by:

$$
T(x, y) = (x+2y, 3x+4y, 5x+6y)
$$

This is a linear map that takes a 2-dimensional vector $v \in V$ into 3-dimensional space $w \in W$. The basis vectors of $V$ are $ \left[ \begin{smallmatrix} 1 \cr 0 \end{smallmatrix} \right] $ and $ \left[ \begin{smallmatrix} 0 \cr 1 \end{smallmatrix} \right] $ while basis vectors of $W$ are $ \left[ \begin{smallmatrix} 1 \cr 0 \cr 0 \end{smallmatrix} \right] $ , $ \left[ \begin{smallmatrix} 0 \cr 1 \cr 0\end{smallmatrix} \right] $ and $ \left[ \begin{smallmatrix} 0 \cr 0 \cr 1\end{smallmatrix} \right] $.

Applying the map to the first basis vector in $V:$

$$
T(1, 0) = (1+0, 3+0, 5+0)
$$

Which can be written as a **linear combination** of the basis vectors in $W$:

$$
T\left[ \begin{smallmatrix} 1 \cr 0 \end{smallmatrix} \right] = 1\left[ \begin{smallmatrix} 1 \cr 0 \cr 0\end{smallmatrix} \right] + 3\left[ \begin{smallmatrix} 0 \cr 1 \cr 0\end{smallmatrix} \right] + 5\left[ \begin{smallmatrix} 0 \cr 0 \cr 1\end{smallmatrix} \right]
$$

Thus the matrix of this linear map $T$ is:

$$
\mathcal{M}(T) = \begin{bmatrix} 1 & 2 \cr 3 & 4 \cr 5 & 6\end{bmatrix}
$$

<!--- A link to an equation directive: {eq}`matrixoflinearmap` --->


## Inner Product Spaces
In making the definition of a vector space, we generalized the linear structure (addition and scalar multiplication) of R2 and R3. We ignored other important features, such as the notions of length and angle. These ideas are embedded in the concept we now investigate, inner products
---

## Bibliography

```{bibliography} ../../_bibliography/references.bib
:filter: docname in docnames
:style: plain
```
