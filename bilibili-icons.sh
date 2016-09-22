#!/bin/sh
wget http://www.bilibili.com/index/index-icon.json -O index-icon.json.gz
gzip -d -f index-icon.json.gz
[ ! -d gif ] && mkdir gif
python download-icons.py
