import json
import urllib.request
import os
icons=json.load(open('index-icon.json'))
for a in icons['fix']:
    img=urllib.request.urlopen(a['icon']).read()
    filename='gif/'+a['title']+'.gif'
    if os.path.exists(filename):
        continue
    print(a['title'])
    f=open(filename,'wb')
    f.write(img)
    f.close()
