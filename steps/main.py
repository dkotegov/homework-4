from pages.edit import EditPage
from pages.iframe import IframePage
from pages.main import MainPage
from pages.new_proj import NewProjPage
from pages.source import SourcePage
from pages.tag import TagPage
from pages.transform import TransformPage
from pages.watch import WatchPage
from steps.default import Steps


class MainSteps(Steps):
    def __init__(self, driver):
        Steps.__init__(self, MainPage(driver))

    def logout(self):
        self.page.form.logout_click()

    def clone(self, name, new_name):
        proj_id = self.page.project_list.get_proj_id(name)
        self.page.project_list.clone_click(proj_id)
        self.page.accept_alert_input(new_name)
        return self.page.accept_alert_text()

    def delete_proj(self, name):
        proj_id = self.page.project_list.get_proj_id(name)
        self.page.project_list.delete_click(proj_id)
        self.page.accept_alert_text()
        return self.page.accept_alert_text()

    def go_to_new_proj(self):
        self.page.menu.new_proj_click()
        self.page.waitRedirect(NewProjPage.BASE_URL + NewProjPage.PATH)

    def go_to_new_source(self):
        self.page.menu.new_source_click()
        self.page.waitRedirect(SourcePage.BASE_URL + SourcePage.PATH)

    def go_to_tag(self, name):
        self.page.tag_list.tag_click(name)
        self.page.waitRedirect(TagPage.BASE_URL + TagPage.PATH + "?tag=" + name)

    def go_to_edit(self, proj_id):
        self.page.project_list.edit_click(proj_id)
        self.page.waitRedirect(EditPage.BASE_URL + EditPage.PATH + "?p_id={}".format(proj_id))

    def go_to_watch(self, proj_id):
        self.page.project_list.watch_click(proj_id)
        self.page.waitRedirect(WatchPage.BASE_URL + WatchPage.PATH + "?p_id={}".format(proj_id))

    def go_to_transform(self):
        self.page.menu.transform_click()
        self.page.waitRedirect(TransformPage.BASE_URL + TransformPage.PATH)

    def go_to_iframe(self):
        self.page.menu.iframe_click()
        self.page.waitRedirect(IframePage.BASE_URL + IframePage.PATH)

    def get_proj_id(self, name):
        return self.page.project_list.get_proj_id(name)
