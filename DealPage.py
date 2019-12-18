from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DealPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_input = 'input[name=Login]'
        self.password_input = 'input[name=Password]'
        self.login_button = '.login-button'
        self.name_input = '.todo-new-summary-input'
        self.name_label = '.todo-new-main__disabled'
        self.today_button = '.todo-new-main'
        self.create_button = '.button-create'
        self.item_content = '.panel-item-content'

    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def enter_login(self, login):
        elem = self.driver.find_element_by_css_selector(self.login_input)
        elem.send_keys(login)

    def enter_password(self, password):
        elem = self.driver.find_element_by_css_selector(self.password_input)
        elem.send_keys(password)

    def login(self):
        elem = self.driver.find_element_by_css_selector(self.login_button)
        elem.click()

    def enter_deal_name(self, name):
        elem = self.driver.find_element_by_css_selector(self.name_input)
        elem.send_keys(name)

    def click_on_name_deal(self):
        elem = self.driver.find_element_by_css_selector(self.name_label)
        elem.click()

    def click_on_today_btn(self):
        elem = self.driver.find_element_by_css_selector(self.today_button)
        elem.click()

    def click_on_add_btn(self):
        elem = self.driver.find_element_by_css_selector(self.create_button)
        elem.click()

    def checkDeal(self):
        elem = self.driver.find_element_by_css_selector(self.item_content).text
        return elem

    def wait_redirect(self, url, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
