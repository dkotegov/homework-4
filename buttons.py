from pages import Button


class EnterButton(Button):
    BUTTON = '//*[@id="PH_authLink"]'
    CHECK_ELEMENT = '//*[@id="ph_login"]'


class SubmitLoginButton(Button):
    BUTTON = '//span[@data-action="login"]'
    CHECK_ELEMENT = '//span[@data-name="home"]'


class UploadButton(Button):
    BUTTON = '//*[@data-name="upload"]/span'
    CHECK_ELEMENT = '//div[@class="layer_upload"]'
    # CHECK_ELEMENT = '//div[@class="b-layer__container"]'


class CloseUploadFormButton(Button):
    BUTTON = "//div[@class='b-layer__placeholder']/button[@data-name='close']"
    CHECK_ELEMENT = '//span[@data-name="home"]'


class SelectAllCheckbox(Button):
    BUTTON = '//div[@data-name="toggleBtn"]'
    CHECK_ELEMENT = '//div[@data-name="remove"]'


class DeleteButton(Button):
    BUTTON = '//div[@data-name="remove"]'
    CHECK_ELEMENT = '//div[@class="b-layer__container"]'


class DeleteSubmitButton(Button):
    BUTTON = '//button[@data-name="remove"]'
    CHECK_ELEMENT = '//div[@data-name="share"]'


# Oleg
class MoreButton(Button):
    BUTTON = '//div[@data-group="more"]'
    CHECK_ELEMENT = '//a[@data-name="copy"]'


class CopyElementButton(Button):
    BUTTON = '//a[@data-name="copy"]'
    CHECK_ELEMENT = '//div[@class="layer_copy"]'


class DoCopyButton(Button):
    BUTTON = '//button[@data-name="copy"]'
    CHECK_ELEMENT = '//div[@data-name="share"]'


class CreateFolderInCopyButton(Button):
    BUTTON = '//button[@data-name="create-folder"]'
    CHECK_ELEMENT = '//div[@class="layer_add"]'


class CreateButton(Button):
    BUTTON = '//div[@data-group="create"]'
    CHECK_ELEMENT = '//a[@data-name="folder"]'


class CreateFolderButton(Button):
    BUTTON = '//a[@data-name="folder"]'
    CHECK_ELEMENT = '//div[@class="layer_add"]'


# class AddFolderButton(InputName):
#     INPUT = '//button[@data-name="add"]'
class AddFolderButton(Button):
    BUTTON = '//button[@data-name="add"]'
    CHECK_ELEMENT = '//div[@data-name="share"]'
