import os
from selenium.webdriver import DesiredCapabilities, Remote


def default_setup(t):
    """ Осуществляет авторизацию в studhunt.ru и настраивает браузер.
    :param t: unittest.TestCase
    :return: None
    """
    t.EMAIL_APPL = os.environ['EMAIL_APPL']
    t.PASSWORD_APPL = os.environ['PASSWORD_APPL']
    t.EMAIL_EMPL = os.environ['EMAIL_EMPL']
    t.PASSWORD_EMPL = os.environ['PASSWORD_EMPL']
    t.EMAIL_EMPL_COMP = os.environ['EMAIL_EMPL_COMP']
    t.PASSWORD_EMPL_COMP = os.environ['PASSWORD_EMPL_COMP']

    browser = os.environ.get('BROWSER', 'CHROME')

    t.driver = Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=getattr(DesiredCapabilities, browser).copy()
    )
