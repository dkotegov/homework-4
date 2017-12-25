# -*- coding: utf-8 -*-

import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


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
        user_login = os.environ['LOGIN']
        user_password = os.environ['PASSWORD']

        auth_form = AuthForm(self.driver)
        auth_form.set_login(user_login)
        auth_form.set_password(user_password)
        auth_form.submit()


class MainPage(Page):
    SEARCH = 'field_query'
    SEARCH_SUGGESTIONS_SHOWALL_LINK = '//div[@class="search_suggest_show-all"]'
    SEARCH_BTN = 'lsBtn'
    SEARCH_RESULTS = 'searchResults'

    def search(self, request):
        self.driver.find_element_by_id(self.SEARCH).send_keys(request)

    def get_search_suggestions_showall_text(self):
        return self.driver.find_element_by_xpath(self.SEARCH_SUGGESTIONS_SHOWALL_LINK).text

    def submit_search(self):
        self.driver.find_element_by_id(self.SEARCH_BTN).click()


class PhotoPage(Page):
    CREATE_NEW_ALBUM = '//div[@class="portlet_h_inf"]'
    # NEW_ALBUM_MENU = 'field_photoAlbumName'
    PHOTO_ALBUMS_HEADER = '//div[@class="photo-sc_w"]'
    ALBUM_NAME_HEADER = '.photo-h'
    NEW_ALBUM_NAME = 'field_photoAlbumName'
    ALBUM_EDIT = '//div[@class="photo-menu_edit iblock-cloud_show"]'
    ALBUM_NAME_EDIT = '//div[@class="photo-panel_cover"]'
    REMOVE_ALBUM = "//a[contains(text(), 'Удалить альбом')]"
    ALBUM_DELETE_CONFIRM_TABLE = 'table.mw_tbl'
    ALBUM_DELETE_BUTTON = '//input[@id="hook_FormButton_button_delete_confirm"]'
    UPLOAD_PHOTO = '//input[@class="html5-upload-link __before-upload"]'
    NEW_PICTURE_CREATED_CSS = '.input-l'
    REMOVE_PICTURE = '//a[@class="photo-widget __del"]'
    ALBUM_NAME = '//span[@class="photo-h_cnt_t ellip"]'

    def __init__(self, driver):
        Page.__init__(self, driver)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                self.PHOTO_ALBUMS_HEADER
            ))
        )

    def remove_picture(self):
        self.driver.find_element_by_xpath(self.REMOVE_PICTURE).click()

    def get_album_name(self):
        return self.driver.find_element_by_xpath(self.ALBUM_NAME).text

    def new_album_click(self):
        self.driver.find_element_by_xpath(self.CREATE_NEW_ALBUM).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.ID,
                self.NEW_ALBUM_NAME
            ))
        )

    def create_new_album(self, name):
        self.driver.find_element_by_id(self.NEW_ALBUM_NAME).send_keys(name)

        self.driver.find_element_by_id(self.NEW_ALBUM_NAME).send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                self.ALBUM_NAME_HEADER
            ))
        )

    def album_edit_click(self):
        self.driver.find_element_by_xpath(self.ALBUM_EDIT).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                self.ALBUM_NAME_EDIT
            ))
        )

    def delete_album(self):
        self.driver.find_element_by_xpath(self.REMOVE_ALBUM).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                self.ALBUM_DELETE_CONFIRM_TABLE
            ))
        )

    def delete_album_confirm(self):
        self.driver.find_element_by_xpath(self.ALBUM_DELETE_BUTTON).click()

    def post_new_photo(self, path):
        self.driver.find_element_by_xpath(self.UPLOAD_PHOTO).send_keys(path)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                self.NEW_PICTURE_CREATED_CSS
            ))
        )


class SearchFilterPage(Page):
    NOT_FOUND = -1
    FEMALE = '//div[@data-aid="PS_Click_Gender_Female"]'
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
    GROUP_SEARCH = '//span[@data-field_mode="Groups"]'
    MUSIC_SEARCH = '//span[@data-field_mode="Music"]'
    GROUP_SEARCH_TYPE_CSS = '.gs_filter_t'
    SEARCH_INPUT = '//input[@id="query_usersearch"]'
    ALBUM_SEARCH = '//div[@data-aid="PS_Click_MusicType_Album"]'
    SEARCH_RESULTS_HEADER = '.portlet_h_name_t'
    SEARCH_GROUP_UNIVERSITY = '//div[@data-aid="PS_Click_CommunityKind_University"]'

    def click_university_search(self, found_text):
        self.driver.find_element_by_xpath(self.SEARCH_GROUP_UNIVERSITY).click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR,
                self.SEARCH_RESULTS_HEADER),
                found_text
            )
        )

    def get_search_result_header(self):
        return self.driver.find_element_by_css_selector(self.SEARCH_RESULTS_HEADER)

    def click_album_search(self):
        self.driver.find_element_by_xpath(self.ALBUM_SEARCH).click()

    def click_music_search(self, group_selector):
        self.driver.find_element_by_xpath(self.MUSIC_SEARCH).click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR,
                self.GROUP_SEARCH_TYPE_CSS),
                group_selector
            )
        )

    def search_for_university(self, university, request_parameter):
        self.send_search_query(university, request_parameter)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                self.SEARCH_RESULTS_HEADER
            ))
        )

    def send_search_query(self, query, request_parameter):
        self.driver.find_element_by_xpath(self.SEARCH_INPUT).send_keys(query, Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.current_url.find(request_parameter) != -1
        )

    def search_for_album(self, album, request_parameter):
        self.send_search_query(album, request_parameter)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                self.SEARCH_RESULTS_HEADER
            ))
        )

    def click_group_search(self, group_selector):
        self.driver.find_element_by_xpath(self.GROUP_SEARCH).click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR,
                self.GROUP_SEARCH_TYPE_CSS),
                group_selector
            )
        )

    def get_country_select(self):
        return Select(self.driver.find_element_by_id(self.COUNTRY_SELECTOR))

    def get_from_age_select(self):
        return Select(self.driver.find_element_by_id(self.FROM_AGE_SELECTOR))

    def get_till_age_select(self):
        return Select(self.driver.find_element_by_id(self.TILL_AGE_SELECTOR))

    def set_from_age(self, age):
        self.get_from_age_select().select_by_value(str(age))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                self.SEARCH_TAGS
            ))
        )

    def set_till_age(self, age):
        self.get_till_age_select().select_by_value(str(age))
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((
                By.XPATH,
                self.SEARCH_TAGS),
                str(age)
            )
        )

    def get_search_results(self):
        return self.driver.find_elements_by_css_selector(self.SEARCH_RESULTS) + \
               self.driver.find_elements_by_css_selector(self.SEARCH_RESULTS_WITH_STATUS)

    def set_country(self, country):
        self.click_change_place()
        self.get_country_select().select_by_visible_text(country)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                self.SEARCH_TAGS
            ))
        )

    def get_town_input(self):
        return self.driver.find_element_by_id(self.TOWN_NAME)

    def set_town(self, town):
        self.get_town_input().send_keys(town, Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((
                By.XPATH,
                self.SEARCH_TAGS),
                town
            )
        )

    def click_change_place(self):
        self.driver.find_element_by_xpath(self.CHANGE_PLACE_MENU).click()

    def set_female(self, query):
        self.driver.find_element_by_xpath(self.FEMALE).click()
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.current_url.find(query) != self.NOT_FOUND
        )
