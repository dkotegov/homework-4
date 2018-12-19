from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePageObject(object):

    layout = None
    wait = None
    type_dict = {
        'css': By.CSS_SELECTOR,
        'class': By.CLASS_NAME,
        'id': By.ID,
    }

    def __init__(self, layout, wait):
        self.layout = layout
        self.wait = wait

    def find_element_by(self, by_type, value, clickable=False):
        selector_type = self.type_dict[by_type]
        element = self.wait.until(
            EC.presence_of_element_located(
                (selector_type, value)
            )
        )

        if clickable:
            self.wait.until(
                EC.element_to_be_clickable(
                    (selector_type, value)
                )
            )

        return element


