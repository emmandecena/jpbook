# Probability Theory

**Probability theory** is the study of **probability spaces** resulting from a particular experiment or trial whose outcome is not completeley pre-determined.{cite}`grimmett2014probability`

Intuitively, 
- (i) the set of all possible outcomes of the experiment,
- (ii) a list of all the events which may possibly occur as consequences of the experiment,
- (iii) an assessment of the likelihoods of these events.


## Probability Spaces

```{admonition} Definition
A **probability space** is a 3-tuple $(\Omega,\mathcal{F},\mathbb{P})$ of objects such that $\lambda \in F$:
1. a non-empty set
2. an e
3. test
``` 


### General form of a Linear Map

$\text{Let } m, n > 0 \in \mathbb{Z} \text{ and }A_{j,k} \in F \text{ for } j = 1, \ldots ,m \text{ and } k = 1,...,n.$

$\text{A linear map } T \text{ from the set of all linear maps } \mathcal{L}(F^{n},F^{m}) \text{ has the general form: }$

```{math}
:label: linearmapgeneralform
T(x_{1},...,x_{n}) = (A_{1,1} x_{1}+ \cdots +A_{1,n} x_{n}, \ldots , A_{m,1} x_{1}+ \cdots +A_{m,n} x_{n})
```


---


## Bibliography

```{bibliography} ../../_bibliography/references.bib
:filter: docname in docnames
:style: plain
```
