from component import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class FoldersSettingsOld(Component):
    BASE = '//div[contains(@class,"b-panel_settings")] '
    SUBMIT_BASE = '//div[@class="is-folder-remove_in"] '

    DELETE_FOLDER_BUTTON = BASE + '//div[@data-name="remove"][@data-id="1"]'
    SUBMIT_DELETE = SUBMIT_BASE + '//button[@type="submit"]'

    def click_delete(self):
        delete_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DELETE_FOLDER_BUTTON)
        )
        action=ActionChains(self.driver)
        action.move_to_element(delete_button)
        action.click().perform()


    def click_submit_delete(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT_DELETE)
        ).click()

