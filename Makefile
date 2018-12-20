

test: test-chrome test-firefox


#----------------------------------------------

test-firefox:
	BROWSER=FIREFOX PASSWORD="Welc0me_to_Tarad0s!" LOGIN="tarados_feroces" python ./run_tests.py

test-chrome:
	BROWSER=CHROME PASSWORD="Welc0me_to_Tarad0s!" LOGIN="tarados_feroces" python ./run_tests.py
