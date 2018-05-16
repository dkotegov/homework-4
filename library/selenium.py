from unittest import TestCase, TextTestRunner, TextTestResult
from urllib.parse import urljoin
from os.path import dirname, realpath, join, pardir
from os import environ
from datetime import datetime
from selenium.webdriver import DesiredCapabilities, Remote
from warnings import warn
import config


class ScreenshotTextTestResult(TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super(ScreenshotTextTestResult, self).__init__(stream, descriptions, verbosity)
        self.current_test = None

    def save_screenshot(self):
        current_directory = dirname(realpath(join(__file__, pardir)))
        now = datetime.now().strftime('%Y.%m.%d-%H:%M:%S')
        screenshot_name = '{id}-{now}.png'.format(id=self.current_test.id(), now=now)
        screenshot_path = join(current_directory, config.get('TESTS_DIR'),
                               config.get('SCREENSHOT_DIR'), screenshot_name)
        saved = self.current_test.driver.save_screenshot(screenshot_path)
        if not saved:
            warn('Saving screenshot "{}" failed with IOError'.format(screenshot_path))

    def startTest(self, test):
        self.current_test = test
        super(ScreenshotTextTestResult, self).startTest(test)

    def stopTest(self, test):
        super(ScreenshotTextTestResult, self).stopTest(test)
        self.current_test = None

    def addError(self, test, err):
        self.save_screenshot()
        super(ScreenshotTextTestResult, self).addError(test, err)

    def addFailure(self, test, err):
        self.save_screenshot()
        super(ScreenshotTextTestResult, self).addFailure(test, err)


class ScreenshotTextTestRunner(TextTestRunner):
    resultclass = ScreenshotTextTestResult


class SeleniumTestCase(TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        super(SeleniumTestCase, cls).setUpClass()

        browser = environ.get('BROWSER', 'CHROME')
        cls.driver = Remote(
            command_executor=config.get('COMMAND_EXECUTOR'),
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        cls.driver.implicitly_wait(config.get('IMPLICITLY_WAIT'))

    @classmethod
    def tearDownClass(cls):
        super(SeleniumTestCase, cls).tearDownClass()
        cls.driver.quit()


class Page(object):
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    @classmethod
    def get_url(cls):
        return urljoin(config.get('BASE_URL'), cls.PATH)

    def open(self):
        self.driver.get(self.get_url())
        self.driver.maximize_window()
        return self


class Component(object):
    def __init__(self, driver):
        self.driver = driver
