---
title: Convolutional-NeuralNetwork
date: 2024-09-25 12:40:32
tags:
categories: MachineLearning
---

Learning Note for "Convolutional Neural Networks" by DeepLearning.AI

<!--more-->

# Foundation of Convolutional Neural Networks

在对大图片进行神经网络学习的时候特征太多了，需要使用卷积操作来减小复杂度。需要使用一个核函数来做卷积操作，具体核函数的内容需要通过机器学习来获得。

## Edge Dection

假如有一个7 x 7的图片，想要用卷积来检测图片里的边缘需要先定义一个卷积核filter，他是3 x 3的.然后把这两个东西做卷积操作，即先把卷积核放到一个地方，逐项相乘后求和得到一个数。

![image-20240925125401652 PM](https://raw.githubusercontent.com/1982606762/picgo/master/image-20240925125401652%E2%80%AFPM.png)

得到的矩阵会有有数的和0，有数的地方就是原图片里的边缘。

所以同理我们有水平边缘检测核函数：
$$
1 1 1\\
0 0 0\\
-1 -1 -1
$$

## Padding

对于一个n x n大小的输入，应用一个f x f大小的核函数后得到一个n-f+1大小的结果。因此图片每次计算都会缩小，而且在边界的像素点只使用了一次，而中间的像素点被使用了很多次。

要想解决这个问题可以把输入的图片用数字填充一层，比如之前是6x6输入和3x3核，变成8x8输入后输出就变成6x6了。

有两种卷积方法，Valid和Same卷积。Valid就是没有padding的卷积，输出会越来越小。Same代表输出的大小和输入的大小一样，需要(f-1)/2大小的padding，因此filter最好是奇数大小。

## Strided Convoulution

还可以修改每次前进的步幅，这样得到的输出就是$(n+2p-f)/s +1$大小。

## Convolution over 3D volumes

卷积不仅可以对2维图像实现，还可以对3维对象进行卷积操作。

假如我们要对一个RGB的图像做卷积，这个图像可以看做是n x n x 3的物体，这时就可以用3x3x3的卷积核进行计算,输出后可以得到一个一层的矩阵。

具体计算卷积的时候需要把卷积核放在左上，然后求和27个乘积来作为第一个结果，然后继续往前走直到结束。

## 应用多个filter进行处理

如果要应用多个filter就需要先让每个filter对图片进行卷积得到一个二维的结果，然后把所有结果堆叠起来得到一个d高度的三维矩阵，这里的d代表应用的filter数量。

![image-2024092531323353 PM](https://raw.githubusercontent.com/1982606762/picgo/master/image-2024092531323353%E2%80%AFPM.png)

## 卷积神经网络

有了卷积操作后我们可以搭建卷积神经网络。

例如：第一层输入一个RGB图像，经过两个卷积核操作后分别使用非线性方程处理（ReLU）然后得到两个值，堆叠后得到第一层的结果。这个步骤类似神经网络中的z = wa+b, a1=g(z)操作，经过一层处理后得到一个4x4x2的输出。

对于一个这样的神经网络有$2*(3*3*3+1)$个参数需要学习。

每一层的结果大小都是$(n+2p-f)/s +1$，高度是前一层filter的数量。

在最后一层可以把所有数字都展开成一个变量，然后使用逻辑回归或softmax来处理得到一个结果。

## Pooling layer and fully connect layer

除了卷积层，卷积神经网络还可以用两种其他的层。

### Pooling layer

Max pooling使用一个filter获得每个filter区域里的最大值，它可以定义大小f和步长s，这两个参数定义之后就不改了。

如果应用于三维物体的话就对每一层分别使用filter，然后获得一个一样层数的输出。

还有别的，如average pooling就是算每个区域里的平均值。

一般来讲使用max pooling更多。

![img](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/mDHvv_JvTj-WDyCFRwer2w_c4980b8165d946c4a04aa134c8fadaa1_Screenshot-2022-10-08-at-6.15.38-PM.png?expiry=1727395200000&hmac=PDVtDpIxfcPyoRZtFE_pRRB2tJXv6_SmNTQg-kIX0k0)

## Reason for using convolution

卷积神经网络可以使用更少的参数来获得结果，这样可以大大加快训练速度。使用更少参数的原因有两点：

* Parameter sharing：一个卷积核可以作用于多个位置，这样用相同的参数可以训练不一样的数据，从而减少参数数量。
* Sparsity of connect： 
