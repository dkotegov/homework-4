# coding=utf-8
from base import BasePage
from tests.elements.main import MainElements
from tests.elements.send_message import SendMessageElements

from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    url = 'https://e.mail.ru/messages/'

    def get_username(self):
        return MainElements(self.driver).user_email().wait_for_visible().get().text

    def send_message(self, email, subj, txt):
        MainElements(self.driver).send_message_elem().wait_for_clickable().get().click()

        to = SendMessageElements(self.driver).send_to().wait_for_clickable().get()
        to.click()
        to.clear()
        to.send_keys(email + ' ')

        subject = SendMessageElements(self.driver).send_subject().wait_for_visible().get()
        subject.click()
        subject.clear()
        subject.send_keys(subj)

        text = SendMessageElements(self.driver).send_text().wait_for_clickable().get()
        text.click()
        text.clear()
        text.send_keys(txt)

        SendMessageElements(self.driver).send_button().wait_for_clickable().get().click()
        return True

    def check_recieve_message(self):
        self.navigate()

        MainElements(self.driver).recieve_elem().wait_for_presence().get().click() 

        MainElements(self.driver).last_recieve_elem().wait_for_visible().get().click()
        subject = MainElements(self.driver).subject_elem().wait_for_presence().get().text
        text = MainElements(self.driver).text_elem().wait_for_presence().get().text
        to = MainElements(self.driver).to_elem().wait_for_presence().get().text
        return to, subject, text

        


    def check_sent_message(self):
        self.navigate()

        MainElements(self.driver).sent_message_elem().wait_for_presence().get().click()

        MainElements(self.driver).last_message_elem().wait_for_visible().get().click()

        subject = MainElements(self.driver).subject_elem().wait_for_presence().get().text
        text = MainElements(self.driver).text_elem().wait_for_presence().get().text
        to = MainElements(self.driver).to_elem().wait_for_presence().get().text
        return to, subject, text

    def delete_sent(self):
        self.navigate()
        MainElements(self.driver).sent_message_elem().wait_for_presence().get().click()
        check_box = MainElements(self.driver).last_checkbox().wait_for_clickable().get()
        del_elem = MainElements(self.driver).delete_elem().wait_for_presence().get()
        self.driver.execute_script("$(arguments[0]).click();", del_elem)

    def delete_recieve(self):
        self.navigate()
        MainElements(self.driver).recieve_elem().wait_for_presence().get().click()
        check_box = MainElements(self.driver).last_recieve_checkbox().wait_for_clickable().get()
        del_elem = MainElements(self.driver).delete_elem().wait_for_presence().get()
        self.driver.execute_script("$(arguments[0]).click();", del_elem)


