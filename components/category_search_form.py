from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class CategorySearchFormLocators:
    def __init__(self):
        self.root = '//div[@class="category"]'
        self.category = '//div[@class="category-sec-row"]'
        self.category_name = 'category-sec-row__sphere'


class CategorySearchForm(BaseComponent):
    def __init__(self, driver):
        super(CategorySearchForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = CategorySearchFormLocators()

    def click_on_category(self) -> str:
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.category)))

        category = element.find_element_by_class_name(self.locators.category_name)
        text = category.get_attribute('innerText')
        element.click()
        return text
