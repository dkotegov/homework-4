import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://sport.mail.ru")
        # self.assertIn("Python", driver.title)
        # elem = driver.find_element_by_xpath(//span[@name='clb6144303']/a)
        elem = driver.find_element_by_name("clb6143763")
        # elem2 = elem.findElement(By.xpath("//span/a"))
        elem.click()
        # elem.send_keys("pycon")
        # assert "No results found." not in driver.page_source
        # elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
