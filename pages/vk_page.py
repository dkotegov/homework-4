# coding=utf-8
from time import sleep

class VKPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://vk.com/")

    def auth(self, login, password):
        inputEmail = self.driver.find_element_by_name("email")
        inputEmail.send_keys(login)

        inputPass = self.driver.find_element_by_name("pass")
        inputPass.send_keys(password)

        self.driver.find_element_by_class_name("flat_button").click()

        #чтобы успела отправиться авторизация
        sleep(3)
        # WebDriverWait(self.driver, 3).until_not(
        #     lambda x: x.find_element_by_id('quick_forgot')
        # )