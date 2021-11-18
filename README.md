# LioKor Mail e2e tests

URL: https://mail.liokor.ru

### WARNING: if running on macOS file uploads won't be checked
### WARNING: Don't interact with OS while tests are running, because avatar path will be typed to the native file selection window at some point

## HowTo Run:
1. Copy `settings.template.py` to `settings.py` and specify `USERNAME` AND `PASSWORD` from `mail.liokor.ru` in it
2. Create `bin` folder
3. Download and put to `bin` folder:
   - `selenium-server-standalone-3.141.59.jar` from http://selenium-release.storage.googleapis.com/index.html?path=3.141/
   - `geckodriver` from https://github.com/mozilla/geckodriver/releases
   - `chromedriver` from http://chromedriver.storage.googleapis.com/index.html?path=94.0.4606.61/
4. Launch Selenium hub with `java -jar selenium-server-standalone-3.141.59.jar -role hub` from `bin` folder
5. Launch Selenium node with `java -Dwebdriver.chrome.driver="./chromedriver" -Dwebdriver.gecko.driver="./geckodriver" -jar selenium-server-standalone-3.141.59.jar -role node -hub http://localhost:4444/grid/register -browser browserName=chrome,maxInstances=2 -browser browserName=firefox,maxInstances=2` from `bin` folder
6. Navigate to project root and install python requirements with `pip3 install -r requirements.txt`
7. Start testing with `python3 run_tests.py`