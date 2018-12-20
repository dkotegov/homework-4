from base_page_object import BasePageObject
from time import sleep

def log(msg):
    # print msg
    pass

class HeaderObject(BasePageObject):
    
    filter_button = None
    search_panel  = None
    search_panel_state = 'search_panel_empty'

    css_selectors = {
        'search_panel_empty': 'div[class="search-panel-button js-shortcut"]',
        'search_panel_args': 'input[class="b-operand__input js-input js-shortcut"]',

        'filters': {
            'search_panel': {
                'unread': 'div[class="search-panel-recent-item search-panel-recent-item_flag search-panel-recent-item_flag_unread"]',
                'flag': 'div[class="search-panel-recent-item search-panel-recent-item_flag search-panel-recent-item_flag_flagged"]',
                'attach': 'div[class="search-panel-recent-item search-panel-recent-item_flag search-panel-recent-item_flag_attach"]',
            },
            'check_in_line': {
                'unread': 'div[data-qa-id="q_read:"]',
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


    def click_filter_on_search(self, filter_type):
        log('-----------------------------------------------')
        
        self.search_panel = self.find_search_panel()
        self.search_panel.click()

        log(self.search_panel_state + ': clicked search panel')

        # self.find_element_by('css', 'div[class="search-panel-recent__filters"]')

        log(self.search_panel_state + ': search element ' + self.css_selectors['filters']['search_panel'][filter_type])

        filter_element = self.find_element_by(
            'css',
            self.css_selectors['filters']['search_panel'][filter_type],
            clickable=True
        )
        log(self.search_panel_state + ': element found')

        filter_element.click()
        log(self.search_panel_state + ': element clicked')

        filt = self.find_element_by(
            'css',
            self.css_selectors['filters']['check_in_line'][filter_type],
            clickable=True
        )
        filt.click()
        log(self.search_panel_state + ': element checked in line')

        self.search_panel_state = 'search_panel_args'
        log('update state: ' + self.search_panel_state)
        log('-----------------------------------------------')

