java \
    -Dwebdriver.chrome.driver="./chromedriver.exe" \
    -Dwebdriver.gecko.driver="./geckodriver.exe" \
    -jar selenium-server-standalone-3.141.59.jar \
    -role node -hub http://localhost:4444/grid/register \
    -browser browserName=firefox,maxInstances=2 \
    -browser browserName=chrome,maxInstances=2
