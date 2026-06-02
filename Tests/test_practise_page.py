import time
import pytest
from pageObjects.practise_page import practise_page


@pytest.mark.usefixtures("setup")
class Test_practise_page:

    def setup_method(self):
        self.practise_page_obj = practise_page(self.driver)     #Best way to create a single object that can be utilized to multiple test cases
        self.driver.implicitly_wait(10)                         #Best place to mention implicitly wait to apply on all the test cases together.


    def test_radio_button(self):

        self.practise_page_obj.getRadioButton().click()



    def test_search_country(self):

        self.practise_page_obj.getCountry().send_keys("Ind")
        dropdown_obj = self.practise_page_obj.getCountryOptioins()
        for option in dropdown_obj:
            if option.text == "India":
                option.click()


    def test_dropdown(self):
        self.practise_page_obj.getDropDownButton().click()
        dropdown_obj = self.practise_page_obj.getDropDownSelection()
        for option in dropdown_obj:
            if option.text == "Option3":
                option.click()


    def test_checkbox(self):
        self.practise_page_obj.getCheckboxButton().click()

