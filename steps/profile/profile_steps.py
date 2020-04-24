from selenium.webdriver.remote.webelement import WebElement

from steps.base_steps import BaseSteps
from pages.profile.profile import ProfilePage


class ProfileSteps(BaseSteps):
    VALUE = 'value'

    NAME = 'input[id="firstname"]'
    NAME_ERROR = '[data-test-id="firstname-field-error"]'
    EMPTY_NAME_ERROR = '[data-test-id="firstname-field-error"]'

    SAVE = 'button[data-test-id="save-button"]'
    CANCEL = '[data-test-id="cancel-button"]'

    GENDER = 'label[data-test-id$="-not-checked"]'
    PERSONAL_DATA = '[data-test-id="card-footer"]'

    CITY = '[data-test-id="city-field-input"]'
    SUGGEST_ITEM = '[data-test-id="select-value:Санок, Польша"]'
    CITY_ERROR = '[data-test-id="city-field-error"]'

    BIRTH_DAY = '[data-test-id="birthday__day-value"]'
    BIRTH_MONTH = '[data-test-id="birthday__month-value"]'
    BIRTH_YEAR = '[data-test-id="birthday__year-value"]'
    BIRTH_ERROR = '[data-test-id="birthday-field-error"]'

    VALUE_DAY = '[data-test-id="select-value:3"]'
    VALUE_MONTH = '[data-test-id="select-value:7"]'
    VALUE_YEAR = '[data-test-id="select-value:2020"]'

    LEAP_DAY = '[data-test-id="select-value:29"]'
    LEAP_MONTH = '[data-test-id="select-value:2"]'
    LEAP_YEAR = '[data-test-id="select-value:2000"]'

    DAY_VALUE = '[data-test-id="birthday__day-value"]'

    PHOTO_BUTTON = '[data-test-id="upload-photo-button"]'
    PHOTO_INPUT = '[data-test-id="photo-file-input"]'
    SAVE_PHOTO = '[data-test-id="save-button"]'
    CHOOSER = '[data-test-id="crop-popup"]'

    POP_UP_ERROR_FORMAT = '[data-test-id="formatError_popup"]'
    POP_UP_ERROR_SIZE = '[data-test-id="dimensionsError_popup"]'
    CANCEL_PHOTO = '[data-test-id="cancel-button"]'
    DESCRIPTION_FORMAT_ERROR = '[data-test-id="error-description"]'
    CROSS = '[data-test-id="cross"]'

    def __init__(self, driver, page=None):
        super().__init__(driver, ProfilePage)

    def cross_pop_up(self):
        self.page.waiting_for_invisible_by_selector(self.CROSS)
        self.page.driver.find_element_by_css_selector(self.CROSS).click()

    def get_photo_format_error(self, elem):
        return elem.find_element_by_css_selector(self.DESCRIPTION_FORMAT_ERROR).text

    def photo_size_error(self):
        self.page.waiting_for_visible_by_selector(self.POP_UP_ERROR_SIZE)
        p = self.page.driver.find_element_by_css_selector(self.POP_UP_ERROR_SIZE)
        error = self.get_photo_format_error(p)
        p.find_element_by_css_selector(self.CANCEL_PHOTO).click()
        return error

    def photo_error(self):
        self.page.waiting_for_visible_by_selector(self.POP_UP_ERROR_FORMAT)
        p = self.page.driver.find_element_by_css_selector(self.POP_UP_ERROR_FORMAT)
        error = self.get_photo_format_error(p)
        p.find_element_by_css_selector(self.CANCEL_PHOTO).click()
        return error

    def upload_photo_button(self):
        self.page.waiting_for_visible_by_selector(self.PHOTO_BUTTON)

    def choose_photo(self, photo):
        self.page.driver.find_element_by_css_selector(self.PHOTO_INPUT).send_keys(photo)
        self.page.waiting_for_visible_by_selector(self.PHOTO_BUTTON)

    def save_photo(self):
        self.page.waiting_for_visible_by_selector(self.CHOOSER)
        pop = self.page.driver.find_element_by_css_selector(self.CHOOSER)
        self.page.waiting_for_visible_by_selector(self.SAVE_PHOTO)
        pop.find_element_by_css_selector(self.SAVE_PHOTO).click()

    def save(self):
        self.page.waiting_for_visible_by_selector(self.SAVE)
        self.page.driver.find_element_by_css_selector(self.SAVE).click()

    def cancel(self):
        self.page.waiting_for_visible_by_selector(self.CANCEL)
        self.page.driver.find_element_by_css_selector(self.CANCEL).click()

    def change_gender(self):
        self.page.waiting_for_visible_by_selector(self.GENDER)
        gender_before = self.page.driver.find_element_by_css_selector(self.GENDER)
        gender_before.click()
        self.save()
        gender_after = self.page.driver.find_element_by_css_selector(self.GENDER)
        return gender_before, gender_after

    def set_name(self, name):
        self.page.waiting_for_visible_by_selector(self.NAME)
        self.page.driver.find_element_by_css_selector(self.NAME).clear()
        self.page.driver.find_element_by_css_selector(self.NAME).send_keys(name)

    def set_empty_name(self):
        self.page.waiting_for_visible_by_selector(self.NAME)
        input_name = self.page.driver.find_element_by_css_selector(self.NAME)
        input_name.click()
        input_name.send_keys("sfsdf")
        input_name.clear()

    def name_error_message(self):
        self.page.waiting_for_visible_by_selector(self.NAME_ERROR)
        return self.page.driver.find_element_by_css_selector(self.NAME_ERROR).text

    def empty_name_error(self):
        self.page.waiting_for_visible_by_selector(self.EMPTY_NAME_ERROR)
        return self.page.driver.find_element_by_css_selector(self.EMPTY_NAME_ERROR).text

    def get_name(self):
        self.page.waiting_for_visible_by_selector(self.NAME)
        return self.page.driver.find_element_by_css_selector(self.NAME).get_attribute(self.VALUE)

    def personal(self):
        self.page.waiting_for_visible_by_selector(self.PERSONAL_DATA)
        self.page.driver.find_element_by_css_selector(self.PERSONAL_DATA).click()

    def set_city(self, town):
        self.page.waiting_for_visible_by_selector(self.CITY)
        self.page.driver.find_element_by_css_selector(self.CITY).clear()
        self.page.driver.find_element_by_css_selector(self.CITY).send_keys(town)

    def suggest_city(self):
        self.page.waiting_for_visible_by_selector(self.SUGGEST_ITEM)
        self.page.driver.find_element_by_css_selector(self.SUGGEST_ITEM).click()

    def get_city(self):
        self.page.waiting_for_visible_by_selector(self.CITY)
        return self.page.driver.find_element_by_css_selector(self.CITY).get_attribute(self.VALUE)

    def city_error(self):
        self.page.waiting_for_visible_by_selector(self.CITY_ERROR)
        return self.page.driver.find_element_by_css_selector(self.CITY_ERROR).text

    def future_burthday(self):
        self.page.waiting_for_visible_by_selector(self.BIRTH_DAY)
        self.page.waiting_for_visible_by_selector(self.BIRTH_MONTH)
        self.page.waiting_for_visible_by_selector(self.BIRTH_YEAR)

        self.page.driver.find_element_by_css_selector(self.BIRTH_DAY).click()
        self.page.waiting_for_visible_by_selector(self.VALUE_DAY)
        self.page.driver.find_element_by_css_selector(self.VALUE_DAY).click()

        self.page.driver.find_element_by_css_selector(self.BIRTH_MONTH).click()
        self.page.waiting_for_visible_by_selector(self.VALUE_MONTH)
        self.page.driver.find_element_by_css_selector(self.VALUE_MONTH).click()

        self.page.driver.find_element_by_css_selector(self.BIRTH_YEAR).click()
        self.page.waiting_for_visible_by_selector(self.VALUE_YEAR)
        self.page.driver.find_element_by_css_selector(self.VALUE_YEAR).click()

    def birth_error(self):
        self.page.waiting_for_visible_by_selector(self.BIRTH_ERROR)
        return self.page.driver.find_element_by_css_selector(self.BIRTH_ERROR).text

    def set_birthday(self):
        self.page.waiting_for_visible_by_selector(self.BIRTH_DAY)
        self.page.waiting_for_visible_by_selector(self.BIRTH_MONTH)
        self.page.waiting_for_visible_by_selector(self.BIRTH_YEAR)

        self.page.driver.find_element_by_css_selector(self.BIRTH_YEAR).click()
        self.page.waiting_for_visible_by_selector(self.LEAP_YEAR)
        self.page.driver.find_element_by_css_selector(self.LEAP_YEAR).click()

        self.page.driver.find_element_by_css_selector(self.BIRTH_DAY).click()
        self.page.waiting_for_visible_by_selector(self.LEAP_DAY)
        self.page.driver.find_element_by_css_selector(self.LEAP_DAY).click()

        self.page.driver.find_element_by_css_selector(self.BIRTH_MONTH).click()
        self.page.waiting_for_visible_by_selector(self.LEAP_MONTH)
        self.page.driver.find_element_by_css_selector(self.LEAP_MONTH).click()

    def get_day(self):
        self.page.waiting_for_visible_by_selector(self.DAY_VALUE)
        return self.page.driver.find_element_by_css_selector(self.DAY_VALUE).text
