from tests.todo import TaskTest, TaskListTest

CHROME_BIN = './bin/mac_m1/chromedriver'
FIREFOX_BIN = './bin/mac_m1/geckodriver'
SELENIUM_BIN = 'bin/selenium.jar'

TESTS = [
    TaskTest,
    TaskListTest
]
