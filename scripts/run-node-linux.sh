sudo java -D webdriver.chrome.driver="./drivers/linux/chromedriver" \
    -D webdriver.gecko.driver="./drivers/linux/geckodriver" \
    -jar drivers/selenium-server-standalone-3.141.59.jar \
    -role node \
    -hub http://127.0.0.1:4444/grid/register \
    -browser browserName=chrome,maxInstances=2 \
    -browser browserName=firefox,maxInstances=2