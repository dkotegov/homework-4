from base_page_object import BasePageObject
from time import sleep

from selenium.common.exceptions import TimeoutException


def log(msg):
    print "HeaderObject: " + msg
    pass



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
        log('-----------------------------------------------')
        
        # sleep(0.1)

        try_count = 10

        while try_count:

            self.empty_click()
            log(self.search_panel_state + ': empty click ')
            
            self.search_panel = self.find_search_panel()
            self.search_panel.click()

            log(self.search_panel_state + ': clicked search panel')
            log(self.search_panel_state + ': search element ' + self.css_selectors['filters']['search_panel'][filter_type])

            # Searching filter button
            filter_element = self.find_element_by(
                'css',
                self.css_selectors['filters']['search_panel'][filter_type],
                clickable=True
            )
            log(self.search_panel_state + ': element found')
            

            filter_element.click()
            log(self.search_panel_state + ': element clicked')            
            
            try:
                # Searching filter-in-row element
                self.find_element_by(
                    'css',
                    self.css_selectors['filters']['check_in_line'][filter_type],
                    clickable=True
                )
                log(self.search_panel_state + ': row element found')
            except TimeoutException:
                try_count -= 1
            else: 
                try_count = 0
                self.search_panel_state = 'search_panel_args'
                log('update state: ' + self.search_panel_state)


            # self.fix_page('.sources/row_element_found_'+filter_type+'.html')


            self.empty_click()
            log(self.search_panel_state + ': empty click ')

            log('-----------------------------------------------')