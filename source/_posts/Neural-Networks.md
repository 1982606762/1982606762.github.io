---
title: Neural-Networks
date: 2023-11-21 18:32:47
tags: neural-network
categories: MachineLearning

---

A note for the Coursera course "Advanced Learning Algorithms"

<!--more-->

# Neural networks intuition

## Neural networks model

![image-2023112164650789 PM](https://raw.githubusercontent.com/1982606762/picgo/master/image-2023112164650789%E2%80%AFPM.png)

右上角的角标代表他在哪一层，右下角的角标代表一层layer里的每一个神经元里包含的两个参数。除了输出层其他的都叫hidden layer. Layer3 有三个neuran. g()叫做激活函数(activation function).他现在是一个sigmoid function

> Sigmoid function: $S(x) = \frac{1}{1+e^{-x}}$
>
> ![sigmoid function](https://raw.githubusercontent.com/1982606762/picgo/master/sigmoid%20function.png)

## Forward propagation(正向传播)

Use a 3-layer neural network to do handwritten digit recognition.

![image-2023112170609225 PM](https://raw.githubusercontent.com/1982606762/picgo/master/image-2023112170609225%E2%80%AFPM.png)

这里x以一个列距阵的形式输入，求完内积之后会得到一个数，然后再加b.所以a1是一个25个内容的列矩阵。

## Use TensorFlow to implement

`x = np.array([[1],[2],[3]])`列向量

Define a layer:`layer_1 = Dense(units=3,activation='sigmoid')`

Get the result from layer:`a1 = layer_1(x)`

Use the Sequential function to let TensorFlow build a model for you: `model = Sequential([layer_1,layer_2])`

Then use `model.fit(x,y)` to train the model

Use `model.predict(x_new)` to predict

