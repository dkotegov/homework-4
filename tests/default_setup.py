import os
from selenium.webdriver import DesiredCapabilities, Remote


def default_setup(t):
    t.USER_LOGIN = os.environ['USER_LOGIN']
    t.USER_PASSWORD = os.environ['USER_PASSWORD']
    t.RESTAURANT_LOGIN = os.environ['RESTAURANT_LOGIN']
    t.RESTAURANT_PASSWORD = os.environ['RESTAURANT_PASSWORD']

    browser = os.environ.get('BROWSER', 'CHROME')

    t.driver = Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=getattr(DesiredCapabilities, browser).copy()
    )

    t.driver.implicitly_wait(7)
