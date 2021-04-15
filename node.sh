#!/usr/bin/env bash

ARCH=""

if [ "$(uname)" = "Linux" ]; then
    ARCH="linux"
fi

if [ "$(uname)" = "Darwin" ]; then
    ARCH="mac"
fi

java -Dwebdriver.chrome.driver="./chromedriver_$ARCH" \
    -Dwebdriver.gecko.driver="./geckodriver_$ARCH" \
    -jar selenium-server-standalone-3.141.59.jar \
    -role node \
    -hub http://127.0.0.1:4444/grid/register \
    -browser browserName=chrome,maxInstances=2 \
    -browser browserName=firefox,maxInstances=2