class WrongData(object):
    LONG_LASTNAME = 'Technoparktechnoparktechnoparktechnoparktechnoparktechnoparktechnoparktechnoparktechnoparktechnoparktechnopark'
    LONG_FIRSTNAME = 'Testemailtestemailtestemailtestemailtestemailtestemailtestemailtestemailtestemailtestemailtestemailtestemailss'
    WRONG_CODE_COUNTRY = '1432123'
    WRONG_CODE_CITY = 'test'
    WRONG_PHONE_NUMBER = '321412test'
    WRONG_INSTITUTION_NAME = ''
    WRONG_FACULTY = ''
    WRONG_OBJECTIVE = ''

    def set_up_wrong_data(self):
        for i in range(0, 522):
            self.WRONG_INSTITUTION_NAME += 'a'

        for i in range(0, 138):
            self.WRONG_FACULTY += 'b'

        for i in range(0, 110):
            self.WRONG_OBJECTIVE += 'c'

