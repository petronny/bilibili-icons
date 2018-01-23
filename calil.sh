#!/bin/sh
cd `dirname $0`

git reset --hard
git pull

sh bilibili-icons.sh

git add .
git commit -m "[$(LANG=C date)]auto update"
git push
