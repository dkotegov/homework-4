set-env:
	export BROWSER_DRIVERS=$(PWD)/drivers && export LOGIN=$LOGIN && export PASS=$PASS

set-chrome:
	make set-env && export BROWSER=CHROME

set-firefox:
	make set-env && export BROWSER=FIREFOX

grid:
	java -jar selenium-server-standalone-3.7.1.jar -role hub

node:
	java -Dwebdriver.chrome.driver="./drivers/chromedriver" \
    -Dwebdriver.gecko.driver="./drivers/geckodriver" \
    -jar selenium-server-standalone-3.7.1.jar \
    -role node \
    -hub http://127.0.0.1:4444/grid/register \
    -browser browserName=chrome,maxInstances=2 \
    -browser browserName=firefox,maxInstances=2

run-tests:
	python run_tests.py