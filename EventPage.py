from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class EventPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_input = 'input[name=Login]'
        self.password_input = 'input[name=Password]'
        self.login_button = '.login-button'
        self.event_input = '.event-summary-input'
        self.open_menu_button = 'div.header-menu-item.header-menu-item__sidebutton.header-menu-item__plus'
        self.back_button = '.header-menu-item__back'
        self.ok_button = '.header-menu-item__ok'
        self.event_item = 'div.panel-item.brief-event'
        self.first_event_item = 'div.panel-item-text.brief-event-title'
        self.item_container = 'div.panels-container'
        self.edit_button = '.header-menu-item__edit'
        self.remove_button = '.button-delete'

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

    def enter_event_name(self, name):
        elem = self.driver.find_element_by_css_selector(self.event_input)
        # Clear old data
        elem.clear()
        # Enter new data
        elem.send_keys(name)

    def open_menu_plus(self):
        elem = self.wait_presence_located(self.open_menu_button)
        elem.click()

    def click_on_back_btn(self):
        elem = self.wait_render_btn(self.back_button)
        elem.click()

    def click_on_ok_btn(self):
        elem = self.wait_render_btn(self.ok_button)
        elem.click()

    def click_on_first_event(self):
        elem = self.wait_render_btn(self.event_item)
        elem.click()

    def get_first_event(self):
        elems = self.wait_invisible_all(self.first_event_item)
        if elems[0].is_displayed():
            return elems[0]

    def get_count_of_events(self):
        self.wait_presence_located(self.item_container)
        childs = self.driver.find_elements_by_css_selector(self.event_item)
        return len(childs)

    def create_event(self, name):
        self.open_menu_plus()
        self.enter_event_name(name)
        self.click_on_ok_btn()

    def click_on_edit_btn(self):
        elem = self.wait_render_btn(self.edit_button)
        elem.click()

    def click_on_remove_btn(self):
        elem = self.wait_render_btn(self.remove_button)
        elem.click()

    def wait_redirect(self, url, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.url_matches(url))

    def wait_render_btn(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def wait_presence_located(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_invisible(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_invisible_all(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector)))
