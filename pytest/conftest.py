import pytest

@pytest.fixture(scope="session")
def browser():
    print("Conf test file browser")
