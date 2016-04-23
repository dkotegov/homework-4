# coding=utf-8
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class BlockFindNewObraz:
    def __init__(self, driver):
        self.driver = driver

    def get_message_no_success(self):
        message = self.driver.find_element_by_class_name("article__text")
        return message.text

    def message_is_success(self, msg, obraz):
        return msg.find(obraz + u" найдено") != -1 or (
            msg.find(u" / Толкование образа") != -1 and msg.find(obraz) != -1)

    def message_is_no_success(self, msg):
        return msg.find(u"не найдено") != -1

    def get_message_success(self):
        str1 = self._get_message1_success()
        if str1 != None:
            return str1
        else:
            return self._get_message2_success()

    def _get_message1_success(self):
        try:
            message = self.driver.find_element_by_class_name("hdr_search")
            return message.text
        except NoSuchElementException:
            return None

    def _get_message2_success(self):
        try:
            message = self.driver.find_element_by_class_name("hdr__inner")
            return message.text
        except NoSuchElementException:

            return None

    def find(self, obraz):
        input = self.driver.find_element_by_name("q")
        input.send_keys(obraz)

        self.driver.find_element_by_name("clb11934144").click()


class BlockRepostToSocialNet:
    def __init__(self, driver, mypage):
        self.driver = driver
        self.mypage = mypage

    def getCountReposts(self):
        try:
            return int(self.driver.find_element_by_class_name("sharelist__count").text)
        except NoSuchElementException:
            return 0

    def postToVkAlreadyAuth(self):
        self.driver.find_element_by_class_name("share_vk").click()
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]

        self.driver.switch_to_window(window_after)

        # ждем загрузки элемента autosize_helpers, который ниже чем скрипты, которые вешаются на кнопку post_button
        WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_id('autosize_helpers'))
        self.driver.find_element_by_id("post_button").click()

        self.driver.switch_to_window(window_before)
        self.driver.get(self.mypage)

    def authVK(self, login, password):
        self.driver.get("https://vk.com/")

        inputEmail = self.driver.find_element_by_name("email")
        inputEmail.send_keys(login)

        inputPass = self.driver.find_element_by_name("pass")
        inputPass.send_keys(password)

        self.driver.find_element_by_id("quick_login_button").click()
        WebDriverWait(self.driver, 3) \
            .until(lambda x: x.find_element_by_id('feed_summary_wrap'))

    def postToVkWithAuth(self, login, password):
        self.driver.find_element_by_class_name("share_vk").click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)

        try:
            btn = self.driver.find_element_by_class_name("popup_login_btn")
            inputEmail = self.driver.find_element_by_name("email")
            inputEmail.send_keys(login)

            inputPass = self.driver.find_element_by_name("pass")
            inputPass.send_keys(password)

            btn.click()
        except NoSuchElementException:
            pass
