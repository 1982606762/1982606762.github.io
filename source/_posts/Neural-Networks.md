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

Use a 3-layer neural network to do handwritten digit recognition. Each layer is a dense layer.

![image-2023112170609225 PM](https://raw.githubusercontent.com/1982606762/picgo/master/image-2023112170609225%E2%80%AFPM.png)

这里x以一个列距阵的形式输入，求完内积之后会得到一个数，然后再加b.所以a1是一个25个内容的列矩阵。

## Use TensorFlow to implement

`x = np.array([[1],[2],[3]])`列向量

Define a layer:`layer_1 = Dense(units=3,activation='sigmoid')`

Get the result from layer:`a1 = layer_1(x)`

Use the Sequential function to let TensorFlow build a model for you: `model = Sequential([layer_1,layer_2])`

Then use `model.fit(x,y)` to train the model

Use `model.predict(x_new)` to predict

Define a model:

```python
model = Sequential(
    [               
        tf.keras.Input(shape=(400,)),    #specify input size
        tf.keras.layers.Dense(units=25,activation='sigmoid'),
        tf.keras.layers.Dense(units=15,activation='sigmoid'),
        tf.keras.layers.Dense(units=1,activation='sigmoid')
    ], name = "my_model" 
)   
```

Use a loss function:

```python
model.conpile(loss=BinaryCrossentropy())
```



After fitting make a prediction:

The input to `predict` is an array so the single example is reshaped to be two dimensional.

```python
prediction = model.predict(X[0].reshape(1,400))  # a zero
print(f" predicting a zero: {prediction}")
prediction = model.predict(X[500].reshape(1,400))  # a one
print(f" predicting a one:  {prediction}")
```

要想减小计算误差可以添加

`model.conpile(loss=BinaryCrossentropy(from_logitc = true))`

这可以让TensorFlow自动优化浮点数计算





## Vectorisation

Originally the calculation can be done in a for loop, but by using vector maltiplication it can be much more easier.

This image is the for loop code, it needs to get each parameter of the neurons and multiply and plus number b.

![image-2023121334422692 PM](https://raw.githubusercontent.com/1982606762/picgo/master/image-2023121334422692%E2%80%AFPM.png)

The code for this dense function:

```py
def my_dense(a_in, W, b, g):
    """
    Computes dense layer
    Args:
      a_in (ndarray (n, )) : Data, 1 example 
      W    (ndarray (n,j)) : Weight matrix, n features per unit, j units
      b    (ndarray (j, )) : bias vector, j units  
      g    activation function (e.g. sigmoid, relu..)
    Returns
      a_out (ndarray (j,))  : j units
    """
    units = W.shape[1]
    a_out = np.zeros(units)
    for j in range(units):
        w = W[:,j]
        z = np.dot(w,a_in) + b[j]
        a_out[j] = g(z)
    return(a_out)

```



The following img is vectorized implementation:

<img src="https://raw.githubusercontent.com/1982606762/picgo/master/image-20231213123737601%E2%80%AFPM.png" alt="image-20231213123737601 PM" style="zoom:33%;" />

Code:

```python
def my_dense_v(A_in, W, b, g):
    """
    Computes dense layer
    Args:
      A_in (ndarray (m,n)) : Data, m examples, n features each
      W    (ndarray (n,j)) : Weight matrix, n features per unit, j units
      b    (ndarray (1,j)) : bias vector, j units  
      g    activation function (e.g. sigmoid, relu..)
    Returns
      A_out (tf.Tensor or ndarray (m,j)) : m examples, j units
    """
    Z = np.matmul(A_in,W) + b
    A_out = g(Z)
    return(A_out)
```



### matrix multiplication

点乘是简单乘，绝大多数都是点乘.

$\mathbf{XW}$  is a matrix-matrix operation with dimensions $(m,j_1)(j_1,j_2)$ which results in a matrix with dimension  $(m,j_2)$. To that, we add a vector $\mathbf{b}$ with dimension $(1,j_2)$.  $\mathbf{b}$ must be expanded to be a $(m,j_2)$ matrix for this element-wise operation to make sense. This expansion is accomplished for you by NumPy broadcasting.



# Neural network training

1. Create the model

   Define how many layers and how many units in each layer and their activation function

2. Select loss and cost functions

   Select a loss function such as `BinaryCrossentropy()` from keras.losses

3. Train the model using gradient descent

   repeat 
   $$
   \begin{align*}
   w_j^{[l]} &= w_j^{[l]} - \alpha \frac{\partial}{\partial w_j} J(\hat{w}, b) \\
   b_j^{[l]} &= b_j^{[l]} - \alpha \frac{\partial}{\partial b_j} J(\hat{w}, b)
   \end{align*}
   $$

​	tensorflow can do it for you, you can just use `model.fit(X,y,epochs=100)` 

## Activation Functions

### Sigmoid

Better used on the binary classification problem

![fbbb9b2c-c2f4-43ed-92f6-1c635dece716](https://raw.githubusercontent.com/1982606762/picgo/master/fbbb9b2c-c2f4-43ed-92f6-1c635dece716.jpg)

The sigmoid activation function is defined as:

$$ S(x) = \frac{1}{1 + e^{-x}} $$

where:
- \( S(x) \) is the output of the sigmoid function,
- \( e \) is the base of the natural logarithm,
- \( x \) is the input to the function.

### ReLU

Better used on the regression problem



The ReLU (Rectified Linear Unit) activation function is defined as:

$$ g(z) = \max(0, z) $$

where:
- \( g(z) \) is the output of the ReLU function,
- \( z \) is the input to the function.

### Linear function

Better used on the regression problem



$g(z) = z$

### What if we don't use activation function?

It will be the same as linear regression

## Multiclass Classification

### Softmax algorithm

For original logistic regression using sigmoid output can be denoted as $$ a_1 = g(z) = \frac{1}{1+e^{-z}} = P(y = 1|x) $$

Softmax allows to have multiple options being predicted with formula as
$$
a_1 = \frac{e^{z_1}}{e^{z_1} + e^{z_2} + e^{z_3} + e^{z_4}} = P(y = 1|x)
$$
a是y成为某一个结果的概率

It in general can be denoted as:
$$
z_j = \mathbf{W}_j \cdot \mathbf{x} + b_j \quad j = 1, \ldots, N\\

a_j = \frac{e^{z_j}}{\sum_{k=1}^{N} e^{z_k}} = P(y = j|x)
$$

### Cost function for softmax

$$
a_1 = \frac{e^{z_1}}{e^{z_1} + e^{z_2} + \dots + e^{z_N}} = P(y = 1|\mathbf{x})
$$
$$
\vdots
$$
$$
a_N = \frac{e^{z_N}}{e^{z_1} + e^{z_2} + \dots + e^{z_N}} = P(y = N|\mathbf{x})
$$
$$
\text{loss}(a_1, \dots, a_N, y) =
\begin{cases}
-\log a_1 & \text{if } y = 1 \\
-\log a_2 & \text{if } y = 2 \\
\vdots \\
-\log a_N & \text{if } y = N
\end{cases}
$$

### How to add Softmax into neural network

Change the last output layer from 1 unit to multiple units and let it work as softmax algorithm.

### Multi-label classification

在这种问题里y可以是一个数组，例如识别一张图片中有没有三种不一样的物体，y就会输出三个数

Solution 1 is to treat it as 3 separate different problems and build 3 neural networks.

Solution2 is to build one neural network with three outputs, so a[3] has three elements.

## optimization algorithm

### Adam Algorithm

Adaptive Moment estimation

If w or b keeps moving in same direction it will increase $\alpha$.

If w or b keeps oscillating it will reduce $\alpha$.

要想使用需要如下代码：

```python
model.compile(optimizer=tf.keras.optimizera.Adam(learning_rate=le-3),lost=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))
```

## Complex model example

Below, compose a three-layer model:

- Dense layer with 120 units, relu activation
- Dense layer with 40 units, relu activation
- Dense layer with 6 units and a linear activation (not softmax)
  Compile using
- loss with `SparseCategoricalCrossentropy`, remember to use `from_logits=True`
- Adam optimizer with learning rate of 0.01.

```python
# UNQ_C3
# GRADED CELL: model
import logging
logging.getLogger("tensorflow").setLevel(logging.ERROR)

tf.random.set_seed(1234)
model = Sequential(
    [
        ### START CODE HERE ### 
        tf.keras.layers.Dense(units=120,activation='relu'),
        tf.keras.layers.Dense(units=40,activation='relu'),
        tf.keras.layers.Dense(units=6,activation='linear')
        
        ### END CODE HERE ### 

    ], name="Complex"
)
model.compile(
    ### START CODE HERE ### 
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.01)
    ### END CODE HERE ### 
)
```



Reconstruct your complex model, but this time include regularization. Below, compose a three-layer model:

- Dense layer with 120 units, relu activation, `kernel_regularizer=tf.keras.regularizers.l2(0.1)`
- Dense layer with 40 units, relu activation, `kernel_regularizer=tf.keras.regularizers.l2(0.1)`
- Dense layer with 6 units and a linear activation. Compile using
- loss with `SparseCategoricalCrossentropy`, remember to use `from_logits=True`
- Adam optimizer with learning rate of 0.01.

```python
# UNQ_C5
# GRADED CELL: model_r

tf.random.set_seed(1234)
model_r = Sequential(
    [
        ### START CODE HERE ###         
        tf.keras.layers.Dense(units=120,activation='relu',kernel_regularizer=tf.keras.regularizers.l2(0.1)),
        tf.keras.layers.Dense(units=40,activation='relu',kernel_regularizer=tf.keras.regularizers.l2(0.1)),
        tf.keras.layers.Dense(units=6,activation='linear')
        
        ### START CODE HERE ### 
    ], name= None
)
model_r.compile(
    ### START CODE HERE ### 
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.01)
    ### START CODE HERE ### 
)

```





# Evaluating a model

## Bias and variance

Calculate $J_{train}$ and $J_{CV}$and see what's the result.

CV means cross-validation

If both are high it means bias is high, if train is low and cv is high it means variance is high.

### Regularization and bias/variance

$J(\hat{w},b) = \frac{1}{2m} \sum_{i=1}^{m} \left( f_{\hat{w},b}(x^{(i)}) - y^{(i)} \right)^2 + \frac{\lambda}{2m} \sum_{j=1}^{n} w_j^2$

成本函数中有lambda用于控制正则化(Regularization)过程的参数。lambda大的时候正则化效果强，模型会有high bias. lambda小的时候模型会过拟合导致high variance.

如何选择合适的lambda？

从0开始试，然后试0.01,0.02……逐渐增加。计算所有的Jcv，选择最小的那个对应的lambda。

### Baseline level of performance

给一些例子来帮助判断数字是高还是低

假如人类的误差是10.6%，训练集误差是10.8%，交叉验证集误差是14.8%那么训练集误差可视为很低，但是交叉验证集误差高，代表可能是方差很高

如果训练集的误差也很高说明可能是high bias

### Learning curve

画一条曲线显示误差随着训练集增加的变化。训练集误差和验证集误差趋势如下图。

![image-2024011842639798 PM](https://raw.githubusercontent.com/1982606762/picgo/master/image-2024011842639798%E2%80%AFPM.png)

如果模型有high bias,那么增加数据量不会对模型有帮助。

如果有high variance，增加数据量会提高Jtrain并且接近人类水平并且降低Jcv。

### Example reciple

如果在训练集效果不好-》使用更大的网络。如果训练集效果好，验证集效果不好-》更多数据。目标是验证集效果好

# Decision tree model

## Decision tree

用于当特征是离散值的时候，例如耳朵形状，脸大小等。

最上边是root node，中间的是decision node，下边的是leaf node

构建决策树：

1. 从根节点出发把训练集分成两部分
2. 左右分别选择特征来分离数据
3. 当结束条件触发的时候结束
4. 把结果按照标签构建叶子结点，即决策的结果

问题：

什么时候结束？

* 当一个节点结果全都是一个标签的数据
* 当深度触发最大值
* 当纯净值足够大
* 当某个节点的结果数量太少

## measure of impurity

使用嫡函数(entropy function)来表示纯净性。

![image-2024012884947964 PM](https://raw.githubusercontent.com/1982606762/picgo/master/image-2024012884947964%E2%80%AFPM.png)

这里的p1是指是一种类型的比例,纵坐标是嫡的数据。

$p_0 = 1 - p_1$

$H(p_1) = -p_1log_2(p_1) - (1 - p_1) log_2(1 - p_1)$

## Choosing a split

如何选择使用哪个属性来做分隔，需要使用information gain方法。

xxxxxxxxxxx

## Use one-hot encoding to code features

如果一个feature可以接受k个不一样的赋值那么就创建k个二进制数来代表这个feature。

这样就可以吧多个特征变成一串01数

## 使用连续变量

可以画一条线，高于这个值的都是1，低于这个值的都是0

这条线的选址通常是使用Information gain来获取最佳的取值

