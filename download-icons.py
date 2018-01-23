import json
import urllib.request
import os
import time
icons=json.load(open('index-icon.json'))
for a in icons['fix']:
    filename='gif/'+a['title']+'.gif'
    #if os.path.exists(filename):
    #    continue
    print(a['title'])
    if a['icon'][0:2]=='//':
        a['icon']='http:'+a['icon']
    a['icon']=a['icon'].replace('http:////','http://')
    img=urllib.request.urlopen(a['icon']).read()
    f=open(filename,'wb')
    f.write(img)
    f.close()
    time.sleep(0.5)
