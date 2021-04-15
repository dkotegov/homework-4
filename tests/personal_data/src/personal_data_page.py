from selenium.webdriver.support.ui import WebDriverWait
from tests.personal_data.page_component import Page, Component
from selenium.common.exceptions import StaleElementReferenceException


class PersonalDataForm(Component):
    FIRSTNAME_FIELD = '//*[@data-test-id="firstname-field-input"]'
    LASTNAME_FIELD = '//*[@data-test-id="lastname-field-input"]'
    NICKNAME_FIELD = '//*[@data-test-id="nickname-field-input"]'
    MONTH_MENU = '//*[@data-test-id="birthday__month"]'
    DAY_MENU = '//*[@data-test-id="birthday__day"]'
    YEAR_MENU = '//*[@data-test-id="birthday__year"]'
    SUBMIT_BUTTON = '//*[@data-test-id="save-button"]'
    ERROR_TEXT = '//*[@data-test-id="error-footer-text"]'
    AVATAR = '//*[@data-test-id="photo-file-input"]'
    ERROR_AVATAR = '//*[@data-test-id="error-caption"]'
    SAVE_AVATAR = '//*[@data-test-id="save-button"]'
    CITY_FIELD = '//*[@data-test-id="city-field-input"]'

    def submit(self):
        submit_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT_BUTTON)
        )

        submit_button.click()

    def check_error(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ERROR_TEXT)
        )

    def edit_firstname(self, firstname):
        input_firstname = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FIRSTNAME_FIELD)
        )
        input_firstname.send_keys(firstname)

    def edit_lastname(self, lastname):
        input_lastname = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LASTNAME_FIELD)
        )
        input_lastname.send_keys(lastname)

    def edit_nickname(self, nickname):
        input_nickname = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NICKNAME_FIELD)
        )
        input_nickname.send_keys(nickname)

    def edit_date(self, day, month, year):
        self.edit_day(day)
        self.edit_month(month)
        self.edit_year(year)

    def edit_day(self, day):
        day_input = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DAY_MENU)
        )
        day_input.click()

        day_selector = '//*[@data-test-id="select-value:' + str(day) + '"]'
        selected_day = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DAY_MENU + day_selector)
        )

        selected_day.click()

    def edit_month(self, month):
        month_input = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MONTH_MENU)
        )
        month_input.click()

        month_selector = '//*[@data-test-id="select-value:' + str(month) + '"]'
        selected_month = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MONTH_MENU + month_selector)
        )
        selected_month.click()

    def edit_year(self, year):
        year_input = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.YEAR_MENU)
        )
        year_input.click()

        year_selector = '//*[@data-test-id="select-value:' + str(year) + '"]'
        selected_year = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.YEAR_MENU + year_selector)
        )
        selected_year.click()

    def load_avatar(self, path):
        avatar_input = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.AVATAR)
        )
        avatar_input.send_keys(path)

    def check_avatar_error(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ERROR_AVATAR)
        )

    def save_avatar(self):
        save_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SAVE_AVATAR)
        )
        save_button.submit()

    def edit_city(self, city):
        input_city = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CITY_FIELD)
        )
        input_city.clear()
        input_city.send_keys(city[:1])

        try:
            selected_value = WebDriverWait(self.driver, 30, 0.1, ignored_exceptions=StaleElementReferenceException).until(
                lambda d: d.find_element_by_xpath('//*[@data-test-id="select-value:' + str(city) + '"]')
            )
            selected_value.click()
        except:
            input_city.send_keys(city)



class PersonalDataPage(Page):
    PATH = '/profile'

    @property
    def form(self):
        return PersonalDataForm(self.driver)
