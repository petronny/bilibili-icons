#!/bin/sh
wget http://www.bilibili.com/index/index-icon.json -O index-icon.json
[ ! -d gif ] && mkdir gif
python download-icons.py
