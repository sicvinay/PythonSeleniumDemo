import time

from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/#top")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@value='option1']").click()
