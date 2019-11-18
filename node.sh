#!/usr/bin/env bash

java -Dwebdriver.gecko.driver="./geckodriver" \
    -Dwebdriver.chrome.driver="./chromedriver" \
    -jar selenium-server-standalone-3.141.59.jar \
    -role node \
    -hub http://127.0.0.1:4444/grid/register \
    -browser browserName=firefox \
    -browser browserName=chrome