#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    java -Dwebdriver.chrome.driver="./chromedriver_linux" \
        -Dwebdriver.gecko.driver="./geckodriver" \
        -jar selenium-server-standalone-3.141.59.jar \
        -role node \
        -hub http://127.0.0.1:4444/grid/register \
        -browser browserName=chrome,maxInstances=2 \
        -browser browserName=firefox,maxInstances=2
elif [[ "$OSTYPE" == "darwin"* ]]; then
    java -Dwebdriver.chrome.driver="./chromedriver_osx" \
        -Dwebdriver.gecko.driver="./geckodriver" \
        -jar selenium-server-standalone-3.141.59.jar \
        -role node \
        -hub http://127.0.0.1:4444/grid/register \
        -browser browserName=chrome,maxInstances=2 \
        -browser browserName=firefox,maxInstances=2
fi
