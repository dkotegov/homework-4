from components.base_component import BaseComponent


class PrivacyForm(BaseComponent):
    ALL_USERS = "@value = '0'"
    ONLY_FRIENDS = "@value = '1'"
    NO_ONE   = "@value = '2'"
    TAG_MY_PHOTO = "@name='st.accessForMAKE_PHOTOPINS'"
    SAVE_BUTTON = "//input[@id='hook_FormButton_button_changeProfileType']"
    

    def get_radiobutton_by_name_and_value(self, name, value):
        return self.get_clickable_element("//input["+ name + " and "+ value + "]")
    def get_save_button(self):
        return self.get_clickable_element(self.SAVE_BUTTON)
