from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class SubscriptionLocators:
    def __init__(self):
        self.root = '//div[@class="profile-view__wrapper"]'
        self.subscription_btn = '//input[@class="subscription__btn"]'
        self.umoney_button = '//button[@class="button2 button2_theme_action button2_size_ml button2_type_submit i-bem button2_js_inited"]'


class SubscriptionForm(BaseComponent):
    def __init__(self, driver):
        super(SubscriptionForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = SubscriptionLocators()
        self.umoney_url = "https://yoomoney.ru/quickpay/confirm.xml"

    def click_subscription(self):
        """
        Открывает панель настроек
        """
        open_form_button = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.subscription_btn))
        )
        open_form_button.click()

    def check_umoney_open(self) -> bool:
        """
        Проверяет открытие панели настроек
        """
        open_form_button = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.locators.umoney_button))
        )
        return self.driver.current_url == self.umoney_url
