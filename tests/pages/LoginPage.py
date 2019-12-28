from ..utils.utils import Utils
from .selectors import LoginSelectors as SL

class LoginPage(Utils):
  
  def __init__(self, driver):
    self.driver = driver
  
  def open(self):
    self.driver.get(self.LOGIN_URL)
    self.driver.maxsize_window()
    
  def enter_login(self,login):
    elem = self.wait_render(SL.selectors.login_input)
    elem.send_key(login)
    
  def enter_password(self,login):
    elem = self.wait_render(SL.selectors.password_input)
    elem.send_key(login)
    
  def click_next(self):
    elem = self.wait_render(SL.selectors.next_button)
    elem.click()