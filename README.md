# Tests

### Run hub
    java -jar selenium-server-standalone-3.11.0.jar -role hub

### Run Node
    java -Dwebdriver.chrome.driver="./chromedriver" -Dwebdriver.gecko.driver="./geckodriver" -jar selenium-server-standalone-3.11.0.jar -role node -hub http://localhost:4444/grid/register -browser browserName=chrome,maxInstances=2 -browser browserName=firefox,maxInstances=2
