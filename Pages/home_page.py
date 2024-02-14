from selenium.webdriver.common.by import By
from Helper_functions.helpers import Helper
import logging


class HomePage(Helper):
    sign_in_loc = (By.XPATH, '//a[@href="/users/sign_in"]') 
    create_a_new_account_loc =(By.XPATH, '//a[@href="/users/sign_up"]')
    i_already_have_an_account_loc = (By.XPATH,'//aside[@class="sign-up__sign-in"]')

    def go_to_create_a_new_account(self):        
            try:            
                self.find_element_and_click(self.sign_in_loc)
                logging.info("'Sign in' button was clicked.")
                self.find_element_and_click(self.create_a_new_account_loc)
                logging.info("'Create a new account' button was clicked.")
                self.wait_for_element_in_dom(self.i_already_have_an_account_loc)
                logging.info("User was navigated to 'Create a new account' page.")
            except Exception as e:
                logging.error(f"An error occurred while navigating to 'Create a new account' page: {str(e)}")