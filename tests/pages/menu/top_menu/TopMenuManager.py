from tests.pages.BasicPage import BasicPage

class TopMenuManager(BasicPage):
  top_menu_move = 'div.portal-menu-element_move'
  top_menu_trash = 'div.portal-menu-element_remove'
  
  def click_menu_remove_letter_button(self):
    elem = self.wait_render(self.top_menu_trash)
    elem.click()
    
  def click_top_menu_move_letter_button(self):
    elem = self.wait_render(self.top_menu_move)
    elem.click()