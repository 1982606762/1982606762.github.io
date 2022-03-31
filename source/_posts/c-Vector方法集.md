---
title: c++ Vector方法集
date: 2022-02-24 21:54:17
tags:
categories: C/C++
---

![image-20220224215604333](https://img.zhaoxuanlang.cn/image-20220224215604333.png)

<!--more-->

# 迭代器

1. [begin()](https://www.geeksforgeeks.org/vectorbegin-vectorend-c-stl/) – 返回一个指向向量中第一个元素的迭代器
2. [end()](https://www.geeksforgeeks.org/vectorbegin-vectorend-c-stl/) – 返回一个迭代器，指向向量中最后一个元素之后的理论元素
3. [rbegin()](https://www.geeksforgeeks.org/vector-rbegin-and-rend-function-in-c-stl/) – 返回一个反向迭代器，指向向量中的最后一个元素（反向开始）。它从最后一个元素移动到第一个元素
4. [rend()](https://www.geeksforgeeks.org/vector-rbegin-and-rend-function-in-c-stl/) – 返回一个反向迭代器，指向向量中第一个元素之前的理论元素（视为反向结束）
5. [cbegin()](https://www.geeksforgeeks.org/vector-cbegin-vector-cend-c-stl/) – 返回指向向量中第一个元素的常量迭代器。
6. [cend()](https://www.geeksforgeeks.org/vector-cbegin-vector-cend-c-stl/) – 返回一个常量迭代器，指向向量中最后一个元素之后的理论元素。
7. [crbegin()](https://www.geeksforgeeks.org/vectorcrend-vectorcrbegin-examples/) – 返回一个常量反向迭代器，指向向量中的最后一个元素（反向开始）。它从最后一个元素移动到第一个元素
8. [crend()](https://www.geeksforgeeks.org/vectorcrend-vectorcrbegin-examples/) – 返回一个常量反向迭代器，指向向量中第一个元素之前的理论元素（被视为反向端）

```c++
// C++ program to illustrate the
// iterators in vector
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<int> g1;

	for (int i = 1; i <= 5; i++)
		g1.push_back(i);

	cout << "Output of begin and end: ";
	for (auto i = g1.begin(); i != g1.end(); ++i)
		cout << *i << " ";

	cout << "\nOutput of cbegin and cend: ";
	for (auto i = g1.cbegin(); i != g1.cend(); ++i)
		cout << *i << " ";

	cout << "\nOutput of rbegin and rend: ";
	for (auto ir = g1.rbegin(); ir != g1.rend(); ++ir)
		cout << *ir << " ";

	cout << "\nOutput of crbegin and crend : ";
	for (auto ir = g1.crbegin(); ir != g1.crend(); ++ir)
		cout << *ir << " ";

	return 0;
}

```

**输出：**

```
begin 和 end 的输出：1 2 3 4 5 
cbegin 和 cend 的输出：1 2 3 4 5 
rbegin 和 rend 的输出：5 4 3 2 1 
crbegin 和 crend 的输出：5 4 3 2 1
```

# 容量

**容量**

1. [size()](https://www.geeksforgeeks.org/vectorempty-vectorsize-c-stl/) – 返回向量中元素的数量。
2. [max_size()](https://www.geeksforgeeks.org/vector-max_size-function-in-c-stl/) – 返回向量可以容纳的最大元素数。
3. [capacity()](https://www.geeksforgeeks.org/vector-capacity-function-in-c-stl/) – 返回当前分配给向量的存储空间大小，以元素数表示。
4. [resize(n)](https://www.geeksforgeeks.org/vector-resize-c-stl/) – 调整容器大小，使其包含“n”个元素。
5. [empty()](https://www.geeksforgeeks.org/vectorempty-vectorsize-c-stl/) – 返回容器是否为空。
6. [shrink_to_fit()](https://www.geeksforgeeks.org/vector-shrink_to_fit-function-in-c-stl/) – 减小容器的容量以适应其大小并销毁超出容量的所有元素。
7. [Reserve()](https://www.geeksforgeeks.org/using-stdvectorreserve-whenever-possible/) – 请求向量容量至少足以包含 n 个元素。

# 元素访问

1. [引用运算符 [g\]](https://www.geeksforgeeks.org/vectoroperator-vectoroperator-c-stl/) – 返回对向量中位置“g”处元素的引用
2. [at(g)](https://www.geeksforgeeks.org/vectorat-vectorswap-c-stl/) – 返回对向量中位置“g”处元素的引用
3. [front()](https://www.geeksforgeeks.org/vectorfront-vectorback-c-stl/) – 返回对向量中第一个元素的引用
4. [back()](https://www.geeksforgeeks.org/vectorfront-vectorback-c-stl/) – 返回对向量中最后一个元素的引用
5. [data()](https://www.geeksforgeeks.org/vector-data-function-in-c-stl/) – 返回指向向量内部用于存储其拥有的元素的内存数组的直接指针。

```c++
// C++ program to illustrate the
// element accesser in vector
#include <bits/stdc++.h>
using namespace std;

int main()
{
	vector<int> g1;

	for (int i = 1; i <= 10; i++)
		g1.push_back(i * 10);

	cout << "\nReference operator [g] : g1[2] = " << g1[2];

	cout << "\nat : g1.at(4) = " << g1.at(4);

	cout << "\nfront() : g1.front() = " << g1.front();

	cout << "\nback() : g1.back() = " << g1.back();

	// pointer to the first element
	int* pos = g1.data();

	cout << "\nThe first element is " << *pos;
	return 0;
}

```

**Output:**

```
Reference operator [g] : g1[2] = 30
at : g1.at(4) = 50
front() : g1.front() = 10
back() : g1.back() = 100
The first element is 10
```

# 修饰符

1. [assign()](https://www.geeksforgeeks.org/vector-assign-in-c-stl/) - 它通过替换旧元素为向量元素分配新值
2. [push_back()](https://www.geeksforgeeks.org/vectorpush_back-vectorpop_back-c-stl/) – 将元素从后面推入向量
3. [pop_back()](https://www.geeksforgeeks.org/vectorpush_back-vectorpop_back-c-stl/) - 它用于从后面的向量中弹出或删除元素。
4. [insert()](https://www.geeksforgeeks.org/vector-insert-function-in-c-stl/) - 在指定位置的元素之前插入新元素
5. [erase()](https://www.geeksforgeeks.org/vectorclear-vectorerase-c-stl/) - 用于从容器中删除指定位置或范围的元素。
6. [swap()](https://www.geeksforgeeks.org/vectorat-vectorswap-c-stl/) - 用于将一个向量的内容与另一个相同类型的向量交换。尺寸可能不同。
7. [clear()](https://www.geeksforgeeks.org/vectorclear-vectorerase-c-stl/) - 用于删除向量容器的所有元素
8. [emplace()](https://www.geeksforgeeks.org/vector-emplace-function-in-c-stl/) - 它通过在位置插入新元素来扩展容器
9. emplace_back() \- 用于将新元素插入向量容器中，新元素添加到向量的末尾

```c++
// C++ program to illustrate the
// Modifiers in vector
#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main()
{
	// Assign vector
	vector<int> v;

	// fill the array with 10 five times
	v.assign(5, 10);

	cout << "The vector elements are: ";
	for (int i = 0; i < v.size(); i++)
		cout << v[i] << " ";

	// inserts 15 to the last position
	v.push_back(15);
	int n = v.size();
	cout << "\nThe last element is: " << v[n - 1];

	// removes last element
	v.pop_back();

	// prints the vector
	cout << "\nThe vector elements are: ";
	for (int i = 0; i < v.size(); i++)
		cout << v[i] << " ";

	// inserts 5 at the beginning
	v.insert(v.begin(), 5);

	cout << "\nThe first element is: " << v[0];

	// removes the first element
	v.erase(v.begin());

	cout << "\nThe first element is: " << v[0];

	// inserts at the beginning
	v.emplace(v.begin(), 5);
	cout << "\nThe first element is: " << v[0];

	// Inserts 20 at the end
	v.emplace_back(20);
	n = v.size();
	cout << "\nThe last element is: " << v[n - 1];

	// erases the vector
	v.clear();
	cout << "\nVector size after erase(): " << v.size();

	// two vector to perform swap
	vector<int> v1, v2;
	v1.push_back(1);
	v1.push_back(2);
	v2.push_back(3);
	v2.push_back(4);

	cout << "\n\nVector 1: ";
	for (int i = 0; i < v1.size(); i++)
		cout << v1[i] << " ";

	cout << "\nVector 2: ";
	for (int i = 0; i < v2.size(); i++)
		cout << v2[i] << " ";

	// Swaps v1 and v2
	v1.swap(v2);

	cout << "\nAfter Swap \nVector 1: ";
	for (int i = 0; i < v1.size(); i++)
		cout << v1[i] << " ";

	cout << "\nVector 2: ";
	for (int i = 0; i < v2.size(); i++)
		cout << v2[i] << " ";
}

```

**Output:**

```
The vector elements are: 10 10 10 10 10 
The last element is: 15
The vector elements are: 10 10 10 10 10 
The first element is: 5
The first element is: 10
The first element is: 5
The last element is: 20
Vector size after erase(): 0

Vector 1: 1 2 
Vector 2: 3 4 
After Swap 
Vector 1: 3 4 
Vector 2: 1 2
```

