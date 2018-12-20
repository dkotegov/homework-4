from base_page_object import BasePageObject
from time import sleep

from selenium.common.exceptions import TimeoutException


TRY_COUNT = 3


class HeaderObject(BasePageObject):
    
    filter_button = None
    search_panel  = None
    search_panel_state = 'search_panel_empty'

    css_selectors = {
        'search_panel_empty': 'span[class="search-panel-button__icon"]',
        'search_panel_args': 'input[class="b-operand__input js-input js-shortcut"]',

        'filters': {
            'search_panel': {
                'unread': 'div[class="search-panel-recent-item search-panel-recent-item_flag search-panel-recent-item_flag_unread"]',
                'flag': 'div[class="search-panel-recent-item search-panel-recent-item_flag search-panel-recent-item_flag_flagged"]',
                'attach': 'div[class="search-panel-recent-item search-panel-recent-item_flag search-panel-recent-item_flag_attach"]',
            },
            'check_in_line': {
                'unread': 'div[data-qa-id="q_read:"]', # 'div[class="b-operand b-operand_q_read"]'
                'flag': 'div[data-qa-id="q_flag:"]',
                'attach': 'div[data-qa-id="q_attach:"]',
            }
        }
    }

    def __init__(self, layout, wait, fix_page):
        super(HeaderObject, self).__init__(layout, wait, fix_page)

        self.filter_button = self.find_element_by(
            'css', 
            'div[class="filters-control filters-control_short filters-control_pure"]',
            clickable=True
        )

        self.search_panel = self.find_search_panel()


    def find_search_panel(self):
        return self.find_element_by(
            'css', 
            self.css_selectors[self.search_panel_state],
            clickable=True
        )

    def empty_click(self):
        self.find_element_by('css', 'div[class="w-x-ph__auth__dropdown__inner"]', clickable=True).click()

    def panel_search_click(self):
        self.search_panel = self.find_search_panel()
        self.search_panel.click()


    def click_filter_on_search(self, filter_type):
        try_count = TRY_COUNT

        while try_count:

            self.empty_click()
            
            self.search_panel = self.find_search_panel()
            self.search_panel.click()

            # Searching filter button
            filter_element = self.find_element_by(
                'css',
                self.css_selectors['filters']['search_panel'][filter_type],
                clickable=True
            )
            
            filter_element.click()
            
            try:
                # Searching filter-in-row element
                self.find_element_by(
                    'css',
                    self.css_selectors['filters']['check_in_line'][filter_type],
                    clickable=True
                )
            except TimeoutException:
                try_count -= 1
            else: 
                try_count = 0
                self.search_panel_state = 'search_panel_args'

            self.empty_click()
           