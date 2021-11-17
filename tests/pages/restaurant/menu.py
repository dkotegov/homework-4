from tests.pages.base import Page


class RestaurantMenuPage(Page):
    """
    Стриница меню ресторана
    """

    """ Section """
    SECTION_NAME = '//h3[@class="section-container__name"]'
    BUTTON_ADD_SECTION = '//span[@class="menu-container__btn"]'
    BUTTON_EDIT_SECTION = '//h3[contains(text(),"{}") and @class="section-container__name"]/../' \
                            'div/img[@class="card__header-icon icon-edit"]'
    BUTTON_OPEN_CONFIRM_DELETE_SECTION = '//h3[contains(text(),"{}") and @class="section-container__name"]/../' \
                            'div/img[@class="card__header-icon icon-delete"]'
    INPUT_SECTION_NAME = '//input[@name="name"]'
    BUTTON_SAVE_SECTION = '//input[@type="submit"]'
    BUTTON_DELETE = '//span[@class="confirmation-success confirmation-btn"]'

    """ Dish """
    BUTTON_ADD_DISH = '//h3[contains(text(),"{}") and @class="section-container__name"]/../../' \
                          'ul/li[@class="card-add card"]'
    INPUT_DISH_NAME = '//input[@name="name"]'
    INPUT_DISH_DESCRIPTION = '//input[@name="description"]'
    INPUT_DISH_COST = '//input[@name="price"]'
    INPUT_DISH_WEIGHT = '//input[@name="weight"]'
    BUTTON_SAVE_DISH = '//input[@type="submit"]'
    SECTION_DISHES_NAME = '//span[@class="card__name"]'
    BUTTON_EDIT_DISH = '//span[contains(text(),"{}") and @class="card__name"]/../' \
                      'div/img[@class="card__header-icon icon-edit"]'
    BUTTON_OPEN_CONFIRM_DELETE_DISH = '//span[contains(text(),"{}") and @class="card__name"]/../' \
                       'div/img[@class="card__header-icon icon-delete"]'

    """ Error """
    ERROR_SECTION_NAME = '//p[@id="nameError"]'
    ERROR_DISH_NAME = '//p[@id="nameError"]'
    ERROR_DISH_DESCRIPTION = '//p[@id="descriptionError"]'
    ERROR_DISH_COST = '//p[@id="priceError"]'
    ERROR_DISH_WEIGHT = '//p[@id="weightError"]'

    def __init__(self, driver):
        self.PATH = 'restaurant/menu'
        super(RestaurantMenuPage, self).__init__(driver)

    """ SECTION """
    def open_new_section_form(self):
        self.driver.find_element_by_xpath(self.BUTTON_ADD_SECTION).click()

    def open_section_form(self, name):
        self.driver.find_element_by_xpath(self.BUTTON_EDIT_SECTION.format(name)).click()

    def set_section_name(self, name):
        elem = self.driver.find_element_by_xpath(self.INPUT_SECTION_NAME)
        elem.clear()
        elem.send_keys(name)

    def save_section(self):
        self.driver.find_element_by_xpath(self.BUTTON_SAVE_SECTION).click()

    def get_all_sections_name(self):
        elements = self.driver.find_elements_by_xpath(self.SECTION_NAME)
        sections = []
        for i in range(len(elements)):
            elements = self.driver.find_elements_by_xpath(self.SECTION_NAME)  # need to become stable
            sections.append(elements[i].text)
        return sections

    def open_delete_section_confirm(self, name):
        self.driver.find_element_by_xpath(self.BUTTON_OPEN_CONFIRM_DELETE_SECTION.format(name)).click()

    def delete_section_in_confirm(self):
        self.driver.find_element_by_xpath(self.BUTTON_DELETE).click()

    def get_section_name_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_SECTION_NAME).text

    """ DISH """
    def open_new_dish_form_in_section(self, section_name):
        self.driver.find_element_by_xpath(self.BUTTON_ADD_DISH.format(section_name)).click()

    def set_dish_name(self, name):
        elem = self.driver.find_element_by_xpath(self.INPUT_DISH_NAME)
        elem.clear()
        elem.send_keys(name)

    def set_dish_description(self, description):
        elem = self.driver.find_element_by_xpath(self.INPUT_DISH_DESCRIPTION)
        elem.clear()
        elem.send_keys(description)

    def set_dish_cost(self, cost):
        elem = self.driver.find_element_by_xpath(self.INPUT_DISH_COST)
        elem.clear()
        elem.send_keys(cost)

    def set_dish_weight(self, weight):
        elem = self.driver.find_element_by_xpath(self.INPUT_DISH_WEIGHT)
        elem.clear()
        elem.send_keys(weight)

    def save_dish(self):
        self.driver.find_element_by_xpath(self.BUTTON_SAVE_DISH).click()

    def get_all_dishes_name(self):
        elements = self.driver.find_elements_by_xpath(self.SECTION_DISHES_NAME)
        dishes = []
        for i in range(len(elements)):
            elements = self.driver.find_elements_by_xpath(self.SECTION_DISHES_NAME)  # need to become stable
            dishes.append(elements[i].text)
        return dishes

    def open_dish_form_in_section(self, dish_name):
        self.driver.find_element_by_xpath(self.BUTTON_EDIT_DISH.format(dish_name)).click()

    def open_delete_dish_confirm(self, dish_name):
        self.driver.find_element_by_xpath(self.BUTTON_OPEN_CONFIRM_DELETE_DISH.format(dish_name)).click()

    def delete_dish_in_confirm(self):
        self.driver.find_element_by_xpath(self.BUTTON_DELETE).click()

    def get_dish_name_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_DISH_NAME).text

    def get_dish_description_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_DISH_DESCRIPTION).text

    def get_dish_cost_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_DISH_COST).text

    def get_dish_weight_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_DISH_WEIGHT).text
