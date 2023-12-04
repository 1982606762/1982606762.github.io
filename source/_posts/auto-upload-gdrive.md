---
title: auto-upload-gdrive
date: 2023-02-24 18:50:48
tags: rclone
categories: Linux

---

Develop a system that can add a torrent on the website, after completing the download it will automatically upload the file to my google drive while showing the upload log to the website so that I can see the procedure of uploading.

* install Qbittorrent command-line version
* Setup after-download-script
* Show real-time log on the website

<!--more-->

# Install Qbittorrent-nox

In Ubuntu, it's called qBittorrent-nox.

## Install qBittorrent-nox

Add the qBittorrent repository:

```bash
sudo add-apt-repository -y ppa:qbittorrent-team/qbittorrent-stable
```

Install qBittorrent-nox:

```bash
sudo apt install -y qbittorrent-nox
```

After installation, we can check the qBittorrent-nox version:

```bash
qbittorrent-nox --version
```

## Run qBittorrent-nox as a service

In order to run qBittorrent-nox as a service we need to configure systemd. Create a systemd unit file:

```bash
sudo nano /etc/systemd/system/qbittorrent-nox.service
```

Add the following content to the file:

```plaintext
[Unit]
Description=qBittorrent client
After=network.target

[Service]
ExecStart=/usr/bin/qbittorrent-nox --webui-port=8080
Restart=always

[Install]
WantedBy=multi-user.target
```

You can change the web interface port if you want.

Start qBittorrent-nox service:

```plaintext
sudo service qbittorrent-nox start
```

You can run the following command to make sure that the qBittorrent-nox service is running:

```plaintext
sudo service qbittorrent-nox status
```

Also, you can stop or restart the service:

```plaintext
sudo service qbittorrent-nox stop
sudo service qbittorrent-nox restart
```

To enable qBittorrent-nox to start on boot, run the following command:

```plaintext
sudo systemctl enable qbittorrent-nox
```

## Testing qBittorrent-nox

Open a browser and enter the URL address `http://<IP_ADDRESS>:8080`, where `<IP_ADDRESS>` is the IP address of your machine. You can log in to the web UI with the default username (`admin`) and password (`adminadmin`).

# Setup after-download-script

> qbt now doesn't give shell environment by default, you'll either need to specify full path `/usr/bin/rm` or invoke the shell by yourself `/usr/bin/sh -c <command>`.

So we need to add `/bin/bash  /Torrent.bash "%N" "%F"` in external program field

And create a bash file with content as follows:

```bash
#!/bin/bash
#echo "$1" >> /root/1.txt
rclone copy $2 gdrive1:美剧/$1 -P >> /root/qbitdown/log
```

Of course, you can add whatever you want into the bash file, I'm just showing my own configuration.

# Show real-time log on the website

First, we need to add some blocks to the HTML file:

```html
<p class="log-title">update log</p>
<div id="log-container"></div>
<script>
      function updateLogs() {
          // 创建XMLHttpRequest对象
          var xhr = new XMLHttpRequest();
          // 设置请求的URL和HTTP方法
          xhr.open('GET', '/api/logs', true);
          // 注册请求完成的回调函数
          xhr.onload = function() {
              if (xhr.status === 200) {
                  // 将响应的JSON格式数据解析为JavaScript对象
                  var data = JSON.parse(xhr.responseText);
                  // 获取日志内容并插入到页面中
                  var logContainer = document.getElementById('log-container');
                  var logs = data.logs;
                  var logHtml = '';
                  for (var i = 0; i < logs.length; i++) {
                      logHtml += '<p>' + logs[i] + '</p>';
                  }
                  logContainer.innerHTML = logHtml;
              }
          };
          // 发送请求
          xhr.send();
      }
      window.onload = function() {
          updateLogs();
          setInterval(updateLogs, 1000); // 1秒钟更新一次
      };
  </script>
```

Then we need to add a new router in the flask code:

```python
@app.route('/api/logs')
def get_logs():
    output = subprocess.check_output(['tail', '-n', '50', '/root/qbitdown/log'])
    logs = output.decode('utf-8', 'ignore').split('\n')
    return jsonify({'logs': logs})
```

The 'ignore' can prevent the system being crashed because of some decoding error...Which is very important

# reference

https://lindevs.com/install-qbittorrent-nox-on-ubuntu

https://github.com/qbittorrent/qBittorrent/issues/11042

https://www.reddit.com/r/unRAID/comments/lhilzu/comment/ipckgr1/
