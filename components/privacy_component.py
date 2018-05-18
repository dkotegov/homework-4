from components.base_component import BaseComponent


class PrivacyForm(BaseComponent):
    ALL_USERS = "@value = '0'"
    ONLY_FRIENDS = "@value = '1'"
    NO_ONE   = "@value = '2'"
    MY_AGE = "@name='st.accessForAGE_VISIBILITY'"
    MY_GAMES_AND_APPLICATIONS = "@name='st.accessForGAMES_APPS_VISIBILITY'"
    MY_GROUPS = "@name='st.accessForGROUPS_VISIBILITY'"
    MY_SUBSCRIBERS_SUBSCRIPTIONS = "@name='st.accessForSUBSCRIPTION_VISIBILITY'"
    MY_RELETIONSHIP = "@name = 'st.accessForRELATIONS_BLOCK_VISIBILITY'"
    GAMES_INVITE = "@name = 'st.accessForGAMES_INVITE'"
    GROUPS_INVITE = "@name = 'st.accessForGROUPS_INVITE'"
    MARK_IN_TOPIC = "@name = 'st.accessForMARK_IN_TOPICS'"
    SAVE_BUTTON = "//input[@id='hook_FormButton_button_changeProfileType']"

    

    def get_radiobutton_by_name_and_value(self, name, value):
        return self.get_clickable_element("//input["+ name + " and "+ value + "]")
    def get_save_button(self):
        return self.get_clickable_element(self.SAVE_BUTTON)
