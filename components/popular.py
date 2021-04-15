from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class PopularCategoriesLocators:
    def __init__(self):
        self.root = '//div[@class="category"]'

        self.category = '//div[@class="category-sec-row"]'
        self.footer_btn = '//div[@class="btm-create-account"]'


class PopularCategories(BaseComponent):
    def __init__(self, driver):
        super(PopularCategories, self).__init__(driver)
        self.locators = PopularCategoriesLocators()

    def click_category(self, category: str) -> None:
        categories = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.category))
        )
        for c in categories:
            if category in c.text:
                c.click()
                return

    def click_footer_btn(self):
        text = self.get_field(self.locators.footer_btn)
        self.click_locator(self.locators.footer_btn)
        return text
