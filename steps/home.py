from steps.default import DefaultSteps
from pages.home import HomePage

class HomeSteps(DefaultSteps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = HomePage(driver)

    def createFolder(self):
        self.page.open()
        self.page.clickOnCreateSomething()
        self.page.clickOnCreateFolder()
        self.page.fillCreateNewFolderForm("KEKW")
        self.page.createNewFolderSubmit()

