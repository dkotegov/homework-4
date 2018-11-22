from page_object import PageObject

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MessageActivities(PageObject):
    
    def move_all_msgs(self, destination):
        all_dropdown = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.b-dropdown_selectAll > .b-dropdown__ctrl > .b-dropdown__arrow')))
        
        print all_dropdown.is_displayed()
        if not all_dropdown.is_displayed():
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.b-dropdown_selectAll > .b-dropdown__ctrl > .b-dropdown__arrow')))

        all_dropdown.click()

        toggle_data = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.b-dropdown_selectAll > .b-dropdown__list')))
        toggle_data.find_element_by_css_selector('div[data-group="selectAll"] > .b-dropdown__list > a[data-name="all"]').click()
    
        self.__move(destination)

    def move_n_msgs(self, n, destination):
        checkboxes = self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'b-datalist__item__cbx')))
        print len(checkboxes)
        for i in range(0, n):
            checkboxes[i].click()

        self.__move(destination)

    def __move(self, destination):
        move_to = self.driver.find_element_by_css_selector('div[data-group="moveTo"]')
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-group="moveTo"]')))
        move_to.click()

        target_dir = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.b-dropdown__group_ > a[data-text="{}"]'.format(destination))))
        target_dir.click()
        