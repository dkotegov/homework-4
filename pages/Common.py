import urlparse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class Page(object):
    BASE_URL = "https://otvet.mail.ru/"
    PATH = ""
    QUESTIONS_CLASS = "q--li--text"
    POPUP_CLASS = "popup--content "
    FORM_CLASS = "form-form"
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)

    def open_login_frame(self):
        self.driver.find_element_by_id("PH_authLink").click()
        self.driver.switch_to_frame(self.driver.find_element_by_class_name("ag-popup__frame__layout__iframe"))

    def close_login_frame(self):
        self.driver.switch_to_default_content()

    def auth_form(self):
        return AuthFormFrame(self.driver)

    def open_question(self):
        self.driver.find_element_by_class_name(self.QUESTIONS_CLASS).click()
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, self.FORM_CLASS)))

    def error_poput(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME,self.POPUP_CLASS)))
        return self.driver.find_element_by_class_name(self.POPUP_CLASS).text


class Element(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(Page):
    BASE_URL = "https://mail.ru/"


class AuthFormFrame(Element):
    LOGIN_EMAIL = "Username"
    PASSWORD = "Password"
    SUBMIT = "button"
    DOMAIN_DROPDOWN = "b-dropdown__ctrl"

    def __init__(self, driver):
        super(AuthFormFrame, self).__init__(driver)
        self.form = self.driver.find_element_by_name("login")

    def set_login(self, login):
        self.form.find_element_by_name(self.LOGIN_EMAIL).send_keys(login)

    def set_domain(self, domain):
        domain_item = "//a[@data-value='"+domain+"']"
        self.form.find_element_by_class_name(self.DOMAIN_DROPDOWN).click()
        self.form.find_element_by_xpath(domain_item).click()

    def set_password(self, password):
        self.form.find_element_by_name(self.PASSWORD).send_keys(password)

    def login(self):
        self.form.find_element_by_tag_name(self.SUBMIT).click()