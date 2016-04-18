from pages import Input


class DragAndDrop(Input):
    INPUT = '//input[@class="drop-zone__input"]'


class FileInput(Input):
    INPUT = '//input[@class="layer_upload__controls__input"]'
