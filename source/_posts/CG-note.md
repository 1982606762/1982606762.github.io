---
title: CG_note
date: 2023-04-19 15:12:24
tags:
categories: UCPH
Mathjax: true
---

A personal note in reading the book "Computational Geometry Algorithms and Applications 3rd Edition"

<!--more-->

# 1. Computational Geometry

## Convex Hulls

问题：给定一个点的set，如何求最大的Convex Hull

A subset $S$ of the plane is called convex if and only if for any pair of points $p, q \in S$ the line segment $\overline{p q}$ is completely contained in $S$. The convex hull $\operatorname{eH}(S)$ of a set $S$ is the smallest convex set that contains $S$. To be more precise, it is the intersection of all convex sets that contain $S$.

![image-20230407114241044 AM](https://i.imgur.com/COGIsyY.png)

可以想象用橡皮筋箍住的最外圈是一个convex hull of P

如何表示输入输出？

可以顺时针方向列出所有多边形的点：

![image-20230407114630549 AM](https://i.imgur.com/TFKqpg9.png)

edge of a convex hull pq:

我们画一条经过pq两点的直线，假如多边形在直线的一侧，那么所有点都在这一侧，那么pq就是一条边

慢convexHull算法：

![image-20230407124506613 PM](https://i.imgur.com/9sMJGcC.png)

![image-20230407124520501 PM](https://i.imgur.com/BWxGDU8.png)

遍历每个点对pq，对于每个不等于pq的点r，假如所有的点都在pq的右边那么pq就是一条边并加到E里。（为什么是在右边是因为最终返回的多边形是顺时针方向的，所以所有的edge的边的右边都对应多边形的内部）

对于这个算法有两点关键：

1. 第五行我们如何判断r在pq的左边？

   本书假定有一种方法可以在constant time实现判断，并且有一些库函数已经实现了这个。但是这一步会影响算法的总效率和正确率

2. 最后一步如何实现？
   可以通过随机选一条边e1，把他的origin作为多边形的起点，找到以他的终点为origin的下一条边，移出E并加入L，以此类推。

这个算法要使用$O(n^3)$时间

特殊情况：

1. 如果pq线上有别的点怎么办？

修改pq定义，如果所有点都在pq左边或者在开放直线pq上就是一条edge

2. 由于float精度问题会导致判断点在线的左边错误，从而让算法返回多余的边或少返回边

总结：简单算法时间长，不够健壮

增长算法：首先通过x轴坐标排序，获得一个列表。之后通过这个列表拿到upper hull 也就是最左边到最右边的上边的点， 然后再拿到lower hull，也就是下半部分的顺时针方向边缘。

# Line Segment Intersection(map overlay)

问题：给出一系列线段s找这些线段的所有交点

用遍历所有线段的方法时间复杂度是$O(n^2)$

Output-sensitive algorithm: 运行时间和输出规模有关的算法。也可以叫做intersection-sensitive，因为在这个问题中交点的数量决定输出规模

如何优化？

思路：两条线段要想相交首先需要离得近，所以我们只需要判断离得近的线段就够。首先我们定义y-interval是线段在y轴上的正交投影，因此任意两条线段若他们的y-interval不重叠(overlap)，就可以得到他们离得很远，从而不可能有交点。因此我们只需要判断那些y-interval有overlap的对即可。

![image-20230409124223109 AM](https://i.imgur.com/X63HBaI.png)

具体做法是取一根直线上下扫描，同时相交的线段就是有overlap的线段，这个方法叫做plane sweep algorithm.线叫sweep line, 线的status是与这条线相交的那一组线段。在线上下滑动的过程中status也在变化，但不是连续的。只有在遇到特殊点的时候才会变，在这个情况下是线段的顶点。



# Polygon Triangulation

问题：有一个多边形的艺术馆需要安装摄像机，每个摄像机都是固定的，在一个艺术馆中需要多少个摄像机才能看守整个场馆？

![image-2023041495810993 AM](https://i.imgur.com/Pitvbxf.png)

这取决于场馆的复杂程度，因此我们需要获得多边形的顶点数n来计算。但是就算两个多边形有同样数量的顶点，复杂程度也不一样，因此我们需要找到任何情况下都适用的最小摄像机数。但是这个问题是NPhard的

要想解决这个问题可以通过分解多边形，因此需要把多边形分解成多个三角形，通过画对角线的方式

![image-20230414110347161 AM](https://i.imgur.com/zFL8Pe1.png)

是否一个多边形可以被triangulated？

**Theorem** ：每个简单多边形都能被triangulated并且n个顶点可以分出n-2个三角形

证明：

使用数学归纳法。

n=3的时候多边形就是三角形

n>3的时候假设定理对于m<n都成立，

首先需要证明多边形P中存在diagonal。让v是最左边的点，u和w是挨着v的两个点，假如三角形uvw中没有其他顶点那么uw就是一条对角线，假如uvw中有顶点，让离uw最远的点叫做v’，我们可以知道线段vv‘上没有其他的顶点，（因为v'是最远的点，如果vv’上有点x的话x就会变成最远的点）所以vv'是对角线。因此P中有对角线。

![image-2023041431416250 PM](https://i.imgur.com/hBpymI1.png)

对角线把P分割成$P_1$和$P_2$，设$P_1$有$m_1$个顶点，$P_2$有$m_2$个顶点，那么$m_1$和$m_2$都<n,根据假设可得$P_1$和$P_2$ 都能被triangulated.因此这两个图形都转换之后合并可得P也是triangulated，即证明n=n的时候成立。

还需要证明多边形P的triangulation有n-2个三角形。由于m1,m2 < n,所以P1可以被分成m1-2个三角形，P2被分为m2-2个，同时m1+m2 = n+2.因此加起来就是n-2.

因此得证。

现在我们需要找一个P的点集，让每个三角形都至少对应点集里的一个点，然后把摄像机放到选出来的点上。要想获得这样的点集，我们可以应用三色定理，从而得到点集中有n/3个点。

**Theorem**: 有n个点的多边形需要n/3个摄像机来足够监控。

## 把多边形分解成单调的

给定一个有n个点的简单多边形（内部没有洞）我们已经知道它可以被三角化by 找一条对角线，triangulate两个小polygon。但是这个步骤要花三次方时间。如果多边形是一个convex polygon的话只要选一个点然后向所有其他点连线，只需O(n)，但是把多边形分解成convex也很困难，所以我们要把多边形分解成y-monotone pieces就可以很简单。

一个monotone的多边形是指在某一个方向上的直线只能与这个多边形有两个交点。或者说，如果我们沿着左边（或右边）的边界链从最上面的顶点走到最下面的顶点，那么我们总是向下或水平移动，从不向上移动。

![y-monotone polygon](https://i.imgur.com/tx1MZSN.png)

我们需要先把多边形分解成y-monotone的，可以做以下步骤：我们可以将一个多边形分割成如下的单调片段。想象一下，从P的最上面的顶点沿着左边边界最下面的顶点。我们行走的方向由下往上或由上往下转换的顶点称为转折顶点。

![turn vertex](https://i.imgur.com/hLFbcFn.png)

要想分解就需要解决掉所有转折点。假如有先向上再向下的点，并且多边形内部在这个点的上方，那么就需要从这个点向上引一条对角线来划分多边形，假如有先向下再向上的点就需要向下引对角线。因此我们需要定义各种点的类型，如下图：

![vertices types](https://i.imgur.com/rQMZOFE.png)

我们需要去除split 和 merge vertex

去除split点：

首先需要对多边形的顶点按照y轴坐标进行排序，然后用一条水平直线(sweep line)从上到下进行扫描。要想去除split点$v_i$就需要添加一条对角线来拆分，但是我们需要连到哪个点呢？很自然的选择是离$v_i$最近的某个点，因为这样就可以连接线段而不穿过另一条多边形的边。定义$e_j$是$v_i左手的边$,$e_k是右手的边$.这样我们就可以连接到这两条边中间的某个点。如果没有这个点那么就可以连接到$e_j的上顶点或e_k的上顶点$。我们把这样的点叫做$helper(e_j)$。

![image-2023041842830252 PM](https://i.imgur.com/kKXaFyG.png)

现在我们知道了如何消除split点：连接到它左边边的helper点。如何消除merge点？

假如vi是一个merge点，那么我们把他看做是$e_j$的helper，然后把他和$e_j和e_k之间$最高的点连起来即可。

我们使用doubly-connected-edge list来表示一个多边形P

要handle不同点的时候需要精确一些，在应对以下情况时需要额外考虑：

* 在处理split点和更换merge vertex为helper的时候检查是否需要添加对角线
* 更新状态数据结构的值

## 时间分析

构造优先队列要用O(n),初始化状态树用O(1),检索和更新平衡二叉树用O(logn)，因此一共使用O(nlogn)时间

## Triangulating a Monotone Polygon

假设我们获取到严格y-monotone的多边形P，也就是所有点都是分上下的，没有平行的边，这样就很容易实现triangulation。

* 我们需要同时处理两个boundary chain上的点，按y轴坐标排序。
* 建一个栈，（栈里放着所有已经处理过但还可以再连线的点。）
* 当遇到一个点的时候我们从这个点到栈里的点尽可能多的连线并分隔出三角，
* 那些被处理但是没被分隔的点就是在还需三角化的多边形的边界上。

遇到的新点$v_j$只有两种可能：一种是和栈前边的这些点在一边，另一种的不在一边。

不在一边的时候：

$v_j$可以向现在栈里除了栈底的其他所有点都连线（栈底的点已经和$v_j$在连着了，因为是y坐标排序，并且$v_j$是第一个另一边的点，所以一定是和这边的第一个点连着），因此需要全部出栈，连线分隔三角后把y坐标最低的那个点和$v_j$入栈，因为这两个点还是待三角化的多边形的边上。

![image-2023041925244713 PM](https://i.imgur.com/xuVGVFt.png)

在一边的时候：

现在不能简单的向所有栈里的点连线，因为有可能无法连对角线。做法是先出栈第一个点，也就是当前和$v_j$相连的那个点。然后一直出栈并连线直到遇到某个点不能连线的时候就停，并且把上一个出栈的点入栈，然后再入栈$v_j$，因为这两个点是最新的边界的点。

![image-2023041925552819 PM](https://i.imgur.com/ZwbI2mz.png)

算法如下：

![image-2023041924742698 PM](https://i.imgur.com/CVbtXd8.png)

if内解释：

* 假如不在一边就全部出栈，然后除了第一个点其他点全部连线，然后入栈两个点
* 假如在一边就出栈一个，然后只要能连线就出栈并连线，把最后一个出栈的入栈并且入栈$v_j$

## 时间复杂度

前两部是O(n)+O(1)，for循环是n-3次，每次最多入栈2个点，这就是2n-6。因为pop不能超过push次数，所以整体是O(n)

**Theorem** A simple polygon with n vertices can be triangulated in O(nlogn) time with an algorithm that uses O(n) storage.

# Manufacturing with Molds

有很多地方都要用到模具，这章要讨论能否在不破坏模具的前提下把物品取出来。
