from components.notes_component import NotesComponent
from components.page import Page
from constants import dialog


class NotesPage(Page):
    PAGE = '/technopark55/statuses'

    def __init__(self, driver):
        super(NotesPage, self).__init__(driver)
        self.notes_component = NotesComponent(self.driver)

    def public_note(self):
        self.notes_component.get_note_input().click()
        self.notes_component.get_note_input_text().send_keys(dialog.TEST_MESSAGE)
        self.notes_component.get_submit_button().click()

    def delete_note(self):
        self.get_hover(self.notes_component.get_note_href())
        self.notes_component.get_delete_href().click()

    def open_friends_list(self):
        self.notes_component.get_friends_news_button().click()

    def get_href_data(self):
        print self.notes_component.get_note_href().get_attribute('href')[-14:]
        return self.notes_component.get_note_href().get_attribute('href')[-14:]

    def get_receiver_href_data(self):
        try:
            if self.notes_component.get_note_receiver_href() is False:
                return False
            return self.notes_component.get_note_receiver_href().get_attribute('href')[-14:]
        except AttributeError:
            return False

    def get_check_searching(self):
        return self.notes_component.get_check_search()



