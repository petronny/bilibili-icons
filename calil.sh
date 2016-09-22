#!/bin/sh
cd `dirname $0`
sh bilibili-icons.sh
js-beautify -i index-icon.json -o index-icon.json
git add .
git commit -m "[$(LANG=C date)]auto update"
git push
