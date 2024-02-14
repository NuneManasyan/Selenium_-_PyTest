from selenium.webdriver.common.by import By
from Helper_functions.helpers import Helper
import logging
import my_config
from Test_data.data import credentials



class Register(Helper):    
    first_name_loc = (By.ID, "user[first_name]")
    last_name_loc = (By.ID, "user[last_name]")
    email_loc = (By.ID, "user[email]")
    password_loc = (By.ID, "user[password]")
    terms_of_use_loc = (By.ID, "user[terms]")
    sign_up_btn = (By.XPATH, '//button[@class="button button-primary g-recaptcha"]')  
    user_credentials_loc = (By.XPATH, '//button[@class="dropdown__toggle-button"]')
    first_name = credentials['first_name']
    last_name = credentials['last_name']
    email = credentials['email']
    password = credentials['password']
    
    def save_fake_credentials_in_json(self):
        self.write_to_json (credentials, my_config.json_file_path)
        logging.info(f"Fake credentials were saved in {my_config.json_file_name}")

    def registration(self):        
        try:            
            self.find_element_by_id(self.first_name_loc).send_keys(self.first_name)
            logging.info("'First name' was entered.")
            self.find_element_by_id(self.last_name_loc).send_keys(self.last_name)    
            logging.info("'Last name' was entered.")   
            self.find_element_by_id(self.email_loc).send_keys(self.email)
            logging.info("'Email' was entered.")
            self.find_element_by_id(self.password_loc).send_keys(self.password)
            logging.info("'Password' was entered.")
            self.find_element_by_id(self.terms_of_use_loc).click()
            logging.info("Checkbox for the 'Terms of use' button was checked.")

            self.find_element_and_click(self.sign_up_btn)
            logging.info("'Sign_up' button was clicked.")
            
            self.make_screenshot("success_register_screen.png")

        except Exception as e:
            logging.error(f"An error occurred while registering: {e}")
            self.make_screenshot("failed_register_screen.png")


    def find_user_credentials_in_homepage(self):
        self.wait_until_element_visible(self.user_credentials_loc)
        logging.info("User credentials were displayed after successful register.")
                   

             
    
    
    
