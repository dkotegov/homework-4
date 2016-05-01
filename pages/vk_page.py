# coding=utf-8
from time import sleep

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
        # событие не успевает повесится на кнопку post_button
        sleep(1)
        # по хорошему нужно так:
        # кликать, если событие не произошло, кликать еще раз
        # или  повесить wait на событие, после которого кнопка точно будет готова

        self.driver.find_element_by_id("post_button").click()

        window_before = self.driver.window_handles[0]
        self.driver.switch_to_window(window_before)