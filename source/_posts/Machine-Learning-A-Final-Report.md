---
title: Machine-Learning-A-Final-Report
date: 2023-01-30 00:59:43
tags:
categories: UCPH
---

1. The Basic Assumptions (5 points) 
2. Weighted Neighbors (15 points)
3. The Impact of Dependence (20 points)
4. Sleep Well (30 points) 
5. Thanks for the Fish (15 points) 
6. Clustering (15 points) 

<!--more-->

# 1 The Basic Assumptions (5 points) 

1. Two basic assumptions are:
   1. The samples in S are i.i.d.
   2. The new samples come from the same distribution as the samples in S

2. 1. If samples are not i.i.d. it means they are associated with each other, then in extreme situation all of the samples in S are associated, the train effect is the same as there're only one example.
   2. If new samples doesn't come from the same distribution, then the train result model cannot be applied to it, because the new samples have no connection with train data, there's no sense to use the model to predict those new samples.





# 3 The Impact of Dependence (20 points)

1. As the data in subset S' are taken from each subset, so they are independent,and according to Theorem3.2 (Machine Learning Lecture Notes Yevgeny Seldin) we have $\mathbb{P}\left(\exists h \in \mathcal{H}: L(h) \geq \hat{L}(h, S)+\sqrt{\frac{\ln \frac{M}{\delta}}{2 n}}\right) \leq \delta$.

   So with probability at least $ 1-\delta$ for all $h \in \mathcal{H}$ we have 

   $L(h) \leq \hat{L}(h, S)+\sqrt{\frac{\ln \frac{M}{\delta}}{2 n}}$.

2. As we got the bound in the first question, it's target was S' = $\left\{\left(X_1, Y_1\right),\left(X_{r+1}, Y_{r+1}\right),\left(X_{2 r+1}, Y_{2 r+1}\right), \ldots\right\}$ 

   Now we imagine  $S_2 = \left\{\left(X_2, Y_2\right),\left(X_{r+2}, Y_{r+2}\right),\left(X_{2 r+2}, Y_{2 r+2}\right), \ldots\right\}$

   Untile $S_j = \left\{\left(X_j, Y_j\right),\left(X_{r+j}, Y_{r+j}\right),\left(X_{2 r+j}, Y_{2 r+j}\right), \ldots\right\}$

   each of them has a bound $L(h) \leq \hat{L}(h, S)+\sqrt{\frac{\ln \frac{M}{\delta}}{2 n}}$, so we sum them together and form a $S = S_1 + S_2 +...S_j$.

   And to this S we have the bound $L(h) \leq \hat{L}(h, S)+\sqrt{\frac{\ln \frac{M}{\delta}}{2 n}}$.

   

# 4 Sleep Well (30 points) 

## 4.1 Data understanding and preprocessing

I used numpy to load the data file,then use Counter to count the number of each class and divide it by the lenth, then print it out and got the following result:

> Class:  0.0 frequency:  0.5208753410034397 
>
> Class:  1.0 frequency:  0.09551061558533981 
>
> Class:  2.0 frequency:  0.25272802751749496 
>
> Class:  3.0 frequency:  0.04693986478472305 
>
> Class:  4.0 frequency:  0.08394615110900248

## 4.2 Principal component analysis

I used PCA from sklearn to do the PCA work,it uses fit to do the calculate work with Xtrain value and the eigenvalue is it's explained_variance_ / sum of eigenvalues. following is the plot and it's y axis is scaled by log.

![image-2022103124653275 PM](https://i.imgur.com/ZBtBHCt.png)

Then I sum the explained_variance which is the information each eigenvalue holds untile it is greater than 0.9 and print it, and got it needs 5 components to reach 90% variance.	

Then I used pca.transform to project the data on the principal components and take the first two to plot this:

![image-20221030122108004 AM](https://i.imgur.com/ub1pttZ.png)

## 4.3 Clustering

I used KMeans from sklearn and specify n_clusters = 5 to perform 5-means clustering. Following is the plot. We can see the centers are in the class points and they are in each classes field, but it doesn't perform very well. Maybe it's because the data are all stack together

![image-20221030122612558 AM](https://i.imgur.com/SMkBWH8.png)

## 4.4 Classification

### logistic regression

I used L2 regularization which changes the loss function to this:$\frac{1}{N} \sum_{i=1}^N(\hat{Y}-Y)^2+\lambda \sum_{i=1}^N \theta_i^2$ , it will keep all the characteristic value but reduce the magnitude of it.It will prevent the model being overfit.

Following is the cost output:

> Train loss: 0.14950776894793025 
>
> Test loss: 0.09920149629523056

### Random forests

I used RandomForest from sklearn and set the n_estimators to 50,100 and 200.Random forests training and test loss are as follows:

> Train loss for 50 trees: 0.00029652473016249557 
>
> Test loss for 50 trees: 0.1122940795626214 
>
> Train loss for 100 trees: 0.0 
>
> Test loss for 100 trees: 0.10970433781742321 
>
> Train loss for 200 trees: 0.0 
>
> Test loss for 200 trees: 0.11107114596072225

### knn

I used KNeighbors from sklearn to setup a  KNN model and used GridSearchCV to look for the best k grid by grid in a range of 1-30 with 5 folds, so it will search in 5*29=145 fits and get the best k.After searching here's the result:

> Fitting 5 folds for each of 29 candidates, totalling 145 fits 
>
> Best K:  26 
>
> Train loss: 0.14135333886846163 
>
> Test loss: 0.10164736349902885

# 5 Thanks for the Fish (15 points) 

First I used numpy to load the data, and I used The pseudo inverse to solve the question.

For pseudo inverse I first added a colomn of 1 to the input matrix, then use the fomula $ w^* = (X^TX)^-1X^Ty$ to calculate the parameters. Then I got b as 1105.41535282 and w1 as 44.73450994, w2 as -36.8333.

MSE:79709.30475880645 

biased sample variance:1193588.0208333333



# 6 Clustering (15 points) 

1. if k = 1 ,then after choosen a point randomly by k-means++ and calculate the center with k-means I got the center as (-0.5,0)

2. It will choose from these 6 points with probobally for each as 1/6 for the first point

3. As A is chosen to be $c_1$ then we can get $D((-6,2),c_1)$ = $\sqrt{173}$, $D((-6,-2),c_1) = \sqrt{173}$, $D((0,2),c_1) = \sqrt{53}$,$D((0,-2),c_1) = \sqrt{53}$,$D((2,0),c_1) = 5$.

   Then we calculate$c_2=\left\{\begin{array}{lll}(-6,2) & \text { w.p. } & \frac{173}{477} \\ (-6,-2) & \text { w.p. } & \frac{173}{477} \\ (0,2) & \text { w.p. } & \frac{53}{477}\\ (0,-2) & \text { w.p. } & \frac{53}{477} \\ (2,0) & \text { w.p. } & \frac{25}{477} \end{array}\right.$

​				And then we use roulette wheel selection to select one from these 5 points as $c_2$

4. As A is $c_1$ and F is $c_2$,when calculating D we select C,D,E to be with F and B with A as they are the nearest center.Then we can get $D((-6,-2),c_2) = 4$,$D((0,2),c_2) = 6$,$D((0,-2),c_2) = \sqrt{52}$,$D((2,0),c_1) = 5$.

   Then we can calculate $c_3=\left\{\begin{array}\\ (-6,-2) & \text { w.p. } & \frac{16}{129} \\ (0,2) & \text { w.p. } & \frac{36}{129}\\ (0,-2) & \text { w.p. } & \frac{52}{129} \\ (2,0) & \text { w.p. } & \frac{25}{129} \end{array}\right.$

   And then we use roulette wheel selection to select one from these 4 points as $c_3$.

5. we can calculate the loss as $16+8+8 = 32$ 

6. First we get 3 clusters which is {A},{F,E},{B,C,D}.

   Then we calculate each center of these 3 clusters and got(7,0),(-6,0),(2/3,0).

   Then we get 3 clusters which is {A},{F,E},{B,C,D} with there new centering.

   Then we calculate each center and found it converges, and the clustering is done.

   The loss is 4+4+16/9+40/9+40/9=56/3
