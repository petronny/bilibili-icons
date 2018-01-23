#!/bin/python3
import json
import urllib.request
import os
from socket import timeout
icons=json.load(open('index-icon.json'))
for a in icons['fix']:
    filename='gif/'+a['title']+'.gif'
    #if os.path.exists(filename):
    #    continue
    print(a['title'])
    if a['icon'][0:2]=='//':
        a['icon']='http:'+a['icon']
    a['icon']=a['icon'].replace('http:////','http://')
    flag=False
    while not flag:
        try:
            img=urllib.request.urlopen(a['icon'],timeout=3).read()
            flag=True
        except timeout:
            flag=False
    f=open(filename,'wb')
    f.write(img)
    f.close()
