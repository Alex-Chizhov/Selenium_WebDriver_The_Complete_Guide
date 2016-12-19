import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.maximize_window()
    request.addfinalizer(wd.quit)
    return wd
