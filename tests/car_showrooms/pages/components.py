# -*- coding: utf-8 -*-
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AddShowroomForm(Component):
    TITLE = u'ДОБАВИТЬ АВТОСАЛОН'

    __OPEN_BUTTON = 'button.button.button_wide.button_type-1.js-show_form'
    __FORM_TITLE = 'div.box__title'
    __FIO_EDIT = 'manager_fio'
    __PHONE_EDIT = '//input[@name="manager_phone"]/..' \
                   '//input[@class="input__data__value js-phone__number js-phone__part"]'
    __EMAIL_EDIT = 'manager_email'
    __NAME_EDIT = 'name'
    __ADDRESS_EDIT = 'address_salon'
    __SHOWROOM_PHONE1_EDIT = '//input[@name="phone1"]/..' \
                             '//input[@class="input__data__value js-phone__number js-phone__part"]'
    __SHOWROOM_EMAIL_EDIT = 'email_salon'
    __SHOWROOM_SITE_EDIT = 'url_salon'
    __SUBMIT_BUTTON = '//span[@class="button__text" and text()="Отправить заявку"]'
    __SUBMIT_OK_TITLE = '//div[@class="box__title" and text()="Ваша заявка отправлена"]'

    def open_form(self):
        self.driver.find_element_by_css_selector(self.__OPEN_BUTTON).click()

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.__FORM_TITLE))
        )

    def set_required_fields(self, fio, phone, email, name, address, showroom_phone):
        self.set_fio(fio)
        self.set_phone(phone)
        self.set_email(email)
        self.set_name(name)
        self.set_address(address)
        self.set_showroom_phone(showroom_phone)

    def get_title(self):
        return self.driver.find_element_by_css_selector(self.__FORM_TITLE).text

    def set_fio(self, fio):
        fio_edit = self.driver.find_element_by_name(self.__FIO_EDIT)
        fio_edit.clear()
        fio_edit.send_keys(fio)

    def __get_phone_edit_element(self):
        return self.driver.find_element_by_xpath(self.__PHONE_EDIT)

    def set_phone(self, phone):
        phone_edit = self.__get_phone_edit_element()
        phone_edit.clear()
        phone_edit.send_keys(phone)

    def is_phone_valid(self):
        parent = self.__get_phone_edit_element().find_element_by_xpath('../../../../..')
        return 'invalid' not in parent.get_attribute('class')

    def set_email(self, email):
        email_edit = self.driver.find_element_by_name(self.__EMAIL_EDIT)
        email_edit.clear()
        email_edit.send_keys(email)

    def is_email_valid(self):
        parent = self.driver.find_element_by_name(self.__EMAIL_EDIT).find_element_by_xpath('../../..')
        return 'invalid' not in parent.get_attribute('class')

    def set_name(self, name):
        name_edit = self.driver.find_element_by_name(self.__NAME_EDIT)
        name_edit.clear()
        name_edit.send_keys(name)

    def set_address(self, address):
        address_edit = self.driver.find_element_by_name(self.__ADDRESS_EDIT)
        address_edit.clear()
        address_edit.send_keys(address)

    def __get_showroom_phone_edit_element(self):
        return self.driver.find_element_by_xpath(self.__SHOWROOM_PHONE1_EDIT)

    def set_showroom_phone(self, phone):
        phone_edit = self.__get_showroom_phone_edit_element()
        phone_edit.clear()
        phone_edit.send_keys(phone)

    def is_showroom_phone_valid(self):
        parent = self.__get_showroom_phone_edit_element().find_element_by_xpath('../../../../..')
        return 'invalid' not in parent.get_attribute('class')

    def set_showroom_email(self, email):
        email_edit = self.driver.find_element_by_name(self.__SHOWROOM_EMAIL_EDIT)
        email_edit.clear()
        email_edit.send_keys(email)

    def is_showroom_email_valid(self):
        parent = self.driver.find_element_by_name(self.__SHOWROOM_EMAIL_EDIT).find_element_by_xpath('../../..')
        return 'invalid' not in parent.get_attribute('class')

    def set_showroom_site(self, site):
        site_edit = self.driver.find_element_by_name(self.__SHOWROOM_SITE_EDIT)
        site_edit.clear()
        site_edit.send_keys(site)

    def is_showroom_site_valid(self):
        parent = self.driver.find_element_by_name(self.__SHOWROOM_SITE_EDIT).find_element_by_xpath('../../..')
        return 'invalid' not in parent.get_attribute('class')

    def submit(self):
        self.driver.find_element_by_xpath(self.__SUBMIT_BUTTON).click()

    def is_correct_submit(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.__SUBMIT_OK_TITLE))
        )
        return True


class ShowroomList(Component):
    __PAGE_TITLE = '//h1[@class="page__title"]'
    __ITEM = '//div[contains(@class, "dealer-card_lst") or contains(@class, "dealer-card clear")]'
    __ITEM_TITLE = 'div.dealer-card__title a'
    __ITEM_PAGE_TITLE = 'span.bread__curr'
    __ITEM_ADDRESS = 'div.dealer-card__adress'
    __ITEM_PHONE = 'div.dealer-card__phone'
    __PAGINATOR_CURRENT_PARAM = "a.pager__pin.pager__pin_perpage.pager__pin_on"
    __PAGINATOR_PARAM = "a.pager__pin.pager__pin_perpage"
    __DEALER_MODEL_ICON = '//img[@alt and @title and @class="dealer-card__aside__item"]'
    __DEALER_MODEL_ICON_FOR_MODEL_FORMAT = '//img[@alt="{0}" and @title="{0}" and @class="dealer-card__aside__item"]'
    __DEALER_CARD_METRO_STATION = '//span[@class="dealer-card__metro__item"]'
    __EMPTY_LIST_MESSAGE = '//div[@class="empty"]'

    def get_item_titles(self):
        item_titles = []
        item_pages_title = []

        items_count = self.get_items_count()
        items_ids = [0, items_count / 2, items_count - 1]
        for item_id in items_ids:
            item = self.driver.find_elements_by_css_selector(self.__ITEM_TITLE)[item_id]

            item_titles.append(item.text)
            item.click()
            item_pages_title.append(self.get_item_page_title())
            self.driver.back()

        return item_titles, item_pages_title

    def get_item_page_title(self):
        return self.driver.find_element_by_css_selector(self.__ITEM_PAGE_TITLE).text

    def get_items_addresses(self):
        addresses = []
        for address in self.driver.find_elements_by_css_selector(self.__ITEM_ADDRESS):
            addresses.append(address.text)
        return addresses

    def get_items_phones(self):
        phones = []
        for phone in self.driver.find_elements_by_css_selector(self.__ITEM_PHONE):
            phones.append(phone.text)
        return phones

    def get_items_count(self):
        return len(self.driver.find_elements_by_xpath(self.__ITEM))

    def set_pagination_count_params(self, count):
        for param in self.driver.find_elements_by_css_selector(self.__PAGINATOR_PARAM):
            if int(param.text) == count:
                param.click()
                return

    def get_pagination_count_current_param(self):
        return int(self.driver.find_element_by_css_selector(self.__PAGINATOR_CURRENT_PARAM).text)

    def get_items_official_dealers_by_model(self, model):
        return self.driver.find_elements_by_xpath(self.__DEALER_MODEL_ICON_FOR_MODEL_FORMAT.format(model))

    def get_items_metro_stations(self):
        return [item.text for item in self.driver.find_elements_by_xpath(self.__DEALER_CARD_METRO_STATION)]

    def is_list_empty(self):
        try:
            empty_message = self.driver.find_elements_by_xpath(self.__EMPTY_LIST_MESSAGE)
            return True
        except NoSuchElementException:
            return False

    def get_items_official_dealers(self):
        official_items = []
        items = self.driver.find_elements_by_xpath(self.__ITEM)
        for item in items:
            dealer_model_icons = []
            try:
                dealer_model_icons = item.find_elements_by_xpath(self.__DEALER_MODEL_ICON)
            except NoSuchElementException:
                pass

            if len(dealer_model_icons) > 0:
                official_items.append(item)

        return

    def get_page_title(self):
        return self.driver.find_element_by_xpath(self.__PAGE_TITLE).text


class SpecialOffersList(Component):
    __ITEM_TITLE = 'span.offer-mini__title'
    __ITEM_PAGE_TITLE = 'h1.car__title__text'
    __ITEM_YEAR = 'span.offer-mini__info'
    __ITEM_PRICE = 'span.offer-mini__price__box'

    def get_item_titles(self):
        return [item.text for item in self.driver.find_elements_by_css_selector(self.__ITEM_TITLE)]

    def get_item_titles_with_page_titles(self):
        item_titles = []
        item_pages_title = []

        items_count = self.get_items_count()
        items_ids = [0, items_count / 2, items_count - 1]
        for item_id in items_ids:
            item = self.driver.find_elements_by_css_selector(self.__ITEM_TITLE)[item_id]

            item_titles.append(item.text)
            item.click()
            item_pages_title.append(self.get_item_page_title())
            self.driver.back()

        return item_titles, item_pages_title

    def get_item_page_title(self):
        return self.driver.find_element_by_css_selector(self.__ITEM_PAGE_TITLE).text

    def get_items_years(self):
        years = []
        for year in self.driver.find_elements_by_css_selector(self.__ITEM_YEAR):
            years.append(year.text)
        return years

    def get_items_prices(self):
        prices = []
        for price in self.driver.find_elements_by_css_selector(self.__ITEM_PRICE):
            prices.append(price)
        return prices

    def get_items_count(self):
        return len(self.driver.find_elements_by_css_selector(self.__ITEM_TITLE))


class RegionSelectionForm(Component):
    TITLE = '//div[text()="Выбор региона"]'
    COUNTRY = u'//span[@class="tab__pin__text" and text()="{}"]'
    REGION_INPUT = '//input[@placeholder="Введите название города или региона"]'
    SUBMIT_BUTTON = '//span[@class="button__text" and text()="Выбрать"]'
    OPEN_FORM_BUTTON = '//span[contains(@class, "js-geo_name")]'
    FOUNDED_REGIONS = '//div[@class="input__box input__box_dropdown"]/div/div[@data-val]'
    CANCEL_BUTTON = '//span[@class="button__text" and text()="Отменить"]'

    def open_form(self):
        self.driver.find_element_by_xpath(self.OPEN_FORM_BUTTON).click()
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.TITLE))
        )
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.REGION_INPUT))
        )

    def set_country(self, country):
        self.driver.find_element_by_xpath(self.COUNTRY.format(country)).click()
        WebDriverWait(self.driver, 30).until(
            lambda d: regions_search_done(d)
        )

    def set_region(self, region):
        self.driver.find_element_by_xpath(self.REGION_INPUT).send_keys(region)
        WebDriverWait(self.driver, 30).until(
            lambda d: regions_search_done(d)
        )

    def get_founded_regions(self):
        regions = []
        for region in self.driver.find_elements_by_xpath(self.FOUNDED_REGIONS):
            self.driver.execute_script("return arguments[0].scrollIntoView();", region)
            regions.append(region.text)
        return list(regions)

    def submit(self):
        self.select_first_region()
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.OPEN_FORM_BUTTON))
        )

    def select_first_region(self):
        self.driver.find_element_by_xpath(self.FOUNDED_REGIONS).click()

    def cancel(self):
        self.driver.find_element_by_xpath(self.CANCEL_BUTTON).click()

    def current_region(self):
        return self.driver.find_element_by_xpath(RegionSelectionForm.OPEN_FORM_BUTTON).text


def regions_search_done(driver):
    try:
        founded_elements = driver.find_elements_by_xpath(RegionSelectionForm.FOUNDED_REGIONS)
        var = list(e.text for e in founded_elements)
        return True
    except StaleElementReferenceException:
        return False


class SearchForm(Component):
    MODEL_DROPDOWN = '//div[contains(@class, "selt-firm_id")]/div/div/div[contains(@class, "js-select__selected__option")]'
    MODEL_DROPDOWN_ITEMS = '//div[@data-optidx and contains(@class, "js-select__options__item input__data__value_in-group")]'
    MODEL_DROPDOWN_ITEM_BY_NAME = '//div[@data-optidx and contains(@class, "js-select__options__item input__data__value_in-group") and text()="{}"]'
    STATION_DROPDOWN = '//div[contains(@class, "selt-subway_id")]/div/div/div[contains(@class, "js-select__selected__option")]'
    STATION_DROPDOWN_ITEMS = '//div[@data-optidx and contains(@class, "subway")]'
    STATION_DROPDOWN_ITEM_BY_NAME = u'//div[@data-optidx and contains(@class, "subway") and text()="{}"]'
    CHECKBOX_SHOWROOM_IS_OFFICIAL = '//span[@class="input-flag__text" and text()="Официальный дилер"]'
    SUBMIT = '//span[text()="Найти"]/../..'
    TOOLTIP = '//div[@class="tooltip js-tooltip tooltip_left tooltip_lower"]'
    FORM = '//form[@id="search_dealers_form"]'

    @property
    def region_selection_form(self):
        return RegionSelectionForm(self.driver)

    def model_dropdown_drop(self):
        self.driver.find_element_by_xpath(self.MODEL_DROPDOWN).click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.MODEL_DROPDOWN_ITEMS))
        )

    def model_dropdown_items(self):
        models = []
        for model in self.driver.find_elements_by_xpath(self.MODEL_DROPDOWN_ITEMS):
            self.driver.execute_script("return arguments[0].scrollIntoView();", model)
            models.append(model.text)
        return list(models)

    def model_dropdown_item_select(self, model):
        item = self.driver.find_element_by_xpath(self.MODEL_DROPDOWN_ITEM_BY_NAME.format(model))
        self.driver.execute_script("return arguments[0].scrollIntoView();", item)
        item.click()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.MODEL_DROPDOWN)).perform()

    def station_dropdown_drop(self):
        self.driver.find_element_by_xpath(self.STATION_DROPDOWN).click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.STATION_DROPDOWN_ITEMS))
        )

    def station_dropdown_items(self):
        stations = []
        for station in self.driver.find_elements_by_xpath(self.STATION_DROPDOWN_ITEMS):
            self.driver.execute_script("return arguments[0].scrollIntoView();", station)
            stations.append(station.text)
        return list(stations)

    def station_dropdown_item_select(self, station):
        item = self.driver.find_element_by_xpath(self.STATION_DROPDOWN_ITEM_BY_NAME.format(station))
        self.driver.execute_script("return arguments[0].scrollIntoView();", item)
        item.click()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.MODEL_DROPDOWN)).perform()

    def is_official_checkbox_click(self):
        self.driver.find_element_by_xpath(self.CHECKBOX_SHOWROOM_IS_OFFICIAL).click()
        WebDriverWait(self.driver, 30).until(
            lambda d: wait_for_is_official_checkbox_apply(d)
        )

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


def wait_for_is_official_checkbox_apply(driver):
    submit_button = driver.find_element_by_xpath(SearchForm.SUBMIT)
    button_href = submit_button.get_attribute("href")

    form = driver.find_element_by_xpath(SearchForm.FORM)
    form_href = form.get_attribute("href")
    if form_href is None:
        return False

    if "is_official=on" in button_href and "is_official=on" in form_href:
        return True
    else:
        return False
