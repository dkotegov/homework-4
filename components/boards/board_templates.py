from base_classes.component import Component


class BoardTemplates(Component):
    CONTAINER = '//div[@class="group-template-board"]'
    CREATE_WEEK_PLAN_BUTTON = '//div[@data-template-name="week_plan"]'
    CREATE_PROJECT_MANAGEMENT_BUTTON = '//div[@data-template-name="product_management"]'

    WEEK_PLAN_BOARD_NAME = 'План на неделю'
    PROJECT_MANAGEMENT_BOARD_NAME = 'Планирование проекта'

    def create_week_plan_board(self):
        self.driver.find_element_by_xpath(self.CREATE_WEEK_PLAN_BUTTON).click()

    def create_project_management_board(self):
        self.driver.find_element_by_xpath(self.CREATE_PROJECT_MANAGEMENT_BUTTON).click()
