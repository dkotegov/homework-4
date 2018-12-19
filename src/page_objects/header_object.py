from base_page_object import BasePageObject



class HeaderObject(BasePageObject):
    
    filter_button = None
    search_panel  = None

    css_selectors = {
        'search_panel': {
            'unread': 'div[class="search-panel-recent-item search-panel-recent-item_flag search-panel-recent-item_flag_unread"]'
        }
    }

    def __init__(self, layout, wait):
        super(HeaderObject, self).__init__(layout, wait)

        self.filter_button = self.find_element_by(
            'css', 
            'div[class="filters-control filters-control_short filters-control_pure"]',
            clickable=True
        )

        self.search_panel = self.find_element_by(
            'css', 
            'div[class="search-panel-button js-shortcut"]',
            clickable=True
        )

    def click_filter_on_search(self, filter_type):
        self.search_panel.click()

        filter_element = self.find_element_by(
            'css',
            self.css_selectors['search_panel'][filter_type],
            clickable=True
        )

        filter_element.click()


