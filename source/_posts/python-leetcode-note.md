---
title: python-leetcode-note
date: 2024-03-18 15:53:25
tags:
categories:
---

<!--more-->

## Python 使用字典

使用{}创建的时候如果尝试访问字典中不存在的键就会抛出异常

使用defaultdict创建的时候可以传入一个类型，假如访问到不存在的键就会初始化一个这个类型

```python
from collections import defaultdict

dd = defaultdict(list)
dd['key'].append('value')  # 不需要先检查'key'是否存在
print(dd['key'])  # 输出：['value']
```

## 对字典内容进行排序

对键排序：

```python
my_dict = {'apple': 10, 'banana': 5, 'orange': 20}

# 根据字典的键进行排序
sorted_keys = sorted(my_dict)

# 打印排序后的键
for key in sorted_keys:
    print(key, my_dict[key])
```

使用参数进行排序：

```python
my_dict = {'apple': 10, 'banana': 5, 'orange': 20}

# 根据字典的值进行排序
sorted_items = sorted(my_dict.items(), key=lambda x: x[1])

# 打印排序后的键值对
for key, value in sorted_items:
    print(key, value)
```

