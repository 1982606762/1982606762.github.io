---
title: 7-2 jmu-ds-顺序表区间元素删除 (15分)
tags: []
id: '212'
categories:
  - - c/c++语言
date: 2020-02-28 21:03:32
---

若一个线性表L采用顺序存储结构存储，其中所有的元素为整数。设计一个算法，删除元素值在\[x,y\]之间的所有元素，要求算法的时间复杂度为O(n)，空间复杂度为O(1)。

### 输入格式:

三行数据，第一行是顺序表的元素个数，第二行是顺序表的元素，第三行是x和y。

### 输出格式:

删除元素值在\[x,y\]之间的所有元素后的顺序表。

### 输入样例:

10  
5 1 9 10 67 12 8 33 6 2  
3 10

### 输出样例:

1 67 12 33 2

```
#include <stdio.h>

int main()
{
    int m;
    scanf("%d",&m );

    int list[999];
    for (int i = 0; i < m; ++i) {
        scanf("%d",&list[i]);
    }

    int x,y;
    scanf("%d%d",&x,&y);

    int list2[999],q=0;

    for (int j = 0; j < m; ++j) {
        if (x>list[j]y<list[j])
        {
            list2[q]=list[j];
            q++;
        }
    }

    for (int i = 0; i < q-1; ++i) {
        printf("%d ",list2[i]);
    }
    printf("%d",list2[q-1]);
    return 0;
}
```