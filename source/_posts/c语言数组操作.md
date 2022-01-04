---
title: C语言数组操作
tags: []
id: '206'
categories:
  - - c/c++语言
date: 2020-02-28 19:10:46
---

1.数组定义

int a\[5\]

int a\[5\] = {1,2,3}

int a\[\]={1,2,3,4,5}

int a\[5\]={1,2,3,4,5}

例：

```
# include <stdio.h>
int main(void)
{
    int a[5] = {0};  //数组清零初始化
    int i;
    printf("请输入5个数:");
    for (i=0; i<5; ++i)
    {
        scanf("%d", &a[i] );
    }
    for (i=0; i<5; ++i)
    {
        printf("%d\x20", a[i]);
    }
    printf("\n");
    return 0;
}
```