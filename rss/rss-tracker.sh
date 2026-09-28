#!/bin/bash

mkdir -p ~/tmp
count=0

while [ "$count" -lt 240 ]
do
  echo "===== $(date) ====="
  ps -eo pid,rss,args --sort=-rss | grep java | grep -v grep
  count=$((count + 1))
  sleep 3600
done >> ~/tmp/java-rss-history.log