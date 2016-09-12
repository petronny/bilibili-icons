#!/bin/sh
cd `dirname $0`
wget http://www.bilibili.com/index/index-icon.json -O index-icon.json.gz
gzip -d -f index-icon.json.gz
[ ! -d gif ] && mkdir gif
python download-icons.py
js-beautify -i index-icon.json -o index-icon.json
git add .
git commit -m "[$(LANG=C date)]auto update"
git push
