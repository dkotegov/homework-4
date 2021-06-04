from Pages.profile_page import ProfilePage


def get_profile_login(t):
    profile_page = ProfilePage(t.driver)
    profile_page.open()
    return profile_page.get_username()
