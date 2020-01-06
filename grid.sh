#!/usr/bin/env bash

java -jar ./drivers/selenium-server-standalone-2.53.1.jar -role hub

java \
    -Dwebdriver.chrome.driver=./drivers/chromedriver \
    -jar /drivers/selenium-server-standalone-2.53.1.jar \
    -role node \
    -hub http://localhost:4444/grid/register \
    -nodeConfig node1Config.json
# java -Dwebdriver.chrome.driver="./drivers/chromedriver" \
#     -Dwebdriver.gecko.driver="./drivers/geckodriver" \
#     -jar ./drivers/selenium-server-standalone-3.141.59.jar \
#     -role node \
#     -hub http://127.0.0.1:4444/grid/register \
#     -browser browserName=chrome,maxInstances=2 \
#     -browser browserName=firefox,maxInstances=2