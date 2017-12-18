# -*- coding: utf-8 -*-

import urlparse

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Page:
    BASE_URL = 'https://ok.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class AuthForm:
    LOGIN = '//input[@id="field_email"]'
    PASSWORD = '//input[@id="field_password"]'
    LOGIN_BUTTON = '//input[@class="button-pro __wide"]'

    def __init__(self, driver):
        self.driver = driver

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()


class AuthPage(Page):
    def login(self):
        # user_login = os.environ['LOGIN']
        # user_password = os.environ['PASSWORD']

        user_login = 'technopark6'
        user_password = 'testQA1'
        auth_form = AuthForm(self.driver)#self.form
        auth_form.set_login(user_login)
        auth_form.set_password(user_password)
        auth_form.submit()


class MainPage(Page):
    SEARCH = 'field_query'
    SEARCH_SUGGESTIONS_SHOWALL_LINK = '//div[@id="toolbar_search"]//div[@class="search_suggest_show-all"]'
    SEARCH_BTN = 'lsBtn'
    SEARCH_RESULTS = 'searchResults'

    def search(self, request):
        self.driver.find_element_by_id(self.SEARCH).send_keys(request)

    def get_search_suggestions_showall_text(self):
        return self.driver.find_element_by_xpath(self.SEARCH_SUGGESTIONS_SHOWALL_LINK).text

    def submit_search(self):
        self.driver.find_element_by_id(self.SEARCH_BTN).click()


class PhotoPage(Page):
    CREATE_NEW_ALBUM = '//div[@class="portlet_h_inf"]/a[1]'
    NEW_ALBUM_MENU = '//div[@id="hook_Block_PopLayer"]'
    PHOTO_ALBUMS_HEADER = '.photo-stream .photo-sc_w .portlet_h.__photo'
    ALBUM_NAME_HEADER = '.photo-h'
    NEW_ALBUM_NAME = '//div[@class="it_w"]/input'
    ALBUM_EDIT = '//div[@class="photo-menu_edit iblock-cloud_show"]/a[1]'
    ALBUM_NAME_EDIT = '//div[@class="photo-panel_cover"]'
    REMOVE_ALBUM = '//div[@class="photo-panel __shift"]/div/div[2]/ul/li[2]/a'
    ALBUM_DELETE_CONFIRM_TABLE = 'table.mw_tbl'
    ALBUM_DELETE_BUTTON = '//input[@id="hook_FormButton_button_delete_confirm"]'
    UPLOAD_PHOTO = '//input[@class="html5-upload-link __before-upload"]'
    NEW_PICTURE_CREATED_CSS = '.input-l'
    REMOVE_PICTURE = '//a[@class="photo-widget __del"]'

    def remove_picture(self):
        self.driver.find_element_by_xpath(self.REMOVE_PICTURE).click()

    def new_album_click(self):
        self.driver.find_element_by_xpath(self.CREATE_NEW_ALBUM).click()

    def create_new_album(self, name):
        self.driver.find_element_by_xpath(self.NEW_ALBUM_NAME).send_keys(name, Keys.ENTER)

    def album_edit_click(self):
        self.driver.find_element_by_xpath(self.ALBUM_EDIT).click()

    def delete_album(self):
        self.driver.find_element_by_xpath(self.REMOVE_ALBUM).click()

    def delete_album_confirm(self):
        self.driver.find_element_by_xpath(self.ALBUM_DELETE_BUTTON).click()

    def post_new_photo(self, path):
        self.driver.find_element_by_xpath(self.UPLOAD_PHOTO).send_keys(path)


class SearchFilterPage(Page):
    FEMALE = '//div[@id="facets"]//div[@data-aid="PS_Click_Gender_Female"]'
    SEARCH_RESULTS = '.gs_result_i_w'
    SEARCH_RESULTS_WITH_STATUS = '.gs_result_i_w.__status'
    CHANGE_PLACE_MENU = '//div[@id="customPlaceItemSpan"]'
    COUNTRY_SELECTOR = 'field_country_int'
    FROM_AGE_SELECTOR = 'field_fromage'
    TILL_AGE_SELECTOR = 'field_tillage'
    TOWN_NAME = 'field_city'
    USERS_WITH_STATUS = 'gs_result_i_w __status'
    USERS_WITHOUT_STATUS = 'gs_result_i_w '
    SEARCH_TAGS = '//div[@id="filterTags"]'
    GROUP_SEARCH = '//div[@id="categoriesList"]/ul/li[2]/span'
    MUSIC_SEARCH = '//div[@id="categoriesList"]/ul/li[4]/span'
    GROUP_SEARCH_TYPE_CSS = '.gs_filter_t'
    SEARCH_INPUT = '//input[@id="query_usersearch"]'
    ALBUM_SEARCH = '//ul[@class="gs_filter_list"]/li[3]'
    SEARCH_RESULTS_HEADER = '.portlet_h_name_t'
    SEARCH_GROUP_UNIVERSITY = '//ul[@class="gs_filter_list"]/li[4]'

    def click_university_search(self):
        self.driver.find_element_by_xpath(self.SEARCH_GROUP_UNIVERSITY).click()

    def get_search_result_header(self):
        return self.driver.find_element_by_css_selector(self.SEARCH_RESULTS_HEADER)

    def click_album_search(self):
        self.driver.find_element_by_xpath(self.ALBUM_SEARCH).click()

    def click_music_search(self):
        self.driver.find_element_by_xpath(self.MUSIC_SEARCH).click()

    def send_search_query(self, query):
        self.driver.find_element_by_xpath(self.SEARCH_INPUT).send_keys(query, Keys.ENTER)

    def click_group_search(self):
        self.driver.find_element_by_xpath(self.GROUP_SEARCH).click()

    def get_country_select(self):
        return Select(self.driver.find_element_by_id(self.COUNTRY_SELECTOR))

    def get_from_age_select(self):
        return Select(self.driver.find_element_by_id(self.FROM_AGE_SELECTOR))

    def get_till_age_select(self):
        return Select(self.driver.find_element_by_id(self.TILL_AGE_SELECTOR))

    def set_from_age(self, age):
        self.get_from_age_select().select_by_value(str(age))

    def set_till_age(self, age):
        self.get_till_age_select().select_by_value(str(age))

    def get_search_results(self):
        return self.driver.find_elements_by_css_selector(self.SEARCH_RESULTS) + \
               self.driver.find_elements_by_css_selector(self.SEARCH_RESULTS_WITH_STATUS)

    def set_country(self, country):
        self.click_change_place()
        self.get_country_select().select_by_visible_text(country)

    def get_town_input(self):
        return self.driver.find_element_by_id(self.TOWN_NAME)

    def set_town(self, town):
        self.get_town_input().send_keys(town, Keys.ENTER)

    def click_change_place(self):
        self.driver.find_element_by_xpath(self.CHANGE_PLACE_MENU).click()

    def set_female(self):
        self.driver.find_element_by_xpath(self.FEMALE).click()
