from pages.default import Page, Component


class MainPage(Page):
    PATH = 'page/menu'
    HEADER = '//h2[contains(text(), "меню")]'

    @property
    def menu(self):
        return MainMenu(self.driver)

    @property
    def project_list(self):
        return ProjectList(self.driver)

    @property
    def tag_list(self):
        return TagList(self.driver)


class MainMenu(Component):
    LOGOUT = '//div[@id="exitLogOutBtn"]'
    TRANSFORM = '//div[@id="imageTransformBtn"]'
    IFRAME = '//div[@id="myIframeBtn"]'
    NEW_PROJ = '//div[@id="projectNewButton"]'
    NEW_SOURCE = '//div[@id="newSourceBtn"]'

    def logout_click(self):
        self.wait_for_visible(self.LOGOUT)
        self.driver.find_element_by_xpath(self.LOGOUT).click()

    def transform_click(self):
        self.wait_for_visible(self.TRANSFORM)
        self.driver.find_element_by_xpath(self.TRANSFORM).click()

    def iframe_click(self):
        self.wait_for_visible(self.IFRAME)
        self.driver.find_element_by_xpath(self.IFRAME).click()

    def new_proj_click(self):
        self.wait_for_visible(self.NEW_PROJ)
        self.driver.find_element_by_xpath(self.NEW_PROJ).click()

    def new_source_click(self):
        self.wait_for_visible(self.NEW_SOURCE)
        self.driver.find_element_by_xpath(self.NEW_SOURCE).click()


class ProjectList(Component):
    PROJ_CONTAINER = '//div[@id="projectsListBox"]'
    PROJ_ID = '//div[@class="project-element-class"][contains(., "Название: {name}")]//div[@data-project-id]'
    EDIT = '//div[@onclick="redactorProject(this)"][@data-project-id="{id}"]'
    WATCH = '//div[@onclick="watchMyProject(this)"][@data-project-id="{id}"]'
    DELETE = '//div[@onclick="dropProject(this)"][@data-project-id="{id}"]'
    CLONE = '//div[@onclick="cloneProject(this)"][@data-project-id="{id}"]'

    def get_proj_id(self, proj_name):
        self.wait_for_visible(self.PROJ_CONTAINER)
        proj_container = self.driver.find_element_by_xpath(self.PROJ_ID.format(name=proj_name))
        proj_id = proj_container.get_attribute("data-project-id")
        return proj_id

    def edit_click(self, proj_id):
        self.wait_for_visible(self.EDIT.format(id=proj_id))
        self.driver.find_element_by_xpath(self.EDIT.format(id=proj_id)).click()

    def watch_click(self, proj_id):
        self.wait_for_visible(self.WATCH.format(id=proj_id))
        self.driver.find_element_by_xpath(self.WATCH.format(id=proj_id)).click()

    def delete_click(self, proj_id):
        self.wait_for_visible(self.DELETE.format(id=proj_id))
        self.driver.find_element_by_xpath(self.DELETE.format(id=proj_id)).click()

    def clone_click(self, proj_id):
        self.wait_for_visible(self.CLONE.format(id=proj_id))
        self.driver.find_element_by_xpath(self.CLONE.format(id=proj_id)).click()


class TagList(Component):
    TAG_BTN = '//div[@data-t-value="{name}"]'

    def tag_click(self, tag_name):
        self.wait_for_visible(self.TAG_BTN.format(name=tag_name))
        self.driver.find_element_by_xpath(self.TAG_BTN.format(name=tag_name)).click()
