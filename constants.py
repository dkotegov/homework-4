import os

COMMAND_EXECUTOR = 'http://127.0.0.1:4444/wd/hub'
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
SCREENSHOT_PATH = os.path.join(DIRECTORY, 'screenshots')
WAIT_TIME = 5
MAKE_SCREENSHOTS = False
BASE_URL = 'https://ok.ru/'
