---
title: APIs
date: 2024-09-28 17:45:54
tags:
categories: BackEnd
---

Learning note for full-stack/api.

<!--more-->

## 工具推荐

使用curl来发送http请求

使用postman来分析请求

insomnia是一个集成app来开发api。

## REST best practice

* Keep it simple: 一个api只做一个事情。
* Filter，order：api可以使用filter来过滤结果，或者只返回某些结果
* versioning：只用几个版本
* caching：支持存储数据，这样可以减小数据库压力。
* Rate limit，mornitor：支持监视和限制用量。

### 安全性

* SSL：设置ssl，使用https
* 签字：开发者发出请求时需要sign，可以使用hmac

## First API test

背景：书店系统

数据库内容：

* Title: charfield max255
* Author: charfield max255
* Price: DecimalField 5 digits
* Inventory: IntegerField

API内容：

* /api/books: 返回所有库存的书
* /api/books/{bookId}：返回某一本书，如果没有就返回404，返回值是一个object

具体操作：

首先在app的models.py里添加book类：

```python
from django.db import models

# Create your Book model here.
# Create Meta class inside the Book model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()
    class Meta():
        indexes = models.Index(fields=['price']),
        
```

然后在admin里注册这个类：

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```

然后登录后添加一些数据。

然后在views.py里写api的代码：

```python
from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.

@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({"books": list(books)})
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        book = Book(title=title, author = author, price = price)
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)
        return JsonResponse(model_to_dict(book), status=201)

```

然后在两个url文件里更新相关url：

```python
from django.urls import path
from . import views

urlpatterns = [
    path('books',views.books)
]
```

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('BookListAPI.urls')), 
]

```

然后就可以通过访问**http://127.0.0.1:8000/api/books**来获得所有书的数据。

