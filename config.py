from os import environ

__all__ = [
    'TESTS_DIR', 'TEST_PATTERN',
    'COMMAND_EXECUTOR', 'IMPLICITLY_WAIT',
    'SCREENSHOT_DIR',
    'BASE_URL', 'LOGIN', 'PASSWORD'
]

# Tests discover options
TESTS_DIR = 'tests'
TEST_PATTERN = '*_test.py'

# Browser options
"""
BROWSER choices: {
    FIREFOX, INTERNETEXPLORER, EDGE, CHROME, OPERA, SAFARI, HTMLUNIT, HTMLUNITWITHJS, 
    IPHONE, IPAD, ANDROID, PHANTOMJS, WEBKITGTK
}
"""
BROWSER = None
COMMAND_EXECUTOR = 'http://127.0.0.1:4444/wd/hub'
IMPLICITLY_WAIT = 1  # sec

SCREENSHOT_DIR = 'screenshots'

# Common ok options
BASE_URL = 'https://ok.ru'
LOGIN = 'technopark14'
PASSWORD = None


def get(name, default=None):
    value = default
    if name in __all__:
        value = globals()[name]
    return value or environ.get(name, default)
