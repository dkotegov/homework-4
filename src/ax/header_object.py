from base_page_object import BasePageObject
from time import sleep



def log(msg):
    print msg
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


    def click_filter_on_search(self, filter_type):
        log('-----------------------------------------------')
        
        # sleep(0.1)

        self.search_panel = self.find_search_panel()
        #self.fix_page('.sources/element_found_'+filter_type+'.html')
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
        
        #self.fix_page('.sources/element_found_'+filter_type+'.html')

        filter_element.click()
        log(self.search_panel_state + ': element clicked')

        #self.fix_page('.sources/after_click_element_'+filter_type+'.html')
        
        # sleep(0.3)
        
        # Searching filter-in-row element
        self.find_element_by(
            'css',
            self.css_selectors['filters']['check_in_line'][filter_type],
            clickable=True
        )
        log(self.search_panel_state + ': row element found')

        # self.fix_page('.sources/row_element_found_'+filter_type+'.html')


        self.empty_click()
        log(self.search_panel_state + ': empty click ')

        self.search_panel_state = 'search_panel_args'
        log('update state: ' + self.search_panel_state)
        log('-----------------------------------------------')

