#!/usr/bin/env bash

java -Dwebdriver.chrome.driver="./$1" \
    -Dwebdriver.gecko.driver="./$2" \
    -jar $3 \
    -role node \
    -hub http://127.0.0.1:4444/grid/register \
    -browser browserName=chrome,maxInstances=2 \
    -browser browserName=firefox,maxInstances=2
