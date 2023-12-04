#!/usr/bin/env python
f = open('./test3', 'r')
words = f.read().split('\n')
tags = []
categories = []
for word in words:
    if "categories" in word:
        if len(word.split(':')) > 1:
            temp = word.split(':')[1].strip()
            if temp != '' and temp != '[]':
                categories.append(temp)
    else:
        if len(word.split(':')) > 1:
            temp = word.split(':')[1].strip()
            if temp != '' and temp != '[]':
                if '[' in temp:
                    temp = temp.replace('[', '')
                    temp = temp.replace(']', '')
                    temp = temp.replace('\'', '')
                    temp = temp.split(',')
                    for tag in temp:
                        tags.append(tag)
                else:
                    tags.append(temp)

print ("填写范例：")
print (
'''
单标签：        多标签：

tags:           tags:
  hexo              [easy,leetcode]
''')
print ("现有的tags:")
for i in list(set(tags)):
    print (i, end=' ')
print ("\n\n现有的categories:")
for i in list(set(categories)):
    print (i, end=' ')
print ("\n")
print ("使用{%asset_img [file] [title]%}来添加图片链接。")
f.close()
