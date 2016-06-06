import json
import urllib
import os
icons=json.load(open('index-icon.json'))
for a in icons['fix']:
    img=urllib.urlopen(a['icon']).read()
    filename='gif/'+a['title']+'.gif'
    if os.path.exists(filename):
        continue
    f=open(filename,'wb')
    f.write(img)
    f.close()
