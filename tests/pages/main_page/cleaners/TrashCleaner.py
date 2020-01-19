from tests.pages.BasicPage import BasicPage
from tests.pages.main_page.confirmationers.RemoveConfirmationer import RemoveConfirmationer

class TrashCleaner(BasicPage):
  link_to_clean_trash = "a.link[rel='noopener noreferer']"
  
  def __init__(self, driver):
    self.driver = driver
    self.remove_confirmationer = RemoveConfirmationer(self.driver)
        
  def click_link_clean_trash(self):
    elem = self.wait_render(self.link_to_clean_trash)
    elem.click()
    
  def clean(self):
    self.click_link_clean_trash()
    self.remove_confirmationer.confirm()
    
  