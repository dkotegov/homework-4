#!/usr/bin/env bash

java -Dwebdriver.chrome.driver="./drivers/chromedriver-2.33-macos64" \
    -Dwebdriver.gecko.driver="./drivers/geckodriver-v0.19.1-macos64" \
    -jar ./selenium/selenium-server-standalone-3.7.1.jar \
    -role node \
    -hub http://127.0.0.1:4444/grid/register \
    -browser browserName=chrome,maxInstances=2 \
    -browser browserName=firefox,maxInstances=2
