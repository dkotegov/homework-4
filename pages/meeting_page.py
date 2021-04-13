from pages.base_page import Page
from pages.navbar import NavBar
from pages.base_component import Component

class MeetingPage(Page, Component):
    PATH = '/meeting?meetId=1'

    GO_BUTTON = '//button[contains(@class, "meet__button")]'
    LIKE_ICON = '//div[@class="meet__like-icon-wrapper"]'

    MEET_MEMBER = '//div[@class="meet__member"]'

    GO_UPDATE_CONFIRMATION = '//div[@class="mtoasts__toast"]/p[contains(text(), "Зарегистрировалиь")] | //div[@class="mtoasts__toast"]/p[contains(text(), "Вы отменили регистрацию")]'
    LIKE_UPDATE_CONFIRMATION = '//div[@class="mtoasts__toast"]/p[contains(text(), "Вы убрали лайк")] | //div[@class="mtoasts__toast"]/p[contains(text(), "Вы оценили мероприятие")]'

    @property
    def navbar(self):
        return NavBar(self.driver)

    def click_go_button(self):
        self._wait_until_clickable(self.GO_BUTTON).click()

    def click_like_icon(self):
        self._wait_until_clickable(self.LIKE_ICON).click()

    def click_meet_member(self):
        self._wait_until_clickable(self.MEET_MEMBER).click()

    def handle_like(self):
        self._wait_until_preset(self.LIKE_UPDATE_CONFIRMATION)

    def handle_go_button(self):
        self._wait_until_preset(self.GO_UPDATE_CONFIRMATION)