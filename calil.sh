#!/bin/sh
(
cd `dirname $0`
git reset --hard
git pull
sh bilibili-icons.sh
python parse-index.py
js-beautify -i index-icon.json -o index-icon.json
) > log.txt
git add .
git commit -m "[$(LANG=C date)]auto update"
git push
