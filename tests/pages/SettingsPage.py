from BasicPage import BasicPage

from selenium.webdriver import ActionChains


class SettingsPage(BasicPage):
    firstname = '#FirstName'
    lastname = '#LastName'
    nickname = '#NickName'
    city = '#your_town'
    city_suggest = '#formPersonal > div:nth-child(19) > div.form__row__widget > div:nth-child(2) > div'
    save_button = '#formPersonal > div.form__actions__wrapper > div > div > button'
    error_message = 'div.form__top-message.form__top-message_error'
    error_field_message = '#formPersonal > div:nth-child(12) > div.form__row__widget > div'
    mailling_tab = '#LEGO > div.b-layout.b-layout_main > div.b-layout__col.b-layout__col_1_2 > div > div:nth-child(3) > a > span'
    mailling_checkbox = '#send_ads'
    save_mailling_button = '#formMail > div.form__actions__wrapper > div > div > button'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.SETTINGS_URL)

    def enter_firstname(self, text):
        elem = self.wait_render(self.firstname)
        elem.clear()
        elem.send_keys(text)

    def enter_lastname(self, text):
        elem = self.wait_render(self.lastname)
        elem.clear()
        elem.send_keys(text)

    def enter_nickname(self, text):
        elem = self.wait_render(self.nickname)
        elem.clear()
        elem.send_keys(text)

    def enter_city(self, city):
        elem = self.wait_render(self.city)
        elem.clear()
        elem.click()
        elem.send_keys(city)

    def choose_city(self):
        elem = self.wait_render(self.city_suggest)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()

    def save(self):
        self.scroll_to_bottom()
        elem = self.wait_render(self.save_button)
        elem.click()

    def mailling_settings(self):
        elem = self.wait_render(self.mailling_tab)
        elem.click()

    def mailling_switch(self):
        elem = self.wait_render(self.mailling_checkbox)
        elem.click()

    def save_mailling(self):
        elem = self.wait_render(self.save_mailling_button)
        elem.click()
