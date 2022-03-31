---
title: c++ set/map 方法集
date: 2022-03-14 10:58:38
tags: 
categories: C/C++
---

增加，删除，查找，遍历，大小

<!--more-->

# Set

```c++
set<int> s;
//增加
s.insert(1);
//删除
s.erase(1);
//查找
bool is_in = s.find(1) != s.end();
//遍历
for(auto i : s){
    cout<<i;
 }
//大小
s.size();
```

# Map

```c++
map<int,int>m;
//增加
map[1] = 1;
map.insert(pair<int,int>(2,2));
//删除
m.erase(1);
//查找
bool is_in = s.find(1) != s.end();
//遍历
 for(auto i : m){
        cout << i.first << i.second << endl;
    }

```

