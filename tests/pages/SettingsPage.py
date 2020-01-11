from BasicPage import BasicPage

from selenium.webdriver import ActionChains


class SettingsPage(BasicPage):
    firstname = '#FirstName'
    city = '#your_town'
    city_suggest = 'div.form__field__suggest:nth-child(1) > span:nth-child(1) > div:nth-child(1)'
    save_button = '#formPersonal > div.form__actions__wrapper > div > div > button'
    error_message = 'div.form__top-message.form__top-message_error'
    error_field_message = '#formPersonal > div:nth-child(12) > div.form__row__widget > div'
    notification_tab = '#LEGO > div.b-layout.b-layout_main > div.b-layout__col.b-layout__col_1_2 > div > div:nth-child(9) > a > span'
    notification_checkbox = 'div.c2165'
    save_message = 'div > div.notify__content > span.notify__message'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.SETTINGS_URL)

    def enter_firstname(self, login):
        elem = self.wait_render(self.firstname)
        elem.clear()
        elem.send_keys(login)

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

    def notification_settings(self):
        elem = self.wait_render(self.notification_tab)
        elem.click()

    def notification_change_mode(self):
        elem = self.wait_render(self.notification_checkbox)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
