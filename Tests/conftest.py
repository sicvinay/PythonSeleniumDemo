import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.implicitly_wait(5)
    driver.fullscreen_window()
    request.cls.driver = driver
    yield
    driver.close()
