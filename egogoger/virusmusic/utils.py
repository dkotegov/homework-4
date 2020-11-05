from egogoger.utils import get_datetime


def get_correct_values():
	timestamp = get_datetime()
	return ['Name_'+timestamp, 'Login_'+timestamp, 'email_'+timestamp+'@mail.ru', 'password', 'password']