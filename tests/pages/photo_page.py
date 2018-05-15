from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page import Page, Component


class PhotoPage(Page):
    PATH = ''

    @property
    def photo(self):
        return Photo(self.driver)


class Photo(Component):
    DESCRIPTION = 'photo-description'
    LIKE = "//div[contains(@class, 'np_photoBox')]//a[@data-func='performLike']"
    CANCEL_LIKE = "//div[contains(@class, 'np_photoBox')]//a[@data-func='unReact']"
    LIKES_COUNT = 'ecnt'

    @property
    def description(self):
        return self.driver.find_element_by_class_name(self.DESCRIPTION).text

    @property
    def likes_count(self):
        try:
            likes_count = WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.LIKES_COUNT))
            )
            return int(likes_count.text)
        except TimeoutException:
            return 0

    def like(self):
        WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, self.LIKE))
        ).click()

        WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, self.CANCEL_LIKE))
        )

    def cancel_like(self):
        WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, self.CANCEL_LIKE))
        ).click()

        WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, self.LIKE))
        )
