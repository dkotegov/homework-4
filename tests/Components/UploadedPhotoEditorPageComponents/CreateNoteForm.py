from tests.Components.Component import Component


class CreateNoteForm(Component):
    NOTE_TEXT_AREA = '//textarea[@name="st.description"]'
    CREATE_NOTE_BUTTON = '//input[@name="postAfterUpload"]'

