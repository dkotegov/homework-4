from components.base_component import BaseComponent


class PrivacyForm(BaseComponent):
    ALL_USERS = "@value = '0'"
    ONLY_FRIENDS = "@value = '1'"
    NO_ONE   = "@value = '2'"
    TAG_MY_PHOTO = "@name='st.accessForMAKE_PHOTOPINS'"

    def get_radiobutton_by_name_and_value(self, name, value):
        return self.driver.find_element_by_xpath("//input["+ name + " and "+ value + "]")
