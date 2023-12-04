---
title: SIP_note
date: 2023-04-06 14:36:09
tags: ImageProcessing
categories: UCPH
---

A brief note for the class Signal and Image Processing includes most of the class.

<!--more-->

# Signal and Image Processing notes

## Intro

We are dealing with signals, an image can also be considered a kind of signal.

### Image and signal basics and terminology

a digital image is an n-dimensional array of quantities, if n = 2 then it's a pixel.

The resolution is given by the number of pixels in the image array

### Color and spectral measurements

color can be represented in RGB(Red Greed Blue) and HSV(Hue Saturation Value)

Convert RGB to gray scale: Gray = 0.299R + 0.587G + 0.114B

## Pixel-wise Operations, Intensity Transformations, Image Formation, and the Convolution Integral

### Image basics

JPEG: unsigned 8-bit int(lossy)

PNG: 1,2,4,8,16 bit unsigned int

TIFF: 1-32 bit unsigned int

### Basic pixel-wise operations

Adding or subtracting a constant: J(r,c) = I(r,c)+C

Multiplication or division by a constant: J(r,c) = C*I(r,c)

Adding or subtracting images (pixel-wise): J(r, c) = I A (r, c) + I B (r, c)

Multiplication or division of images (pixel-wise): J(r, c) = I A (r, c)⋅ I B (r, c)

**Be careful to handle over- and underflow! Usually, clip
the values to the quantization range.**

### Pixel-wise intensity transforms

The Dynamic range is the actual range of intensity
values [I min, I max] present in the image. 

We can change the dynamic range of an image by
applying functions on intensity values.

#### Logarithmic transform of intensities:

$\begin{aligned} & J(x, y)=c \ln \left[1+\left(e^\alpha-1\right) I(x, y)\right]  \alpha>0\end{aligned}$

用于查看图片暗处的细节，原理是把暗处intensity拉伸，同时亮处的intensity不怎么变

#### Exponential transform of intensities：

$\begin{aligned} J(x, y) & =c\left[(1+\alpha)^{I(x, y)}-1\right]\alpha  >0 .\end{aligned}$

用于查看亮处细节，原理同上

#### Power-law (Gamma) transform

$J(x, y)=c[I(x, y)]^\gamma$

可以对动态范围做调整

![image-20230405123311371 PM](https://i.imgur.com/7cKLkeh.png)

#### bit-plane slicing

把图片每个像素点分解成8层后做逻辑和操作获得八张图片

例如10010110,每层都拿一个对应的数，如第八层拿第一个1，以此类推。这种情况下第八层是最significant的，因为它可以表达出图片的大致轮廓，只需要通过这个图片就能大概知道原图的形状。

![image-20230405124017052 PM](https://i.imgur.com/UWbKimM.png)

为了节省空间可以只取前几层的图片做叠加。

### A Mathematical Model of Image Formation (Camera)

照相机可以视为对进入的光源做PSF变化再加噪音后返回一张图片

PSF使用convolution对图片进行操作

有多种不同的PSF构造方式

## filtering

可以通过应用多种不同的滤镜来处理图片。

输入一个图片，经过处理（卷积）后输出处理后的图片，基于neighborhood

有linear和non-linear两种

linear是可以写出具体kernel的，但是两种都是shift invariant。

### Linear filtering

Applying the linear filter to the image f is done by convolution:
$$
g(x, y)=\{f * h\}(x, y)=\iint_{-\infty}^{\infty} f\left(x^{\prime}, y^{\prime}\right) h\left(x-x^{\prime}, y-y^{\prime}\right) d x^{\prime} d y^{\prime}
$$
In discrete filtering,we compute a new value for a traget pixel, we need to define a filter center for the target pixel.Normally it's the center if the window size is odd.

### Some common linear filters

#### Mean filter

$$
\boldsymbol{h}_N=\frac{1}{N}[1, \cdots, 1]
$$

### 边界处理

* Pad the border 用数字填充，通常是0.缺点是卷积后的图片边界比较暗
* Symmetric mirroring 使用另一边的镜像填充
* Periodic boundary 把图像看做周期性的
* Leave border pixels unchanged 直接复制边缘
* Filter only inside the image and crop away the border 只做能处理的边界，但是会让图片变小

#### Linear separable filters

A linear filter is linear separable, if it can be decomposed into a linear filter along the x-axis and another along the y-axis.
$$
f * \boldsymbol{h}_{N \times N}=f * \frac{1}{N^2}\left[\begin{array}{ccc}
1 & \cdots & 1 \\
\vdots & \ddots & \vdots \\
1 & \ldots & 1
\end{array}\right]=f * \frac{1}{N}[1, \cdots, 1] * \frac{1}{N}\left[\begin{array}{c}
1 \\
\vdots \\
1
\end{array}\right]
$$
即一个2D的kernel可以表示为两个1D的矩阵乘法的结果，可以让计算更快



#### Filtering multi-channel images

对RGB分别应用filter有可能会让颜色泄露出来，需要知道与对HSV的V应用结果不一样

#### Discrete Gaussian filter

由高斯方程得到的一个线性可分的filter，特点是中心权重大

参数有sigma和kernelsize

#### Derivative filter

对图片求导，由于图片是离散的所以取一个近似，即

$\frac{\partial f}{\partial x} \approx f(x+1, y)-f(x, y)$

$\frac{\partial f}{\partial y} \approx f(x, y+1)-f(x, y)$

对应的卷积核：

[1 -1]

$\left[\begin{array}{c}1 \\ -1\end{array}\right]$

还有多种其他的卷积核：

![image-2023021913252907 PM](https://i.imgur.com/y9WB0KY.png)

可用于边界检测

噪声对于求导卷积影响很大



### Non-linear filtering

#### median filter

rank filter的一种特殊情况，每次先排序然后取中位数

## Fourier Transform

Power spectrum 是由音波图经过傅里叶变换得来的，表达的是声音的frequency perspective

图片经过傅里叶变化也可以得到一个图,这个图显示了图片的频率，经过shift后中心的点是高频

图片经过傅里叶变化后可以通过遮盖特定部分来去除那一块频率的噪音，做法是给那一块加一个黑块。

高斯的傅里叶还是高斯

## intensity thresholding and intensity histograms

### Intensity Thresholding

Simple thresholding formula:
$J(x, y)= \begin{cases}1 & , \text { if } I(x, y)>\tau \\ 0 & , \text { Otherwise }\end{cases}$

可以得到一个binary image

也可以在颜色通道上进行Thresholding

### Intensity Histograms

Intensity histogram: Count the number of pixels having a specific intensity level 

$H_I(v)=\#\{(x, y), \quad I(x, y)=v\}, \quad v \in[0, L-1]$

可以使用Histogram做thresholding，只保留某些intensity值

### Histogram Matching

把一幅曝光不好的图像做Histogram Matching到另一副图像上可以调整亮度

### Histogram equalization

可以让图像的histogram分布均匀

也可以应用在色彩通道

## Mathematical morphology, distance transform, and connected components

### Mathematical morphology

图像形态学，主要操作包括膨胀与腐蚀

Dilation: $X \oplus B=\{p \in \Omega \mid p=x+\mathrm{b}, \mathrm{x} \in X$ and $\mathrm{b} \in B\}$

把b绕着X转一圈后扩大X的面积，可用于去除中心的空洞

Erosion: $X \ominus B=\{p \in \Omega \mid p+\mathrm{b} \in X$ for all $\mathrm{b} \in B\}$

把b在$\Omega$遍历一遍，删掉所有不能覆盖的部分

Opening: $X \ominus B \oplus B$

Closing: $(X \oplus B) \ominus B$

还可以用于边缘检测

![image-2023040530508959 PM](https://i.imgur.com/1P3I6me.png)

参考链接：[链接](https://blog.csdn.net/cutemypig/article/details/107575375?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168069897816800180664562%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=168069897816800180664562&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-107575375-null-null.142^v81^wechat,201^v4^add_ask,239^v2^insert_chatgpt&utm_term=%E5%9B%BE%E7%89%87%E5%BD%A2%E6%80%81%E5%AD%A6&spm=1018.2226.3001.4187)

## Image Restoration and Deconvolution

### Laplacian image sharpening

拉普拉斯算子在图像中变化明显的地方很容易检测到。

用原图减图片的二阶导可以实现image sharpening

但是缺点是如果原图有噪音这个操作会增加噪音，因为求导操作会增大噪音



### Models of image degradation



### Deconvolution without and with noise

图像形成过程：f(x,y) * h(x,y) + n(x,y) = g(x,y)

图像还原过程： g(x,y) use h(x,y) = $\hat f(x,y)$

Wiener filter可以用来还原带噪音的图像。

$$\frac{1}{H^{\prime}(u, v)}=\frac{1}{H(u, v)} \frac{|H(u, v)|^2}{|H(u, v)|^2+S_n(u, v) / S_f(u, v)}$$

Where $S_n(u, v)=|N(u, v)|^2, S_f(u, v)=|F(u, v)|^2$ are the power spectra of the noise and the original image.

## transformations

### Motivation

Object shape can be a curve that represents the outline fo the object boundary

我们会获得各种图片，需要对图片进行一些变化以符合要求，如旋转，拉伸等

### Transformations of points and intensities:

#### homogeneous coordinates

A 2D point $(x, y)$ has, for any $w \neq 0$, a homogeneous coordinate representation $[w x, w y, w]^{\top}$.

### Image warps (transformation of intensities)

有多种转换方式

## Features

### Intensity edges

Use local maxima of gradient magnitude to detecte edge

Canny edge detector: use thresholding and analysis of connectivity to detect

## scalespace

### Image Pyramids

Discrete scale

### Linear scale space theory

Continouos scale 

### Multi-scale feature detection 

## segmentation

### intensity based

使用threshold

或把图片拆分成多个高斯曲线的叠加

### edge based 



### Region based

region growing

### Energy minimization

minimize this formula:
$$
E(f)=\sum_{p \in \mathcal{P}} D_p\left(f_p\right)+\sum_{p, q \in \mathcal{N}} V_{p, q}\left(f_p, f_q\right)
$$

### Chan-Vese

minimize this formula to be 0
$$
\begin{aligned}
F_1(C)+F_2(C)= & \int_{\text {inside }(C)}\left|u_0(x, y)-c_1\right|^2 d x d y \\
& +\int_{\text {outside }(C)}\left|u_0(x, y)-c_2\right|^2 d x d y
\end{aligned}
$$

### Hough transform

将原图中$\rho_{\circ}=x \cdot \cos \theta_{\circ}+y \cdot \sin \theta_{\circ}$ 转化成关于$\theta,\rho$ 的坐标系

1. Chose range and discretization of ρ and θ.
   a. θ in [0, 180] degrees
   b. ρ in [-d, d] where d is the length of the edge image’s diagonal.

2. Create accumulator 2D array (Hough Space) and initialize to zero.
3. For every edge pixel, loop through θ range, calculate corresponding ρ, and increment the accumulator at these coordinates.

4. Lines correspond to accumulator values larger than a certain threshold.

可以用来检测直线

### Supervised machine learning for image segmentation

## Texture

can be used to identify regions containing distinct textures

Use filter banks

## Shape models and procrustes alignment

### Procrustes alignment

1. Translational alignment
2. Scaling alignment
3. Rotational alignment

Translational alignment: subtracting the sample mean

Scaling: S = sI
$$
s=\frac{\sum_{i=1}^N \overrightarrow{x'}_i^T \overrightarrow{\mathbf{x}_i}}{\sum_{i=1}^N \overrightarrow{\mathbf{x}}_i^T \overrightarrow{\mathbf{x}_i}}
$$
其中$x'$是target

rotation:
$$
\mathbf{H}=\mathbf{V}^T \mathbf{R}=\mathbf{I} \quad \Rightarrow \quad \mathbf{R}=\mathbf{V} \mathbf{U}^T
$$
where $\mathbf{U}$ and $\mathbf{V}$ are obtained from the SVD of $\mathbf{X Y} \mathbf{Y}^T$ - ie from $\mathbf{X Y}^T=\mathbf{U S V}^T$.
