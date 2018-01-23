import json
import urllib.parse
icons=json.load(open('index-icon.json'))
for a in icons['fix']:
    for i in range(0,len(a['links'])):
        a['links'][i]=urllib.parse.unquote(a['links'][i])
f=open('index-icon.json','w')
json.dump(icons,f,ensure_ascii=False,sort_keys=True,indent=4)
f.close()
