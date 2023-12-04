---
title: deploy flask with nginx on ubuntu
date: 2023-02-05 15:56:47
tags: [nginx, flask]
categories: Linux
---

* Configure nginx
* configure flask app

<!--more-->

# Configure nginx

First, install nginx using `apt-get install nginx`. 

修改/etc/nginx/sites-enabled/default，改文件名成xxx.com后修改内容

```
	listen 80;	
	server_name stock.joticia.cn;

	location / {
		proxy_pass http://0.0.0.0:5000/;
	}

	location /stock{
		proxy_pass http://0.0.0.0:5000/stock;
	}
```

使用软连接把文件连接到sites-available里

# Configure flask app

In app.py need to use `app.run(host='0.0.0.0')` so all access can be done through ip:5000



