---
title: Django-learn
date: 2024-09-07 23:09:25
tags: Django
categories: BackEnd
---

Django note from the course "Django Web Framework" by Meta.

<!--more-->

# Intro to Django

## Creating first project

Django 可以用`django-admin`或者文件夹里的`manage.py`来控制。

创建新项目：`$ django-admin createproject`



app是用来进行某一种任务的，project是大项目。

Views.py用来处理request并且返回页面。

urls.py用来



创建新app:`$ python -m django startapp myapp`

创建app之后需要在installed_apps添加app名



创建新页面：在app的view.py文件里添加：

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```

然后去project文件夹里的urls.py添加路由信息：

```python
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
```

然后就可以看到了



Include app的 view：

`    path('', include('myapp.urls'))`





运行服务器：`$ python manage.py runserver`

## MVT

Django 是 MVT 模型， 包含model,view 和template.

model存储数据，view处理逻辑，template是表示层。

数据层负责和数据库的交互

# Views

使用View处理HTTP request，在app 文件夹里的views.py文件里定义。

每个函数都需要接收一个http request参数，返回一个HTTP response.

要想显示这个view里的函数，需要去project级的urls.py先import这个view文件，然后在urlpatterns里添加。

### View logic

view的用处主要是通过request来获取数据，应用一些处理后返回response。

他可以处理REST API：

```python
from django.shortcuts import render     

def myview(request): 
    if request.method=='GET': 
        val = request.GET['key'] 
        #perform read or delete operation on the model 
    if request.method=='POST': 
        val = request.POST['key'] 
        #perform insert or update operation on the model 
```

返回值需要是HTTPresponse类型的obj

## Request and URLs

### HTTP requests

Get: 从服务器获取数据

post：向服务器发送数据

put：更新数据

delete：删除数据

一个HTTP返回值包含很多消息，例如当前使用的HTTP版本，请求信息。200是成功。

HTTPS使用加密来保护request 和 response的安全。

在view里接收到request之后，根据他种类不同可以进行不同操作。

### URL parameter

`path('drinks/<str:name>'view.drinks,name="drinks"),`

这里name就是一个url的参数，通过改变这个值就可以返回不同的response。

在view的函数里需要定义接收参数：

```python
def drinks(request, drink_name):
    drink = {
        'mocha' : 'type of coffee',
        'tea' : 'type of hot beverage',
        'lemonade': 'type of refreshment'
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)
```

还可以使用正则表达式(regular expressions来匹配参数，这时需要用`re_path`函数。

## Error Handling

在view.py里可以添加error handler,可以处理400,401,402,404,500

在settings.py里添加DEBUG=FALSE可以关闭默认error信息：

![image-2024091013158334 PM](https://raw.githubusercontent.com/1982606762/picgo/master/image-2024091013158334%E2%80%AFPM.png)

只有关闭默认debug模式后才能显示自定义的error页面。

首先在project的urls.py里添加：

```python
from . import views
...
handler404 = 'test1.views.handler404'
```

然后在这个文件夹里新建一个view.py文件，里边定义error 处理函数：

```python
from django.http import HttpResponse

def handler404(request, exception):
    return HttpResponse("1111404: Page not found")
```

# Model

使用model可以进行从App到数据库的交互，并且进行CURD操作。这些操作都有django预设的函数实现。

## 创建model

一个model就相当于一个数据表，在app的models.py文件里创建。

```python
class Menu(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
```

## 用migration更新表结构

假如想给model表加一个字段，只需要在class里添加一行字段，然后在cmd里使用migration语句来更新。

语句：

- makemigrations
- migrate
- sqlmigrate
- showmigrations

sqlmigrate是用来显示当前操作对应的SQL语句的，可以帮助你debug或者理解。

### 更新

先用`makemigration`来初始化，然后用`migrate`应用变化。

makemigration后边加app名也可以只更新这个app的model。

### 回溯

每次变化都会在migrations文件夹里新建一个py文件，使用`migrate 0001`可以回溯到这次的更改。

### 注册到admin界面

在app的admin.py里使用：

```python
from .models import Book
admin.site.register(Book)
```

就可以把模型注册到后台，然后就可以在admin后台管理数据库，就只能用shell来管理。

## 使用外链（forieign keys)

使用`    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)`来定义外链变量。

## 使用form交换数据

form会发送一个post request。Django使用Form class来接收数据，只需要在class里定义数据类型，django会自动生成对应的form。

```python
from django import forms    

class ApplicationForm(forms.Form): 
    name = forms.CharField(label='Name of Applicant', max_length=50) 
    address = forms.CharField(label='Address', max_length=100) 
    posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator')) 
    field = forms.ChoiceField(choices=posts) 
```

field类型：

* CharField
* IntegerField
* FloatField
* FileField
* ImageField
* ChoiceField

需要自定义一个html模板来保存表单，这个文件需要保存在app里的templates文件夹中

* Booking.html

```html
<p> Booking for Little Lemon ! </p>

<form action = "" method = "post", style="background-color: #E0E0E2;">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
</form>

<button onclick="window.location.href = '/';">Go to Home Page</button>
```



## 保存form数据到数据库

使用ModelForm类来保存数据，需要在models里定义一个类，然后在forms.py里使用ModelForm类，然后在views里执行保存操作。

* 在models里定义类

  ```python
  class Booking(models.Model):
      first_name = models.CharField(max_length = 200)
      last_name = models.CharField(max_length = 200)
      guest_count = models.IntegerField()
      reservation_time = models.DateTimeField(auto_now=True)
      comments = models.CharField(max_length=1000)
      def __str__(self)://这两行的用处是新建object后将firstname设置为object的名称。
        return self.first_name
  ```

* 在app文件夹新建forms，并且在里边使用这个类生成一个form

* 这里Meta类是一个内嵌的类，用来告诉ModelForm如何处理模型的字段，这里model指定表单对应的模型是Booking，fields表示表单应该包含所有字段。制定后Django就会根据model里的字段生成CharField等。

```python
from django import forms

from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
```

* 在view中定义保存操作

```python
def booking(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'booking.html', {'form': form})
```

## Django Admin

创建用户：在terminal中使用`$ python manage.py createsuperuser`

每个用户都需要有特定的permission，有三种用户级别：superuser, staff user, user.staff 可以用admin界面，user不能用。

对于特定app的某个model有很多种权限，如查看，权限名称的结构是`myapp.view.mymodel`。可以用`has_perm`来查看一个用户是否有对应的权限：`request.user.has_perm('myapp.view_mymodel')`如果没有就可以`raise PermissionDenied()`

还可以通过创建group来管理，给group添加权限就不用一个个给user加。

## Django Database Configuration

Django默认使用SQLlite，在setting文件里设置。但是Django支持很多其他数据库，例如PostgreSQL和MySQL。

用brew安装mysql，启动服务使用`brew services start mysql`

链接数据库：`mysql -u root -p` u是user，p是password

链接Django到数据库：修改settings文件

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mydatabase",
        "USER": "mydatabaseuser",
        "PASSWORD": "mypassword",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

然后执行migrate后就会在这个数据库里进行操作。

# Templates

Template里可以包含动态内容，用大括号包裹。

默认Django使用自己的template engine，在settings文件里设置。也可以使用多个engine，如jinja2，可以通过在options选项里添加environment选项改成jinja2.

一般来讲template放在特别的文件夹里，用的时候可以直接inherite。可以在views里使用`render(request,'index.html',{})`来使用某个模板。

如果要添加变量就可以使用`    <h1>Welcome to My Project{{ name }}</h1>`包裹，然后在view里使用`    return render(request, 'index.html',{"name":'  myapp'})`传入参数。还可以使用{%if%}等来进行条件判断。

## Django Template language

用于在template里处理逻辑。

包含四种：

* Variables:`{{var1}}`,`{{var1.name}}`

* Tags: 

  * If:

    ```html
    {% if expression == True %} 
    HTML block 1 
    {% else %} 
    HTML block 2 
    {% endif %} 
    ```

  * For: 

```html
<ul>
	{% for item in list %}
  	<li>{{item.name}}{{item.price}}</li>
   {% end if%}
 <li>
```

* Filters: `{{string|upper}}`
* Comments: 

```html
{%comment%}
```

## 在template里使用Model中保存的数据：

```python
def menu(request):
    menu_items = Menu.objects.all()
    items_dict = {"menu": menu_items}
    return render(request, "menu.html", items_dict)
```

```html
{% if menu %}

{% for item in menu %}
{{ item.name }} : {{ item.price }}
<br>
{% endfor %}
{% else %}
<p> No items to display !</p>
{% endif %}
```

## Template inheritance

* include
  * 用来使用另一个template文件
  * 

* extends
  * 用来扩展另一个文件

# Debugging

## unit test

使用Django.test包

基于测试类的测试，一般写在test.py文件里。

