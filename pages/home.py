import urllib.parse as urlparse
from pages.default import Page

class HomePage(Page):
    BASE_URL = 'https://cloud.mail.ru/'
    PATH = 'home'

    CREATE= 'div[data-name="create"]'
    CREATE_FOLDER =  'div[data-name="createFolder"]'
    MODAL_INPUT = 'div[data-qa-modal] input'
    SUBMIT_BUTTON = 'div[data-qa-modal] button[class*=primary]'
    # ALL_FILES = 'div[data-name = "/"]'
    # CREATE_FOLDER = 'div[data-name = "/${process.env.CREATE_FOLDER}"]'
    
    def clickOnCreateSomething (self):
        self.driver.find_element_by_css_selector(self.CREATE).click()

    def clickOnCreateFolder(self):
        self.driver.find_element_by_css_selector(self.CREATE_FOLDER).click()

    def fillCreateNewFolderForm(self, folderName):
        self.driver.find_element_by_css_selector(self.MODAL_INPUT).send_keys(folderName)

    def createNewFolderSubmit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT_BUTTON).click()