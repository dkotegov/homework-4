import os

from pages.default_page import DefaultPage, Component
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from helpers import *


class UserinfoPage(DefaultPage):
    URL = 'https://e.mail.ru/settings/userinfo'

    @property
    def form(self):
        return UserinfoForm(self.driver)

class UserinfoForm(Component):
    TOWN = 'input[name="your_town"]'
    SURNAME = 'input[name="LastName"]'            
    SAVE = 'div.form__actions__inner button[type="submit"]'
    CANCEL = '#formPersonal a.btn'
    TOP_MESSAGE = 'div.content__page  span'
    TOWN_ERROR = 'input[name="your_town"] ~ .form__message.form__message_error'
    SURNAME_ERROR = '#formPersonal div.form__message_error'
    MAKE_SNAPSHOT = '#js-edit-avatar button.js-camera'
    LOAD_IMAGE = '#js-edit-avatar input[name="avatar"]'
    SAVE_AVATAR = '#MailRuConfirm div[data-fire="save"]'
    CANCEL_AVATAR = '#MailRuConfirm div[data-fire="cancel"]'
    PHONE_LINK = '#phonesContainer a.js-click-security-recovery'
    TIMEZONE_TICK = 'input[name=UseAutoTimezone]'
    TIMEZONE_SELECTOR = 'select[name=TimeZone]'
    SUGGESTS = '//*[@class="content__page"]/descendant::span[@class="div_inner ac-items form__field__suggest__inner"]'
    SUGGESTS_ITEM = '//form[@id="formPersonal"]//*[@class="form__field__suggest__item"]'
    GENDER_MALE = 'label[for="man1"] input'
    GENDER_FEMALE = 'label[for="man2"] input'

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
        return self.driver.find_element_by_css_selector(self.TIMEZONE_SELECTOR)

    def get_url_phone_link(self):
        wait_for_element(self.driver, self.PHONE_LINK)
        return self.driver.find_element_by_css_selector(self.PHONE_LINK).get_attribute("href")  

    def load_image(self, image):
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
            self.driver.switch_to_alert()
            Alert(self.driver).dismiss()   

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

    def get_surname_message(self):
        wait_for_element_by_selector(self.driver, self.SURNAME_ERROR)
        return self.driver.find_element_by_css_selector(self.SURNAME_ERROR).text

    def get_suggests_for_town(self):
        wait_for_element_by_xpath(self.driver, self.SUGGESTS_ITEM)
        suggests = self.driver.find_elements_by_xpath(self.SUGGESTS_ITEM)
        return [suggest.text for suggest in suggests]

    def wait_for_suggests_invisible(self):
        return wait_for_element_by_xpath(self.driver, self.SUGGESTS, False)

    def wait_for_last_suggest(self, text):
        locator = f'{self.SUGGESTS_ITEM}[last()]'
        return WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, locator), text)
        )

    def get_unselected_gender(self):
        wait_for_element_by_selector(self.driver, self.GENDER_MALE)
        gender_male = self.driver.find_element_by_css_selector(self.GENDER_MALE)
        wait_for_element_by_selector(self.driver, self.GENDER_FEMALE)
        gender_female = self.driver.find_element_by_css_selector(self.GENDER_FEMALE)
        return gender_female if gender_male.is_selected() else gender_male    


