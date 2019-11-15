from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Steps(object):
    BASE_URL = ''

    def __init__(self, core):
        self.driver = core
        self.driver.get(self.BASE_URL)

    def wait(self, until=None, timeout=30):
        return WebDriverWait(self.driver, timeout).until(until)

    def waitForVisible(self, selector=None, state=True):
        print(self)
        print(self.wait(EC.visibility_of_element_located((By.CSS_SELECTOR, selector))))
        return state == self.wait(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def click(self, selector=None):
        return self.waitForVisible(selector).click()

    def waitForBeBlocked(self, selector=None, state=None):
        currentState = self.waitForVisible(selector + '.b-dropdown__list__item_unselectable')
        if (currentState == state):
            return True
        else:
            return False

    def addGroup(self, name=''):
        self.waitForVisible('#js-labels-dropdown')
        self.click('#js-labels-dropdown')
        input = self.waitForVisible('.js-add-label-to-dropdown-input')
        self.click('.js-add-label-to-dropdown-input')
        input.send_keys(name)
        Steps.waitForVisible('.js-add-label-to-dropdown-button')
        Steps.click('.js-add-label-to-dropdown-button')


class TestKek(Steps):
    BASE_URL = 'https://e.mail.ru/addressbook'

    def enterGroupName(self, name=''):
        input = self.waitForVisible('.js-add-label-to-dropdown-input')
        self.click('.js-add-label-to-dropdown-input')
        input.send_keys(name)
