---
title: monitor-csgo-item-price
date: 2023-01-06 18:58:34
tags: crawler
categories: Python
---

This article describes how to trace the items in your stock and get a summary of how much you profit/lose from it.

* Use a Web crawler to get the current item price
* Save daily price into sqlite3 database
* Use crontab to run the script daily
* Use cronitor to monitor crontab
* Call system notification after it's done or fail
* Use flask and echarts to visualize the data

<!--more-->

## Use a Web crawler to get the current item price

First, log in to the NetEase BUFF platform, and find an item you want to trace. Open F12 and in Network, you'll find a file named "sell_order?game=csgo&goods_id=xxx". In the preview of the file, you will find a JSON file containing all the information about its market. 

First, you need to get the cookies and header in "Headers", the header is its User-Agent.

Then, use Python to save this information

```python
headers = {
    'your header'
}
cookie_str = 'your cookie'
cookies = {}
for line in cookie_str.split(';'):
    name, value = line.strip().split('=', 1)
    cookies[name] = value

```

Then, define the URLs and the stock you have. The user can be found by right-clicking the file "sell_order" and selecting "copy-copy link address".

```python
urls = {
    '火神': 'https://buff.163.com/api/market/goods/buy_order?game=csgo&goods_id=33976&page_num=1&_=1672999623684'
}
stock = {
    '火神': [1099,1]
}
```

The list in stock value contains the price it originally bought and the number of items you have.

Then we use the requests to send the request and get the result. For this part, you need to import requests.

```python
for name, status in stock.items():
        num = status[1]
        url = urls[name]
        oldprice = status[0]
        while num:
            time.sleep(0.3)
            r = requests.get(url, headers=headers, cookies=cookies)
            data = r.json()
    				#do sth here
            num -=1
```

## Save daily price into sqlite3 database

First import sqlite3.

Connect to database:

```python
db = '/Users/xuanlang/study/python/csgo.db'
conn = sqlite3.connect(db)
```

Start cursor:

```python
c = conn.cursor()
```

Create database:

```python
text_create_table = '''CREATE TABLE IF NOT EXISTS stock (
    Date DATE,
    Name TEXT,
    CurrentPrice REAL,
    OriginalPrice REAL
)'''
c.execute(text_create_table)

```

write into the database:

```python
sql_text_insert = "INSERT INTO stock VALUES ('%s', '%s', '%s', '%s')" % (today,name, curprice, oldprice)
c.execute(sql_text_insert)
```

View current profit:

```python
conn = sqlite3.connect(db)
c = conn.cursor()
sql_text_select = "SELECT SUM(OriginalPrice) FROM stock WHERE date = '%s'" % today
c.execute(sql_text_select)
cost = c.fetchall()[0][0]
print(cost)
sql_text_select = "SELECT SUM(CurrentPrice) FROM stock WHERE date = '%s'" % today
c.execute(sql_text_select)
cur = c.fetchall()[0][0]
print("成本",cost,"现价",format(cur,".2f"),"盈利",round(cur-cost,2),"盈利率",round((cur-cost)/cost* 100,2),"%")

```

There's a point you need to be aware of which are you need to determine if today's data has been written into the database you just need to update it, so you need to determine first:

```python
# 判断数据库中是否有今天的数据
sql_text_select = "SELECT * FROM stock WHERE date = '%s'" % today
c.execute(sql_text_select)
result = c.fetchall()
if result:
  update()
else:
  insert()
```

## Use crontab to run the script daily

To run the script automatically you need to use crontab(in macOS).

First use `crontab -e` to write a new cron with the format `* * * * * * ~/miniconda3/bin/python3 /Users/xuanlang/study/python/test.py`

For more information about cron, you can go to https://crontab.guru/

The crontab's log will be sent to macOS terminal mailbox, use `mail` to see them.

You can define cron's environment variables in crontab itself, like:

```bash
LANG=nb_NO.UTF-8
LC_ALL=nb_NO.UTF-8
# m h  dom mon dow   command

* * * * * sleep 5s && echo "yo"
```

There might be some problems occur, to solve them:

1. Count the right number of * !!!
2. Check cron's shell and env is the same as your terminal, or it won't find some instruction sometimes.
3. Use mail to trace the log.

## Use cronitor to monitor crontab

[cronitor](https://cronitor.io/app/welcome?env=production&time=24h) is a tool that can trace some jobs as well as some other things. We will use it to monitor cron work.

1. install CronitorCLI
2. Run `cronitor discover` to find cron jobs

for more information go to its document https://cronitor.io/docs.

## Call system notification after it's done or fail

to do this you need to import os.

```python
def show_notification(title, text):
  os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

```

Usage:

```python
str_result = "成本: %s 现价: %s 盈利: %s 盈利率: %s" % (cost, format(cur,".2f"), round(cur-cost,2), round((cur-cost)/cost* 100,2))
show_notification("csgo track result", str_result)
```

the system will pop up a notification when it's called.

## Use flask and echarts to visualize the data

### Flask

First, install flask by `conda install flask`

Then create dirs for flask:

- flask
  - static
    - CSS, js...etc
  - templates
    - index.html
  - app.py

in 'app.py ' you need to fetch data from the database, host a server and pass the data to the front end. Here I made two routes, one is "/" for the Html page and the other is "/stock" to send the JSON data so it can catch those data and display them in the front end.

Then run the python file and go to the browser to check if the website works well. several problems may occur, check these solutions:

* If the flask is installed correctly. Use `flask run` in the flask dir to check this.
* If the index.html is in the templates directory. the dir name must be right or it won't be able to find the file.
* If all the other resources like CSS and js files are placed in the static directory, otherwise the  HTML file may not be able to load them.

### echarts

go to the apache [echarts website](https://echarts.apache.org/examples/en/index.html) and search for the one you want to use. I used the stacked line chart for my website. Just copy it into the index.html and read about its data to figure out its usage.

Import jquery into your HTML and use ajax to get data from the back end. Fit those data into eharts to show the result.

Then configure the page to make it look better. 

Set the legend's type to scroll can make show less at once on the page, and set its width and height and top to fit the view.

Set the grid to adjust the graph's position.

Set the x-axis and y-axis's names to show their names.

Set some other thing.

## Reference

* https://cloud.tencent.com/developer/article/1823287
* https://echarts.apache.org/examples/en/index.html#chart-type-line
* https://getbootstrap.com/docs/5.3/components/navbar/#how-it-works
* https://www.w3cschool.cn/echarts_tutorial/echarts_tutorial-2dbe2cgw.html
* https://www.w3cschool.cn/echarts_tutorial/echarts_tutorial-5c3q2cj7.html
* https://blog.csdn.net/zSY_snake/article/details/105412370
* https://blog.csdn.net/chelen_jak/article/details/81131786
