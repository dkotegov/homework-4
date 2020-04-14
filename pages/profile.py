from selenium.webdriver.support.ui import Select

from pages.default import DefaultPage, DefaultSteps


class ProfilePage(DefaultPage):

    @property
    def steps(self):
        return ProfileSteps(self.driver)


class ProfileSteps(DefaultSteps):
    CITY = '[data-test-id="city-field-input"]'
    NAME = 'input[id="firstname"]'
    SAVE = 'button[data-test-id="save-button"]'
    CANCEL = '[data-test-id="cancel-button"]'
    NAME_ERROR = '[data-test-id="firstname-field-error"]'
    GENDER = 'label[data-test-id$="-not-checked"]'
    EMPTY_NAME_ERROR = '[data-test-id="firstname-field-error"]'
    PERSONAL_DATA = '[data-test-id="card-footer"]'
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


    def save(self):
        self.waiting_for_visible(self.SAVE)
        self.driver.find_element_by_css_selector(self.SAVE).click()

    def cancel(self):
        self.waiting_for_visible(self.CANCEL)
        self.driver.find_element_by_css_selector(self.CANCEL).click()

    def change_gender(self):
        self.waiting_for_visible(self.GENDER)
        gender_before = self.driver.find_element_by_css_selector(self.GENDER)
        gender_before.click()
        self.save()
        gender_after = self.driver.find_element_by_css_selector(self.GENDER)
        return gender_before, gender_after

    def set_name(self, name):
        self.waiting_for_visible(self.NAME)
        self.driver.find_element_by_css_selector(self.NAME).clear()
        self.driver.find_element_by_css_selector(self.NAME).send_keys(name)

    def name_error_message(self):
        self.waiting_for_visible(self.NAME_ERROR)
        return self.driver.find_element_by_css_selector(self.NAME_ERROR).text

    def empty_name_error(self):
        self.waiting_for_visible(self.EMPTY_NAME_ERROR)
        return self.driver.find_element_by_css_selector(self.EMPTY_NAME_ERROR).text

    def get_name(self):
        self.waiting_for_visible(self.NAME)
        return self.driver.find_element_by_css_selector(self.NAME).get_attribute('value')

    def personal(self):
        self.waiting_for_visible(self.PERSONAL_DATA)
        self.driver.find_element_by_css_selector(self.PERSONAL_DATA).click()

    def set_city(self, town):
        self.waiting_for_visible(self.CITY)
        self.driver.find_element_by_css_selector(self.CITY).clear()
        self.driver.find_element_by_css_selector(self.CITY).send_keys(town)

    def suggest_city(self):
        self.waiting_for_visible(self.SUGGEST_ITEM)
        self.driver.find_element_by_css_selector(self.SUGGEST_ITEM).click()

    def get_city(self):
        self.waiting_for_visible(self.CITY)
        return self.driver.find_element_by_css_selector(self.CITY).get_attribute('value')

    def city_error(self):
        self.waiting_for_visible(self.CITY_ERROR)
        return self.driver.find_element_by_css_selector(self.CITY_ERROR).text

    def future_burthday(self):
        self.waiting_for_visible(self.BIRTH_DAY)
        self.waiting_for_visible(self.BIRTH_MONTH)
        self.waiting_for_visible(self.BIRTH_YEAR)

        self.driver.find_element_by_css_selector(self.BIRTH_DAY).click()
        self.waiting_for_visible(self.VALUE_DAY)
        self.driver.find_element_by_css_selector(self.VALUE_DAY).click()

        self.driver.find_element_by_css_selector(self.BIRTH_MONTH).click()
        self.waiting_for_visible(self.VALUE_MONTH)
        self.driver.find_element_by_css_selector(self.VALUE_MONTH).click()

        self.driver.find_element_by_css_selector(self.BIRTH_YEAR).click()
        self.waiting_for_visible(self.VALUE_YEAR)
        self.driver.find_element_by_css_selector(self.VALUE_YEAR).click()


    def birth_error(self):
        self.waiting_for_visible(self.BIRTH_ERROR)
        return self.driver.find_element_by_css_selector(self.BIRTH_ERROR).text

    def set_birthday(self):
        self.waiting_for_visible(self.BIRTH_DAY)
        self.waiting_for_visible(self.BIRTH_MONTH)
        self.waiting_for_visible(self.BIRTH_YEAR)

        self.driver.find_element_by_css_selector(self.BIRTH_YEAR).click()
        self.waiting_for_visible(self.LEAP_YEAR)
        self.driver.find_element_by_css_selector(self.LEAP_YEAR).click()

        self.driver.find_element_by_css_selector(self.BIRTH_DAY).click()
        self.waiting_for_visible(self.LEAP_DAY)
        self.driver.find_element_by_css_selector(self.LEAP_DAY).click()

        self.driver.find_element_by_css_selector(self.BIRTH_MONTH).click()
        self.waiting_for_visible(self.LEAP_MONTH)
        self.driver.find_element_by_css_selector(self.LEAP_MONTH).click()

    def get_day(self):
        self.waiting_for_visible(self.DAY_VALUE)
        return self.driver.find_element_by_css_selector(self.DAY_VALUE).text







