

test: test-firefox


#----------------------------------------------

test-firefox:
	BROWSER=FIREFOX PASSWORD="333" LOGIN="keker" python ./run_tests.py

test-chrome:
	BROWSER=CHROME PASSWORD="333" LOGIN="keker" python ./run_tests.py