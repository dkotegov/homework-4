import os
import configparser

from pages.default_page import DefaultPage, Component
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from helpers import wait, wait_redirect, wait_for_element, wait_for_element_by_selector, wait_for_element_by_xpath


class UserinfoPage(DefaultPage):
    URL = 'https://e.mail.ru/settings/userinfo'

    @property
    def form(self):
        return UserinfoForm(self.driver)

class UserinfoForm(Component):
    config = configparser.ConfigParser()

    TOWN = 'input[name="your_town"]'
    SURNAME = 'input[name="LastName"]'            
    SAVE = 'div.form__actions__inner button[type="submit"]'
    CANCEL = 'body div.form__actions.form__actions_floating a'
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

    FIRST_NAME = '#FirstName'
    LAST_NAME = '#LastName'
    NICK_NAME = '#NickName'

    DAY_INPUT = 'select[name="BirthDay"]'
    DAY_INPUT_CHILD = 'select[name="BirthDay"] option[value="%d"]'
    MONTH_INPUT = 'select[name="BirthMonth"]'
    MONTH_INPUT_CHILD = 'select[name="BirthMonth"] option[value="%d"]'
    YEAR_INPUT = 'select[name="BirthYear"]'
    YEAR_INPUT_CHILD = 'select[name="BirthYear"] option[value="%d"]'

    DAY_VALUE = '.form__row__subwidget_short div.form__select__box'
    MONTH_VALUE = '.form__row__subwidget_large div.form__select__box__text'
    YEAR_VALUE = '.form__row__shift-small.form__row__subwidget_medium div.form__select__box__text'

    IMAGE_INPUT = 'input[name="avatar"]'
    SAVE_IMAGE_BUTTON = 'div[data-fire="save"]'

    LOGOUT_BUTTON = '#PH_logoutLink'
    HELP_BUTTON = '#settigns_toolbar__right  a.b-toolbar__btn'

    SUBMIT_BUTTON = 'div.form__actions__inner button[type="submit"]'

    OK_AFTER_SUBMIT_URI = 'https://e.mail.ru/settings?result=ok&afterReload=1'
    AFTER_LOGOUT_URI = 'https://mail.ru/?from=logout'
    LOGIN_URI = 'https://e.mail.ru/login\?.*'
    HELP_URI = 'https://help.mail.ru/mail-help/settings/userinfo'

    def set_town(self, town):
        element = wait_for_element(self.driver, self.TOWN)
        element.clear()
        element.send_keys(town)

    def save(self):
        element = wait_for_element(self.driver, self.SAVE)
        element.click()

    def cancel(self):
        CANCEL_NOT_FULL_SCREEN = '#formPersonal a.btn'
        try:
            self.driver.find_element_by_css_selector(CANCEL_NOT_FULL_SCREEN).click()
        except NoSuchElementException:
            self.driver.find_element_by_css_selector(self.CANCEL).click()

    def get_top_message(self):
        element = wait_for_element(self.driver, self.TOP_MESSAGE)
        return element.text

    def get_town_message(self):
        element = wait_for_element(self.driver, self.TOWN_ERROR)
        return element.text

    def uncheck_town(self):
        tick = wait_for_element(self.driver, self.TIMEZONE_TICK)
        if tick.is_selected():
            tick.click()

    def get_town_selector(self):
        return self.driver.find_element_by_css_selector(self.TIMEZONE_SELECTOR)

    def get_url_phone_link(self):
        element = wait_for_element(self.driver, self.PHONE_LINK)
        return element.get_attribute("href")  

    def load_image(self):
        image_path = (os.path.dirname(os.path.abspath(__file__))+'test.png').replace("pages", "")
        self.driver.find_element_by_css_selector(self.LOAD_IMAGE).send_keys(image_path)
    
    def get_save_avatar_button(self):
        return wait_for_element(self.driver, self.SAVE_AVATAR)
            
    def get_cancel_avatar_button(self):
        return wait_for_element(self.driver, self.CANCEL_AVATAR)

    def dismiss_snapshot_request(self):
        make_snapshot = self.driver.find_element_by_css_selector(self.MAKE_SNAPSHOT)
        if make_snapshot.is_enabled():    
            make_snapshot.click()
            self.driver.switch_to_alert()
            Alert(self.driver).dismiss()   

    def set_surname(self, surname):
        surname_elem = wait_for_element(self.driver, self.SURNAME)
        surname_elem.clear()
        surname_elem.send_keys(surname)        

    def get_last_name_value(self):
        return wait_for_element(self.driver, self.LAST_NAME).get_attribute("value")  

    def get_firstname_value(self):
        return wait_for_element(self.driver, self.FIRST_NAME).get_attribute("value")     

    def get_nickname_value(self):
        return wait_for_element(self.driver, self.NICK_NAME).get_attribute("value")     

    def get_last_name_message(self):
        return wait_for_element(self.driver, self.SURNAME_ERROR).text

    def clear_town(self):
        wait_for_element(self.driver, self.TOWN).clear()

    def get_surname_message(self):
        return wait_for_element_by_selector(self.driver, self.SURNAME_ERROR).text

    def get_suggests_for_town(self):
        suggests = wait_for_element_by_xpath(self.driver, self.SUGGESTS_ITEM)
        return [suggest.text for suggest in suggests]

    def get_birth_day(self):
        return wait_for_element_by_selector(self.driver, self.DAY_VALUE).text

    def get_birth_month(self):
        return wait_for_element_by_selector(self.driver, self.MONTH_VALUE).text

    def get_birth_year(self):
        return wait_for_element_by_selector(self.driver, self.YEAR_VALUE).text


    def wait_for_suggests_invisible(self):
        return wait_for_element_by_xpath(self.driver, self.SUGGESTS, False)

    def wait_for_last_suggest(self, text):
        locator = f'{self.SUGGESTS_ITEM}[last()]'
        return WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, locator), text)
        )

    def get_unselected_gender(self):
        gender_male = wait_for_element_by_selector(self.driver, self.GENDER_MALE)
        gender_female = wait_for_element_by_selector(self.driver, self.GENDER_FEMALE)
        return gender_female if gender_male.is_selected() else gender_male    

    def get_image(self):        
        self.config.read('test_data.ini')
        return self.config['DEFAULT']['ImageFile']

    def click_submit_button(self):
        self.click_element(self.SUBMIT_BUTTON, False)

    def input_firstname(self, firstName = 'test1'):
        self.clear_and_send_keys_to_input(self.FIRST_NAME, firstName, False)

    def input_lastname(self, lastName = 'test1'):
        self.clear_and_send_keys_to_input(self.LAST_NAME, lastName, False)

    def input_nickname(self, nickName = 'test1'):
        self.clear_and_send_keys_to_input(self.NICK_NAME, nickName, False)

    def wait_for_ok_after_submit(self):
        wait_redirect(self.driver, self.OK_AFTER_SUBMIT_URI)

    def input_test_image(self):
        image_path = (os.path.dirname(os.path.abspath(__file__))+'test.png').replace("pages", "")
        self.clear_and_send_keys_to_input(self.IMAGE_INPUT, image_path, False, False)


    def click_save_image_button(self):
        self.click_element(self.SAVE_IMAGE_BUTTON, True)

    def open_settings_in_new_window(self):
        self.driver.execute_script('''window.open("https://e.mail.ru/settings?result=ok&afterReload=1","_blank");''')
        self.switch_to_window(1)

    def click_logout_button(self):
        wait_for_element_by_selector(self.driver, self.LOGOUT_BUTTON)
        self.click_element(self.LOGOUT_BUTTON, False)

    def wait_for_logout(self):
        wait_redirect(self.driver, self.AFTER_LOGOUT_URI)

    def match_to_login_URI(self):
        wait(self.driver, expected_conditions.url_matches(self.LOGIN_URI))

    def click_on_day_input(self):
        self.click_element(self.DAY_INPUT, False)

    def click_on_day_child_input(self, day_num = 20):
        self.click_element(self.DAY_INPUT_CHILD % day_num, False)

    def click_on_month_input(self):
        self.click_element(self.MONTH_INPUT, False)

    def click_on_month_child_input(self, month_num = 12):
        self.click_element(self.MONTH_INPUT_CHILD % month_num, False)

    def click_on_year_input(self):
        self.click_element(self.YEAR_INPUT, False)

    def click_on_year_child_input(self, year_num = 1997):
        self.click_element(self.YEAR_INPUT_CHILD % year_num, False)

    def click_on_help(self):
        self.click_element(self.HELP_BUTTON, False)

    def wait_for_help(self):
        wait_redirect(self.driver, self.HELP_URI)
