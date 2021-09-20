# Probability Theory

**Probability theory** is the study of **probability spaces** resulting from a particular ***experiment*** or ***trial*** whose ***outcome*** or ***events*** are not completeley pre-determined {cite}`grimmett2014probability`.





Intuitively, doing a **particular experiment** gives rise to a **probability space** consisting of:
- (i) the **set of all** possible **outcomes** or **events** of the experiment,
- (ii) a **subset of particular events** which can occur resulting from the experiment
- (iii) a **measure of the likelihoods** of these events.

## Intuition

We denote a paricular experiment as $\mathcal{E}$. We define the set of all outcomes resulting from $\mathcal{E}$ is denoted as $\Omega$. A particular event which is a member of $\Omega$ is denoted as $\omega$.

For example, suppose an experiment consists of picking a random ball from a container with 10 balls, numbered from 1 to 10. We denote:
- $\mathcal{E}$ - picking a single ball
- $\Omega$ - $ \\{ 1,2,3,4,5,6,7,8,9,10 \\} $

We can then define **events** which are interesting to us, as **subsets** of $\Omega$. For example, we can define the events of picking an even-numbered ball as the subset $ \\{ 2,4,6,8,10 \\} $.

The connection between **events** as **subsets** is intuitive. For instance, if we define $A$ and $B$ as subsets of $\Omega$, then:
- $A \cup B $ can correspond to the event of either A or B event occur
- $A \cap B $ can correspond to the event of both A or B event occur

More generally, if $A_1, A_2, \dots, A_n $ are events, then the union of all subsets $\bigcup\limits_{i=1}^{\infty} A_{i}$ can be defined as $A_i$ occurring for some $i$. 

Similarly, the intersection of all subsets $\bigcap\limits_{i=1}^{\infty} A_{i}$ can be defined as $A_i$ occurring for all $i$.
 
## Event Spaces

From the **subsets** of $\Omega$ which are interesting for our purposes, we define a **collection of subsets** $\mathcal{F} = \\{ A_i : i \in I \\} $ where each $A \in \mathcal{F}$ is called an **event**. 

Thus, we define $\mathcal{F}$ formally as a mathematical space below:

```{admonition} Definition


A collection $\mathcal{F}$ of subsets of the sample space $\Omega$ is called an **event space** if:


1. $\mathcal{F}$ is non-empty
2. If $A \in \mathcal{F}$, then $\Omega \backslash A \in \mathcal{F}$
3. test
``` 

## Probability Measure


## Probability Spaces


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
