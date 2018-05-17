from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.page import Component, url_changer
from pages.photo_page import PhotoPage
from pages.settings_page import SettingsPage


class ConfirmModal(Component):
    CONFIRM = '//input[@name="button_delete"]'
    CANCEL = '//a[@data-l="t,cancel"]'

    def confirm(self):
        self.driver.find_element_by_xpath(self.CONFIRM).click()

    def cancel(self):
        self.driver.find_element_by_xpath(self.CANCEL).click()


class LeftActionBar(Component):
    DELETE = 'ic_delete'
    SETTINGS: str = '//*[@id="hook_Block_LeftColumnTopCardAltGroup"]/ul/li[4]/a'

    @url_changer
    def delete(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.{}'.format(self.DELETE)))
        )
        self.driver.execute_script('''
            document.getElementsByClassName('{}')[0].click()
        '''.format(self.DELETE))
        ConfirmModal(self.driver).confirm()

    @property
    def to_settings_page(self) -> SettingsPage:
        path = self.driver.find_element_by_xpath(self.SETTINGS).get_attribute('href')
        setting_page = SettingsPage(self.driver, path=path)
        setting_page.open()
        return setting_page


class MainNavBar(Component):
    PHOTO = '//a[@data-l="aid,NavMenu_AltGroup_Albums"]'

    @property
    def photo_page(self) -> PhotoPage:
        path = self.driver.find_element_by_xpath(self.PHOTO).get_attribute('href')
        return PhotoPage(self.driver, path=path)


class ApplicationPortlet(Component):
    APP_NAME = '//*[@id="hook_Block_AltGroupAppsPortletRB"]/div/div/div[2]/div/div/div/div[2]/div/div[1]'

    def __init__(self, driver, elem):
        super(ApplicationPortlet, self).__init__(driver)
        self.elem = elem

    def find_app(self, name):
        app = self.elem.find_element_by_xpath(self.APP_NAME)
        print(app.text)
        if app.text == name:
            return True
        return False


class CreateTopicPopup(Component):
    MESSAGE = '//*[@id="hook_Block_pfnull"]/div[2]/div[1]/div/div[2]'
    SEND_BUTTON = 'posting_submit'
    TOPIC_POPUP = '//*[@id="mtLayer"]/div[1]'

    def enter_message(self, msg: str):
        self.driver.find_element_by_xpath(self.MESSAGE).click()
        self.driver.find_element_by_xpath(self.MESSAGE).send_keys(msg)

    def send(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.SEND_BUTTON)))
        self.driver.find_element_by_class_name(self.SEND_BUTTON).click()
        # WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, self.TOPIC_POPUP)))


class CommentPopup(Component):
    MESSAGE = '//*[@id="ok-e-d"]'
    SEND_BUTTON = '//*[@id="ok-e-d_button"]'
    FIRST_COMMENT = '//*[@id="d-id-cmnt-local--101-m"]'

    def enter_message(self, msg: str):
        self.driver.find_element_by_xpath(self.MESSAGE).send_keys(msg)

    def send(self):
        self.driver.find_element_by_xpath(self.MESSAGE).click()
        self.driver.find_element_by_xpath(self.SEND_BUTTON).click()

    def save_id_comment(self):
        el = self.driver.find_element_by_xpath(self.FIRST_COMMENT)
        return el.find_element_by_tag_name("div").get_attribute('id')
