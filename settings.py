from tests.todo import TaskTest, TaskListTest, SortTest
from tests.moneycat import MoneyCatAuthTest, MoneyCatRegistrationTest, MoneyCatConverterTest, MoneyCatSettingsTest,\
    MoneyCatSellTest, MoneyCatHeaderTest

CHROME_BIN = 'bin/mac_m1/chromedriver'
FIREFOX_BIN = 'bin/mac_m1/geckodriver'
SELENIUM_BIN = 'bin/selenium.jar'

TESTS = [
    MoneyCatSellTest,
    MoneyCatHeaderTest,
    MoneyCatConverterTest,
    MoneyCatRegistrationTest,
    MoneyCatAuthTest,
    MoneyCatSettingsTest,
    TaskListTest,
    TaskTest,
    SortTest
]

BROWSERS = [
    'CHROME',
    'FIREFOX',
]
