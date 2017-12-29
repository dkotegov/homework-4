# -*- coding: utf-8 -*-
import urlparse

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
    BASE_URL = 'http://ok.ru/'
    PATH = ''
    WINDOW_WIDTH = 1920
    WINDOW_HEIGHT = 1080

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.set_window_size(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)


class GroupsPage(Page):
    PATH = 'groups/'

    @property
    def form(self):
        return AllGroups(self.driver)

class MyGroupPage(Page):
    PATH = ''

    def __init__(self, driver, path):
        Page.__init__(self, driver)
        self.PATH = path

    @property
    def form(self):
        return MyGroup(self.driver)


class GroupSettingsPage(Page):
    PATH = ''

    def __init__(self, driver, path):
        Page.__init__(self, driver)
        self.PATH = path

    @property
    def form(self):
        return GroupSettings(self.driver)


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class Groups(Component):
    CREATE_GROUP = '//a[@class="add-stub al add-stub__hor"]'
    PUBLIC_GROUP = '//a[@class="create-group-dialog_i"]'
    NAME_INPUT = '//input[@id="field_name"]'
    CREATE_BUTTON = '//input[@id="hook_FormButton_button_create"]'
    CATEGORY = '//select[@name="st.layer.pageMixedCategory"]'
    OPTION = '//option[@value="subcatVal12001"]'

    def create_public_group(self, group_name):
        self.driver.find_element_by_xpath(self.CREATE_GROUP).click()
        create_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PUBLIC_GROUP)
        )
        create_button.click()
        input_field = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NAME_INPUT)
        )
        input_field.send_keys(group_name)
        self.driver.find_element_by_xpath(self.CATEGORY).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.OPTION))
        )
        self.driver.find_element_by_xpath(self.OPTION).click()
        self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath(self.CREATE_BUTTON))
        return MyGroupPage(self.driver, self.driver.current_url).form


class AllGroups(Groups):
    JOIN_BUTTON = '//button[text()="Присоединиться"][@class="button-pro __small"]'

    def join(self):
        self.driver.find_element_by_xpath(self.JOIN_BUTTON).click()


class MyGroup(Component):
    CREATE_THEME = '//div[text()="Создать новую тему"]'
    INSERT_TEXT = '//div[@id="posting_form_text_field"]'
    SHARE_BUTTON = '//input[@value="Поделиться" and @class="button-pro"]'
    SETTINGS = '//span[text()="Настройки"]'
    DESCRIPTION_INPUT = '//textarea[@name="st.description"]'
    SAVE = '//input[@value="Сохранить"]'
    GROUP_DESCRIPTION = '//div[@class="group-info_desc"]'
    OVERLAY = '//div[@class="posting-form_overlay invisible"]'
    TOP_MENU = '//div[@id="mainTopContentRow"]'
    BOOKMARK_DEFAULT = '//span[text()="Закладка"]'
    BOOKMARK_ADDED = '//span[text()="Закладка добавлена"]'
    GROUP_MIDDLE_MENU = '//div[@id="hook_Block_MiddleColumnTopCard_MenuAltGroup"]'
    GROUP_INFO_CATEGORIES = '//div[@class="group-info_cnt"]'
    FEED_POST_DESCRIPTION = '//div[@class="media-text_cnt_tx emoji-tx textWrap"]'
    PIN = '//a[@class="ico-inline ic12 ic12_pin"][@title="Прикрепить"]'
    UNPIN = '//a[@class="ico-inline ic12 ic12_unpin"][@title="Открепить"]'
    LIKE_BUTTON = '//button[@class="h-mod widget_cnt controls-list_lk"]'

    def create_new_theme(self, text):
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.CREATE_THEME))
        )
        self.driver.find_element_by_xpath(self.CREATE_THEME).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.OVERLAY)
        )
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.INSERT_TEXT))
        )
        element = self.driver.find_element_by_xpath(self.INSERT_TEXT)
        self.driver.execute_script("arguments[0].click();", element)
        element.send_keys(text)
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.SHARE_BUTTON))
        )
        self.driver.find_element_by_xpath(self.SHARE_BUTTON).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TOP_MENU)
        )

    def set_bookmark(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.BOOKMARK_DEFAULT)
        ).click()

    def is_added_to_bookmarks(self):
        bookmark_added = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.BOOKMARK_ADDED)
        )
        return bookmark_added.is_displayed()

    def change_description(self, new_description):

        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.SETTINGS))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_xpath(self.SETTINGS)).click().perform()
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.DESCRIPTION_INPUT))
        )
        self.driver.find_element_by_xpath(self.DESCRIPTION_INPUT).click()
        self.driver.find_element_by_xpath(self.DESCRIPTION_INPUT).send_keys(new_description)
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.SAVE))
        )
        self.driver.find_element_by_xpath(self.SAVE).click()

    def check_group_description(self, description):
        text = self.driver.find_element_by_xpath(self.GROUP_DESCRIPTION).text
        return text == description

    def open_settings(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.SETTINGS))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_xpath(self.SETTINGS)).click().perform()
        return GroupSettingsPage(self.driver, self.driver.current_url).form

    def check_section_visible(self, section_string):
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.GROUP_MIDDLE_MENU))
        )
        photos_exist = False
        for item in self.driver.find_element_by_xpath(self.GROUP_MIDDLE_MENU).find_elements_by_tag_name('a'):
            if item.text == section_string:
                photos_exist = True
                break
        return photos_exist

    def check_group_category_is_star(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.GROUP_INFO_CATEGORIES))
        )
        for item in self.driver.find_element_by_xpath(self.GROUP_INFO_CATEGORIES).find_elements_by_tag_name('div'):
            if u'Известная личность или коллектив' in item.text:
                return True
        return False

    def get_all_posts_texts(self):
        def all_elements_found(d):
            elements = d.find_elements_by_xpath(self.FEED_POST_DESCRIPTION)
            if len(elements) == 2:
                return map(lambda e: e.text, elements)

        texts = WebDriverWait(self.driver, 2, 0.5).until(
            all_elements_found
        )
        return texts

    def click_pin_post(self, post_num):
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, self.PIN))
        )

        def select_pin(d):
            elements = d.find_elements_by_xpath(self.PIN)
            if len(elements) == 2:
                actions = ActionChains(self.driver)
                actions.move_to_element(elements[post_num]).click().pause(2).perform()
                return elements

        WebDriverWait(self.driver, 30, 0.5).until(
            select_pin
        )

    def click_unpin_post(self, post_num):
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, self.UNPIN))
        )

        def select_unpin(d):
            elements = d.find_elements_by_xpath(self.PIN)
            if len(elements) == 1:
                actions = ActionChains(self.driver)
                actions.move_to_element(elements[post_num]).click().pause(2).perform()
                return elements

        WebDriverWait(self.driver, 30, 0.5).until(
            select_unpin
        )

    def click_like_post(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, self.LIKE_BUTTON))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_xpath(self.LIKE_BUTTON)).click().pause(0.5).perform()

    def get_post_likes_count(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, self.LIKE_BUTTON))
        )
        return self.driver.find_element_by_xpath(self.LIKE_BUTTON).get_attribute("data-count")


class AuthForm(Component):
    LOGIN = '//input[@id="field_email"]'
    PASSWORD = '//input[@name="st.password"]'
    SUBMIT = '//input[@type="submit"][@class="button-pro __wide"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class GroupSettings(Component):
    MANAGEMENT = '//i[@class="tico_img ic ic_nav_control"]'
    PHOTOS_SECTION = '//select[@id="field_opt_PhotosTabHidden"]'
    VIDEOS_SECTION = '//select[@id="field_opt_VideoTabHidden"]'
    SAVE_CHANGES_BUTTON = '//input[@id="hook_FormButton_button_save_settings"]'
    SPECIFY_CATEGORY_LINK = '//span[@id="showPageCategoriesSelectsId"]'
    SUPERCATEGORY_SELECT = '//select[@id="field_pageSuperCategory"]'
    SUPERCATEGORY_SELECT_STAR_OPTION = '//option[@value="STAR"]'

    def change_section_visibility(self, visibility, section):
        option_text = u'Показывать' if visibility else u'Скрывать'
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.MANAGEMENT))
        )
        self.driver.find_element_by_xpath(self.MANAGEMENT).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, section))
        )
        for option in self.driver.find_element_by_xpath(section).find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.SAVE_CHANGES_BUTTON))
        )
        self.driver.find_element_by_xpath(self.SAVE_CHANGES_BUTTON).click()

    def change_group_category_to_star(self):

        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.SPECIFY_CATEGORY_LINK))
        )
        self.driver.find_element_by_xpath(self.SPECIFY_CATEGORY_LINK).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.SUPERCATEGORY_SELECT))
        )
        self.driver.find_element_by_xpath(self.SUPERCATEGORY_SELECT).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.SUPERCATEGORY_SELECT_STAR_OPTION))
        )
        self.driver.find_element_by_xpath(self.SUPERCATEGORY_SELECT_STAR_OPTION).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.SAVE_CHANGES_BUTTON))
        )
        self.driver.find_element_by_xpath(self.SAVE_CHANGES_BUTTON).click()
