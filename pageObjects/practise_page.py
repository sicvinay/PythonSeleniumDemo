from selenium.webdriver.common.by import By

class practise_page:
    def __init__(self, driver):
        self.driver = driver

    button_option = "radio2"
    radio_button = (By.XPATH, f"//div[@id='radio-btn-example']//input[@value='{button_option}']")
    def getRadioButton(self):
        return self.driver.find_element(*practise_page.radio_button)

    suggest_country = (By.ID, "autocomplete")
    def getCountry(self):
        return self.driver.find_element(*practise_page.suggest_country)

    suggest_country_options = (By.XPATH, "//li[@class='ui-menu-item']")
    def getCountryOptioins(self):
        return self.driver.find_elements(*practise_page.suggest_country_options)


    dropdown_button = (By.ID, 'dropdown-class-example')
    def getDropDownButton(self):
        return self.driver.find_element(*practise_page.dropdown_button)


    select_dropdown = (By.XPATH, "//select[@id='dropdown-class-example']//option")
    def getDropDownSelection(self):
        return self.driver.find_elements(*practise_page.select_dropdown)

    checkboxOption = "option1"
    checkboxButton = (By.XPATH, f"//input[@value='{checkboxOption}']")
    def getCheckboxButton(self):
        return self.driver.find_element(*practise_page.checkboxButton)
