from selenium.webdriver.support.ui import WebDriverWait

from base_classes.component import Component


class JoinForm(Component):
    FORM = '//div[@class="auth-form-join"]'
