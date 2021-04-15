from pages.base_page import Page
from pages.navbar import NavBar
from pages.base_component import Component

class MeetingsPage(Page, Component):
    PATH = '/meetings'

    SLIDE = '//div[@class="meet-slide"][2]'
    CARD = '//div[@class="meet-card"]'

    SLIDE_GO_BUTTON = SLIDE + '//button[@class="meet-slide__go-button"]'
    SLIDE_LIKE_ICON = SLIDE + '//div[@class="meet-slide__like-icon-wrapper"]'

    MY_MEETINGS = '//button[contains(text(),"Мои мероприятия")]'
    DISGUISHT_MEETINGS = '//button[contains(text(),"Избранное")]'
    REMOVE_FILTERS = '//button[contains(text(),"Убрать фильтры")]'

    CARD_LIKE_ICON = CARD + '//img[@class="meet-card__like"]'

    GO_UPDATE_CONFIRMATION = '//div[@class="mtoasts__toast"]/p[contains(text(), "Зарегистрировалиь")] | //div[@class="mtoasts__toast"]/p[contains(text(), "Вы отменили регистрацию")]'
    LIKE_UPDATE_CONFIRMATION = '//div[@class="mtoasts__toast"]/p[contains(text(), "Вы убрали лайк")] | //div[@class="mtoasts__toast"]/p[contains(text(), "Вы оценили мероприятие")]'

    @property
    def navbar(self):
        return NavBar(self.driver)

    def click_card(self):
        self._wait_until_clickable(self.CARD).click()

    def click_slide(self):
        self._wait_until_clickable(self.SLIDE).click()

    def click_slide_like(self):
        self._wait_until_clickable(self.SLIDE_LIKE_ICON).click()

    def click_slide_go_button(self):
        self._wait_until_clickable(self.SLIDE_GO_BUTTON).click()

    def click_card_like(self):
        self._wait_until_clickable(self.CARD_LIKE_ICON).click()

    def click_my_meetings(self):
        self._wait_until_clickable(self.MY_MEETINGS).click()

    def click_disguisht(self):
        self._wait_until_clickable(self.DISGUISHT_MEETINGS).click()

    def click_remove_filters(self):
        self._wait_until_clickable(self.REMOVE_FILTERS).click()

    def wait_page_load(self, url):
        self.wait_for_url(url)

    def wait_for_like_update_confirmation(self):
        self._wait_until_preset(self.LIKE_UPDATE_CONFIRMATION)

    def wait_for_go_update_confirmation(self):
        self._wait_until_preset(self.GO_UPDATE_CONFIRMATION)

    # TODO: add missing components
