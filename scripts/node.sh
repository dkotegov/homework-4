#!/usr/bin/env bash

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
ARCH=""

if [ "$(uname)" = "Linux" ]; then
    ARCH="linux"
fi

if [ "$(uname)" = "Darwin" ]; then
    ARCH="macos"
fi

java -Dwebdriver.chrome.driver="$CURRENT_DIR/../bin/chromedriver_$ARCH" \
    -Dwebdriver.gecko.driver="$CURRENT_DIR/../bin/geckodriver_$ARCH" \
    -jar "$CURRENT_DIR/../bin/selenium-server-standalone-3.141.59.jar" \
    -role node \
    -hub http://127.0.0.1:4444/grid/register \
    -browser browserName=chrome,maxInstances=2 \
    -browser browserName=firefox,maxInstances=2
