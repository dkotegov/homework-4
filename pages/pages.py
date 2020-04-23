import urllib.parse as urlparse

from selenium.webdriver import ActionChains

from utils.wait import Waiter


class Page(object):
    BASE_URL = 'https://comandus.now.sh/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class AuthPage(Page):
    PATH = '/login'

    @property
    def form(self):
        return AuthForm(self.driver)


class CreateJobPage(Page):
    PATH = '/new-job'
    CREATE_BTN = '//a[@data-test-id="top-new-job"]'

    @property
    def form(self):
        return JobForm(self.driver)

    def open_form(self):
        Waiter.wait_by_xpath(self.driver, self.CREATE_BTN).click()


class JobListPage(Page):
    PATH = '/my-job-postings'

    @property
    def item(self):
        return JobListItem(self.driver)


class JobPage(Page):
    TITLE = '//h2[@data-test-id="job-page-title"]'
    EDIT = '//a[@data-test-id="job-page-edit"]'
    TOGGLE_PUBLISH = '//button[@data-test-id="job-page-toggle-pub"]'

    def get_job_title(self, title):
        return Waiter.wait_by_xpath(self.driver, self.TITLE+'[text()="'+title+'"]').text

    def get_toggle_text(self):
        return Waiter.wait_by_xpath(self.driver, self.TOGGLE_PUBLISH).text

    def toggle_publish(self):
        Waiter.wait_by_xpath(self.driver, self.TOGGLE_PUBLISH).click()

    def check_toggle(self, text):
        Waiter.wait_by_xpath(self.driver, self.TOGGLE_PUBLISH + '[text()="'+text+'"]')

    def open_edit_form(self):
        Waiter.wait_by_xpath(self.driver, self.EDIT).click()

    @property
    def form(self):
        return JobForm(self.driver)


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '//input[@name="email"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//button[@data-test-id="login_submit_btn"]'
    LOGIN_BUTTON = '//a[@data-test-id="top_login_btn"]'

    def open_form(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class JobForm(Component):
    TITLE = '//input[@name="title"]'
    DESCRIPTION = '//textarea[@name="description"]'
    BUDGET = '//input[@name="paymentAmount"]'
    TAGS = '//input[@data-test-id="job-form-tags"]'
    selectCategory = '//div[@data-test-id="job-form-category-select"]//div[@class="select-custom__header"]'
    selectSpec = '//div[@data-test-id="job-form-spec-select"]//div[@class="select-custom__header"]'
    selectCountry = '//div[@data-test-id="job-form-country-select"]//div[@class="select-custom__header"]'
    selectCity = '//div[@data-test-id="job-form-city-select"]//div[@class="select-custom__header"]'
    catItem = '//div[@data-test-id="job-form-category-select"]//div[@class="select-custom__dropdown"]/ul/li[1]'
    specItem = '//div[@data-test-id="job-form-spec-select"]//div[@class="select-custom__dropdown"]/ul/li[1]'
    countryItem = '//div[@data-test-id="job-form-country-select"]//div[@class="select-custom__dropdown"]/ul/li[1]'
    cityItem = '//div[@data-test-id="job-form-city-select"]//div[@class="select-custom__dropdown"]/ul/li[1]'
    selectFirstItem = '//li[@data-val="0"]'
    LEVEL_RADIO = '//span[@data-test-id="radio-label-3"]'
    SUBMIT = '//button[@data-test-id="job-form-submit"]'
    TYPE_RADIO = '//span[@data-test-id="radio-label-0"]'
    BUDGET_ERROR = '//span[@data-test-id="budget-error"]'
    HIDDEN_TAG_INPUT = '//input[@name="tagLine"]'
    TITLE_ERROR = '//span[@data-test-id="job-form-title-error"]'
    HEADER_TEXT = '//h1[@data-test-id="job-form-header"]'

    def set_type(self):
        Waiter.wait_by_xpath(self.driver, self.TYPE_RADIO).click()

    def set_title(self, title):
        Waiter.wait_by_xpath(self.driver, self.TITLE).clear()
        Waiter.wait_by_xpath(self.driver, self.TITLE).send_keys(title)
        Waiter.wait_by_xpath(self.driver, '//h1').click()

    def set_description(self, description):
        Waiter.wait_by_xpath(self.driver, self.DESCRIPTION).send_keys(description)
        Waiter.wait_by_xpath(self.driver, '//h1').click()

    def set_category(self):
        Waiter.wait_by_xpath(self.driver, self.selectCategory)
        Waiter.wait_clickable_by_xpath(self.driver, self.selectCategory).click()
        Waiter.wait_by_xpath(self.driver, self.catItem)
        element = Waiter.wait_clickable_by_xpath(self.driver, self.catItem)
        element.click()

    def set_spec(self):
        Waiter.wait_by_xpath(self.driver, self.selectSpec)
        Waiter.wait_clickable_by_xpath(self.driver, self.selectSpec).click()
        element = Waiter.wait_clickable_by_xpath(self.driver, self.specItem)
        element.click()

    def set_tag(self, tag):
        self.driver.find_element_by_xpath(self.TAGS).send_keys(tag)
        self.driver.find_element_by_xpath(self.TAGS).send_keys('\uE007')

    def set_budget(self, budget_amount):
        self.driver.find_element_by_xpath(self.BUDGET).send_keys(budget_amount)

    def set_country(self):
        Waiter.wait_by_xpath(self.driver, self.selectCountry)
        self.driver.find_element_by_xpath(self.selectCountry).click()
        Waiter.wait_by_xpath(self.driver, self.catItem)
        element = Waiter.wait_clickable_by_xpath(self.driver, self.countryItem)
        element.click()

    def set_city(self):
        Waiter.wait_by_xpath(self.driver, self.selectCity)
        Waiter.wait_clickable_by_xpath(self.driver, self.selectCity).click()
        element = Waiter.wait_clickable_by_xpath(self.driver, self.cityItem)
        element.click()

    def set_level(self):
        self.driver.find_element_by_xpath(self.LEVEL_RADIO).click()

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def get_budget_error(self):
        return Waiter.wait_by_xpath(self.driver, self.BUDGET_ERROR).text

    def get_form_tags(self):
        return Waiter.wait_by_xpath(self.driver, self.HIDDEN_TAG_INPUT).get_attribute("value")

    def get_title_error(self):
        return Waiter.wait_by_xpath(self.driver, self.TITLE_ERROR).text

    def get_header(self, text):
        return Waiter.wait_by_xpath(self.driver, self.HEADER_TEXT + '[text()="' + text + '"]').text


class JobListItem(Component):
    ITEM = '//section[@class="item router-link"][1]'
    BTN_DELETE = '//section[@class="item router-link"][1]//button[@class="delete-job-action manage-btn"][1]'
    MODAL_WINDOW = '//*[@data-test-id="approve-delete-dialog"]'
    BTN_APPROVE = '//*[@data-test-id="approve-delete-button"]'
    TOGGLE_PUBLISH = '//section[@class="item router-link"][1]//button[@data-test-id="toggle-publish"]'

    def delete(self):
        item = Waiter.wait_by_xpath(self.driver,self.ITEM)

        hover = ActionChains(self.driver).move_to_element(item)
        hover.perform()

        Waiter.wait_by_xpath(self.driver, self.BTN_DELETE).click()
        Waiter.wait_by_xpath(self.driver, self.MODAL_WINDOW)
        Waiter.wait_by_xpath(self.driver, self.BTN_APPROVE).click()

        Waiter.wait_by_xpath(self.driver, self.ITEM)

    def get_toggle_text(self):
        item = Waiter.wait_by_xpath(self.driver, self.ITEM)

        hover = ActionChains(self.driver).move_to_element(item)
        hover.perform()

        return Waiter.wait_by_xpath(self.driver, self.TOGGLE_PUBLISH).text

    def toggle_publish(self):
        item = Waiter.wait_by_xpath(self.driver, self.ITEM)

        hover = ActionChains(self.driver).move_to_element(item)
        hover.perform()

        Waiter.wait_by_xpath(self.driver, self.TOGGLE_PUBLISH).click()

    def check_toggle(self, text):
        item = Waiter.wait_by_xpath(self.driver, self.ITEM)

        hover = ActionChains(self.driver).move_to_element(item)
        hover.perform()

        Waiter.wait_by_xpath(self.driver, self.TOGGLE_PUBLISH + '[text()="'+text+'"]')








