import pytest

# @pytest.fixture(scope="module") it will run only once since its defined scope as module

# @pytest.fixture This block of function will run when each function is called +
# if parameterized in any function

# use above 2 fixtures and run and check one by one
@pytest.fixture(scope="module")
def browswersetup():
    print("Open Chrome browser")

def test_initialcheck(browswersetup):
    print("Hi This is a my first playwrite class")

def test_secondcheck(browser):
    print("This is second function")



# Command to run only one funcition in a class file
# pytest test_PytestValidation.py::test_initialcheck

# pytest <File name>:: <Function name>

# pytest <File name>:: <Function name> -s (Print logs also use -s)