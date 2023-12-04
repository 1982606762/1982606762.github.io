---
title: AADS-ExamNotes
date: 2023-01-30 00:40:07
tags:
categories: UCPH

---

* MaxFlow
* Linear Programming Problem
* Randomized Algorithm
*  Hash
* Veb Tree
* NP Completeness
* Exact Exponetial problems
* Approximation Algorithm
* Polygon Triangulation

<!--more-->

# maxflow

## outline

* flow network,
* flow: a function return a real value and has two constraints
  * Capacity constraint
  * flow conservation
* FF method
  * Initialize flow f, while there's an augmenting path p in the residual network, add it
  * residual network
    * residual capacity
    * flow augmentation
* cut off flow networks
  * definition: a partition of V into S and T
  * f(S,T) = s到t所有边的f - t到s所有边的f
  * minimum cut: a cut whose capacity is the minimum overall cut of the network

## presentation

**flow network:** G=(V,E) is a directed graph in which each edge $(u,v)\in E$ has a nonnegative capacity $c(u,v)\ge 0$. We also require if E contains an edge(u,v) there's no reverse edge (v,u). If there's no edge between two vertexes we define the capacity between these two vertex to be 0. There's a source s and a sink t in a network.

**flow:** a function receive two vertexes and return a real value which stands for the flow value between them. A flow has two properties: 

the first is capacity constraint, which is for all $u,v\in V$ we require $0 \le f(u,v) \le c(u,v)$.

The second is flow conservation, which is for all $u \in V-\{s, t\}$ we require $\sum_{v \in V} f(v, u)=\sum_{v \in V} f(u, v)$, which means the flow that goes out is equal to the flow that goes in.

The value |f| of a flow is the sum of all flow go out from souce minuse all flow goes in the source, and defined as $|f|=\sum_{\nu \in V} f(s, v)-\sum_{\nu \in V} f(v, s)$

In max-flow we want to find a flow of maximum value.

To solve the problem we can use Ford-Fulkerson Method. It forst init a flow f to be 0, and while there's an augmenting path p in the residual network $G_f$ we augment the flow f with p.

**Residual network:**a residual network is made up of the same nodes, and between two adjencnt nodes we add two reverse edges. The capacity of each edges are from current flow of the graph and it's based of this:$c_f(u, v)= \begin{cases}c(u, v)-f(u, v) & \text { if }(u, v) \in E \\ f(v, u) & \text { if }(v, u) \in E \\ 0 & \text { otherwise }\end{cases}$

we can remove all edges that has a capacity of 0.

After we get the flow from the algorithm we want to know if it's actually a max flow, so we need to use Max-flow min-cut theorem

First we need to specify what's a cut.

**cut**:a cut of flow is a partition of V into S and T such that source node is in set S and the sink node is in set T.

The net flow of a cut is the total flow from set S to set T minus the total flow from set T to set S and it's denoted as $f(S, T)=\sum_{u \in S} \sum_{v \in T} f(u, v)-\sum_{u \in S} \sum_{v \in T} f(v, u)$..

The capacity of a cut is the sum of all capacities from set S to set T and it's denoted as $c(S, T)=\sum_{u \in S} \sum_{v \in T} c(u, v)$.

Then we have the theorem: if f is a flow in a flow network G with source s sink t, then we have following equivalent conditions:

1. f is a max flow in G
2. the residual network $G_f$ contains no augmenting paths
3. |f| = c(S,T) for some cut(S,T) of G

**Proof:**

(1)=>(2): suppose f is a max flow and there's an augmenting path $f_p$ in residual network, then after augmenting $f_p$ the value of f will increase, which contradics with f is a max flow.

(2)=>(3):suppose $G_f$ has no augmenting path, so it have no path from source to sink.Let set S = $\left\{v \in V:\right.$ there exists a path from $s$ to $v$ in $\left.G_f\right\}$and T = V - S

The partition (S,T) is a cut.

Now we can say there's a u in S and v in T. If(u,v) is in E, then we must have f(u,v) = c(u,v) because otherwise residual network will have an augment path.  If (v,u) is in E,then we must have f(v,u) = 0 because otherwise in residual there will be some room for cancellation. And if (u,v)and(v,u) both not in E we have both two flow to be 0.

Then we have:
$$
\begin{aligned}
f(S, T) & =\sum_{u \in S} \sum_{v \in T} f(u, v)-\sum_{v \in T} \sum_{u \in S} f(v, u) \\
& =\sum_{u \in S} \sum_{v \in T} c(u, v)-\sum_{v \in T} \sum_{u \in S} 0 \\
& =c(S, T)
\end{aligned}
$$
Then by lemma 4 that is flow value of a cut is equal to the net flow value of its cut we can get |f| = f(S,T), then we have |f| = c(S,T). Because of the reason of time I don't prove lemma 4 now, you can ask me to do that later.

(3)=>(1):

By Corollary we know that for all cuts the flow value is less or equal to the cut capacity, and when it equals we can know f is a max flow.

![image-20230125104137157 PM](https://i.imgur.com/AK4Quf1.png)

![image-20230125104402866 PM](https://i.imgur.com/E2WAAma.png)

# Linear Programming Problem

Problem: There's a list of variables with some constraints, we have a linear objective function and its feasible solution which is a set of values x1 x2... x6 that can satisfy all constraints. The set of all feasible solutions is called the feasible region. What we want is an optimal solution that has the minimum or maximum objective value.

The solution is the SIMPLEX algorithm.

Start with the standard form. Procedures to produce it:

1. transform minimization problem to maximization problem
2. replace variables that don't have non-negativity constraint into two non-negative variables and xj is replaced by xj' - xj''
   1. 只有x1>=0没有x2>=0
3. change equal constraint into a pair of opposite inequality constraint
   1. x1+x2 = 0 变成x1 + x2 >=0 和 x1 + x2 <= 0
4. change all >= into <=
5. Rename variables

Slack variable

there's a slack between inequality's left side and right side. We add a new variable to the left side and make inequality become equality.Add z = objective function, e.g. z = 0 + 2x1 - 3x2 + 3x3

The feasible solution: all variables including nonbasic(right-hand side) and basic(left-hand side) are positive. 

Basic solution: all nonbasic variables to 0.

SIMPLEX:

1. Pivoting: find x1's binding and add until there's a basic variable that becomes negative. then we have a feasible solution(9,0,0,21,6,0)and z = 27.Then we rewrite the slack form and put x1 to the left side, its binding variable to the right side. And replace all x1 with a formula with x2,x3, and x6.
2. And then you add another none basic variable to become basic until there's no room for the original none basic to grow, now it's the optimal solution.

Termination:

* When all variables in the objective function <= 0
* When LP is unbounded
  * an unbasic increase all basic are also increase

Cycling:

* If a set of basic and none basic is pivoted again
* if SIMPLEX fails to terminate then it cycles
* Avoid: always choose the variable with positive coefficients and pick one with the smallest indices. And pick the smallest indices to leave. (最小下标)
* 

Infeasible First Basic Solution

* Define an auxiliary LP problem
* it's always feasible and bounded

1. Find max -x0
2. Change each ax <= b into ax-x0 <= b
3. add x0 >= 0

it is bounded as x0 >=0 so max -x0 is 0

If it's 0 then the original solution is feasible

if it's negative original is infeasible.

如果是0的话把x0=0就成为原始的simplex问题了，就有一组解可以解决。

Dual problem:

if min of dual = max of original then it's the optimal solution

It's used to prove Simplex

1. Multiply constraints by y1 y2 and make the sum less than the right side's sum
   1. Y1(x1-x2-x3+3x4) + y2(5x1+x2+3x3+8x4)+y3(-x1+2x2+3x3-5x4)<= y1 + 55y2+3y3
2. The left side has an upper bound of LP 
   1. y1+5y2-y3>=4
3. 4x1+x2+5x3+3x4 <= y1+55y2+3y3
4. Minimize the right side with 2's constraints and get its dual problem
5. (transpose the original matrix)

![image-20230109104722576 PM](https://i.imgur.com/uWUZFSY.png)

weak duality

![image-20230109104649736 PM](https://i.imgur.com/lppWVYD.png)

If there's an optimal solution for dual then there's an optimal solution for a primal solution.

![image-20230109105139766 PM](https://i.imgur.com/xqzboKa.png)

![image-20230109105209994 PM](https://i.imgur.com/ybO2cMj.png)

m = constrains数量，n=variables数量

当原始的constrain远大于variables的时候解决Dual比解决原始问题简单



## Outline

1. Introduction
2. Objective function,constraint
3. Example
4. SIMPLEX algorithm

Example:

![image-20230111125255676 PM](https://i.imgur.com/qaweUh5.png)

## Presentation

I'm going talk about linear problem. In real life a lot of problems can be solved by this algorithm, so linear program is quite useful in many practial areas.

a general linear problem consists of an objective function that describes some relation between the variables of the problem, which we want to either be maximize or minimize; it also consists of linear constraints on the variables. 

Given a linear problem, we first need to transform it into standard form.First I need to introduce what's standard form. In standard form we have an maximization object function with n variables and m linear inequalities.And we are going to use these to manage to get the maximize of the object function,like this:

![image-2023011330653524 PM](https://i.imgur.com/MOcnpJH.png)

So there are non-negativity constraints on all the n variables and all other constrains should be less than equal.

(Do standard form)

Then, in order to solve the problem, we need to tranform standard form into slack form by adding a slack variable to make all the inequality to become equal.

(Do slack form)

Then we can apply SIMPLEX algorithm on the slack form by continuously changing the basic solution by pivoting variables to and from the basic variables. Pick a variables in the objective function which positively increases the value, and pivot it with the basic variable that bottlenecks how much the non-basic variable can be increased.

(Do SIMPLEX)

In this example SIMPLEX algorithm runs normally and give a resonable result.However, in some other circumenstences it may occur some special cases, like it won't stop, or basic solution is not feasible, or why it return the optimal solution. Due to limited time I'd like to only discuss about the last one.

First, we have sth called the dual of a linear program.which we can use to show that the SIMPLEX algorithm actually computes the optimal solution to the problem. I just want to talk about the weak duality theorem, which states that the solution to the DUAL of a linear program (PRIMAL) is always an upper bound to the solution to the PRIMAL.

The dual looks like follows:

![image-20230113105655482 PM](https://i.imgur.com/QLqyOJH.png)

So, what the weak duality theorem says is that it is always the case that

![image-20230113105716981 PM](https://i.imgur.com/nwxbLi0.png)

Proof are as follows:

![image-20230113105738794 PM](https://i.imgur.com/X6IqMIZ.png)

# Randomized Algorithm

Randomized algorithms are algorithms that add randomness in the procedure.In some cases they can be the most fast or the most simple one among all other solutions to the problem. There are two types of randomized algorithm which is Las vegas and Monte Carlo. The first one always return the correct answer but the time it consumes may vary. The second one will end in a specfic time but the result it returns may not be that correct.

## Randomized Quick Sort

### Algorithm

It's similar to quick sort but the point is choose tach pivot randomly.

Example:[3,5,2,1,4]. 

### Why it sorts the numbers?

Proof: indoction on n

n=0 trival

Assume true for n-1 numbers

Then we return RandQS(L) + $S_i$ + RandQS(R),L+R <= n-1 

And the result is sorted.

### What might be the case?

#### Lucky case: 

#### $S_i$ is always medium

Running time: T(n) =O(n)+2T(n/2)=...=O(n)+2O(n/2)+4O(n/4)+...+nO(1)

O(nlogn)

#### Unlucky case: 

#### $S_i$ is always minimum

O(n^2)

#### average case:

O(nlogn). proof

$\mathbb{E}[\#$ comparisons $]=\mathbb{E}\left[\sum_{i<j} X_{i j}\right]=\sum_{i<j} \mathbb{E}\left[X_{i j}\right]$

$\mathbb{E}\left[X_{i j}\right]=\left(1-p_{i j}\right) \cdot 0+p_{i j} \cdot 1=p_{i j}$

$\mathbb{E}[\#$ comparisons $]=\sum_{i<j} \mathbb{E}\left[X_{i j}\right]=\sum_{i<j} p_{i j}$

$\begin{aligned} p_{i j} & =\operatorname{Pr}[c \in\{i, j\} \mid c \in\{i, i+1, \ldots, j\} \text { u.a.r. }] \\ & =\frac{2}{|\{i, i+1, \ldots, j\}|}=\frac{2}{j+1-i}\end{aligned}$

$\mathbb{E}[\#$ comparisons $]=\sum_{i<j} p_{i j}=\sum_{i<j} \frac{2}{j+1-i}$

$=\sum_{i<j} \frac{2}{j+1-i}$
$=\sum_{i=1}^{n-1} \sum_{j=i+1}^n \frac{2}{j+1-i}$
$=\sum_{i=1}^{n-1} \sum_{k=2}^{n+1-i} \frac{2}{k}<\sum_{i=1}^n \sum_{k=2}^n \frac{2}{k}$
$=2 n \sum_{k=2}^n \frac{1}{k}=2 n\left(\left(\sum_{k=1}^n \frac{1}{k}\right)-1\right)=2 n\left(H_n-1\right)$
$\leq 2 n \int_1^n \frac{1}{x} d x=2 n \ln n=\mathcal{O}(n \log n)$



## Randomized min-cut

* Why it return a cut?

Prove by induction on the number k of iterations of the loop.If k = 0 then it returnall edges in the graph.suppose it is true for up to k-1 iterations, we can get a graph $G'$ after first iteration and do k-1 iterations, it's a cut in G', but such cut is also a cut in G because it's the same with do K iterations.

* For any min-cut C, the probability that RandMinCut(G) returns C is $\ge \frac{2}{n(n-1)}$

Proof :

1. Let Ei be the event that the edge to be contracted isn't part of C,Then we need to prove 当且仅当每一步都不删除C里的边才会返回C![image-20230114110202228 PM](https://i.imgur.com/VRix2iJ.png)

2. With conditional probability formula we can know 

   ![image-20230114110348933 PM](https://i.imgur.com/a6fdqGV.png)

   Then the pr before can be defined as 此时pi是前i-1步都不删除的前提下第i步也不删除

   ![image-20230114110440511 PM](https://i.imgur.com/8QCX1a3.png)

3. With observation we can know 

   1. $G_i = (V_i,E_i)$has ni = n - i vertices

   2. The min-cut size of ith procedure is >= |C|

   3. 每个点的degree 都>= |C|

      $\left|E_i\right|=\frac{1}{2} \sum_{v \in V_i} d_i(v) \geq \frac{1}{2} n_i|C|$

      第i步后的边数等于总度数/2大于ni乘mincut

      得到第i步后的边数与C的关系

4. 第i步选中C的概率是C的大小/边数，即

   $\begin{aligned} 1-p_i & =\operatorname{Pr}\left[\text { uniformly random } e \in E_{i-1} \text { is in } C \mid \cap_{j=1}^{i-1} \mathcal{E}_j\right] \\ & =\frac{|C|}{\left|E_{i-1}\right|} \leq \frac{|C|}{\frac{1}{2} n_{i-1}|C|}=\frac{2}{n_{i-1}}=\frac{2}{n-(i-1)} \\ \Rightarrow p_i & \geq 1-\frac{2}{n-i+1}=\frac{n-i-1}{n-i+1}\end{aligned}$

5. 连乘逐项相消得到2/n(n-1)

Trade Off:

call it $t \frac{n(n-1)}{2}$ times and let $C^*$ be the smallest cut returned(用到1+x<=$e^x$ )

$\begin{aligned} \operatorname{Pr}\left[C^{\star} \text { is not a min-cut }\right] & \leq\left(1-\frac{2}{n(n-1)}\right)^{t \frac{n(n-1)}{2}} \\ & \leq\left(e^{-\frac{2}{(n-1)}}\right)^{t \frac{n(n-1)}{2}}\end{aligned}$

$=e^{-t}$

$\begin{aligned} \operatorname{Pr}\left[C^{\star} \text { is a min-cut }\right] & \geq 1-e^{-t} \\ & \left.=1-n^{-c} \quad \text { (If we set } t=c \ln n\right)\end{aligned}$

So we repeat it $c \cdot \frac{n(n-1)}{2} \cdot \ln n$ times then P[get a min-cut] is $1-n^{-c}$ .

# Hash

## Hashing fundamentals

Hash function: A hash function h : U->[m] for each x from U,h(x) in [m] is a random variable.

### Truly random:

​		if the variables h(x) for x in U are independent and uniform

​		**(Impractial, because it require |U|logm bits to represent)**

### Universal:

​		for any distinct values, their hash value are same has a small probability

​		$x \neq y \in U: \operatorname{Pr}[h(x)=h(y)] \leq \frac{1}{m}$

### C-approximately universal:		

​		Because sometime we need to compute faster so we need a slack version of universal.

​		h is c-approximately if $x \neq y \in U: \operatorname{Pr}[h(x)=h(y)] \leq \frac{c}{m}$

### strongly universal(2-independent)

* Each key is hashed uniformly into [m]
  * for any x and any q, $Pr[h(x) = q] = \frac{1}{m}$
* Any two distinct keys hash independently
  * there's two keys x,y. If you know h(x) = q you don't know anything about h(y) = ?

​		for all $x \neq y \in U$ ,and $q, r \in[m]: \operatorname{Pr}[h(x)=q \wedge h(y)=r]=\frac{1}{m^2}$

​		explaniation: (h(x)=q is 1/m,h(y)=r is 1/m)

### C-approximately strongly universal

* each key has $Pr[h(x) = q] = \frac{1}{m}$

​		$q, r \in[m]: \operatorname{Pr}[h(x)=q \wedge h(y)=r]=\frac{c}{m^2}$

## Application:Unordered sets

Maintain a set S with at most n keys

need to insert,delete,member

### Hashing with chaining

Define a store array L and $L[i]=$ linked list over $\{y \in S \mid h(y)=i\}$

![image-20230115113819274 PM](https://i.imgur.com/AhcNsP8.png)

Each operation takes $\mathcal{O}(|L[h(x)]|+1)$ time (the first one is to find the element in the chain and the second one is to operate on it)

Prove it only use constant time.

## Application:Signatures

![image-20230116122232950 AM](https://i.imgur.com/5ye5C1J.png)

## Practial hash functions

How to generate hash values

### Multiply-mod-prime

Let $U=[u]$ and Pick prime $p \geq u$ 

for any $a, b \in[p]$, let $h_{a, b}^m: U \rightarrow[m]$ be:

$h_{a, b}^m(x)=((a x+b) \bmod p) \bmod m$

choose a,b independently and uniformly at random. h(x) is a 2-approximately strongly universal hash function

### Multiply-shift

Let $U=\left[2^w\right]$ and $m=2^{\ell}$. For any odd $a \in\left[2^w\right]$ define

$h_a(x):=\left\lfloor\frac{(a x) \bmod 2^w}{2^{w-\ell}}\right\rfloor$

choose a randomly then h is 2-approximately universal hash function

### Strong multiply-shift

![image-2023011635100504 PM](https://i.imgur.com/2mIS37y.png)

## Application:Coordinated sampling

# VEB tree

* proof of O(lg lg u)
* do some operation on the example of vEB

![image-2023012440305148 PM](https://i.imgur.com/Iij29ei.png)



# NP Completeness

* Definition of verification, languages
* Definition of NP, reduction,NPC
* prove CLIQUE from 3-CNF-SAT
* Prove VERTEX-COVER from CLIQUE
* Prove TSP from HAM-CYCLE

**Definition of a problem**: there's a set I of instances and a set S of solutions, a problem is a binary relation between I and S

**Definition of a decision problem**: problem whose result is Yes or No, so S is {0,1}

optimal problems can be transformed into decision problems,e.g. you want to find the shortest path, instead of finding its shortest we can iterate over all the possible results and get the last Yes result instance

**Definition of Languages**: 

1. Alphabet: a finite set $\Sigma$ of symbols
2. language L over $\Sigma$ : a set of strings of symbols from $\Sigma$, e.g.: $\Sigma=\{a, b, c\}$ and $L=\{a, b a, c a b, b b a c, \ldots\}$. The empty string is denoted by(epsilon) $\epsilon$ and empty language is denoted by (emptyset) $\emptyset$ and all strings are denoted by $\Sigma^*$
3. Language acceptance: Let A be an algorithm for a decision problem and denote by $A(x) \in\{0,1\}$, A accepts a string x if A(x) = 1 and rejects a string x if A(x) = 0.The language accepted by A is$L=\left\{x \in\{0,1\}^* \mid A(x)=1\right\}$ .We say all strings not in L are rejected by A, so $A(x)=0 \forall x \in\{0,1\}^* \backslash L$.

**Definition of P and NP:**

 $P=\left\{L \subseteq\{0,1\}^* \mid\right.$ there exists an algorithm $A$ that decides $L$ in polynomial time $\}$.

NP is the class of languages that can be veriﬁed in polynomial time. More precisely, L ∈ NP if and only if there is a polynomial-time veriﬁcation algorithm A and a constant c such that $L=\left\{x \in\{0,1\}^* \mid\right.$ there is a $y \in\{0,1\}^{*}$ with $|y|=O\left(|x|^{c}\right)$ such that $\left.A(x, y)=1\right\}$.

**Verification**

Consider algorithm A taking two parameters, instead of trying to ﬁnd a solution to x (which may take a long time), A instead veriﬁes that c is a solution to x.

The language verified by A is $L=\left\{x \in\{0,1\}^* \mid\right.$ there is a $y \in\{0,1\}^*$ such that $\left.A(x, y)=1\right\}$.

**Reducibility**

Language L 1is polynomial-time reducible to language L 2if there is a polynomial-time computible function f ∶ {0, 1} ∗ → {0, 1} ∗ such that for all x ∈ {0, 1} ∗ ,$x \in L_1 \Longleftrightarrow f(x) \in L_2$. In this case, we write $L_1 \leq p L_2$ , and it shows L1 is no harder to solve than L2.

#### prove CLIQUE from 3-CNF-SAT

* Prove NP
  * consider an algorithm A taking two inputs, <G, k > and a certiﬁcate y.
  * y speciﬁes a subset V ′ of vertices of G.
  * A check that | V ′ | = k and that V ′ is a clique in G.
  * This can easily be done in polynomial time.
* Prove $3-\mathrm{CNF}-\mathrm{SAT} \leq{ }_P$ CLIQUE
  * Given a formula f = C 1∧ C 2∧ . . . ∧ C kin 3-CNF.
  * We will construct a graph G such that f is satisﬁable if and only if G has a clique of size k.
  * For each $C_r=\ell_1^r \vee \ell_2^r \vee \ell_3^r$ , we include three vertices to G.
  * There is an edge $\left(v_i^r, v_j^s\right)$ in $G$ if and only if $r \neq s$ and $\ell_i^r$ is not the negation of $\ell_j^s$.
* ![image-20230118124407756 AM](https://i.imgur.com/zM8753X.png)

**Prove TSP from HAM-CYCLE**

* prove NP
  * consider an algorithm A taking two inputs, G.= <V,E,c> and a certificate y.
  * y specifies a tour in G
  * A check y's cost and get the minimum
  * This can easily be done in polynomial time
* Prove $\mathrm{HAM}-\mathrm{CYCLE} \leq_P$ TSP
  * ![image-2023011810156956 AM](https://i.imgur.com/wIZVHAb.png)

# Exact exponential algorithms



* TSP via DP

Problem: Given cities $c_1, \ldots, c_n$, and distances $d_{i j}=d\left(c_i, c_j\right)$, find tour of minimal length, visiting all cities exactly once. 

We can define a set S which is the subset of the set of points from c2 to cn and select a ci from set S.Then as we are using Dynamic Programming we need to define the structure OPT[s,ci] = minimum length of all paths in $S \cup\left\{c_1\right\}$ that starts from c1, visits all vertexes in S once and ends in ci. Then $\min \left\{\operatorname{OPT}\left[\left\{c_2, \ldots c_n\right\}, c_i\right]+d\left(c_i, c_1\right) \mid c_i \in\left\{c_2, \ldots, c_n\right\}\right\}$ is the length of the minimal tour

We have 

OPT $\left[S, c_i\right]= \begin{cases}d\left(c_1, c_i\right) & \text { if } S=\left\{c_i\right\} \\ \min \left\{\text { OPT }\left[S \backslash\left\{c_i\right\}, c_k\right]+d\left(c_k, c_i\right) \mid c_k \in S \backslash\left\{c_i\right\}\right\} & \text { if }\left\{c_i\right\} \subset S\end{cases}$

To prove this, we first let e = (ck,ci) to be the last edge on this path. If k = 1 we just use the distance from c1 to ci. If k > 1 then the shortest length through e must be OPT $\left[S \backslash\left\{c_i\right\}, c_k\right]+d\left(c_k, c_i\right)$.The shortest such path must use the minimum over all $c_k \in S \backslash\left\{c_i\right\}$.

So we know the formula is correct and we can get shortet path throught it.What about time it consume? 

We can get the solution with this method by computing $O(n^2*2^n)$ shortest paths.Here I'll give the proof.

We enlarge the set where we want to go through from 2 to n-1 and we choose a set of size n-1 from j citys.Then we need to pick one as the last.We can observe it's bounded by $n^2$ and this one we can add more into this and this equals to $n^2*2^n$. And then we return $\min \left\{\operatorname{OPT}\left[\left\{c_2, \ldots c_n\right\}, c_i\right]+d\left(c_i, c_1\right) \mid c_i \in\left\{c_2, \ldots, c_n\right\}\right\}$ and we only compute n-1 times at most.

we assume basic operations take polynomial time in n and the algorithm costs $O^*(2^n)$. We also need to specify what $O^*$​ is

 for any a > 1 we have $O(n^c*a^n)\subset O((a+\epsilon)^n)$

So when comparing exact exponential algorithms the polynomial factors are mostly irrelevant.

$f(n) \in O^*(g(n)) <=> \exists c \in \mathbb{R}: f(n) \in \mathcal{O}\left(n^c \cdot g(n)\right)$

So $O^*$ is the same as O but ignores polynomial factors.

* Bar fight prevention



# Approximation algorithms

* approximation ratio
* Vertex cover
* 3-CNF-SAT

易错点：ratio证明，3-SAT写X=sum。

There are some optimization problems which will take exponential time to get the exact result, but sometimes a solution which is not that good is also acceptable, and it will become much faster to get these results. So we need to use approximation algorithms.

**approximation ratio**

we say that an algorithm for an optimization problem has an approximation ratio of $\rho(n)$ if, for any input of size n:

$\max \left(\frac{C}{C^*}, \frac{C^*}{C}\right) \leq \rho(n)$

If an algorithm achieves an approximation ratio of  (n), we call it a  $\rho(n)$-approximation algorithm.

**Vertex cover**

The following algorithm is a polynomial-time 2-approximation algorithm:

![image-20230119124119184 PM](https://i.imgur.com/JeozAY1.png)

The running time in worst case is O(|V| + |E|) as we will add all vertexs and remove all edges.Now I'd like to prove it's a 2-approximation algorithm:

First let $C^*$ to be an optimal cover, and let $A \subset E$ be the edges chosen by the algorithm. Each edges have two endpoints and one of them must be in $C^*$ ,so $|C^*| \ge |A| = |C|/2$  (|C| =return vertex's number) ,so it's 2-approximate.

**MAX-3-SAT**

There's also another problem called Max-3-CNF which input is some clauses combined with logic connections, the goal is to return an assignment of the variables that maximize the number of clauses evaluating to 1.

The following algorithm is a polynomial time algorithm:

![image-2023011914701123 PM](https://i.imgur.com/XDOS5Vk.png)

The running time of that is O(n) and n is the number of the variables. So it is a polynomial algorithm. Now I will prove it is an 8/7 approximation algorithm.

First, let phi$\Phi=C_1 \wedge \ldots \wedge C_n$ and each of the clauses $C_i=\ell_1 \vee \ell_2 \vee \ell_3$.

So the clause is not satisfied if and only if all three variables are 0, in other words $\neg \ell_1 \wedge \neg \ell_2 \wedge \neg \ell_3$.

So $\operatorname{Pr}\left[\neg C_i\right]=\operatorname{Pr}\left[\neg \ell_1\right] \cdot \operatorname{Pr}\left[\neg \ell_2\right] \cdot \operatorname{Pr}\left[\neg \ell_2\right]=\left(\frac{1}{2}\right)^3=1 / 8$

$\operatorname{Pr}\left[C_i\right]=1-\operatorname{Pr}\left[\neg C_i\right]=1-1 / 8=7 / 8$

And we define a variable X = $\sum_{i=1}^n\left[C_i\right]$ which is the number of satisfied clauses

We want to calculate the expect of X, which is $\mathbf{E}[X]=\mathbf{E}\left[\sum_{i=1}^n\left[C_i\right]\right] {=} \sum_{i=1}^n \mathbf{E}\left[C_i\right]=\sum_{i=1}^n \frac{7}{8}=7 n / 8$

So we can know in this algorithm C is 7n/8, and the optimal solution should be n,so it's approximation ratio is $\frac{\mathcal{C}^*}{\mathcal{C}}=\frac{\mathcal{C}^*}{7 n / 8} \leq \frac{n}{7 n / 8}=8 / 7$

**TSP**

Last I want to give another algorithm, TSP, given a complete undirected graph and each edge has a capacity. we want to find a minimum weight cycle through all vertices.

The approx-tsp algorithm is as follows: first it find the minimum spanning tree in the graph, and make a euler tour W along the MST so it goes through each edge twice,and then we shortcut W to get H and return it.

It's a polynomial time algorithm because each step in it consumes polynomial time. Then I'd like to prove it's a 2-approximation problem.

Let $H^*$ to be the optimal solution, then $c(T)\le c((H^*))$.And we know $c(W) = 2c(T)$, and $c(H) \le c(W)$ because of the triangle inequality.

So we have $c(H) \le 2c(H^*)$ , and it's proven.

# Polygon triangulation

* definition of a monotone polygon
* partitioning into monotone pieces
* Triangulating a monotone polygon

example:![image-2023011934120613 PM](https://i.imgur.com/EefMoDj.png)

There are some problems like the art gallery problem we need to solve, and in order to solve the problem we need to first triangulate the polygon. Then I'll introduce an algorithm that can efficiently triangulate a simple polygon.

**y-monotone polygon**

In geometry, a polygon *P* is called **y-monotone** with respect to a horizontal line *L*, if every line in the boundary of *P* intersects with L at most twice.

If we have a y-monotone polygon then it's easy to triangulate it, which I will discuss it later. If the polygon is not y-monotone then we need to cut it into several parts, I'd like to show how we can do it.

**partitioning**

A simple polygon has several different types of vertices, like start, normal, merge split, and end. From the definition, we can know that a polygon without split and merge and only having one start and one end vertex is a y-monotone polygon, so we need to erase all the merge and split vertexes from our polygon. 

First, we need to introduce the idea of sweeping. We construct a sweeping horizontal line that goes from top to bottom. As we can only explore the part above the line, we can only erase split vertexes when it sweeps down and we can erase merge vertexes when the sweep line goes up.

So, how can we remove the split vertex? 

I'd like to introduce the helper of edges first. The helper for an edge e which has a polygon right of it is the lowest vertex v above the sweep line such that the horizontal line segment connecting e and v are inside the polygon. In another word, it's the first vertex sweep line that will touch if it goes up.

We will also need a status structure to store all edges that have the polygon to the right with their helper and an event list storing all vertices by decreasing y-coordinate. While there are still events in the list we pop and handle them.

How do we handle the event?

**Start v: **

<img src="https://i.imgur.com/kUUD7J2.png" alt="image-2023011940309588 PM" style="zoom:50%;" />

Insert the counterclockwise incident edge in T with v as the helper.

**Regular v:**

<img src="https://i.imgur.com/UARzNQT.png" alt="image-2023011940322092 PM" style="zoom:50%;" />

If the polygon is right of the two incident edges, then replace the upper edge with the lower edge in T, and make v the helper

If the polygon is left of the two incident edges , then find the edge e directly left of v , and replace its helper by v

**Merge v:**

<img src="https://i.imgur.com/RDR9vc9.png" alt="image-2023011940339625 PM" style="zoom:50%;" />

Remove the edge clockwise from v from T Find the edge e directly left of v , and replace its helper by v

**Split v:**

<img src="https://i.imgur.com/LrUGAAq.png" alt="image-2023011940631161 PM" style="zoom:50%;" />

1. add a diagonal from v to the helper of the edge directly left of v.
2. Replace the helper of e by v
3. Insert the edge counterclockwise from v in T with v as its helper

**End v:**

Delete the clockwise incident edge and its helper from T

**How much time does it cost?**

Sorting events costs O(N log N) and if we use a binary search tree as a status structure every event costs O(logn).

So we partitioned the polygon into several y-monoton polygons, we need to trangulate it.

**Triangulate algorithm**

1. Sort all vertices from top to bottom
2. init a stack and push the first two vertices
3. take the next vertex, triangulate as much as possible while popping the stack and push v into the stack

It will take O(n) time.

Probable question: Can we immediately conclude: A simple polygon with n vertices can be triangulated O ( n log n) time?

We need to argue that all y - monotone polygons together that we will triangulate have O ( n ) vertices 

Initially we had n edges . We add at most n - 3 diagonals in the sweeps . These diagonals are used on both sides as edges . So all monotone polygons together have at most 3n - 6 edges , and therefore at most 3n - 6 vertices 

Hence we can conclude that triangulating all monotone polygons together takes only O ( n ) time
