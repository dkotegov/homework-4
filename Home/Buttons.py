from Base import Component


class Buttons(Component):
    VIEW_SELECTOR = '//div[@data-name="view"]'
    SORT_SELECTOR = '//div[@data-name="sort"]'
    LIST_VIEW_SELECTOR = '//div[@data-name="viewList"]'
    THUMBS_VIEW_SELECTOR = '//div[@data-name="viewThumbs"]'

    SORT_BY_ALPHABET_SELECTOR = '//div[@data-name="sortName"]'
    SORT_BY_SIZE_SELECTOR = '//div[@data-name="sortSize"]'
    SORT_BY_DATE_SELECTOR = '//div[@data-name="sortDate"]'

    FILTER_SELECTOR = '//span[@bem-id="69"]'
    FILTER_IMAGE_SELECTOR = '//span[@data-input-name="image"]'
    FILTER_FOLDER_SELECTOR = '//span[@bem-id="102"]'
    FILTER_ALL_SELECTOR = '//span[@data-input-name="all"]'

    def change_view(self):
        self._wait_until_and_click_elem_by_xpath(self.VIEW_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.LIST_VIEW_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.VIEW_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.THUMBS_VIEW_SELECTOR).click()

    def sort_by_alphabet(self):
        self._wait_until_and_click_elem_by_xpath(self.SORT_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.SORT_BY_ALPHABET_SELECTOR).click()

    def sort_by_size(self):
        self._wait_until_and_click_elem_by_xpath(self.SORT_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.SORT_BY_SIZE_SELECTOR).click()

    def sort_by_date(self):
        self._wait_until_and_click_elem_by_xpath(self.SORT_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.SORT_BY_DATE_SELECTOR).click()

    def filter_by_image(self):
        self._wait_until_and_click_elem_by_xpath(self.FILTER_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.FILTER_IMAGE_SELECTOR).click()

    def filter_by_all(self):
        self._wait_until_and_click_elem_by_xpath(self.FILTER_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.FILTER_ALL_SELECTOR).click()