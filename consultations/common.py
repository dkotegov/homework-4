# -*- coding: utf-8 -*-
import os

import urlparse
import requests
from dateutil import relativedelta
from datetime import datetime

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def _del_key_safe(dict_, key):
    try:
        del dict_[key]
    except KeyError:
        pass

def has_class(element, class_name):
    return class_name in element.get_attribute('class')

def save_window(f): 
    def wrapper(self, *args, **kwargs):
        result = f(self, *args, **kwargs) 
        self.driver.back()
        return result
    return wrapper 
    
class Common(object):
    PAGE_TITLE_SELECTOR = '.page-info__title'
    
    #possible args: [by], timeout
    def _wait_for_element(self, **kwargs): #throws TimeoutException
        DEFAULT_WAIT_TIMEOUT = 30
        timeout = kwargs.get('timeout', DEFAULT_WAIT_TIMEOUT) 
        _del_key_safe(kwargs, 'timeout')
        key = kwargs.keys()[0]
        return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((key, kwargs.get(key))))
        
    def get_title(self):
        return self._wait_for_element(**{By.CSS_SELECTOR: self.PAGE_TITLE_SELECTOR}).text
       
    def go_to_iframe(self):
       iframe = self._wait_for_element(**{By.TAG_NAME: 'iframe'})
       self.driver.switch_to_frame(iframe)
 
class Component(Common):
    def __init__(self, driver):
        self.driver = driver
        
class LoginForm(Component):
    LOGIN = 'Username'
    PASSWORD = 'Password'
    SUBMIT = '.btn_form'
    
    def set_login(self, login):
        login_element = self._wait_for_element(**{By.NAME: self.LOGIN})
        login_element.send_keys(login) 
        
    def set_password(self):
        password_element = self._wait_for_element(**{By.NAME: self.PASSWORD})
        password_element.send_keys(os.environ.get('HW4PASSWORD', ''))
        
    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()
                   
class Page(Common):
    BASE_URL = 'https://health.mail.ru/consultation/'
    PATH = ''
    OPEN_FORM_BUTTON = 'a.button'
    LOGIN_IFRAME_CLASS = 'iframe.ag-popup__frame__layout__iframe'
    LOGIN_LINK_ID = 'PH_authLink'
    USERNAME = 'test.test.tp@mail.ru'

    def trigger_login(self):
        self._wait_for_element(**{By.ID: self.LOGIN_LINK_ID}).click()
           
    def __init__(self, driver, **kwargs):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()
        
    def get_breadcrumbs(self):
        return self.driver.find_element_by_css_selector('div.breadcrumbs__item a.link')
        
    def _login(self):
        login_form = LoginForm(self.driver)
        login_form.set_login(self.USERNAME)
        login_form.set_password()
        login_form.submit()
        
    def try_login(self):
        try:
            iframe = self._wait_for_element(**{By.CSS_SELECTOR: self.LOGIN_IFRAME_CLASS})
            self.driver.switch_to_frame(iframe)
            self._login()
        except TimeoutException:
            pass
                
    def open_form(self):
        self.driver.find_element_by_css_selector(self.OPEN_FORM_BUTTON).click()
        self.try_login()
            
    def is_consult_form_opened(self):
        return self._wait_for_element(**{By.CSS_SELECTOR: '.js-form_ask'})
          

#check presence of necessary fields
class Plate(Component):
    OK_CODES = [200, 301, 302, 304]
    
    def __init__(self, element, *args, **kwargs):
        super(Plate, self).__init__(*args, **kwargs)
        self.element = element
        
    def has_text(self, element):
        return hasattr(element, 'text') and element.text
        
    def has_working_link(self, link):
        r = requests.get(link.get_attribute('href'))
        
        if r.status_code not in self.OK_CODES:
            return False
        return True
        
    def has_image(self, element):
        if element.get_attribute('src'): return True
        styles = element.get_attribute('style')
        if styles.find('background-image') != -1: return True
        return False
        
    @save_window
    def has_link_with_title(self, link):
        title = link.text
        link.click()
        return (self.get_title().find(title) != -1)

        
    def wait_for_stale_element(self, selector):
        ATTEMPTS_MAX = 2
        attempts = 0;
        while(attempts < ATTEMPTS_MAX):
            try:
                return self.driver.find_element_by_css_selector(selector)
            except :
                pass
            attempts += 1
       
    def check_fields(self):
        for selector in self.INNER_FIELDS:
            element = self.wait_for_stale_element(selector.get('css_selector'))
            #self.driver.find_element_by_css_selector(selector.get('css_selector'))
            if element and not getattr(self, selector.get('check_function'))(element):
               return False
        return True
 
class QuestionPlate(Plate):
    INNER_FIELDS = [ 
        {   #rubric
            'css_selector': '.entry__info-link',
            'check_function': 'has_link_with_title'
        },
        {   #title
            'css_selector': 'div.entry__name a.entry__link',
            'check_function': 'has_link_with_title'
        },
        {   #descrption
            'css_selector': '.entry__description',
            'check_function': 'has_text'
        }                
    ]
    
# pagination
# valid plates
class QuestionsList(Component):
    NEXT_PAGE_SELECTOR = '.paging__link_nav_next'
    
    def __init__(self, *args, **kwargs):
        self.QuestionPlate = kwargs.get('plate_class', QuestionPlate)
        _del_key_safe(kwargs, 'plate_class')
        super(QuestionsList, self).__init__(*args, **kwargs)
        
    def check_plates(self):
        element = self.driver.find_element_by_css_selector('div.entry')
        if not self.QuestionPlate(element, self.driver).check_fields(): return False
        return True
        
    def go_to_next_page(self):
        self._wait_for_element(**{By.CSS_SELECTOR: self.NEXT_PAGE_SELECTOR}).click()
    
    @save_window
    def is_valid(self):
        if not self.check_plates(): return False
        self.go_to_next_page()
        if not self.check_plates(): return False
        return True

class SliderPlate(Plate):
    INNER_FIELDS = [ 
        {   #avatar
            'css_selector': 'div.consultant-slider__avatar .avatar',
            'check_function': 'has_image'
        },
        {   #link
            'css_selector': 'a.consultant-slider',
            'check_function': 'has_working_link'
        },                      
    ]
    
class Slider(Component):
    SLIDES_PER_GROUP = 4
    SLIDER_SELECTOR = '.slider__item'
    NEXT_SLIDES_SELECTOR = '.js-slider__next'
    SLIDER_ITEM_SELECTOR = '.slider__item'
    SLIDER_ACTIVE_ITEM_SELECTOR = '.slider__item_active'
    SLIDER_CLONE_CLASS = 'js-slider__clone'
    
    def check_plates(self):
        element = self.driver.find_element_by_css_selector(self.SLIDER_SELECTOR)
        if not SliderPlate(element, self.driver).check_fields(): return False
        return True
        
    def check_next_slides_group(self):
        self.driver.find_element_by_css_selector(self.NEXT_SLIDES_SELECTOR).click()
        for i_, element in enumerate(self.driver.find_elements_by_css_selector(self.SLIDER_ITEM_SELECTOR)):
            if has_class(element, self.SLIDER_ACTIVE_ITEM_SELECTOR) and \
               has_class(element, self.SLIDER_CLONE_CLASS) and int(i / self.SLIDES_PER_GROUP) != 1:
                return False
        return True
        
    def is_valid(self): 
        if not self.check_plates(): return False
        if not self.check_next_slides_group(): return False
        return True  
                       
class AskConsultantForm(Component):
    TITLE = 'title'
    DESCRIPTION = 'text'
    RUBRIC = 'rubric'
    CONSULTANT = 'consultant'
    GENDER = 'gender'
    AGE = 'age'
    ANONYMOUS = 'hide_personal_info'
    SUBMIT = 'button.button'
    
    DEFAULT_GENDER = 'female'
    BIRTHDAY_TUPLE = (1994, 04, 24)
    
    @property
    def DEFAULT_AGE(self):
        return relativedelta.relativedelta(datetime.now(), datetime(*self.BIRTHDAY_TUPLE)).years

    def set_title(self, title):
        self.driver.find_element_by_name(self.TITLE).send_keys(title)

    def set_description(self, description):
        self.driver.find_element_by_name(self.DESCRIPTION).send_keys(description)

    def select_rubric(self, rubric):
        selector = self.driver.find_element_by_name(self.RUBRIC)
        for option in selector.find_elements_by_tag_name('option'):
            if option.text == rubric:
                option.click()
                break
                
    def select_consultant(self, consultant):
        selector = self.driver.find_element_by_name(self.CONSULTANT)
        for option in selector.find_elements_by_tag_name('option'):
            if option.text == consultant:
                option.click()
                break
                        
    def select_gender(self, gender): #female or male
        for gender_radiobutton in self.driver.find_elements_by_name(self.GENDER):
            if gender_radiobutton.get_attribute('value') == gender:
                gender_radiobutton.click()
        
    def set_age(self, age):
        self.driver.find_element_by_name(self.AGE).send_keys(age)
        
    def change_anonymous(self):
        self.driver.find_element_by_name(self.ANONYMOUS).click()
        
    def check_preselect_category(self, category):
        selector = self.driver.find_element_by_name(self.RUBRIC)
        return selector.find_element_by_css_selector('.js-select__selected__option').text == category
        
    def check_preselect_doctor(self, doctor):
        selector = self.driver.find_element_by_name(self.CONSULTANT)
        return selector.find_element_by_css_selector('.js-select__selected__option').text == consultant
        
    def check_preset_age(self):
        return int(self._wait_for_element(**{By.NAME: self.AGE}).get_attribute('value')) == self.DEFAULT_AGE
        
    def check_preset_gender(self):
        for gender_radiobutton in self.driver.find_elements_by_name(self.GENDER):
            if gender_radiobutton.get_attribute('value') == self.DEFAULT_GENDER and gender_radiobutton.is_selected():
                return True
        return False
        
    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()    
   

        
