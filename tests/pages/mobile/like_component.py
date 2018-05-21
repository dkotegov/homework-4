from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.mobile.page import Component


class LikeComponent(Component):
    LIKE = "//a[@data-func='performLike']"
    CANCEL_LIKE = "//a[@data-func='unReact']"
    LIKES_COUNT = '//span[@class="widget-list_actors"]/span[@class="ecnt"]'

    def __init__(self, driver, base=''):
        super().__init__(driver)
        self.base = base

    @property
    def likes_count(self):
        try:
            likes_count = WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located((By.XPATH, self.base + self.LIKES_COUNT))
            )
            return int(likes_count.text)
        except TimeoutException:
            return 0

    def like(self):
        WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, self.base + self.LIKE))
        ).click()

        WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, self.base + self.CANCEL_LIKE))
        )

    def cancel_like(self):
        WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, self.base + self.CANCEL_LIKE))
        ).click()

        WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, self.base + self.LIKE))
        )
