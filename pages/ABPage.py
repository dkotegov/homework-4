# coding=utf-8

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from page import Page


class ABPage(Page):
    def wait_for_visible_xpath(self, xpath):
        return WebDriverWait(self.driver, 32).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def wait_elements_for_visible_xpath(self, selector, delay=30):
        WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, selector)))
        elem = self.driver.find_elements_by_xpath(selector)
        return elem

    def click_xpath(self, xpath):
        return self.wait_for_visible_xpath(xpath).click()

    def test_blocked_group(self):
        self.click_xpath('//div[@id="js-labels-dropdown"]')
        self.wait_for_visible_xpath('//div[@class="b-dropdown__list__item b-dropdown__list__item_unselectable"]')

    def add_to_group(self):
        self.click_xpath('//a[@class="js-add-label"]')
        elem = self.wait_for_visible_xpath('//input[@id="label"]')
        self.click_xpath('//input[@id="label"]')
        elem.send_keys('new kek')
        self.click_xpath('//button[@data-bem="btn"]')
        self.click_xpath('//input[@class="messageline__checkbox__input"]')
        self.click_xpath('//div[@id="js-labels-dropdown"]')
        self.click_xpath('//label[@data-id="3"]')
        self.click_xpath('//button[@class="js-change-labels2contacts-links"]')
        self.wait_for_visible_xpath('//span[@data-label="3"]')

    def add_group(self, name):
        self.click_xpath('//div[@id="js-labels-dropdown"]')
        input_field = self.wait_for_visible_xpath('//input[@class="dropdown__list__new-item__input form__field '
                                         'js-add-label-to-dropdown-input"]')
        input_field.click()
        input_field.send_keys(name)
        self.click_xpath('//button[contains(@class, "js-add-label-to-dropdown-button")]')
        self.wait_for_visible_xpath('//label[@data-id="1"]')

    def duplicate_group_name(self):
        self.click_xpath('//div[@id="js-labels-dropdown"]')
        elem = self.wait_for_visible_xpath('//label[@id="labels_1"]//span')
        input_field = self.wait_for_visible_xpath('//input[contains(@class, "js-add-label-to-dropdown-input")]')
        input_field.click()
        input_field.send_keys(elem.text)
        self.click_xpath('//button[contains(@class, "js-add-label-to-dropdown-button")]')
        self.wait_for_visible_xpath('//div[contains(@class, "form__message")]')

    def rename_group(self, name):
        self.wait_for_visible_xpath('//div[contains(@class, "messageline contactline")]')
        self.wait_for_visible_xpath('//div[@data-id="1"]')
        self.wait_for_visible_xpath('//i[contains(@class, "js-edit-label")]')
        self.click_xpath('//a[@class="menu__option__link js-add-label"]')
        self.wait_for_visible_xpath('//div[@class="popup__box"]')
        input_field = self.wait_for_visible_xpath('//input[@name="label"]')
        input_field.send_keys('New Name')
        self.click_xpath('//button[@class="btn btn_main confirm-ok"]')
        self.wait_for_visible_xpath('//div[@data-id="1"]')

    def add_to_favorite(self):
        self.wait_for_visible_xpath('//i[contains(@class, "icon_addressbook_favorite_off")]')
        self.wait_for_visible_xpath('//label[@class="messageline__checkbox"]')
        self.click_xpath('//input[@class="messageline__checkbox__input"]')
        self.click_xpath('//div[@id="js-labels-dropdown"]')
        self.click_xpath('//label[@data-id="favorites"]')
        self.click_xpath('//button[contains(@class, "js-change-labels2contacts-links")]')
        self.wait_for_visible_xpath('//i[contains(@class, "icon_addressbook_favorite_on")]')

    def remove_from_favorite(self):
        self.wait_for_visible_xpath('//i[contains(@class, "icon_addressbook_favorite_on")]')
        self.wait_for_visible_xpath('//label[@class="messageline__checkbox"]')
        self.click_xpath('//input[@class="messageline__checkbox__input"]')
        self.click_xpath('//div[@id="js-labels-dropdown"]')
        self.click_xpath('//label[@id="labels_favorites"]')
        self.click_xpath('//button[contains(@class, "js-change-labels2contacts-links")]')
        self.wait_for_visible_xpath('//i[contains(@class, "icon_addressbook_favorite_off")]')

    def edit_user(self):
        self.click_xpath('//input[@class="messageline__checkbox__input"]')
        self.click_xpath('//div[@data-name="edit"]')
        self.wait_for_visible_xpath('//form[@id="formPersonal"]')

    def edit_field(self):
        self.edit_user()
        elem = self.wait_for_visible_xpath('//input[@id="firstname"]')
        self.click_xpath('//input[@id="firstname"]')
        elem.send_keys('qwertyuio')
        self.click_xpath('//div[@data-name="submit"]')
        self.wait_for_visible_xpath(
            '//span[contains(@class, "menu__item__link__text_linear")][contains(text(), "Все контакты")]')
        self.click_xpath(
            '//span[@class="menu__item__link__text menu__item__link__text_linear"][contains(text(), "Все контакты")]')
        self.wait_for_visible_xpath('//span[@class="contactline__body__item contactline__body__item_name"]')

    def multiple_selected(self):
        for elem in self.wait_elements_for_visible_xpath('//input[contains(@class, "messageline__checkbox__input")]'):
            elem.click()
        self.click_xpath('//div[@data-name="edit"]')
        self.wait_for_visible_xpath('//div[contains(@class, "messagelist-wrapper")]')

    def multiple_delete(self):
        for elem in self.wait_elements_for_visible_xpath('//input[@class="messageline__checkbox__input"]'):
            elem.click()
        self.click_xpath('//div[@id="js-remove-contacts"]')
        self.wait_for_visible_xpath('//div[@class="messagelist-wrapper"]')

    def revert_by_filter(self):
        arr = []
        for elem in self.wait_elements_for_visible_xpath(
                '//span[@class="contactline__body__item contactline__body__item_name"]'):
            arr.append(elem.text)

        self.click_xpath('//span[@class="b-dropdown__ctrl__text"][contains(text(), "Сортировать")]')
        self.click_xpath('//a[@data-name="byName"]')
        kek = []
        for elem in self.wait_elements_for_visible_xpath(
                '//span[@class="contactline__body__item contactline__body__item_name"]'):
            kek.append(elem.text)

        assert (arr[::-1] == kek)

    def double_revert(self):
        arr = []
        for elem in self.wait_elements_for_visible_xpath(
                '//span[@class="contactline__body__item contactline__body__item_name"]'):
            arr.append(elem.text)

        self.click_xpath('//span[@class="b-dropdown__ctrl__text"][contains(text(), "Сортировать")]')
        self.click_xpath('//a[@data-name="byName"]')
        self.click_xpath('//span[@class="b-dropdown__ctrl__text"][contains(text(), "Сортировать")]')
        self.click_xpath('//a[@data-name="byName"]')
        kek = []
        for elem in self.wait_elements_for_visible_xpath(
                '//span[@class="contactline__body__item contactline__body__item_name"]'):
            kek.append(elem.text)

        assert (arr == kek)
