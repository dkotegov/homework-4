from enum import Enum

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.page import Component


class RoleRadioButtons(Enum):
    MODERATOR = '//*[@id="field_index_0"]'
    SUPERMODERATOR = '//*[@id="field_index_1"]'
    EDITOR = '//*[@id="field_index_2"]'
    ANALYST = '//*[@id="field_index_3"]'


class Role(Enum):
    MODERATOR = 'Модератор'
    SUPERMODERATOR = 'Супермодератор'
    EDITOR = 'Редактор'
    ANALYST = 'Аналитик'


class ModerForm(Component):
    RADIO_BUTTON_MODERATOR = '//*[@id="field_index_0"]'
    ADD_BUTTON = '//*[@id="hook_FormButton_button_grant"]'
    REMOVE_BUTTON = '//*[@id="hook_FormButton_button_revoke_confirm"]'
    POPUP_DIALOG = '//*[@id="popLayer_mo"]'

    def add_grant(self, role: RoleRadioButtons):
        self.driver.find_element_by_xpath(role.value).click()
        self.driver.find_element_by_xpath(self.ADD_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, self.POPUP_DIALOG)))

    def remove_grant(self):
        self.driver.find_element_by_xpath(self.REMOVE_BUTTON).click()


class GeneralForm(Component):
    NAME_GROUP_INPUT = '//*[@id="field_name"]'
    DESCRIPTION_GROUP_INPUT = '//*[@id="field_description"]'
    GROUP_CATEGORY = '//*[@id="field_category"]'
    PAGE_CATEGORY = '//*[@id="field_pageSuperCategory"]'
    PAGE_SUBCATEGORY = '//*[@id="field_pageMixedCategory"]'
    CATEGORY_AFTER_SAVE = '//*[@id="categoriesCollapsedId"]/div[2]/span[1]'
    SAVE_BUTTON = '//*[@id="hook_FormButton_button_save_settings"]'
    TIP = '//*[@id="hook_Block_TipBlock"]/div/div'
    TYPE_TEXT = '//*[@id="group-settings-form"]/div/div[1]/div[2]/div/span[1]'
    CHANGE_TYPE = '//*[@id="group-settings-form"]/div/div[1]/div[2]/div/a'
    POPUP = '//*[@id="popLayer_mo"]'
    POPUP_CONFIRM_BUTTON = '//*[@id="hook_FormButton_button_change_type"]'

    class Category(Enum):
        BRAND = 'BRAND'
        LOCAL = 'LOCAL'
        STAR = 'STAR'
        PUBLIC = 'PUBLIC'

    class Subcategory(Enum):
        HUMORIST = 'subcatVal11022'

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def name(self):
        return self.driver.find_element_by_xpath(self.NAME_GROUP_INPUT)

    @name.setter
    def name(self, val):
        input = self.driver.find_element_by_xpath(self.NAME_GROUP_INPUT)
        input.clear()
        input.send_keys(val)

    @property
    def description(self):
        return self.driver.find_element_by_xpath(self.DESCRIPTION_GROUP_INPUT)

    @description.setter
    def description(self, val):
        input = self.driver.find_element_by_xpath(self.DESCRIPTION_GROUP_INPUT)
        input.clear()
        input.send_keys(val)

    @property
    def category(self):
        if self.type == "Страница":
            return Select(self.driver.find_element_by_xpath(self.PAGE_CATEGORY)).first_selected_option.text
        else:
            return Select(self.driver.find_element_by_xpath(self.GROUP_CATEGORY)).first_selected_option.text

    @category.setter
    def category(self, category: Category):
        if self.type == "Страница":
            select_category = Select(self.driver.find_element_by_xpath(self.PAGE_CATEGORY))
            select_category.select_by_value(category.value)
        else:
            select_category = Select(self.driver.find_element_by_xpath(self.GROUP_CATEGORY))
            select_category.select_by_index(1)

    @property
    def subcategory(self):
        select_subcategory = Select(self.driver.find_element_by_xpath(self.PAGE_SUBCATEGORY))
        return select_subcategory.first_selected_option.text

    @subcategory.setter
    def subcategory(self, subcategory: Subcategory):
        if subcategory is not None:
            select_category = Select(self.driver.find_element_by_xpath(self.PAGE_SUBCATEGORY))
            if subcategory.value not in [o.get_attribute('value') for o in select_category.options]:
                select_category.select_by_index(0)
            else:
                select_category.select_by_value(subcategory.value)

    @property
    def type(self):
        return self.driver.find_element_by_xpath(self.TYPE_TEXT).text

    def toggle_type(self):
        self.driver.find_element_by_xpath(self.CHANGE_TYPE).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.POPUP)))
        self.driver.find_element_by_xpath(self.POPUP_CONFIRM_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, self.POPUP)))

    def save(self):
        self.driver.find_element_by_xpath(self.SAVE_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.TIP)))


class ApplicationPopup(Component):
    SHOW_APP_RADIO_BUTTON = '//*[@id="field_place_PORTLET"]'
    INSTALL_BUTTON = '//*[@id="hook_FormButton_button_install"]'
    APP_NAME = '//*[@id="field_name"]'
    POPUP_WINDOW = '//*[@id="popLayer_mo"]'

    def __init__(self, driver):
        super(ApplicationPopup, self).__init__(driver)
        el = self.driver.find_element_by_xpath(self.APP_NAME)
        self.app_name = el.get_attribute('value')

    def apply_install(self):
        self.driver.find_element_by_xpath(self.SHOW_APP_RADIO_BUTTON).click()
        self.driver.find_element_by_xpath(self.INSTALL_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, self.POPUP_WINDOW)))
        return self


class AddGroupLinksPopup(Component):
    POPUP = '//*[@id="popLayer_mo"]'
    SELECT = '//*[@id="hook_InviteChangeCard_4585283105"]/div/div[2]/div[2]/div[2]/div[2]'
    ADD_BUTTON = '//*[@id="hook_FormButton_button_invite"]'
    GROUP_NAME = 'leftCardName'

    def add(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.POPUP)))
        self.driver.execute_script(
            "el = document.getElementsByClassName('ifSelect')[0];"
            "el.style.display = 'block';"
            "el.click();")
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'ifSelect')))
        # self.driver.find_element_by_class_name('ifSelect').click()
        name = self.driver.find_element_by_class_name(self.GROUP_NAME).text
        self.driver.find_element_by_xpath(self.ADD_BUTTON).click()
        return name


class ApplicationForm(Component):
    APPLICATION = '//*[@id="availableApps"]/div[2]/div/div[1]/div[2]/div/div[3]/a'

    def install_app(self):
        self.driver.find_element_by_xpath(self.APPLICATION).click()
        return ApplicationPopup(self.driver)


class WhoCanLeaveComments(Enum):
    NOBODY = 'NOBODY'
    MEMBERS = 'MEMBERS'
    EVERYBODY = 'EVERYBODY'


class ManagmentForm(Component):
    GENERATE_LINK = '//*[@id="group-settings-form"]/div[8]/div[2]/div/div[2]/div/a'
    GENERATE_API_KEY_BUTTON = '//*[@id="hook_FormButton_button_change_token"]'
    API_KEY_INPUT = '//*[@id="hook_Form_PopLayerAltGroupChangeTokenForm"]/form/input[3]'
    OBSCENE_LANGUAGE = '//*[@id="field_opt_ConcealObsceneWordsInCommentsEnabled"]'
    PHOTO_SECTION = '//*[@id="field_opt_PhotosTabHidden"]'
    VIDEO_SECTION = '//*[@id="field_opt_VideoTabHidden"]'
    GOODS_SECTION = '//*[@id="field_opt_advertPage"]'
    COMMENT = '//*[@id="field_opt_whoCanComment"]'
    SAVE_BUTTON = '//*[@id="hook_FormButton_button_save_settings"]'
    TIP = '//*[@id="hook_Block_TipBlock"]/div/div'

    def generate_api_key(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_xpath(self.GENERATE_LINK).click()
        self.driver.find_element_by_xpath(self.GENERATE_API_KEY_BUTTON).click()
        value = self.driver.find_element_by_xpath(self.API_KEY_INPUT).get_attribute('value')
        return value

    def hide_photo_section(self):
        select = Select(self.driver.find_element_by_xpath(self.PHOTO_SECTION))
        select.select_by_value("on")

    def hide_video_section(self):
        select = Select(self.driver.find_element_by_xpath(self.VIDEO_SECTION))
        select.select_by_value("on")

    def show_goods_section(self):
        select = Select(self.driver.find_element_by_xpath(self.GOODS_SECTION))
        select.select_by_value("SHOW")

    def hide_obscene(self):
        select_obscene = Select(self.driver.find_element_by_xpath(self.OBSCENE_LANGUAGE))
        select_obscene.select_by_value("on")
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.TIP)))

    def forbid_leave_comments(self, who: WhoCanLeaveComments):
        select = Select(self.driver.find_element_by_xpath(self.COMMENT))
        select.select_by_value(who.value)

    def save_settings(self):
        self.driver.find_element_by_xpath(self.SAVE_BUTTON).click()


class PopupUserMenu(Component):
    ASSIGN_MODERATOR_POPUP_ITEM = 'ic_moder'
    REMOVE_MODERATOR_POPUP_ITEM = 'ic_moder-off'

    @property
    def assign_as_moderator(self) -> ModerForm:
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.ASSIGN_MODERATOR_POPUP_ITEM))).click()
        return ModerForm(self.driver)

    @property
    def remove_as_moderator(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.REMOVE_MODERATOR_POPUP_ITEM))).click()
        return ModerForm(self.driver)
