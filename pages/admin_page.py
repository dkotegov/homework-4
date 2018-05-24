from selenium.common.exceptions import WebDriverException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.page import Page
from pages.settings_components import PopupUserMenu, RoleRadioButtons, Role
from pages.waits import web_element_locator


class AdminPage(Page):
    BUTTON_ADD_ADMIN = '//*[@id="group-settings-form"]/div[2]/a'
    ADMINISTRATION_LIST_PAGE = '//*[@id="GroupMembersMenu"]/div/div/a[2]'
    ADMINISTRATION_LIST = '//*[@id="hook_Block_GroupMembersResultsBlock"]/div/ul'
    ROLE = '//a[text()="{}"]/../../div[contains(@class, "fs-11")]'
    POPUP = 'gwt-shortcutMenu-content'
    link_text = ''

    def add_moderator(self, name, role):
        self.link_text = name
        self.driver.find_element_by_xpath(self.BUTTON_ADD_ADMIN).click()

        self.show_element_by_class(self.POPUP, name)
        PopupUserMenu(self.driver).assign_as_moderator.add_grant(role)
        return self

    @web_element_locator((By.XPATH, '//a[text()="{}"]'.format(link_text)))
    def show_element_by_class(self, c: str, name):
        self.driver.execute_script('''
                    let mouseover = new Event('mouseover');    
                    let node = document.evaluate('//a[text()="{}"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null ).singleNodeValue;
                    node.dispatchEvent(mouseover);'''.format(name))
        self.driver.execute_script(
            "document.getElementsByClassName('{}')[0].style.display = 'block';".format(c))

    def to_administration_list(self):
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, self.ADMINISTRATION_LIST_PAGE))).click()
        self.driver.find_element_by_xpath(self.ADMINISTRATION_LIST_PAGE).click()

    def remove_moderator(self, name):
        # popup_menu = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.LINK_TEXT, name)))

        popup_menu = self.driver.find_element_by_link_text(name)

        ActionChains(self.driver) \
            .move_to_element(popup_menu) \
            .perform()

        self.driver.execute_script(
            "document.getElementsByClassName('gwt-shortcutMenu-content')[0].style.display = 'block';")
        return PopupUserMenu(self.driver)

    def is_moder_added(self, name, role: Role):
        try:
            self.driver.find_element_by_link_text(name)
        except WebDriverException:
            return False
        if self.driver.find_element_by_xpath(self.ROLE.format(name)).text == role.value:
            return True
        else:
            return False
