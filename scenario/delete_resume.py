from pages.edit_resume import EditResumePage
from pages.profile_page import ProfilePage


def delete_resume(test):
    profile_page = ProfilePage(test.driver)
    edit_resume_page = EditResumePage(test.driver)
    edit_resume_form = edit_resume_page.edit_form

    profile_page.open()
    profile_page.click_my_first_resume_edit()
    edit_resume_form.delete_resume()
