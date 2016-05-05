# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait

class VKPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://vk.com/")

    def auth(self, login, password):
        self.driver.find_element_by_name("email").send_keys(login)
        self.driver.find_element_by_name("pass").send_keys(password)

        self.driver.find_element_by_class_name("flat_button").click()

        WebDriverWait(self.driver, 3).until(
            lambda x: x.find_element_by_id('logout_link')
        )

    def post(self):
        WebDriverWait(self.driver, 100).until(
            lambda x: x.find_element_by_id("dd_menu1")
        )
        button = self.driver.find_element_by_id("post_button")
        button.click()

        window_before = self.driver.window_handles[0]
        self.driver.switch_to_window(window_before)