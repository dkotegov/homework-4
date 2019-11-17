import os

from pages.default_page import DefaultPage, Component
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from helpers import wait_for_element


class UserinfoPage(DefaultPage):
    URL = 'https://e.mail.ru/settings/userinfo'

    @property
    def form(self):
        return UserinfoForm(self.driver)

class UserinfoForm(Component):
    TOWN = 'input[name="your_town"]'
    SURNAME = 'input[name="LastName"]'            
    SAVE = 'div.form__actions__inner button[type="submit"]'
    CANCEL = '#formPersonal > div.form__actions__wrapper > div > div > a'
    TOP_MESSAGE = 'div.content__page > div.form__top-message.form__top-message_error > span'
    TOWN_ERROR = 'input[name="your_town"] ~ .form__message.form__message_error'
    MAKE_SNAPSHOT = '#js-edit-avatar > div.form__row__widget > span.form__row__avatar__infotext > div:nth-child(2) > div:nth-child(2) > button'
    LOAD_IMAGE = '#js-edit-avatar > div.form__row__widget > span.form__row__avatar__infotext > div:nth-child(2) > div:nth-child(1) > div.js-browse.js-fileapi-wrapper > input'
    SAVE_AVATAR = '#MailRuConfirm > div > div.is-avatar_in.popup_avatar > div.js-content.popup_avatar__content > div.popup__controls > div > div:nth-child(1)'
    CANCEL_AVATAR = '#MailRuConfirm > div > div.is-avatar_in.popup_avatar > div.js-content.popup_avatar__content > div.popup__controls > div > div:nth-child(2)'
    PHONE_LINK = '#phonesContainer > div > div:nth-child(2) > a'
    TIMEZONE_TICK = 'input[name=UseAutoTimezone]'
    TIMEZONE_SELECTOR = 'select[name=TimeZone]'
    SURNAME_ERROR = '#formPersonal > div:nth-child(13) > div.form__row__widget > div'
    SUGGESTS = '#formPersonal > div:nth-child(19) > div.form__row__widget > div:nth-child(2) > div > span'

    def set_town(self, town):
        wait_for_element(self.driver, self.TOWN)
        self.driver.find_element_by_css_selector(self.TOWN).send_keys(town)

    def save(self):
        wait_for_element(self.driver, self.SAVE)
        self.driver.find_element_by_css_selector(self.SAVE).click()

    def cancel(self):
        wait_for_element(self.driver, self.CANCEL)
        self.driver.find_element_by_css_selector(self.CANCEL).click()

    def get_top_message(self):
        wait_for_element(self.driver, self.TOP_MESSAGE)
        return self.driver.find_element_by_css_selector(self.TOP_MESSAGE).text

    def get_town_message(self):
        wait_for_element(self.driver, self.TOWN_ERROR)
        return self.driver.find_element_by_css_selector(self.TOWN_ERROR).text

    def uncheck_town(self):
        wait_for_element(self.driver, self.TIMEZONE_TICK)
        tick = self.driver.find_element_by_css_selector(self.TIMEZONE_TICK)
        if tick.is_selected():
            tick.click()

    def get_town_selector(self):
        #wait_for_element(self.driver, self.TIMEZONE_SELECTOR)
        return self.driver.find_element_by_css_selector(self.TIMEZONE_SELECTOR)

    def get_url_phone_link(self):
        wait_for_element(self.driver, self.PHONE_LINK)
        return self.driver.find_element_by_css_selector(self.PHONE_LINK).get_attribute("href")  

    def load_image(self, image):
        #wait_for_element(self.driver, self.LOAD_IMAGE)
        self.driver.find_element_by_css_selector(self.LOAD_IMAGE).send_keys(image)
    
    def get_save_avatar_button(self):
        wait_for_element(self.driver, self.SAVE_AVATAR)
        return self.driver.find_element_by_css_selector(self.SAVE_AVATAR)
            
    def get_cancel_avatar_button(self):
        wait_for_element(self.driver, self.CANCEL_AVATAR)
        return self.driver.find_element_by_css_selector(self.CANCEL_AVATAR)

    def dismiss_snapshot_request(self):
        make_snapshot = self.driver.find_element_by_css_selector(self.MAKE_SNAPSHOT)
        if make_snapshot.is_enabled():    
            makeSnapshot.click()
            driver.switch_to_alert()
            Alert(driver).dismiss()   

    def set_surname(self, surname):
        wait_for_element(self.driver, self.SURNAME)
        surname_elem = self.driver.find_element_by_css_selector(self.SURNAME)
        surname_elem.clear()
        surname_elem.send_keys(surname)        

    def get_surname_value(self):
        wait_for_element(self.driver, self.SURNAME)
        return self.driver.find_element_by_css_selector(self.SURNAME).get_attribute("value")     

    def get_surname_message(self):
        wait_for_element(self.driver, self.SURNAME_ERROR)
        return self.driver.find_element_by_css_selector(self.SURNAME_ERROR).text

    def clear_town(self):
        wait_for_element(self.driver, self.TOWN)
        self.driver.find_element_by_css_selector(self.TOWN).clear()


