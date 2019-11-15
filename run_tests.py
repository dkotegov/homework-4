import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfileTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    # def login(self): 

    # REWRITE!!!
    def wait(self, wait_until=None, timeout=5):
        return WebDriverWait(self.driver, timeout).until(wait_until)

    # REWRITE!!!
    def wait_redirect(self, url=None):
        if url is None:
            self.wait(EC.url_changes(self.driver.current_url))
        else:
            self.wait(EC.url_matches(url))
        

    def test_tick_in_time_zone(self):   
        driver = self.driver
        driver.get("https://e.mail.ru/settings/userinfo?afterReload=1")
        # driver.get("https://e.mail.ru/login")
        self.assertIn("Mail.ru", driver.title)

        frame = self.driver.find_element_by_css_selector('#auth-form iframe')
        self.driver.switch_to.frame(frame)

        email = driver.find_element_by_css_selector('input[name=Login]')
        email.send_keys("yekaterina.kirillova.1998@bk.ru")
        email.submit()

        password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=Password]"))
        )
        password.send_keys("qwerYtuarRyYY12")
        password.submit()


        submit = self.driver.find_element_by_css_selector('button[type=submit]')
        submit.click()
        # driver = self.driver   
        # driver.get("https://e.mail.ru/settings/userinfo?afterReload=1")
        self.wait_redirect('https://e.mail.ru/settings/userinfo?afterReload=1')
        # tick = WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=UseAutoTimezone]"))
        # )
        tick = drNJR iver.find_element_by_css_selector('input[name=UseAutoTimezone]')
        tick.click()
        
        # self.assertIn("Python", driver.title)
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("pycon")
        # assert "No results found." not in driver.page_source
        # elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()