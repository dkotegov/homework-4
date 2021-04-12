import os
from selenium.webdriver import DesiredCapabilities, Remote


def default_setup(t):
    """ Осуществляет авторизацию в studhunt.ru и настраивает браузер.
    :param t: unittest.TestCase
    :return: None
    """
    t.EMAIL = os.environ['EMAIL']
    t.PASSWORD = os.environ['PASSWORD']
    t.EMAIL1 = os.environ['EMAIL1']
    t.PASSWORD1 = os.environ['PASSWORD1']

    browser = os.environ.get('BROWSER', 'CHROME')

    t.driver = Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=getattr(DesiredCapabilities, browser).copy()
    )
