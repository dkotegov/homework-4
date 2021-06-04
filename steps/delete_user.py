from Pages.profile_page import ProfilePage


def delete_user(t):
    profile_page = ProfilePage(t.driver)
    profile_page.open()
    profile_page.delete_user()
