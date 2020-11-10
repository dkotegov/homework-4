from margarita.pages.todo.main_page import MainPage
from margarita.tests.todo.task.default import Test
from egogoger.todo_mail.pages.main_page import MainPage as EgorMainPage


class CreateTaskTest(Test):
    def test(self):
        page = MainPage(self.driver)
        page.create_task("задача")
        count = page.count_tasks()
        self.assertTrue(count > 0)

    def tearDown(self):
        page = EgorMainPage(self.driver)
        page.delete_todos(self)
        self.driver.quit()


class CreateTaskSpacesTest(Test):
    def test(self):
        page = MainPage(self.driver)
        page.create_task("            ")
        count = page.count_tasks()
        self.assertTrue(count > 0)

    def tearDown(self):
        page = EgorMainPage(self.driver)
        page.delete_todos(self)
        self.driver.quit()


class CreateTaskSymbolsTest(Test):
    def test(self):
        page = MainPage(self.driver)
        page.create_task("%$#&@*$@")
        count = page.count_tasks()
        self.assertTrue(count > 0)

    def tearDown(self):
        page = EgorMainPage(self.driver)
        page.delete_todos(self)
        self.driver.quit()