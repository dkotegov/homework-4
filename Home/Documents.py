from Base import Component


class Documents(Component):
    CREATE_SELECTOR = '//div[@data-name="create"]'
    REMOVE_SELECTOR = '//div[@data-name="remove"]'
    CREATE_DOCUMENT_SELECTOR = '//div[@data-name="createDocx"]'
    CREATE_PRESENTATION_SELECTOR = '//div[@data-name="createPptx"]'
    CREATE_TABLE_SELECTOR = '//div[@data-name="createXlsx"]'
    DOC_XPATH_BY_NAME = '//a[@data-qa-type="file" and @data-qa-name="{}"]'
    CONFIRM_DELETE_DOC_BUTTON = '//div[@class="b-layer__controls__buttons"]/button[@data-name="remove"]'

    def create_simple_document(self):
        self._wait_until_and_click_elem_by_xpath(self.CREATE_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.CREATE_DOCUMENT_SELECTOR).click()

    def create_presentation(self):
        self._wait_until_and_click_elem_by_xpath(self.CREATE_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.CREATE_PRESENTATION_SELECTOR).click()

    def create_table(self):
        self._wait_until_and_click_elem_by_xpath(self.CREATE_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.CREATE_TABLE_SELECTOR).click()

    def check_document_exists(self, doc_name):
        return self._check_if_element_exists_by_xpath(self.DOC_XPATH_BY_NAME.format(doc_name))

    def delete_doc(self):
        self._wait_until_and_click_elem_by_xpath(self.REMOVE_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.CONFIRM_DELETE_DOC_BUTTON).click()

    def select_file(self, filename):
        self._wait_until_and_click_elem_by_xpath(self.DOC_XPATH_BY_NAME.format(filename)).click()