import os
from selenium.webdriver import DesiredCapabilities, Remote


def default_setup(t):
    """ Осуществляет авторизацию в flicksbox.ru и настраивает браузер.
    :param t: unittest.TestCase
    :return: None
    """
    t.EMAIL = os.environ['EMAIL']
    t.PASSWORD = os.environ['PASSWORD']

    browser = os.environ.get('BROWSER', 'CHROME')
    # browser = os.environ.get('BROWSER', 'FIREFOX')

    t.driver = Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=getattr(DesiredCapabilities, browser).copy()
    )
