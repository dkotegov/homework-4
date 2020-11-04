#!/usr/bin/env bash

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

java -jar "$CURRENT_DIR/../bin/selenium-server-standalone-3.141.59.jar" \
    -role hub
