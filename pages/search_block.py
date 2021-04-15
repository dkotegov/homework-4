from pages.base_component import Component


class SearchBlock(Component):
    SEARCH_INPUT = '//input[contains(@class, "search-block__search-input")]'
    SEARCH_BLOCK_CONTAINER = '//div[contains(@class, "search-block__offers")]'
    SEARCH_OFFER = '//div[contains(@class, "search-block__offer")]'
    SEARCH_CANCEL = '//button[@class="search-block__cancel-button"]'

    def get_search_offers(self):
        return self._find_elements(self.SEARCH_OFFER)

    def enter_search_query(self, query):
        self._wait_until_clickable(self.SEARCH_INPUT)
        self._find_element(self.SEARCH_INPUT).send_keys(query)

