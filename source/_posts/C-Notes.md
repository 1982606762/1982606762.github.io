---
title: C++_Notes
date: 2024-06-07 10:58:37
tags: C++
categories: C/C++
---

C++笔记

<!--more-->

# 基础部分

```
#include <iostream> //#是预处理(pre processing statement),会在编译之前执行。 include会paste a file to this place
using namespace std;

int main() {
    string input;
    cout << "Enter your input: ";
    cin >> input;
    cout << "You entered: " << input << endl;
    return 0;
}
```

## 头文件

```c++
#ifndef CPP_STUDY_TEST_H
#define CPP_STUDY_TEST_H
//这里ifdef用处是防止重复include 头文件
#endif //CPP_STUDY_TEST_H
```

引用的时候双引号是从当前目录开始找，尖括号是从根目录开始找。

`stdio.h`这种标准库是给c的，结尾是h。c++的标准库没有.h扩展。

## 循环

```c++
for(int i =1; i<10; i++){
  //上边这三个内容也可以用任何其他东西来替换
}
```

控制流语句：continue

```c++
for(int i =1; i<10; i++){
  if(i>2){
    continue;//continue会跳过下边的代码进入下一次循环
  }
  cout<<"Hello";
}

    for (int i = 0; i < 5; i++) {
//       use break to stop the loop
        if (i == 2) {
            break;
        }
        cout << i << endl;
    }

 for (int i = 0; i < 5; i++) {
//       use return to exit the loop
        if (i == 2) {
            return 0;
        }
        cout << i << endl;
    }
```

# 指针

一个指针就是一个内存地址。

```c++
int x = 1;
//定义指针;
int* ptr = nullptr;
//给指针赋值;
ptr = &x;//这里&是获得x的地址
//逆向获得指针的值
*ptr=2
```

这里指针的类型只是为了告诉编译器指针需要多大的内存空间，指针本身只是一串数字代表着内存地址。可以在clion的memory view里查看当前指针对应的内存地址，可以直接输入指针名来查看。

>内存中一个字节(byte)包含8个位(bit)。一般来讲int是4个字节，也就是32位。在clion的内存视图中每一个数字都是16进制，每个十六进制可以表示四位，两个十六进制数字表示一个字节。A (十六进制) = 1010 (二进制)，3 (十六进制) = 0011 (二进制)。所以一个int用八个十六进制来表示。

```c++
 char* string = new char[10];
 memset(string, 9, 10);
```

这里string是一个字符串指针，定义的时候占用了10个字节的空间。然后用memset给这十个字节都赋值9。

![image-2024060822132538 PM](https://raw.githubusercontent.com/1982606762/picgo/master/image-2024060822132538%E2%80%AFPM.png)

## 引用

引用可以引用一个存在的变量，相当于这个变量自身。操作引用等于操作变量。

```c++
int main() {
    int a = 8;
    int& ref = a;
    ref = 2;//此时a=2
    cout << a << endl;
}
```

用处：如果另一个函数想修改这个变量值，可以在那个函数的输入变量使用引用以起到修改原始变量的作用

```c++
void increment(int& value) {
    value++;
}
int main() {
    int a = 8;
    increment(a);
    cout << a << endl;
}
```

注意！引用一旦定义就不能再修改引用对象，如果再次让ref = b其实会把a的值设为b。而且

## *和&用法

两者放在类型后边就是声明一个这个类型的指针/引用

放在变量前边就是对变量进行一些操作（解地址/获取地址）

### *

指针声明

```cpp
int* ptr;
```

访问指针指向的内容

```cpp
int value = *ptr
```

### &

获取变量的地址（也就是到变量的指针）

```cpp
int x = 10;
int* ptr = &x;
```

引用声明

```cpp
int& ref = x;
```



## 智能指针

可以自动调用delete的new指针，建议用智能指针取代new。

首先需要`#include<memory>`.

### Unique_ptr

用完之后会自动delete内存，不能用其他指针指向他或在类之间共享。独占所有权，不能复制，只能移动。

```cpp
std::unique_ptr<int> ptr1(new int(10));
std::unique_ptr<int> ptr2 = std::move(ptr1); // ptr1 不再拥有对象
```





### Shared_ptr

使用引用计数来追踪有多少指针还没有释放，全都释放后才会销毁。共享所有权，多个指针可以共享同一个对象，使用引用计数。

```cpp
std::shared_ptr<int> ptr1(new int(10));
std::shared_ptr<int> ptr2 = ptr1; // ptr1 和 ptr2 共享所有权
```

使用wear_ptr的时候不会增加计数。

### Weak_ptr

不增加引用计数，防止循环引用，配合shared_ptr使用。

```cpp
std::shared_ptr<int> sharedPtr(new int(10));
std::weak_ptr<int> weakPtr = sharedPtr;
if (auto tempPtr = weakPtr.lock()) {
    // 使用临时的 shared_ptr
}
```



```cpp
#include <iostream>
#include <memory>

void uniquePtrExample() {
    std::unique_ptr<int> ptr1(new int(10));
    std::unique_ptr<int> ptr2 = std::move(ptr1); // ptr1 不再拥有对象
    if (ptr1 == nullptr) {
        std::cout << "ptr1 is null" << std::endl;
    }
    std::cout << *ptr2 << std::endl;
}

void sharedPtrExample() {
    std::shared_ptr<int> ptr1(new int(10));
    std::shared_ptr<int> ptr2 = ptr1; // ptr1 和 ptr2 共享所有权
    std::cout << "Reference count: " << ptr1.use_count() << std::endl;
    std::cout << *ptr1 << ", " << *ptr2 << std::endl;
}

void weakPtrExample() {
    std::shared_ptr<int> sharedPtr(new int(10));
    std::weak_ptr<int> weakPtr = sharedPtr;
    if (auto tempPtr = weakPtr.lock()) {
        std::cout << *tempPtr << std::endl;
    }
}

```



# 类

定义类：

```c++
class Player {
public:
    int x, y;
    int speed;

    void move(int xa, int ya) {
        x += xa * speed;
        y += ya * speed;
    }
};
int main() {
    Player player;
    player.x = 5;
    player.y = 5;
    player.speed = 2;
    player.move(1, -1);
    return 0;
}
```

比较好的习惯是把变量设置为private，然后用getter、setter来设置。

### 类与结构体的区别

默认的类成员是private的，而结构体是public的。

## static静态

### 类中的静态成员变量

在类里声明的静态变量会在所有实例中都共享内存，也就是所有实例的这个变量都是一样的。

注意！类的静态成员变量必须在类外部单独定义一次才能完成声明并且分配内存。

```c++
class MyClass {
public:
    static int staticVar;
    void increment() { staticVar++; }
};

int MyClass::staticVar = 0;

int main() {
    MyClass obj1, obj2;
    obj1.increment();
    std::cout << MyClass::staticVar << std::endl;  // 输出1
    obj2.increment();
    std::cout << MyClass::staticVar << std::endl;  // 输出2
    return 0;
}
```

### 函数里的静态局部变量

会在函数内部保持值，只会在第一次调用时初始化

```c++
void myFunction() {
    static int count = 0;
    count++;
    std::cout << count << std::endl;
}

int main() {
    myFunction();  // 输出1
    myFunction();  // 输出2
    myFunction();  // 输出3
    return 0;
}
```

### 类里的静态成员函数

可以通过类名直接调用，不需要创建实例。但是不能访问非静态成员，只能访问静态成员变量和函数。

```c++
class MyClass {
public:
    static void staticFunction() {
        std::cout << "Static function" << std::endl;
    }
};
int main() {
    MyClass::staticFunction();  // 直接通过类名调用
    return 0;
}
```

适用于某些不需要访问实例数据的功能，如全局计数器。

### 文件中的静态变量或函数

如果文件A中有一个static成员变量或函数，那么这个东西的作用域会被限制在这个文件内，这样就可以隐藏实现细节并且防止多个命名冲突。

```c++
// file1.cpp
#include <iostream>

static void hiddenFunction() {
    std::cout << "This is a hidden function" << std::endl;
}

void callHiddenFunction() {
    hiddenFunction();
}
// file2.cpp
#include <iostream>

extern void callHiddenFunction();

int main() {
    callHiddenFunction(); // 输出 "This is a hidden function"
    return 0;
}
```

## 可见性

有三种可见性修饰符：private, public和protected。

类A里private变量只能在类A里使用，外部不能使用，A的派生类也不能使用。

类A的protected可以在A和A的派生类里使用，外部不能使用。





## 构造函数

在实例化类的时候会自动执行的函数。

用于初始化类的成员变量，分配内存，保证实例创建时是有效的。

支持重载构造函数。

```cpp
class MyClass {
public:
    int a,b;
    MyClass() {
        a = 0;
        b = 0;
    }
    MyClass(int x, int y) {//这里可以重载
        a = x;
        b = y;
    }
    void print() const {
        log("Hello from MyClass");
        cout << a << " " << b << endl;
    }
};

int main() {
    MyClass obj(10, 20);
    obj.print();
    return 0;
}
```





## 析构函数

在销毁对象的时候会运行的函数。如果是直接生成在栈内存里的实例，不使用的时候会调用。如果是new的那就会在delete的时候调用。

>堆内存和栈内存区别：
>
>栈内存由编译器管理分配，存着局部变量。
>
>```cpp
>void function() {
>    int stackVar = 10;  // 分配在栈上
>}
>```
>
>堆内存由程序员用new，delete管理，存所有需要的内存。
>
>```cpp
>void function() {
>    int* heapVar = new int(10);  // 分配在堆上
>    // 使用 heapVar
>    delete heapVar;  // 释放堆内存
>}
>```

用于清理内存。

```js
#include <iostream>

class MyClass {
public:
    int* data;

    // 构造函数
    MyClass(int size) {
        data = new int[size];
        std::cout << "Constructor called" << std::endl;
    }

    // 析构函数
    ~MyClass() {
        delete[] data;
        std::cout << "Destructor called" << std::endl;
    }
};

int main() {
    MyClass obj(10);  // 创建对象时调用构造函数
    // 对象超出作用域时自动调用析构函数
    return 0;
}
```

## 创建并初始化对象

可以直接使用类名作为类型来创建新变量

```cpp
Entity e = Entity("Cherno");
```

这样就把变量直接创建到栈（stack)里了，但是当前上下文运行完会自动清除

或者使用new来新建变量，这样就会创建到堆(heap)里

```cpp
Entity* e = new Entity("hello");
//do sth
delete e;//需要释放内存
```

如果没有特殊需求推荐直接在栈上新建。

如果使用`new int[50]`声明就需要用`delete[] e`来删除



## 继承

有一个旧类，可以指定一个新类来继承旧的这个。

```cpp
class MyClass {
public:
    int* data;
    int a, b;
    MyClass(int size) {
        data = new int[size];
        a = 5;
        b = 10;
    }
    void print() {
        log("Hello from MyClass");
        cout << a << ", " << b << endl;
    }
};

//继承
class MyDerivedClass : public MyClass {
public:
    int c;
    MyDerivedClass(int size) : MyClass(size) {//调用父类的构造函数
        c = 10;
    }
    void print() {
        log("Hello from MyDerivedClass");
        cout << a << ", " << b << ", " << c << endl;
    }
};
```

## 虚函数

虚函数是用于实现多态的成员函数，它允许派生类重写基类中的函数，以保证在调用这个函数的时候执行的是调用函数那个对象对应的函数而不是指针的函数版本。

需要在基类中用virtual声明，并且最好在重写的时候用override关键字。

运行时多态：在通过基类的指针或引用调用虚函数的时候实际执行的是派生类的函数版本。

```cpp
class Base {
public:
    virtual void show() {
        cout << "Base class" << endl;
    }
};

class Derived : public Base {
public:
    void show() override {
        cout << "Derived class" << endl;
    }
};

int main() {
    Base* basePtr;
    Derived derivedObj;

    basePtr = &derivedObj;
    basePtr->show();  // 输出 "Derived class"

    return 0;
}
```

### 纯虚函数

可以在基类中定义一个没有实现的函数，然后在子类里实现。子类必须在实现纯虚函数之后才能被实例化。

```cpp
class Printable {
public:
    virtual void print() = 0;

};

class Entity : public Printable {
public:
    void print() override {
        cout << "Entity" << endl;
    }

};

class Player : public Printable {
public:
    void print() override {
        cout << "Player" << endl;
    }
};

void print(Printable* obj) {
    obj->print();
}

int main() {
    Entity* e = new Entity();
    Player* p = new Player();
    print(e);//输出 “Entity”
    print(p);//输出 “Player”
    return 0;
}
```

# 数据类型



## Enum枚举

enum是自定义的数据类型，可以把一组变量打包变成一个类型，如：

```cpp
enum Day { Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday };
Day today = Monday;
```

如果不指定整数值的话默认第一个是0，后边的递增，也可以指定值

## 数组

定义数组用中括号，中括号是用于数组和指针的下表运算符以访问元素，指针ptr加中括号 `ptr[i]=*(ptr+i)` 

```cpp
int main() {
    int a[4];
    int* b = new int[4];
    int* p = a;

    for (int i = 0; i < 4; i++) {
        cout << "Enter a number: " << endl;
        cin >> a[i];
        cout << "Enter another number: " << endl;
        cin >> b[i];
    }

    for (int i = 0; i < 4; i++) {
        log("Hello World!");
        cout << "a[" << i << "] = " << a[i] << endl;      // 打印数组 a 中的第 i 个元素
        cout << "p[" << i << "] = " << p[i] << endl;      // 打印指针 p 当前指向的元素
        cout << "b[" << i << "] = " << b[i] << endl;      // 打印数组 b 中的第 i 个元素
    }

    delete[] b;  // 正确释放内存
    return 0;
}
```

### 静态数组

大小在编译时确定

```cpp
int arr[5];             // 未初始化，元素值不确定
int arr[5] = {1, 2};    // 部分初始化，未指定的元素为 0
int arr[] = {1, 2, 3};  // 大小由初始化列表确定
```

### 动态数组

使用new来分配数组长度

```cpp
int* arr = new int[4];
```

### 函数使用数组传参

传递指向数组首元素的指针，数组名就是指向首元素的指针

```cpp
void func(int arr[], int size);
func(arr, 5);
```

## 字符串

### 定义字符串

字符串的终止是内存中的0，当读到0的时候系统会知道字符串结束。在字符串中体现为`\0`

```cpp
char str[] = "hello";
char* str2 = new char[20];
strcpy(str2,"hello");
```

### 字符串操作函数

```cpp
#include <cstring>

char str1[20] = "Hello";
char str2[20];
strcpy(str2, str1);  // 复制字符串
int len = strlen(str1);  // 获取字符串长度
```

### 使用string库

需要引入string标准库

推荐使用string 而不是char*

### 字符串函数传参

使用`const string& a`来传参，这样使用的时候可以直接用字符串名。如果用`const string*`的话输入需要是一个指针，默认string类型得到的是一个实例。

```cpp
string* concat(const string& a, const string& b) {
    return new string(a + b);
}
int main() {
    string message = "Hello, World!";
    string* a = concat(message, message);
    log(*a);
    delete a;

    return 0;
}
```

## const的用法

### 常量

```cpp
const int a = 1;
```

### 指针

如果是指向常量的指针，那么就不能修改指针的内容，但是可以修改指针的指向。

如果是常量指针，那么就可以修改当前指向的内容，但是不能修改指向。

如果是指向常量的常量指针，那么都不能修改。

```cpp
const int* a = new int;

*a = 2;//error
a = ptr;
```

```cpp
int* const a = new int;
*a = 2;
a = ptr;//error
```

```cpp
const int* const ptr = &x;
*ptr = 20;  // 错误
ptr = &y;  // 错误
```

### 类

常量成员函数不能修改类的成员变量的值。

```cpp
class Entity
{
  private:
	  int x;
  public:
  	int getX() const{
      return x;
    }
}
```

用处是当有其他函数要用const输入时需要有const声明

```cpp
void print(const Entity& e)
{
  cout << e.getX() <<endl;
}
```

假如我想用const函数修改类的变量，可以通过设置变量为mutable来实现（`mutable int var`) 可以用来调试时设置一个变量来追踪函数运行过多少次，不想去掉const的时候就可以添加mutable实现。

## 隐式转换

在定义实例的时候可以直接如下定义：
```cpp
    Entity e = 12;
    Entity e1 = "Cherno";
```

这样12会隐式转换( implicit conversions )成Entity类型。如果不想让构造函数接受隐式转换就需要在函数前加一个explicit.

## Set

定义和初始化set

```c++
set<int> mySet;
mySet.insert(1);
```

查看是否在set中

```cpp
if(mySet.count(1)){
  //在
}
```

遍历set元素

```cpp
for (const int& element : mySet){
  cout << element;
}
```

删除元素

```cpp
mySet.erase(2);
```



## Map

定义和初始化

```cpp
map<int, string> myMap = {{1, "one"}, {2, "two"}, {3, "three"}};
```

插入

```cpp
map<int, string> myMap;
myMap[1] = "one";
myMap[2] = "two";
myMap[3] = "three";
```

查询元素

```cpp
cout << myMap[1] << endl;  // 输出 "one"

auto it = myMap.find(2);
if (it != myMap.end()) {
    cout << it->second << endl;  // 输出 "two"
}
```

遍历

```cpp
for (const auto& pair : myMap) {
    cout << pair.first << ": " << pair.second << endl;
}

// 或者使用迭代器
for (auto it = myMap.begin(); it != myMap.end(); ++it) {
    cout << it->first << ": " << it->second << endl;
}
```

删除

```cpp
myMap.erase(2);
```





# 操作与运算

## 运算符重载

```cpp
#include <iostream>
using namespace std;

class Vector2 {

public:
    float x, y;
    Vector2(float x, float y)
        : x(x), y(y) {}
};

Vector2 operator+(const Vector2& left, const Vector2& right) {
    return Vector2(left.x + right.x, left.y + right.y);
}
Vector2 operator*(const Vector2& left, const Vector2& right) {
    return Vector2(left.x * right.x, left.y * right.y);
}
bool operator==(const Vector2& left, const Vector2& right) {
    return left.x == right.x && left.y == right.y;
}
bool operator!=(const Vector2& left, const Vector2& right) {
    return !(left == right);
}
ostream &operator<<(ostream &stream, const Vector2& vector) {
    stream << vector.x << ", " << vector.y;
    return stream;
}

int main() {
    Vector2 position(4.0f, 4.0f);
    Vector2 speed(0.5f, 1.5f);
    Vector2 powerup(1.1f, 1.1f);

    Vector2 result = position + speed * powerup;
    cout << result << endl;
    cout << (position == result) << endl;
    cout << (position != result) << endl;
    return 0;
}
```

