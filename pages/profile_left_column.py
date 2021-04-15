from selenium.webdriver import ActionChains

from pages.base_component import Component


class ProfileLeftColumn(Component):
    AVATAR = '//img[@class="profile__avatar"]'
    NAME = '//h2[contains(@class, "profile__name")]'
    SUBSCRIBE_BTN = '//button[@class="profile__subscribe-button"]'
    AVATAR_OVERLAY_LABEL = '//label[@class="profile__file-label"]'
    COLUMN = '//div[@class="profile__leftcolumn"]'
    VK = '//a[contains(@class, "profile__vk")]'
    TELEGRAM = '//a[contains(@class, "profile__telegram")]'
    TEST_MEETING = '//div[@class="profile__meetings"]/div/a[contains(text(),"Test")]'
    SUB_CONFIRMATION = '//div[@class="mtoasts__toast"]/p[contains(text(), "Вы подписались на пользователя")]'
    UNSUB_CONFIRMATION = '//div[@class="mtoasts__toast"]/p[contains(text(), "Вы отменили подписку на пользователя")]'
    CLOSE_CONFIRMATION = '//div[@class="closeWrapper"]/span[@class="close"]'
    AVATAR_INPUT = '//input[@class="profile__file-chooser"]'
    AVATAR_SAVE_BTN = '//button[@class="profile__save-button"]'

    def click_vk(self):
        self._wait_until_clickable(self.VK).click()

    def click_telegram(self):
        self._wait_until_clickable(self.TELEGRAM).click()

    def click_test_meeting(self):
        self._wait_until_clickable(self.TEST_MEETING).click()

    def is_subscribe_btn_visible(self):
        return self._is_element_visible(self.SUBSCRIBE_BTN)

    def click_subscribe_btn(self):
        self._wait_until_clickable(self.SUBSCRIBE_BTN).click()

    def wait_for_sub_confirmation(self):
        self._wait_until_visible(self.SUB_CONFIRMATION)

    def wait_for_unsub_confirmation(self):
        self._wait_until_visible(self.UNSUB_CONFIRMATION)

    def click_close_confirmation(self):
        self._wait_until_clickable(self.CLOSE_CONFIRMATION).click()

    def wait_for_col_visibility(self):
        self._wait_until_visible(self.COLUMN)

    def get_sub_btn_text(self):
        return self._find_element(self.SUBSCRIBE_BTN).text

    def hover_on_avatar(self):
        avatar = self._wait_until_visible(self.AVATAR)
        hover = ActionChains(self.driver).move_to_element(avatar)
        hover.perform()

    def get_avatar_overlay_text(self):
        return self._wait_until_visible(self.AVATAR_OVERLAY_LABEL).text

    def click_avatar_overlay(self):
        self._wait_until_visible(self.AVATAR_OVERLAY_LABEL).click()

    def choose_avatar_file(self, filename):
        self._find_element(self.AVATAR_INPUT).send_keys(filename)

    def get_avatar_button_text(self):
        return self._wait_until_visible(self.AVATAR_SAVE_BTN).text

    def get_profile_name_text(self):
        return self._wait_until_visible(self.NAME).text

