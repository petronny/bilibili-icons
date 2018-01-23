#!/bin/sh
wget http://www.bilibili.com/index/index-icon.json -O index-icon.json
python parse-index.py
[ ! -d gif ] && mkdir gif
python download-icons.py
