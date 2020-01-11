from tests.pages.BasicPage import BasicPage
from selenium.webdriver import ActionChains

class NotificationManager(BasicPage):
    notify_inline = '.notify_inline'
    hide_notification_button = '.button2_actions_close'
    
    def hide_notification(self):
        elem = self.wait_render(self.hide_notification_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        self.wait_invisible(self.notify_inline)