import os

from selenium.webdriver import DesiredCapabilities, Remote


def default_setup(t):
    t.LOGIN = os.environ['LOGIN']
    t.PASSWORD = os.environ['PASSWORD']

    browser = os.environ.get('BROWSER', 'CHROME')

    t.driver = Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=getattr(DesiredCapabilities, browser).copy()
    )
    t.driver.implicitly_wait(5)
