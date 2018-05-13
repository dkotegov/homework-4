from selenium.webdriver.common.by import By

from tests.pages.page import Page, Component


class UserAlbumPage(Page):
    PATH = '/dk?st.cmd=userAlbumEdit'

    @property
    def empty_album_content(self):
        return EmptyAlbumContent(self.driver)


class EmptyAlbumContent(Component):
    TITLE = 'ep-ttl-txt'

    @property
    def title(self):
        return self.driver.find_elements(By.CLASS_NAME, self.TITLE)[0].text
