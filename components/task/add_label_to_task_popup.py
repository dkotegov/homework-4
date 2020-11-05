from base_classes.component import Component
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

class AddLabelToTaskPopup(Component):
    CONTAINER = '//div[contains(@class, "js-addNewLabel")]'
    CREATE_NEW_LABEL_BUTTON = '//div[contains(@class, "js-openCreateLabelPopup")]'

    def click_create_new_label_button(self):
        self.driver.find_element_by_xpath(self.CREATE_NEW_LABEL_BUTTON).click()

    def is_label_with_provided_name_exist(self, label_name):
        xpath = f'//div[contains(@class, "js-addOrRemoveLabel") and text()="{label_name}"]'
        label_exist = True
        try:
            WebDriverWait(self.driver, 3, 0.1).until(
                lambda d: self.driver.find_element_by_xpath(xpath)
            )
        except TimeoutException:
            label_exist = False
        
        return label_exist

    def click_label_with_provided_name(self, label_name):
        xpath = f'//div[contains(@class, "js-addOrRemoveLabel") and text()="{label_name}"]'
        label_exist = True
        try:
            WebDriverWait(self.driver, 3, 0.1).until(
                lambda d: self.driver.find_element_by_xpath(xpath)
            )
        except TimeoutException:
            label_exist = False
        
        assert(label_exist)
        self.driver.find_element_by_xpath(xpath).click()


    def close_popup(self):
        self.driver.find_element_by_xpath('//i[contains(@class, "fa-user-friends")]').click()