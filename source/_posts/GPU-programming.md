---
title: GPU programming
date: 2024-07-02 14:28:27
tags: 
categories:
---

Note from https://www.coursera.org/specializations/gpu-programming?myLearningTab=COMPLETED

<!--more-->

# Introduction to concurrent programming

## Core Principles of Parallel Programming

### 并发编程可能出现的问题

* Race Conditions
  * 线程实际运行顺序和期望顺序不一样，如想让线程1读，修改，写，然后线程2读，修改，写。但是可能2会读到1修改之前的数据。
* Resource Contention
  * 多个程序视图读写相同内存块
* 线程死锁
  * 1需要A,A由2产生，2需要1产生的B
* Live Lock
  * 类似死锁，但是是两个进程一直在改变状态但没有进展。类似走廊两个人互相避开对方。
* 资源没有有效利用
  * 线程太少会让CPU闲置，线程太多会花大量时间在切换线程。

### 经典并发问题

哲学家就餐，生产者消费者问题

### 并发解决思想

* Divide and conquer
  * 解决子问题并且合并他们来解决大问题
* Map reduce
* Repository
* Pipeline
* Recursion
  * 在多个gpu的时候不建议用

​	

## Parallel Programming Patterns of Python 3

python3里实现并发编程的库：

* Threading libraries
* Asyncio library
* Multiprocessing library

### Asyncio使用

Asyncio主要组件有以下几个：

1. 事件循环（Event Loop）：

​	•	事件循环是 asyncio 的核心，用于调度和管理异步任务。

​	•	它负责监控和调度所有的异步任务、I/O操作、回调函数等。

2. 协程（Coroutines）：

​	•	协程是可以在运行过程中暂停和恢复的函数，用于执行异步操作。

​	•	使用 async def 定义协程函数，使用 await 调用其他协程或异步操作。

3.  任务（Tasks）：

​	•	任务是由事件循环调度的协程，用于并发运行协程。

​	•	使用 asyncio.create_task 或 asyncio.ensure_future 创建任务。

协程是带async的函数，需要显式调度，如用await或asynic.run()启动。

任务是对协程的包装





基本使用：

```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # 模拟异步操作
    print("World")

# 创建并运行事件循环
asyncio.run(say_hello())
```





使用async定义异步函数

```python
async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # 模拟异步操作，如网络请求
    print("Data fetched")
```

函数中等待的步骤需要用await关键字

