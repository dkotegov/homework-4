from pages.base_component import Component


class ProfileLeftColumn(Component):
    AVATAR = '//img[@class="profile__avatar"]'
    SUBSCRIBE_BTN = '//button[@class="profile__subscribe-button"]'
    CHANGE_AVATAR = '//label[@class="profile__file-label"]'
    VK = '//a[contains(@class, "profile__vk")]'
    TELEGRAM = '//a[contains(@class, "profile__telegram")]'
    TEST_MEETING = '//div[@class="profile__meetings"]/div/a[contains(text(),"Test")]'

    def click_vk(self):
        self._wait_until_clickable(self.VK).click()

    def click_telegram(self):
        self._wait_until_clickable(self.TELEGRAM).click()

    def click_test_meeting(self):
        self._wait_until_clickable(self.TEST_MEETING).click()
