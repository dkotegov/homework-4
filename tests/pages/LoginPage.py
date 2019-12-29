from BasicPage import BasicPage

class LoginPage(BasicPage):
  login_input = '.username input'
  password_input = '.password input'
  next_button = '.last div div:first-child button'
  html_validation = '.password.login-row_error small'
  
  def __init__(self, driver):
    self.driver = driver
  
  def open(self):
    self.driver.get(self.LOGIN_URL)
    
  def enter_login(self,login):
    elem = self.wait_render(self.login_input)
    elem.send_keys(login)
    
  def enter_password(self,login):
    elem = self.wait_render(self.password_input)
    elem.send_keys(login)
    
  def click_next(self):
    elem = self.wait_render(self.next_button)
    elem.click()
    
  def get_valigation_message(self):
    validation_message = self.wait_render(self.html_validation).text
    return validation_message.encode('utf-8', errors='ignore')
    
  def sign_in(self, login, password):
    self.enter_login(login)
    self.click_next()
    self.enter_password(password)
    self.click_next()
    