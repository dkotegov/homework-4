from BasicPage import BasicPage

class MainPage(BasicPage):
  signout_button = '#PH_logoutLink'
  
  def click_signout(self):
    elem = self.wait_render(self.signout_button)
    elem.click()
