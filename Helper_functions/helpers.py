from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
import json
import my_config


class Helper:
    def __init__(self, browser):
        self.browser = browser
        
    def open_url(self, url):
        try:
            self.browser.get(url)
            self.browser.set_page_load_timeout(30)
            logging.info(f"User was navigated to URL: '{url}'")
        except Exception as e:
            logging.error(f"An error occurred while navigating to URL {url}: {str(e)}")
    
    def wait_for_element_in_dom(self, locator, timeout=10):
        try:             
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
            logging.info(f"Element with locator {locator} was found.")
            return element
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")

    def wait_until_element_visible(self, locator, timeout=30):
        condition = EC.visibility_of_element_located(locator)
        return WebDriverWait(self.browser,timeout).until(condition)
    
    def find_element_and_click(self, locator, timeout=30): 
        element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))    
        element.click()
        return element
    
    def find_element_by_id(self, locator, timeout=30):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))    
    
    def move_to_element(self, locator): 
        try:
            element = self.browser.find_element(*locator)
            self.browser.execute_script("arguments[0].scrollIntoView();", element)            
            return element
        except Exception as e:            
            return None

    def find_and_send_keys(self, locator, keys, timeout=30):
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator))
            element.send_keys(keys)
            logging.info(f"Query '{keys}' was entered.")
            return element
        except Exception as e:
            logging.error(f"Error finding element {locator} or sending keys: {e}")
            raise

    def make_screenshot(self, file_name): 
        self.browser.save_screenshot(os.path.join(os.path.dirname(__file__), file_name))

    def write_to_json(self, data, file_path):  
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f , indent=4)
                                              
        except FileNotFoundError as e:
                logging.error(f"An error occurred: {str(e)}")           
 
      
    def read_from_json(self):         
        try:
            if os.path.exists(my_config.json_file_path):
                logging.info(f"The file '{my_config.json_file_path}' exists.")

            with open(my_config.json_file_path, 'r') as f:
                self.data = json.load(f) 
                logging.info(f"The info from '{my_config.json_file_path}' was parsed.")   
                print(self.data)  
                return self.data
           
        except FileNotFoundError as e:
                logging.error(f"An error occurred: {str(e)}")           

    
    
               
